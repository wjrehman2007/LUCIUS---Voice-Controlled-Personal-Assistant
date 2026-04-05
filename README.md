# LUCIUS - Voice-Controlled Personal Assistant
## A Production-Ready AI Assistant for Windows

---

## 🎙️ What is LUCIUS?

**LUCIUS** is a fully-functional, voice-activated personal assistant for Windows PCs. Simply say **"Hello Lucius"** to activate, then give it commands in natural language.

### Features:
- 🎤 **Wake-word detection** - "Hello Lucius" or "Hey Lucius"
- 🌐 **Web search** - Search Google directly from voice commands
- 💻 **System control** - Shutdown, restart, open applications
- ⏰ **Time & information** - Get current time, weather, and more
- ✍️ **Text automation** - Voice-dictated typing into Notepad
- 🧠 **Natural language understanding** - Flexible, conversational commands
- 🔊 **Voice responses** - Speaks back to you

---

## 🚀 Quick Start (5 Minutes)

### Prerequisites:
- Windows 10/11
- Python 3.8+ installed
- Working microphone and speakers

### Installation:
```bash
# 1. Clone or download LUCIUS
git clone https://github.com/your-repo/lucius.git
cd lucius

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run LUCIUS
python main.py
```

### First Use:
1. Wait for: "LUCIUS is online. Say hello lucius to begin."
2. Say: **"Hello Lucius"**
3. LUCIUS responds: **"Yes, how can I help?"**
4. Try: "Search for Peshawar news" or "What time is it?"

---

## 📖 Full Documentation

- **[SETUP.md](SETUP.md)** - Complete installation & troubleshooting guide
- **[ADDING_COMMANDS.md](ADDING_COMMANDS.md)** - How to extend LUCIUS with new commands

---

## 🎯 Supported Commands

### System Control
```
"Shutdown the PC"              → Shut down your computer
"Restart the computer"         → Restart your PC
```

### Information & Time
```
"What time is it?"             → Tell current time
"Tell me the time"             → Current time with date
```

### Web Search
```
"Search for Peshawar news"     → Open Chrome & search Google
"What is the dollar price?"    → Web search
"Find information about X"     → Google search
```

### Application Control
```
"Open Chrome"                  → Launch Google Chrome
"Open Notepad"                 → Launch Notepad
"Open Edge"                    → Launch Microsoft Edge
```

### Text Automation
```
"Open Notepad and write Wajid" → Opens Notepad & types text
"Write hello world"            → Types into open application
```

### Utility
```
"What can you do?"             → Show available commands
"Exit" / "Goodbye"             → Return to wake-word listening
```

---

## 🏗️ Architecture

```
LUCIUS/
├── main.py                 # Main application loop
├── voice_engine.py         # Speech recognition & TTS
├── command_handler.py      # Command parsing & intent matching
├── actions.py              # Command execution
├── logger_config.py        # Logging setup
├── requirements.txt        # Python dependencies
├── logs/                   # Auto-generated log files
├── SETUP.md               # Installation guide
├── ADDING_COMMANDS.md     # Extension guide
└── README.md              # This file
```

### How It Works:

1. **Voice Engine** listens for wake phrase using speech recognition
2. **Command Handler** parses user input into intents and parameters
3. **Action Executor** performs the actual command (open app, search, etc.)
4. **Voice Response** speaks back the result to the user

---

## ⚙️ System Requirements

| Component | Requirement |
|-----------|-------------|
| OS | Windows 10/11 (64-bit) |
| Python | 3.8, 3.9, or 3.10 |
| RAM | 2GB minimum |
| Microphone | Required |
| Speakers | Required |
| Internet | Required (for Google STT and searches) |

---

## 🔧 Technologies Used

- **Python 3** - Core language
- **SpeechRecognition** - Speech-to-text (Google API)
- **pyttsx3** - Text-to-speech (offline)
- **pyautogui** - Keyboard/mouse automation
- **webbrowser** - Browser automation
- **subprocess** - System command execution

---

## 📊 Command Processing Flow

