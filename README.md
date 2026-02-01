# Transcription Automation

YouTube video transcription workflow using UniScribe API.

## Structure

```
transcription-automation/
├── README.md
├── .gitignore
├── scripts/
│   └── transcribe.py          # Main transcription script
├── research/                  # Research/tutorial transcriptions
│   └── yyyy-mm-dd-video-title/
│       ├── transcript.txt
│       ├── raw.json
│       └── url.txt
└── podcast/                   # Podcast transcriptions
    └── {podcast-name}/
        └── yyyy-mm-dd-episode-title/
            ├── transcript.txt
            ├── raw.json
            └── url.txt
```

## Setup

```bash
# API key is already stored at /root/.credentials/uniscribe.json
```

## Usage

### Transcribe a video

```bash
# Research/tutorial
python scripts/transcribe.py \
  --url "https://www.youtube.com/watch?v=..." \
  --output research \
  --title "2026-02-01-tutorial-topic"

# Podcast episode
python scripts/transcribe.py \
  --url "https://www.youtube.com/watch?v=..." \
  --output podcast/ultimate-football-heroes \
  --title "2026-02-01-episode-title"
```

## Process Notes

- **Research transcripts** → Use as SOP/process foundation
- **Podcast transcripts** → Content repurposing (social media, Reddit, SEO)
- Check existing scripts before creating new ones to avoid duplication
