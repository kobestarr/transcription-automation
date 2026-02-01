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


def start_transcription(api_key, youtube_url):
    """Submit YouTube URL for transcription"""
    endpoint = f"{BASE_URL}/transcriptions/youtube"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {"url": youtube_url}
    
    response = requests.post(endpoint, json=data, headers=headers)
    response.raise_for_status()
    return response.json()


def check_status(api_key, transcription_id):
    """Check transcription status"""
    endpoint = f"{BASE_URL}/transcriptions/{transcription_id}/status"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def get_transcription(api_key, transcription_id):
    """Get completed transcription"""
    endpoint = f"{BASE_URL}/transcriptions/{transcription_id}"
    headers = {"Authorization": f"Bearer {api_key}"}
    
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
    if 'text' in data:
        with open(output_dir / "transcript.txt", 'w') as f:
            f.write(data['text'])
    
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


def transcribe(youtube_url, output_base, wait=True, episode_title=None):
    """
    Transcribe a YouTube video using UniScribe.
    
    Args:
        youtube_url: YouTube video URL
        output_base: Base directory for output
        wait: Wait for transcription to complete
        episode_title: Optional episode title (auto-generated if not provided)
    """
    api_key = load_credentials()
    video_id = parse_video_id(youtube_url)
    
    if not episode_title:
        episode_title = f"video_{video_id}"
    
    # Start transcription
    print(f"📤 Submitting: {youtube_url}")
    result = start_transcription(api_key, youtube_url)
    transcription_id = result.get('id')
    
    print(f"✅ Transcription started: ID {transcription_id}")
    
    if not wait:
        print(f"📋 Transcription ID: {transcription_id}")
        print(f"   Check status: {BASE_URL}/transcriptions/{transcription_id}/status")
        return transcription_id
    
    # Wait for completion
    print("⏳ Waiting for transcription...")
    while True:
        status = check_status(api_key, transcription_id)
        state = status.get('status', 'unknown')
        print(f"   Status: {state}")
        
        if state == 'completed':
            break
        elif state == 'failed':
            raise Exception(f"Transcription failed: {status}")
        
        time.sleep(5)
    
    # Get and save
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
    parser.add_argument("--no-wait", action="store_true", help="Don't wait for completion")
    
    args = parser.parse_args()
    
    transcribe(args.url, args.output, wait=not args.no_wait, episode_title=args.title)
