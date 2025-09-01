# Min Stora Dag

A Python script that checks if both "pannkakor" (pancakes) and "stuvade makaroner" (creamed macaroni) are served on the same day at Swedish restaurant Heat - waiting for that one perfect lunch day!

## Setup

### Option 1: Using uv (recommended)

1. Initialize and sync dependencies:
```bash
uv sync
```

2. Run the menu checker:
```bash
# Default mode - returns only True or False
uv run python menu_checker.py

# Verbose mode - shows detailed menu parsing
uv run python menu_checker.py --verbose
# or
uv run python menu_checker.py -v
```

3. Run tests:
```bash
uv run python test_menu_checker.py
```

### Option 2: Using pip

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the menu checker:
```bash
# Default mode - returns only True or False
python menu_checker.py

# Verbose mode - shows detailed menu parsing
python menu_checker.py --verbose
# or
python menu_checker.py -v
```

## How it works

1. Dynamically extracts the current XML feed URL from the restaurant's main webpage
2. Fetches the weekly lunch menu from the discovered XML endpoint  
3. Parses XML data to extract menu items for each weekday (Måndag through Fredag)
4. Searches for "pannkakor" and "stuvade makaroner" in each day's menu
5. Returns `True` if both dishes are found on the same day, `False` otherwise

## 🤖 Automated Checking

This project includes a GitHub Actions workflow that automatically checks for your "Min Stora Dag" every day at 08:30 Stockholm time. When both dishes are found on the same day, it creates a celebratory GitHub issue to notify you!

**Features:**
- Runs automatically every morning
- Creates excited GitHub issues when both dishes are served  
- Handles Swedish timezone automatically
- Can be triggered manually for testing

## Testing

Run the test suite to verify the dish detection logic:

**With uv:**
```bash
uv run python test_menu_checker.py
```

**With pip:**
```bash
python test_menu_checker.py
```

## Files

- `menu_checker.py` - Main script with XML parsing and dish detection logic
- `test_menu_checker.py` - Test cases for dish detection logic
- `pyproject.toml` - Project configuration and dependencies (uv)
- `requirements.txt` - Python dependencies (pip)
- `CLAUDE.md` - Development guidance for Claude Code