# Credentials & APIs Tracker

*Running list of APIs needed to enable Robyn to work autonomously*

---

## Missing Credentials (Total: 5)

### Priority 1: CRITICAL (Blockers)

**1. OpenAI API Key** 🔴
- **Why needed:** Memory search & embeddings currently broken
- **Impact:** Cannot recall past conversations, research, or decisions
- **Location to get:** https://platform.openai.com/api-keys
- **Steps:**
  1. Go to platform.openai.com
  2. Sign up/login
  3. Click API Keys → Create new secret key
  4. Copy and save to `/root/.credentials/openai.json` as:
     ```json
     {"api_key": "sk-..."}
     ```
- **Priority:** HIGHEST - This is the #1 blocker

**2. Google API Credentials** 🟠
- **Why needed:** Memory search uses Google embeddings
- **Impact:** Cannot search memory files semantically
- **Location to get:** https://console.cloud.google.com
- **Steps:**
  1. Create Google Cloud project
  2. Enable Custom Search API
  3. Create credentials (API key)
  4. Save to `/root/.credentials/google.json`
- **Priority:** HIGH - Enables memory recall

### Priority 2: IMPORTANT

**3. Strava API Token** 🟡
- **Why needed:** Morning briefing health data
- **Impact:** Cannot fetch weight, activity stats for morning brief
- **Location to get:** https://www.strava.com/settings/api
- **Steps:**
  1. Go to Strava settings → API
  2. Create application
  3. Get client ID and secret
  4. OAuth flow to get access token
  5. Save to `/root/.credentials/strava.json`
- **Priority:** MEDIUM - Nice to have for briefings

**4. Apify API Token** 🟡
- **Why needed:** Web scraping (Reddit, job boards, etc.)
- **Impact:** Cannot run advanced scrapers for research
- **Location to get:** https://console.apify.com/account/integrations
- **Steps:**
  1. Go to Apify console
  2. Account → Integrations → API Tokens
  3. Copy token
  4. Save to `/root/.credentials/apify.json`
- **Priority:** MEDIUM - Enables scraping workflows

### Priority 3: NICE TO HAVE

**5. Brave Search API** 🟢
- **Why needed:** Web search (already have via web_search tool)
- **Impact:** Minor - current search works but could be faster
- **Location to get:** https://api.brave.com/register
- **Priority:** LOW - Working but could be improved

---

## Currently Working Credentials

| Service | Status | Location |
|---------|--------|----------|
| UniScribe | ✅ Working | `/root/.credentials/uniscribe.json` |
| GitHub | ✅ Working | Token in git remote URL |
| Apify (basic) | ⚠️ Limited | May need full token |

---

## Credentials Format

Save all credentials as JSON in `/root/.credentials/`:

```json
// openai.json
{"api_key": "sk-...", "model": "gpt-4"}

// google.json
{"api_key": "AIza..."}

// strava.json
{"access_token": "...", "refresh_token": "..."}

// apify.json
{"token": "..."}
```

---

## Quick Wins (Already Available)

- **YouTube transcripts:** UniScribe API (working)
- **Git operations:** Token in remote URL (working)
- **Basic web search:** Via OpenClaw tools (working)

---

## Goal: Enable Full Autonomy

With OpenAI + Google APIs:
- ✅ Full memory recall
- ✅ Semantic search across all research
- ✅ Better research capabilities
- ✅ True autonomous operation

---

*Last updated: 2026-02-01*
*Tracking: 5 missing credentials*
