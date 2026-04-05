# LUCIUS - Complete Master Documentation
## Voice-Controlled Personal Assistant for Windows

---

## 📚 TABLE OF CONTENTS

1. [Overview](#overview)
2. [System Requirements](#system-requirements)
3. [Installation](#installation)
4. [Getting Started](#getting-started)
5. [Command Reference](#command-reference)
6. [Architecture](#architecture)
7. [Troubleshooting](#troubleshooting)
8. [Extending LUCIUS](#extending-lucius)
9. [FAQ](#faq)

---

## 🎯 OVERVIEW

**LUCIUS** is a production-ready, modular voice assistant for Windows that:

- Listens for wake phrase ("Hello Lucius")
- Understands natural language commands
- Executes system tasks, web searches, and text automation
- Responds with spoken feedback
- Logs all activities for debugging

### Key Features:
✅ Wake-word detection  
✅ Natural language processing  
✅ Web search automation  
✅ System control (shutdown, restart)  
✅ Text-to-speech responses  
✅ Error handling & logging  
✅ Easily extensible  
✅ No complex setup  

---

## 💻 SYSTEM REQUIREMENTS

| Requirement | Specification |
|------------|--------------|
| **OS** | Windows 10/11 (64-bit) |
| **Python** | 3.8, 3.9, or 3.10 |
| **RAM** | 2GB minimum (4GB+ recommended) |
| **Disk Space** | 500MB for Python + dependencies |
| **Microphone** | Required for speech input |
| **Speaker** | Required for voice output |
| **Internet** | Required for Google STT & web search |
| **Network** | Stable connection (for cloud APIs) |

### Unsupported:
- ❌ Python 3.11+ (compatibility pending)
- ❌ Python 2.x (outdated)
- ❌ Raspberry Pi without proper audio setup
- ❌ Remote connections (WSL without audio passthrough)

---

## 🚀 INSTALLATION

### Option 1: Express Installation (5 minutes)

**Prerequisites:** Python 3.8+ installed

```bash
# 1. Download LUCIUS folder
# 2. Open Command Prompt in folder
# 3. Run:
pip install -r requirements.txt
python main.py
```

### Option 2: Detailed Installation (with verification)

```bash
# 1. Verify Python
python --version  # Must be 3.8+

# 2. Verify pip
pip --version

# 3. Install dependencies
pip install -r requirements.txt

# 4. Test installation
python test_installation.py

# 5. Run LUCIUS
python main.py
```

### Installation Troubleshooting:

**Issue: "pip command not found"**
- Python not added to PATH
- Solution: Reinstall Python, check "Add Python to PATH"

**Issue: "ModuleNotFoundError" after pip install**
- Dependencies not installed in correct Python environment
- Solution: Use `python -m pip install -r requirements.txt`

**Issue: Permission denied**
- Running as restricted user
- Solution: Run Command Prompt as Administrator

---

## 🎤 GETTING STARTED

### Step 1: Launch LUCIUS
```bash
python main.py
```

**Expected output:**
```
INFO - ============================================================
INFO - 🎤 LUCIUS is ACTIVE - Listening for wake word...
INFO - Say: 'Hello Lucius' or 'Hey Lucius' to activate
INFO - ============================================================
```

### Step 2: Activate with Wake Word
**Say clearly:** "Hello Lucius" or "Hey Lucius"

**LUCIUS responds:** "Yes, how can I help?"

### Step 3: Give Commands
**Say your command naturally:**
- "What time is it?"
- "Search for Peshawar news"
- "Open Chrome"
- "Write my name in Notepad"

### Step 4: Listen to Response
LUCIUS executes command and speaks confirmation.

### Step 5: Continue or Exit
- **Continue:** Say another command
- **Exit:** Say "Exit", "Quit", "Goodbye", or "Bye"

---

## 📋 COMMAND REFERENCE

### System Information
```
"What time is it?"
"Tell me the current time"
→ Returns: Current time and date

"What can you do?"
"Show help"
→ Returns: List of available commands
```

### Web Search
```
"Search for Peshawar news"
"Google dollar price in Pakistan"
"Find information about AI"
→ Returns: Opens Chrome with search results
```

### Applications
```
"Open Chrome"
"Open Notepad"
"Open Edge"
→ Returns: Launches requested application
```

### Text Automation
```
"Open Notepad and write Wajid ur Rehman"
"Type hello world"
→ Returns: Opens app and types text
```

### System Control
```
"Shutdown the PC"
"Restart the computer"
→ Returns: Initiates shutdown/restart (10 sec delay)
```

### Navigation
```
"Exit" / "Quit" / "Goodbye" / "Bye"
→ Returns: Exits command mode, returns to wake-word listening
```

---

## 🏗️ ARCHITECTURE

### Component Overview

```
┌────────────────────────────────────────────────┐
│            LUCIUS MAIN APPLICATION             │
│  (main.py - Orchestrates all components)      │
└────────────────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
    ┌──────────┐  ┌──────────────┐  ┌──────────┐
    │  VOICE   │  │   COMMAND    │  │  ACTION  │
    │  ENGINE  │  │   HANDLER    │  │ EXECUTOR │
    └──────────┘  └──────────────┘  └──────────┘
        │               │               │
        ├─ Listens      ├─ Parses      ├─ Executes
        ├─ Transcribes  ├─ Extracts    ├─ Web Search
        └─ Speaks       └─ Routes      └─ System Ctrl
```

### Module Details

#### voice_engine.py
- **Responsibility:** Speech input/output
- **Functions:**
  - `listen_for_audio()` - Captures microphone input
  - `transcribe_audio()` - Converts speech to text (Google API)
  - `speak()` - Converts text to speech (pyttsx3)
  - `cleanup()` - Releases resources

#### command_handler.py
- **Responsibility:** Natural language processing
- **Functions:**
  - `parse_command()` - Matches text against regex patterns
  - `execute_command()` - Delegates to ActionExecutor
  - `_define_commands()` - Command definitions with patterns

#### actions.py
- **Responsibility:** Command execution
- **Functions:**
  - `execute()` - Routes to specific action handler
  - `web_search()` - Opens Chrome & searches
  - `shutdown_pc()` - Initiates PC shutdown
  - `open_application()` - Launches apps
  - `write_text()` - Automates typing
  - And more...

#### logger_config.py
- **Responsibility:** Centralized logging
- **Features:**
  - File logging (detailed)
  - Console logging (brief)
  - Automatic log rotation
  - Timestamp on all entries

---

## 🐛 TROUBLESHOOTING

### Microphone Issues

**Problem:** "Microphone not found"
```
Solution:
1. Go to Windows Settings → System → Sound
2. Under "Input", select your microphone
3. Click "Device properties" and test
4. Set volume to 75-100%
5. Restart LUCIUS
```

**Problem:** "No speech detected"
```
Solution:
1. Check microphone volume (Settings → Sound)
2. Speak louder and closer to microphone
3. Reduce background noise
4. Restart LUCIUS with new microphone calibration
```

### Speaker Issues

**Problem:** "No audio output / TTS not working"
```
Solution:
1. Check speaker is not muted (Volume icon)
2. Increase Windows volume (slider at 100%)
3. Check app volume in Settings → Volume mixer
4. Restart LUCIUS
```

### Speech Recognition Errors

**Problem:** "Google API error" or network timeout
```
Solution:
1. Verify internet connection is active
2. Check firewall allows Python network access
3. Wait a few minutes (API rate limits)
4. Try again
```

**Problem:** "Could not understand audio"
```
Solution:
1. Speak more clearly
2. Reduce background noise
3. Speak at normal pace
4. Don't speak too softly or too harshly
```

### Command Not Working

**Problem:** Command recognized but not executing
```
Solution:
1. Check logs in logs/ folder
2. Verify app is installed (Chrome, Notepad, etc)
3. Ensure text matches command pattern
4. Try rephrasing the command
```

**Problem:** Wrong command executed
```
Solution:
1. Review logs to see what was heard
2. Speak more clearly
3. Use more specific language
Example: Instead of "Search news", say "Search for latest news"
```

### Installation Issues

**Problem:** "ModuleNotFoundError: No module named 'speech_recognition'"
```
Solution:
1. Run: pip install -r requirements.txt
2. Or: python -m pip install SpeechRecognition pyttsx3 pyautogui
3. Verify installation: python test_installation.py
```

**Problem:** Python version too old
```
Solution:
1. Download Python 3.8+ from python.org
2. Reinstall with "Add Python to PATH" checked
3. Run: python --version (should be 3.8+)
```

### General Debugging

**Check Logs:**
```bash
# View latest log file
type logs\lucius_*.log

# On Linux/Mac:
cat logs/lucius_*.log
```

**Run Test:**
```bash
python test_installation.py
```

**Enable Debug Mode:**
Edit `main.py` and set:
```python
logger.setLevel(logging.DEBUG)
```

---

## 🔧 EXTENDING LUCIUS

### Add a New Command (3-Step Process)

#### Step 1: Define Command Pattern
In `command_handler.py`, add to `_define_commands()`:

```python
"calculator": {
    "patterns": [
        r"calculate\s+(.+)",
        r"math\s+(.+)",
    ],
    "intent": "calculate",
    "requires_confirmation": False,
    "capture_group": 1,
},
```

#### Step 2: Add Action Handler
In `actions.py`, add to `__init__()`:
```python
self.action_map["calculate"] = self.calculate
```

Then implement:
```python
def calculate(self, params):
    """Calculate math expression"""
    expr = params.get("query", "").strip()
    if not expr:
        return "Please provide a calculation"
    
    try:
        result = eval(expr.replace("plus", "+").replace("times", "*"))
        return f"The answer is {result}"
    except Exception as e:
        return f"Error: {str(e)}"
```

#### Step 3: Update Intent Mapping
In `command_handler.py`, add to `_intent_to_action()`:
```python
"calculate": "calculate",
```

### Advanced Patterns

**Multiple Captures:**
```python
"patterns": [
    r"remind me to (.+) in (\d+) (minutes|hours)",
],
```

**Optional Segments:**
```python
"patterns": [
    r"(?:please\s+)?open\s+(.+)",
],
```

**Case-Insensitive:**
```python
# Already handled - parse_command() uses .lower()
```

### Common Extensions

1. **Calendar Integration** - Add events
2. **Email Support** - Send emails via SMTP
3. **Weather API** - Real weather data
4. **Task Manager** - Create tasks/todos
5. **File Manager** - Navigate folders
6. **Custom Timers** - Set alarms
7. **Music Control** - Play/pause music
8. **Device Control** - Smart home integration

See **ADDING_COMMANDS.md** for detailed examples.

---

## ❓ FAQ

### Q: Does LUCIUS require internet?
**A:** Yes, for Google Speech Recognition API. You can add offline speech recognition (Vosk) for offline mode (see ADDING_COMMANDS.md).

### Q: Can I change the wake word?
**A:** Yes! Edit `config.py`:
```python
WAKE_WORDS = ["hello lucius", "hey lucius", "activate"]
```

### Q: How do I add new voice personalities?
**A:** Edit `voice_engine.py`, `_configure_tts()`:
```python
voices = self.tts_engine.getProperty("voices")
self.tts_engine.setProperty("voice", voices[0].id)  # Change index
```

### Q: Can LUCIUS run on Mac/Linux?
**A:** Most components are OS-independent. Modifications needed for:
- File paths (use `pathlib`)
- System commands (OS-specific)
- Application launching

### Q: Is my voice data saved?
**A:** Google API receives your audio for transcription. LUCIUS only logs text. No personal data storage.

### Q: Can I use this commercially?
**A:** Check license and Google API terms. This is provided as-is for personal/educational use.

### Q: How accurate is voice recognition?
**A:** Google API achieves ~95% accuracy in quiet environments. Accuracy decreases with:
- Background noise
- Thick accents
- Poor microphone quality
- Speaking too fast/soft

### Q: Can I train custom voice models?
**A:** Not in current version. Google API is cloud-based. For offline custom models, integrate Vosk or OpenAI Whisper.

### Q: How do I uninstall?
**A:** Simply delete the LUCIUS folder. No system registry changes or hidden files.

---

## 🚀 QUICK REFERENCE

### Essential Commands
```bash
python main.py           # Start LUCIUS
python test_installation.py  # Test setup
pip install -r requirements.txt  # Install deps
```

### Wake LUCIUS
```
"Hello Lucius" or "Hey Lucius"
```

### Common Commands
```
"What time is it?"
"Search for [anything]"
"Open Chrome/Notepad/Edge"
"Write [text]"
"Shutdown PC"
"Exit" (to stop listening)
```

### Check Logs
```bash
type logs\lucius_*.log
```

### View This Documentation
```
README.md          - Overview
SETUP.md          - Installation
ADDING_COMMANDS.md - Extend LUCIUS
QUICKSTART.md     - Quick reference
```

---

## 📞 SUPPORT & NEXT STEPS

1. **Read:** Start with README.md
2. **Install:** Follow SETUP.md
3. **Test:** Run test_installation.py
4. **Run:** Execute python main.py
5. **Extend:** Use ADDING_COMMANDS.md for new features

---

## 🎉 YOU'RE READY!

Your voice assistant is complete and ready to use.

**Start with:**
```bash
python main.py
```

Then say: **"Hello Lucius"**

Enjoy your AI assistant! 🚀

---

*For detailed information, see respective documentation files.*
*Last Updated: 2024*
*Version: 1.0.0*
## USE FREE LUCIUS FOR DAILY USES OF YOUR PC AND PRAY FOR ME IN YOUR PRAYERS "WAJID UR REHMAN"
