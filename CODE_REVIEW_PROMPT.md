# Code Review Prompt

Review ALL content in the repository (not just latest commit):
1. **Security** - API keys, credentials, file permissions
2. **Quality** - Code structure, error handling, DRY principle
3. **Python conventions** - PEP8, naming, comments, docs
4. **Completeness** - Missing files, broken imports, edge cases
5. **Best practices** - Modularity, reusability, testing

Output format:
- **Security Issues**: (none/high/medium/low)
- **Code Quality Score**: /10
- **Critical Fixes Needed**: List
- **Improvement Suggestions**: List
- **Files Reviewed**: List all files

Focus areas:
- `scripts/transcribe.py` - Main script
- `README.md` - Documentation clarity
- Any credentials or config files

**Review entire repo contents, not just diffs.**
