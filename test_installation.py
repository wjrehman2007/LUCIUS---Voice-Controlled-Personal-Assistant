"""
LUCIUS Installation Test Script
Tests all dependencies and components before running main application
Run this BEFORE running main.py to verify installation
"""

import sys
import os

print("\n" + "=" * 60)
print("LUCIUS - Installation Verification Test")
print("=" * 60 + "\n")

test_results = {
    "Python Version": False,
    "SpeechRecognition": False,
    "pyttsx3": False,
    "pyautogui": False,
    "Microphone": False,
    "Speaker": False,
}

# =====================================================================
# TEST 1: Python Version
# =====================================================================
print("[1/6] Checking Python Version...")
py_version = sys.version_info
if py_version.major == 3 and py_version.minor >= 8:
    print(f"✓ Python {py_version.major}.{py_version.minor}.{py_version.micro} - OK")
    test_results["Python Version"] = True
else:
    print(f"✗ Python {py_version.major}.{py_version.minor} is too old. Need 3.8+")
    test_results["Python Version"] = False

# =====================================================================
# TEST 2: SpeechRecognition
# =====================================================================
print("\n[2/6] Checking SpeechRecognition...")
try:
    import speech_recognition as sr

    print(f"✓ SpeechRecognition {sr.__version__} - OK")
    test_results["SpeechRecognition"] = True
except ImportError as e:
    print(f"✗ SpeechRecognition not installed: {e}")
    print("  Run: pip install -r requirements.txt")
    test_results["SpeechRecognition"] = False

# =====================================================================
# TEST 3: pyttsx3
# =====================================================================
print("\n[3/6] Checking pyttsx3...")
try:
    import pyttsx3

    engine = pyttsx3.init()
    print(f"✓ pyttsx3 - OK")
    print(f"  Available voices: {len(engine.getProperty('voices'))}")
    test_results["pyttsx3"] = True
except Exception as e:
    print(f"✗ pyttsx3 error: {e}")
    print("  Run: pip install -r requirements.txt")
    test_results["pyttsx3"] = False

# =====================================================================
# TEST 4: pyautogui
# =====================================================================
print("\n[4/6] Checking pyautogui...")
try:
    import pyautogui

    print(f"✓ pyautogui - OK")
    test_results["pyautogui"] = True
except ImportError as e:
    print(f"✗ pyautogui not installed: {e}")
    print("  Run: pip install -r requirements.txt")
    test_results["pyautogui"] = False

# =====================================================================
# TEST 5: Microphone
# =====================================================================
print("\n[5/6] Checking Microphone...")
try:
    import speech_recognition as sr

    mic = sr.Microphone()
    recognizer = sr.Recognizer()

    print("  Microphone found, testing audio input...")
    print("  🎤 Please speak something for 3 seconds...")

    with mic as source:
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            # Try to listen
            audio = recognizer.listen(source, timeout=3)
            print("✓ Microphone - OK (Audio captured)")
            test_results["Microphone"] = True
        except sr.UnknownValueError:
            print("✓ Microphone - OK (No speech detected, but working)")
            test_results["Microphone"] = True
        except sr.RequestError as e:
            print(f"⚠ Microphone works but network issue: {e}")
            test_results["Microphone"] = True

except Exception as e:
    print(f"✗ Microphone error: {e}")
    print("  Check Windows Sound Settings:")
    print("  Settings → Sound → Check 'Input device'")
    test_results["Microphone"] = False

# =====================================================================
# TEST 6: Speaker (TTS)
# =====================================================================
print("\n[6/6] Checking Speaker...")
try:
    import pyttsx3

    engine = pyttsx3.init()
    print("  Testing Text-to-Speech...")
    print("  🔊 You should hear a beep...")

    engine.say("LUCIUS installation test successful")
    engine.runAndWait()

    print("✓ Speaker - OK")
    test_results["Speaker"] = True

except Exception as e:
    print(f"✗ Speaker error: {e}")
    print("  Check Windows Volume and Speaker Settings")
    test_results["Speaker"] = False

# =====================================================================
# RESULTS SUMMARY
# =====================================================================
print("\n" + "=" * 60)
print("TEST RESULTS SUMMARY")
print("=" * 60)

all_passed = True
for test_name, passed in test_results.items():
    status = "✓ PASS" if passed else "✗ FAIL"
    print(f"{status:8} - {test_name}")
    if not passed:
        all_passed = False

print("=" * 60)

if all_passed:
    print("\n✓ ALL TESTS PASSED!")
    print("\nYou're ready to run LUCIUS:")
    print("  python main.py")
    sys.exit(0)
else:
    print("\n✗ SOME TESTS FAILED")
    print("\nFix the issues above and run this test again:")
    print("  python test_installation.py")
    print("\nCommon fixes:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Check microphone in Windows Sound Settings")
    print("3. Increase speaker volume")
    print("4. Restart Python/Command Prompt")
    sys.exit(1)
