# LUCIUS - Voice-Controlled Personal Assistant
## Complete Setup & Installation Guide

---

## 📋 PREREQUISITES

Before you begin, ensure you have:

1. **Windows 10 or Windows 11** (64-bit recommended)
2. **Python 3.8+** installed on your system
3. **Git** (optional, for cloning)
4. **Working microphone and speakers** on your PC
5. **Internet connection** (for Google Speech Recognition and web searches)

---

## 🚀 INSTALLATION STEPS

### Step 1: Download Python
1. Go to [python.org](https://www.python.org/downloads/)
2. Download **Python 3.9 or 3.10** (NOT Python 3.12+ yet, due to compatibility)
3. During installation:
   - ✅ **CHECK** "Add Python to PATH"
   - ✅ **CHECK** "Install pip"
   - Click "Install Now"

### Step 2: Verify Python Installation
Open Command Prompt (Win + R, type `cmd`, press Enter):
```bash
python --version
pip --version
```

You should see version numbers. If not, restart your computer and try again.

### Step 3: Download LUCIUS
Option A - **Using Git** (recommended):
```bash
git clone https://github.com/your-repo/lucius.git
cd lucius
```

Option B - **Manual Download**:
1. Download the LUCIUS folder as ZIP
2. Extract it to a location (e.g., `C:\Users\YourName\Documents\LUCIUS`)
3. Open Command Prompt in that folder

### Step 4: Install Dependencies
Navigate to the LUCIUS folder in Command Prompt:
```bash
cd path\to\lucius\folder
```

Then install all required packages:
```bash
pip install -r requirements.txt
```

**What this installs:**
- `SpeechRecognition` - Converts speech to text
- `pyttsx3` - Converts text to speech
- `pyautogui` - Automates mouse/keyboard

### Step 5: Verify Installation
Create a test file called `test_installation.py`:

```python
try:
    import speech_recognition as sr
    import pyttsx3
    import pyautogui
    print("✓ All dependencies installed successfully!")
except ImportError as e:
    print(f"✗ Missing dependency: {e}")
```

Run it:
```bash
python test_installation.py
```

You should see: `✓ All dependencies installed successfully!`

---

## 🎤 MICROPHONE SETUP (IMPORTANT)

### Windows 10/11 Microphone Configuration:

1. **Settings → System → Sound**
2. Scroll down to **"Input"**
3. Select your microphone under "Choose your input device"
4. Click **"Device properties"**
5. Test your microphone in Settings
6. Set microphone volume to 75-100%

### If Microphone Doesn't Work:

1. Right-click **Volume icon** → **Open Sound settings**
2. Under "Advanced," click **"App volume and device preferences"**
3. Find Python in the list
4. Ensure microphone is enabled

---

## ▶️ HOW TO RUN LUCIUS

### Basic Startup:

1. Open **Command Prompt** or **PowerShell**
2. Navigate to LUCIUS folder:
   ```bash
   cd path\to\lucius\folder
   ```
3. Run LUCIUS:
   ```bash
   python main.py
   ```

### Expected Output:

```
INFO - ============================================================
INFO - 🎤 LUCIUS is ACTIVE - Listening for wake word...
INFO - Say: 'Hello Lucius' or 'Hey Lucius' to activate
INFO - ============================================================
```

### ✅ LUCIUS is now ACTIVE and waiting for commands!

---

## 🎯 USING LUCIUS - COMMAND EXAMPLES

### 1. **Wake Up LUCIUS**
Say: **"Hello Lucius"** or **"Hey Lucius"**

LUCIUS responds: **"Yes, how can I help?"**

### 2. **Tell Time**
Command: "What time is it?"
Response: "The current time is 3:45 PM. Today is Monday, January 15, 2024."

### 3. **Search the Web**
Command: "Search for Peshawar news"
→ Automatically opens Chrome and searches

### 4. **Open Applications**
- "Open Chrome"
- "Open Notepad"
- "Open Edge"

### 5. **Type Text (Automation)**
Command: "Open Notepad and write Wajid ur Rehman"
→ Opens Notepad and types the text automatically

### 6. **Shutdown/Restart**
- Command: "Shutdown the PC"
- Command: "Restart the computer"

### 7. **Get Help**
Command: "What can you do?"
Response: Lists all available commands

### 8. **Exit Command Mode**
Say: "Exit" or "Goodbye" or "Bye"
→ Returns to wake-word listening mode

---

## 🔧 TROUBLESHOOTING

### Issue: "Microphone not found"
**Solution:**
- Check microphone is plugged in
- Go to Windows Settings → Sound → Check input device
- Restart LUCIUS

### Issue: "No speech detected"
**Solution:**
- Ensure microphone volume is at 75-100%
- Speak clearly and closer to microphone
- Reduce background noise
- Check Settings → Sound → Privacy settings allow app microphone access

### Issue: "Text-to-Speech not working"
**Solution:**
- Check Windows sound settings (speakers not muted)
- Volume slider is not at 0
- Restart the application

### Issue: "Speech Recognition API Error"
**Solution:**
- Ensure internet connection is active
- Google API has rate limits (wait a few minutes if overused)
- Check firewall isn't blocking Python network access

### Issue: "Commands not being recognized"
**Solution:**
- Speak clearly and naturally
- Don't speak too fast
- Say full command (e.g., "Search for XYZ" not just "XYZ")

### Issue: "Can't open Chrome/Notepad"
**Solution:**
- Ensure application is installed
- Check app installation path
- Try opening manually to verify it works

---

## 📝 VIEWING LOGS

All activities are logged to `logs/` folder:
- Located: `lucius/logs/`
- Files named: `lucius_YYYYMMDD_HHMMSS.log`
- View with any text editor to debug issues

---

## 🛠️ CONFIGURATION (Optional)

### Adjust TTS Speed (in `voice_engine.py`):
```python
self.tts_engine.setProperty("rate", 150)  # Change 150 to 100-250
```
- Lower = Slower speech
- Higher = Faster speech

### Adjust Microphone Sensitivity (in `voice_engine.py`):
```python
self.recognizer.adjust_for_ambient_noise(source, duration=1)  # Change 1 to 2-5
```
- Higher = More ambient noise filtered out

---

## 🚨 SAFETY NOTES

1. **Shutdown/Restart commands** show a warning message before execution
2. PC will wait 10 seconds before actually shutting down/restarting
3. You can cancel with `shutdown /a` in Command Prompt if needed
4. LUCIUS will ask for voice confirmation on sensitive operations

---

## 📦 PROJECT STRUCTURE

```
LUCIUS/
├── main.py                  # Entry point - main application loop
├── voice_engine.py          # Speech recognition & text-to-speech
├── command_handler.py       # Command parsing & intent matching
├── actions.py               # Command execution logic
├── logger_config.py         # Logging configuration
├── requirements.txt         # Python dependencies
├── SETUP.md                 # This file
├── ADDING_COMMANDS.md       # Guide to extend commands
├── logs/                    # Auto-created folder for log files
└── README.md                # Project overview
```

---

## ✨ NEXT STEPS

1. ✅ Run LUCIUS
2. ✅ Test with voice commands
3. ✅ Adjust microphone sensitivity if needed
4. ✅ Read `ADDING_COMMANDS.md` to extend functionality

---

## 📞 SUPPORT

If you encounter issues:
1. Check the **logs** folder for error messages
2. Verify microphone and speaker are working
3. Ensure internet connection is active
4. Restart LUCIUS
5. Check Python version is 3.8+

---

## 🎉 You're all set! 

Say **"Hello Lucius"** and start using your voice assistant!

