# PEER_REVIEW_PROMPT.md - Peer Review Process

## Context
A different team lead within the company has reviewed the current code/implementation and provided findings below. Important context:

- **They have less context than you** on this project's history and decisions
- **You are the team lead** - don't accept findings at face value
- Your job is to critically evaluate each finding

---

## Peer Review Findings

[PASTE FEEDBACK FROM OTHER MODEL HERE]

---

## Your Evaluation Process

For EACH finding above:

### 1. Verify the Finding
- Actually check the code - does this issue/bug really exist?
- Don't assume the other model is correct
- Check the actual file, function, or implementation

### 2. Assess Validity
- **If it doesn't exist**: Explain clearly why (already handled, different architecture, they misunderstood)
- **If it does exist**: Assess severity (high/medium/low) and impact

### 3. Response Format

```
## Peer Review Analysis

### Findings Confirmed as VALID (Will Fix)
| Issue | Severity | Fix Plan |
|-------|----------|----------|
|       |          |          |

### Findings INVALIDATED (With Explanations)
| Finding | Why It's Invalid |
|---------|------------------|
|         |                  |

### Priority Action Plan
1. [HIGH] 
2. [MEDIUM] 
3. [LOW] 
```

---

## Review Criteria (From CODE_REVIEW_PROMPT.md)

1. **Security** - API keys, credentials, file permissions
2. **Quality** - Code structure, error handling, DRY principle
3. **Python conventions** - PEP8, naming, comments, docs
4. **Completeness** - Missing files, broken imports, edge cases
5. **Best practices** - Modularity, reusability, testing

---

## Critical Reminders

- **Verify before accepting** - Other models may miss context
- **Explain invalid findings** - Don't just dismiss, explain why
- **Prioritize fixes** - Not all issues are equal
- **Be respectful** - The other model was trying to help

---

*Use this prompt before EVERY peer review for consistency.*
