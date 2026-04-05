# LUCIUS - Quick Reference Guide

## 🎙️ WAKE WORDS (Say any of these to activate)
- "Hello Lucius"
- "Hey Lucius"

## 📋 AVAILABLE COMMANDS

### ⏰ TIME & DATE
```
"What time is it?"          → Current time
"Tell me the time"          → Time with date
"What's the current time?"  → Time in Pakistan
```

### 🌐 WEB SEARCH (Opens Chrome automatically)
```
"Search for Peshawar news"           → Search Google
"What is the dollar price in Pakistan?" → Web search
"Find information about X"           → Google search
"Google [anything]"                  → Web search
```

### 💻 OPEN APPLICATIONS
```
"Open Chrome"               → Launch Chrome browser
"Open Notepad"              → Launch Notepad
"Open Edge"                 → Launch Microsoft Edge
```

### ✍️ TEXT AUTOMATION
```
"Open Notepad and write Wajid ur Rehman"  → Opens Notepad & types text
"Write hello world"                        → Type text in active app
```

### 🔌 SYSTEM CONTROL
```
"Shutdown the PC"           → Shut down computer (10 sec delay)
"Restart the computer"      → Restart computer (10 sec delay)
"Power off"                 → Shut down
```

### ℹ️ INFORMATION
```
"What can you do?"          → List all commands
"Help"                      → Show available commands
"Available commands"        → List commands
```

### 🚪 EXIT COMMANDS (Return to wake-word mode)
```
"Exit"
"Quit"
"Goodbye"
"Bye"
```

---

## ⚙️ HOW TO OPERATE

### Step 1: Launch LUCIUS
```bash
python main.py
```

### Step 2: Wait for Activation
Listen for: "LUCIUS is online. Say hello lucius to begin."

### Step 3: Wake LUCIUS
Say clearly: **"Hello Lucius"**

Response: **"Yes, how can I help?"**

### Step 4: Give Commands
Say your command naturally. Examples:
- "Search for Peshawar news"
- "What time is it?"
- "Open Chrome"

### Step 5: Get Response
LUCIUS speaks the response and executes the command.

### Step 6: Exit (Optional)
Say: "Exit" or "Goodbye" to return to wake-word listening.

---

## 🎤 VOICE TIPS

✓ **DO:**
- Speak clearly and naturally
- Use complete sentences
- Speak at normal volume
- Face the microphone

✗ **DON'T:**
- Speak too fast or too soft
- Use unclear accents excessively
- Have loud background noise
- Speak incomplete commands

---

## 🔧 SETUP & INSTALLATION

Quick setup (see SETUP.md for full guide):
```bash
# 1. Install Python 3.8+
# 2. Download LUCIUS folder
# 3. Open Command Prompt in folder
# 4. Run: pip install -r requirements.txt
# 5. Run: python main.py
```

---

## 📊 MICROPHONE SETTINGS

1. **Windows Settings → Sound**
2. Select your microphone
3. Set volume to 75-100%
4. Test microphone
5. Grant microphone permissions to Python

---

## 🐛 QUICK TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Microphone not detected | Check Windows Sound settings |
| "No speech detected" | Increase mic volume, speak louder |
| Commands ignored | Speak clearly after "Yes, how can I help?" |
| App won't open | Check app is installed on your PC |
| Typing doesn't work | Ensure Notepad/app has focus |
| Network errors | Check internet connection |

For more help, see **SETUP.md**

---

## 📝 LOG FILES

Logs stored in: `logs/lucius_YYYYMMDD_HHMMSS.log`

View latest:
```bash
# Windows
type logs\*.log

# Or open in text editor
```

---

## 🚀 EXTENDING LUCIUS

Add new commands in 3 steps (see ADDING_COMMANDS.md):

1. **Pattern** in `command_handler.py`
2. **Handler** in `actions.py`
3. **Test** your command

---

## 📞 SUPPORT

**Common Issues:**
- **Microphone**: Check Windows Sound settings
- **Commands**: Speak clearly, use complete sentences
- **Network**: Verify internet connection
- **Logs**: Check `logs/` folder for error messages

**Still stuck?** See comprehensive guide in SETUP.md

---

## 🎯 NEXT STEPS

1. ✅ Run `python main.py`
2. ✅ Say "Hello Lucius"
3. ✅ Try a command
4. ✅ Check logs if issues
5. ✅ Read ADDING_COMMANDS.md to extend

---

## 💡 POWER TIPS

### Tip 1: Use Natural Language
Good: "Search for news about Peshawar"
Bad: "search peshawar"

### Tip 2: Full Commands
Good: "Open Notepad and write my name"
Bad: "Open Notepad"

### Tip 3: Check Logs
When confused, check: `logs/` folder for what LUCIUS heard

### Tip 4: Microphone Position
Keep microphone 6-12 inches away, facing you

### Tip 5: Quiet Environment
Reduce background noise for better recognition

---

## 📱 File Structure
```
LUCIUS/
├── main.py                 # Run this to start
├── voice_engine.py         # Speech processing
├── command_handler.py      # Command parsing
├── actions.py              # Command execution
├── logger_config.py        # Logging
├── requirements.txt        # Dependencies
├── README.md              # Full documentation
├── SETUP.md               # Installation guide
├── ADDING_COMMANDS.md     # Extension guide
└── logs/                  # Auto-created logs
```

---

## 🎉 GET STARTED NOW!

```bash
python main.py
```

Then say: **"Hello Lucius"**

Enjoy! 🚀

