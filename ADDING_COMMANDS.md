# ADDING NEW COMMANDS TO LUCIUS
## Complete Developer Guide

---

## 🎯 OVERVIEW

LUCIUS is designed to be **easily extended** with new commands. Follow this guide to add your own features.

**The process involves 3 steps:**
1. Add command pattern to `command_handler.py`
2. Add action handler to `actions.py`
3. Test your command

---

## 📚 ARCHITECTURE OVERVIEW

LUCIUS processes commands in this order:

```
User Speech
    ↓
Voice Engine (Transcribe to Text)
    ↓
Command Handler (Parse Intent & Extract Parameters)
    ↓
Action Executor (Execute the actual command)
    ↓
Voice Response (Speak the result)
```

---

## 🔧 STEP-BY-STEP: Adding a New Command

### Example: Add a "Calculator" Command
Let's add the ability to perform simple math: *"Calculate 5 plus 3"*

---

### STEP 1: Add Command Pattern to `command_handler.py`

Open `command_handler.py` and find the `_define_commands()` method.

**Current structure:**
```python
def _define_commands(self):
    commands = {
        "time": { ... },
        "search": { ... },
        # ... other commands
    }
```

**Add your new command:**
```python
"calculator": {
    "patterns": [
        r"calculate\s+(.+)",
        r"(what\s+is\s+)?(\d+)\s+(\+|-|\*|/)\s+(\d+)",
        r"math\s+(.+)",
    ],
    "intent": "calculate",
    "requires_confirmation": False,
    "capture_group": 1,
},
```

**Explanation:**
- `"calculator"`: Command identifier (unique name)
- `"patterns"`: List of regex patterns that match user speech
  - User says: "Calculate 5 plus 3"
  - Matches pattern: `r"calculate\s+(.+)"`
  - Captures: "5 plus 3" as group 1
- `"intent"`: Intent type (maps to action type)
- `"requires_confirmation"`: Whether to ask for permission first
- `"capture_group"`: Which regex group to extract as parameter

---

### STEP 2: Add Handler to `actions.py`

Open `actions.py` and add the execution logic.

**Add to the `__init__` method:**
```python
self.action_map = {
    # ... existing actions
    "calculate": self.calculate,  # ← Add this line
}
```

**Add the actual handler method:**
```python
def calculate(self, params):
    """
    Perform simple mathematical calculations.
    
    Args:
        params (dict): Action parameters containing 'query' (math expression)
        
    Returns:
        str: Calculation result as spoken response
    """
    expression = params.get("query", "").strip()
    
    if not expression:
        return "Please provide a math expression."
    
    logger.info(f"Calculating: {expression}")
    
    try:
        # Simple evaluation (for production, use safer method)
        # Replace word-based operators with symbols
        expression = expression.lower()
        expression = expression.replace("plus", "+")
        expression = expression.replace("minus", "-")
        expression = expression.replace("times", "*")
        expression = expression.replace("divided by", "/")
        
        # Evaluate the expression
        result = eval(expression)
        
        response = f"The answer is {result}."
        logger.info(f"Calculation result: {result}")
        return response
        
    except Exception as e:
        logger.error(f"Calculation error: {str(e)}")
        return f"Sorry, I couldn't calculate that: {str(e)}"
```

---

### STEP 3: Update Command Mapping (if needed)

The command handler automatically maps intents to actions using `_intent_to_action()`.

**If your intent is new, add it to the map:**
```python
def _intent_to_action(self, intent, parameters):
    action_map = {
        # ... existing mappings
        "calculate": "calculate",  # ← Add this line
    }
    return action_map.get(intent, "unknown")
```

---

### STEP 4: Test Your Command

1. **Run LUCIUS:**
   ```bash
   python main.py
   ```

2. **Say the wake word:**
   "Hello Lucius"

3. **Test your command:**
   - "Calculate 5 plus 3"
   - "What is 10 times 2"
   - "Math 100 divided by 4"

4. **Check the logs:**
   ```bash
   # View the latest log file
   type logs\lucius_YYYYMMDD_HHMMSS.log
   ```

---

## 🎨 ADVANCED PATTERNS

### Pattern with Multiple Captures

```python
"flight_search": {
    "patterns": [
        r"search\s+flights\s+from\s+(\w+)\s+to\s+(\w+)",
    ],
    "intent": "search_flights",
    "capture_group": 1,  # First parentheses group
},
```

**Usage:**
```python
def search_flights(self, params):
    origin = params.get("query", "")  # From capture group 1
    # For group 2, you'd need custom extraction
    # See Advanced section below
```

### Optional Parameters

```python
"reminder": {
    "patterns": [
        r"remind\s+me\s+(?:to\s+)?(?:in\s+)?(\d+)\s+(minutes?|hours?|days?)",
    ],
    "intent": "set_reminder",
},
```

### Multiple Captures (Advanced)

For multiple capture groups, customize the handler:

```python
def parse_command(self, text):
    # ... existing code ...
    
    # Custom extraction for flight search
    if command_name == "flight_search":
        match = re.search(patterns[0], text_lower)
        if match:
            parameters = {
                "intent": "search_flights",
                "origin": match.group(1),
                "destination": match.group(2),
            }
            return "search_flights", parameters
```

---

## 📋 EXAMPLE COMMANDS TO ADD

### 1. **Set an Alarm**
```python
"alarm": {
    "patterns": [
        r"set\s+an?\s+alarm\s+(?:for\s+)?(\d{1,2}):?(\d{2})?\s+(am|pm)?",
        r"alarm\s+(?:for\s+)?(\d{1,2}):?(\d{2})?",
    ],
    "intent": "set_alarm",
    "requires_confirmation": True,
},
```