```
┌─────────────────────────────────────┐
│  User speaks "Search for Peshawar"  │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  Voice Engine transcribes to text   │
│  "search for peshawar"              │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  Command Handler parses intent      │
│  Intent: web_search                 │
│  Query: "peshawar"                  │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  Action Executor runs action        │
│  Opens Chrome, searches Google      │
└──────────────┬──────────────────────┘
               ↓
┌─────────────────────────────────────┐
│  Voice Response speaks back         │
│  "Searching for peshawar"           │
└─────────────────────────────────────┘
```

---

## 🛡️ Safety Features

- **Confirmation for dangerous commands** (shutdown, restart)
- **Error handling** throughout the application
- **Comprehensive logging** for debugging
- **Graceful shutdown** with proper cleanup
- **Non-intrusive** - won't execute random commands

---

## 🐛 Troubleshooting

### Issue: Microphone not detected
**Solution:** Check Windows Settings → Sound → Input device selection

### Issue: "No speech detected"
**Solution:** Increase microphone volume, speak closer to mic, reduce background noise

### Issue: Speech Recognition errors
**Solution:** Check internet connection (Google API requires it), try again

### Issue: Commands not working
**Solution:** Speak naturally and clearly, view logs in `logs/` folder for details

See **[SETUP.md](SETUP.md)** for comprehensive troubleshooting.

---

## 🚀 Extending LUCIUS

LUCIUS is **modular and extensible**. Add new commands in 3 steps:

1. **Add command pattern** to `command_handler.py`
2. **Add action handler** to `actions.py`
3. **Test your command**

Example: Add calculator
```python
# In command_handler.py
"calculator": {
    "patterns": [r"calculate\s+(.+)"],
    "intent": "calculate",
},

# In actions.py
def calculate(self, params):
    expr = params.get("query", "")
    # Your calculation logic
    return f"The answer is {eval(expr)}"
```

Full guide: **[ADDING_COMMANDS.md](ADDING_COMMANDS.md)**

---

## 📝 Logging

All activities are logged to `logs/` folder with:
- **Timestamp**
- **Log level** (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- **Component name**
- **Message**

View latest log:
```bash
type logs\*.log
```

---

## 🎯 Roadmap / Future Enhancements

- [ ] Offline speech recognition (Vosk)
- [ ] Email integration
- [ ] Calendar & reminder management
- [ ] Smart home integration
- [ ] Custom voice profiles
- [ ] Command history & statistics
- [ ] Context-aware responses
- [ ] Plugin system for community extensions

---

## 🤝 Contributing

Want to improve LUCIUS? Here's how:

1. Create new commands following [ADDING_COMMANDS.md](ADDING_COMMANDS.md)
2. Test thoroughly
3. Update documentation
4. Submit pull request

---

## 📄 License

LUCIUS is provided as-is for personal and educational use.

---

## 👨‍💻 Author

Built by Senior AI Software Engineer
Version: 1.0.0
Last Updated: 2024

---

## 💬 Support

**Having issues?**
1. Check [SETUP.md](SETUP.md) for detailed troubleshooting
2. Review logs in `logs/` folder
3. Verify microphone is working
4. Ensure Python 3.8+ is installed

---

## ✨ Example Usage Session

```
>>> python main.py

INFO - LUCIUS Assistant - Initializing...
INFO - ✓ All components initialized successfully
INFO - 🎤 LUCIUS is ACTIVE - Listening for wake word...

🔊 LUCIUS: "LUCIUS is online. Say hello lucius to begin."

[User speaks: "Hello Lucius"]

INFO - Heard: hello lucius
INFO - ✓ Wake word detected!
🔊 LUCIUS: "Yes, how can I help?"

[User speaks: "What time is it?"]

INFO - Command: what time is it
INFO - Action: get_time
🔊 LUCIUS: "The current time is 3:45 PM. Today is Monday, January 15, 2024."

[User speaks: "Search for Peshawar news"]

INFO - Command: search for peshawar news
INFO - Action: web_search
🔊 LUCIUS: "Searching for peshawar news. Opening Chrome."

[Chrome opens with search results]

[User speaks: "Exit"]

INFO - Exit command detected
🔊 LUCIUS: "Returning to standby."
INFO - Returning to wake word mode...
```

---

## 🎉 You're ready to go!

Say **"Hello Lucius"** and enjoy your AI assistant!

For detailed setup, see **[SETUP.md](SETUP.md)**
To add new commands, see **[ADDING_COMMANDS.md](ADDING_COMMANDS.md)**

