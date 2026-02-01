#!/usr/bin/env python3
"""
YouTube Video Transcription Script
Uses UniScribe API to transcribe YouTube videos.
"""

import os
import json
import argparse
import requests
import time
import sys
from pathlib import Path
from datetime import datetime

CREDENTIALS_FILE = "/root/.credentials/uniscribe.json"
BASE_URL = "https://api.uniscribe.co/api/v1"


def load_credentials():
    """Load UniScribe API key from secure storage"""
    with open(CREDENTIALS_FILE, 'r') as f:
        creds = json.load(f)
    return creds.get('api_key')


def start_transcription(api_key, youtube_url, language_code="en"):
    """Submit YouTube URL for transcription"""
    endpoint = f"{BASE_URL}/transcriptions/youtube"
    headers = {
        "X-API-Key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "url": youtube_url,
        "language_code": language_code
    }
    
    response = requests.post(endpoint, json=data, headers=headers)
    response.raise_for_status()
    return response.json()


def check_status(api_key, transcription_id):
    """Check transcription status"""
    endpoint = f"{BASE_URL}/transcriptions/{transcription_id}/status"
    headers = {"X-API-Key": api_key}
    
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_transcription(api_key, transcription_id):
    """Get completed transcription"""
    endpoint = f"{BASE_URL}/transcriptions/{transcription_id}"
    headers = {"X-API-Key": api_key}
    
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def save_transcript(output_dir, youtube_url, data):
    """Save transcription files"""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save URL
    with open(output_dir / "url.txt", 'w') as f:
        f.write(youtube_url)
    
    # Save full transcript
    if 'result' in data and 'text' in data['result']:
        with open(output_dir / "transcript.txt", 'w') as f:
            f.write(data['result']['text'])
    
    # Save raw JSON
    with open(output_dir / "raw.json", 'w') as f:
        json.dump(data, f, indent=2)
    
    return output_dir


def parse_video_id(url):
    """Extract YouTube video ID from URL"""
    if 'youtu.be' in url:
        return url.split('/')[-1].split('?')[0]
    if 'v=' in url:
        return url.split('v=')[1].split('&')[0]
    return None


def transcribe(youtube_url, output_base, wait=True, episode_title=None, language_code="en"):
    """
    Transcribe a YouTube video using UniScribe.
    """
    api_key = load_credentials()
    video_id = parse_video_id(youtube_url)
    
    if not episode_title:
        episode_title = f"video_{video_id}"
    
    print(f"📤 Submitting: {youtube_url}")
    result = start_transcription(api_key, youtube_url, language_code)
    transcription_id = result.get('data', {}).get('id') or result.get('id')
    
    print(f"✅ Transcription started: ID {transcription_id}")
    
    if not wait:
        print(f"📋 Transcription ID: {transcription_id}")
        return transcription_id
    
    # Wait for completion
    print("⏳ Waiting for transcription...")
    while True:
        status = check_status(api_key, transcription_id)
        state = status.get('data', {}).get('status', 'unknown')
        print(f"   Status: {state}")
        
        if state == 'completed':
            break
        elif state == 'failed':
            error_msg = status.get('data', {}).get('error_message', 'Unknown error')
            raise Exception(f"Transcription failed: {error_msg}")
        
        time.sleep(10)
    
    print("📥 Fetching transcription...")
    data = get_transcription(api_key, transcription_id)
    
    output_dir = os.path.join(output_base, episode_title)
    save_transcript(output_dir, youtube_url, data)
    
    print(f"✅ Saved to: {output_dir}")
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe YouTube videos using UniScribe")
    parser.add_argument("--url", required=True, help="YouTube URL")
    parser.add_argument("--output", default="./output", help="Output base directory")
    parser.add_argument("--title", help="Episode/title for folder name")
    parser.add_argument("--lang", default="en", help="Language code (default: en)")
    parser.add_argument("--no-wait", action="store_true", help="Don't wait for completion")
    
    args = parser.parse_args()
    
    transcribe(args.url, args.output, wait=not args.no_wait, episode_title=args.title, language_code=args.lang)