### 2. **Open a File**
```python
"open_file": {
    "patterns": [
        r"open\s+(?:the\s+)?(?:file\s+)?(.+)",
    ],
    "intent": "open_file",
},
```

### 3. **Take a Screenshot**
```python
"screenshot": {
    "patterns": [
        r"take\s+a?\s+screenshot",
        r"screenshot",
    ],
    "intent": "take_screenshot",
},
```

### 4. **Send an Email (if configured)**
```python
"send_email": {
    "patterns": [
        r"send\s+(?:an?\s+)?email\s+(?:to\s+)?(.+)",
    ],
    "intent": "send_email",
},
```

---

## 🛡️ BEST PRACTICES

### 1. **Handle Errors Gracefully**
```python
try:
    # Your action code
    result = do_something()
    return f"Success: {result}"
except Exception as e:
    logger.error(f"Error: {str(e)}")
    return f"Sorry, something went wrong: {str(e)}"
```

### 2. **Log Everything**
```python
logger.info(f"Command executed: {action}")
logger.debug(f"Parameters: {params}")
logger.warning(f"Potentially dangerous action: {action}")
logger.error(f"Error occurred: {str(e)}")
```

### 3. **Use Threading for Long Operations**
```python
import threading

def long_running_action(self, params):
    def background_task():
        # Your long operation here
        time.sleep(5)
    
    thread = threading.Thread(target=background_task, daemon=True)
    thread.start()
    return "Starting operation in background..."
```

### 4. **Add User Confirmations**
```python
if params.get("requires_confirmation"):
    # User was already warned during parsing
    logger.info("User confirmed dangerous action")
```

### 5. **Provide Clear Feedback**
```python
# Good ✓
"Opened Chrome and searching for Peshawar news"

# Bad ✗
"Done"
```

---

## 🔍 REGEX PATTERN GUIDE

### Common Patterns

| Pattern | Matches |
|---------|---------|
| `r"hello"` | "hello" anywhere in text |
| `r"^hello"` | "hello" at start |
| `r"hello$"` | "hello" at end |
| `r"hel+o"` | "helo", "hello", "helllo", etc |
| `r"(\w+)"` | Captures one word |
| `r"(\d+)"` | Captures numbers |
| `r"(.*)"` | Captures anything |
| `r"(.*?),"` | Captures until comma (non-greedy) |

### Building Complex Patterns

```python
# User says: "Search flights from Karachi to London tomorrow"
patterns = [
    r"search\s+flights\s+from\s+(\w+)\s+to\s+(\w+)(?:\s+(.+))?",
]
# Group 1: origin (Karachi)
# Group 2: destination (London)
# Group 3: optional date (tomorrow)
```

---

## 📊 COMMAND STATISTICS

Track command usage by adding to logger:

```python
def execute_command(self, action, parameters):
    logger.info(f"COMMAND_STAT: action={action}, params={parameters}")
    # Rest of code
```

Then analyze logs:
```bash
grep "COMMAND_STAT" logs/*.log | wc -l
```

---

## 🚀 ADVANCED PATTERNS

### Natural Language Processing (Future)

For more sophisticated NLP, you could add:

```python
# Future enhancement
from transformers import pipeline
classifier = pipeline("zero-shot-classification")

# Classify command intent automatically
result = classifier("Set a reminder for 3 PM", 
                    ["alarm", "reminder", "notification"])
```

### API Integrations

```python
def weather_api_lookup(self, params):
    """Fetch real weather data"""
    import requests
    
    try:
        response = requests.get("https://api.weather.gov/points/...")
        data = response.json()
        return f"Temperature is {data['temperature']} degrees"
    except Exception as e:
        logger.error(f"API error: {str(e)}")
        return "Couldn't fetch weather data"
```

---

## 🧪 TESTING

### Unit Test Example

Create `test_commands.py`:

```python
from command_handler import CommandHandler
from actions import ActionExecutor

def test_calculator():
    handler = CommandHandler()
    
    # Test command parsing
    action, params = handler.parse_command("Calculate 5 plus 3")
    assert action == "calculate"
    assert params["query"] == "5 plus 3"
    
    # Test execution
    executor = ActionExecutor()
    result = executor.execute(action, params)
    print(f"Result: {result}")

if __name__ == "__main__":
    test_calculator()
```

Run it:
```bash
python test_commands.py
```

---

## 💡 TIPS

1. **Start Simple**: Add basic commands first
2. **Use Descriptive Names**: `calculate_math` is better than `calc`
3. **Test Thoroughly**: Try different phrasings
4. **Check Logs**: Always review `logs/` for issues
5. **Version Control**: Keep track of changes

---

## 📞 COMMON ISSUES

### Issue: "Command not recognized"
**Solution:**
- Check regex pattern matches your test input
- Run test separately: `re.search(pattern, test_text)`
- Add `logger.debug()` statements

### Issue: "Parameter not extracted"
**Solution:**
- Check capture group number
- Verify regex parentheses
- Test regex at https://regex101.com

### Issue: "Action doesn't execute"
**Solution:**
- Ensure method exists in ActionExecutor
- Check action_map includes your action
- Review logs for specific error

---

## 🎯 NEXT STEPS

1. ✅ Pick a new command to add
2. ✅ Follow the 4-step process
3. ✅ Test it thoroughly
4. ✅ Share your additions!

Happy extending LUCIUS! 🚀

