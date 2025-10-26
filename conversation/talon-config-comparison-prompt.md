# Talon Configuration Comparison Prompt

You are helping me compare my local Talon voice recognition configuration with the upstream community/main branch to identify voice recognition configuration changes.

## Context
- Local Talon config is at: `/Users/hamoung/.talon/user/talonconfig/`
- We need to compare against the remote `community/main` branch (NOT `origin/main`)
- Focus on voice recognition configurations, not missing features

## Task Steps

### 1. Setup Remote Branch
Check if remote comparison copy exists at `~/Documents/talon_comparison/community_main/`:

**If it exists:**
```bash
cd ~/Documents/talon_comparison/community_main
git fetch origin
git reset --hard origin/main
```

**If it doesn't exist:**
```bash
cd ~/Documents && mkdir -p talon_comparison && cd talon_comparison
git clone https://github.com/talonhub/community.git community_main
```

### 2. Compare Key Configuration Files
Focus on these critical voice recognition files:
- `core/keys/letter.talon-list` (alphabet)
- `core/keys/symbols.py` (symbol commands)  
- `core/keys/keys.talon` (key commands)
- `core/keys/keystroke.talon` (if exists locally)
- `core/keys/mac/special_key.talon-list` (special keys)
- `core/keys/modifier_key.talon-list` (if exists locally)

### 3. Analysis Focus
For each file comparison, identify:
- **Custom alphabet changes** (different phonetic words)
- **Simplified symbol commands** (removed alternatives)
- **Added/removed key commands**
- **Local-only files** not in upstream
- **Custom modifier shortcuts**

### 4. Generate Report
Create a structured comparison report showing:
- What was changed from upstream defaults
- What was added that doesn't exist upstream
- What was removed from upstream
- The rationale behind changes (accuracy, simplicity, ergonomics)

## Important Notes
- Do NOT modify any files in the local branch
- Use `diff -u` for clear comparison output
- Focus on voice recognition accuracy improvements
- Explain the behavioral differences of any changed commands
