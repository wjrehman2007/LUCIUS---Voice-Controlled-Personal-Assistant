"""
LUCIUS Configuration File
Customize voice, behavior, and settings here
"""

# =====================================================================
# VOICE & AUDIO SETTINGS
# =====================================================================

# Text-to-Speech (TTS) Settings
TTS_SPEECH_RATE = 150  # Words per minute (100-250, lower=slower, higher=faster)
TTS_VOLUME = 0.9  # Volume level (0.0 to 1.0)
TTS_VOICE = "female"  # "female" or "male" (if available)

# Speech Recognition Settings
SPEECH_RECOGNITION_TIMEOUT = 10  # Seconds to listen for speech (default: 10)
SPEECH_RECOGNITION_LANGUAGE = "en-US"  # Language code
AMBIENT_NOISE_DURATION = 1  # Seconds to calibrate microphone (1-5)

# =====================================================================
# WAKE WORD SETTINGS
# =====================================================================

# Wake words that activate LUCIUS
WAKE_WORDS = ["hello lucius", "hey lucius"]

# Exit words to return to sleep mode
EXIT_WORDS = ["exit", "quit", "goodbye", "bye"]

# =====================================================================
# COMMAND MODE SETTINGS
# =====================================================================

# Exit command mode after N consecutive silences
SILENCE_THRESHOLD = 2  # Exit after 2 silences

# Commands that require explicit confirmation
CONFIRMATION_REQUIRED_COMMANDS = ["system_shutdown", "system_restart"]

# =====================================================================
# SYSTEM SHUTDOWN/RESTART SETTINGS
# =====================================================================

# Delay before actual shutdown/restart (in seconds)
# Gives user time to cancel with: shutdown /a
SHUTDOWN_DELAY_SECONDS = 10

# =====================================================================
# APPLICATION PATHS
# =====================================================================

# Custom application paths (leave blank to use system PATH)
CHROME_PATH = None  # e.g., r"C:\Program Files\Google\Chrome\Application\chrome.exe"
EDGE_PATH = None  # e.g., r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
NOTEPAD_PATH = None  # Usually system default

# =====================================================================
# LOGGING SETTINGS
# =====================================================================

# Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_LEVEL = "INFO"

# Maximum log file size in MB (auto-rotate when exceeded)
LOG_MAX_SIZE_MB = 10

# Number of log files to keep
LOG_BACKUP_COUNT = 5

# =====================================================================
# FEATURE FLAGS
# =====================================================================

# Enable/disable features
ENABLE_WEB_SEARCH = True
ENABLE_TEXT_AUTOMATION = True
ENABLE_SYSTEM_CONTROL = True
ENABLE_TIME_QUERIES = True
ENABLE_COMMAND_HISTORY = True

# =====================================================================
# ADVANCED SETTINGS
# =====================================================================

# Default search engine
DEFAULT_SEARCH_ENGINE = "google"  # "google", "bing", "duckduckgo"

# Enable/disable confirmation messages
VERBOSE_MODE = True  # Speak confirmations and status

# Automatically open system default browser (vs Chrome)
USE_DEFAULT_BROWSER = False

# Text typing speed (seconds per character, lower=faster)
TEXT_TYPING_SPEED = 0.02

# =====================================================================
# DEVELOPER SETTINGS
# =====================================================================

# Enable debug mode (more verbose logging)
DEBUG_MODE = False

# Print command parsing details
DEBUG_COMMAND_PARSING = False

# Log all voice input (useful for training/debugging)
LOG_ALL_SPEECH = False
