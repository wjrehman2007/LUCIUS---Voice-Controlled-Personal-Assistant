"""
LUCIUS - Voice-Controlled Personal Assistant for Windows
Main entry point - Orchestrates voice listening, command processing, and execution

Author: Wajid Ur Rehman ( Software Engineer )
Version: 1.0.0
"""

import sys
import time
import logging
from voice_engine import VoiceEngine
from command_handler import CommandHandler
from logger_config import setup_logger

# Initialize logger
logger = setup_logger("LUCIUS")


class LuciusAssistant:
    """
    Main LUCIUS Assistant class.
    Coordinates voice engine, command parsing, and action execution.
    """

    def __init__(self):
        """Initialize LUCIUS with all necessary components."""
        logger.info("=" * 60)
        logger.info("LUCIUS Assistant - Initializing...")
        logger.info("=" * 60)

        try:
            self.voice_engine = VoiceEngine()
            self.command_handler = CommandHandler()
            self.is_running = False
            logger.info("✓ All components initialized successfully")
        except Exception as e:
            logger.critical(f"Failed to initialize LUCIUS: {str(e)}")
            raise

    def start(self):
        """Start LUCIUS - Begin listening for wake word."""
        self.is_running = True
        logger.info("\n" + "=" * 60)
        logger.info("🎤 LUCIUS is ACTIVE - Listening for wake word...")
        logger.info("Say: 'Hello Lucius' or 'Hey Lucius' to activate")
        logger.info("=" * 60 + "\n")

        self.voice_engine.speak("LUCIUS is online. Say hello Lucius to begin.")

        try:
            while self.is_running:
                # Listen for wake word
                wake_word_detected = self._listen_for_wake_word()

                if wake_word_detected:
                    # Enter command mode
                    self._command_mode()

        except KeyboardInterrupt:
            logger.info("\n⚠️  Keyboard interrupt detected")
            self.shutdown()
        except Exception as e:
            logger.error(f"Unexpected error in main loop: {str(e)}")
            self.shutdown()

    def _listen_for_wake_word(self):
        """
        Listen continuously for the wake word.
        Returns True when 'Hello Lucius' or 'Hey Lucius' is detected.
        """
        while self.is_running:
            try:
                audio = self.voice_engine.listen_for_audio(timeout=5)
                if audio is None:
                    continue

                text = self.voice_engine.transcribe_audio(audio)
                logger.info(f"Heard: {text}")

                if self._is_wake_word(text):
                    logger.info("✓ Wake word detected!")
                    self.voice_engine.speak("Yes, how can I help?")
                    return True

            except Exception as e:
                logger.warning(f"Wake word listening error: {str(e)}")
                continue

        return False

    def _command_mode(self):
        """
        Active command mode - Listen for user commands.
        Processes commands until user goes silent or says exit.
        """
        logger.info("\n📝 Command mode activated")
        silence_count = 0
        max_silence_threshold = 2  # Exit after 2 consecutive silences

        while self.is_running and silence_count < max_silence_threshold:
            try:
                logger.debug("Listening for command...")
                audio = self.voice_engine.listen_for_audio(timeout=5)

                if audio is None:
                    silence_count += 1
                    if silence_count >= max_silence_threshold:
                        logger.info("No input detected. Returning to wake word mode.")
                        self.voice_engine.speak("Returning to standby.")
                    continue

                silence_count = 0  # Reset silence counter
                command_text = self.voice_engine.transcribe_audio(audio)
                logger.info(f"Command: {command_text}")

                # Check for exit commands
                if self._is_exit_command(command_text):
                    logger.info("Exit command detected")
                    self.voice_engine.speak("Returning to standby.")
                    break

                # Process command
                self._process_command(command_text)

            except Exception as e:
                logger.error(f"Command processing error: {str(e)}")
                continue

    def _process_command(self, command_text):
        """
        Parse and execute the command.

        Args:
            command_text (str): The user's command as text
        """
        try:
            # Parse command and get action details
            action, parameters = self.command_handler.parse_command(command_text)

            logger.info(f"Action: {action} | Parameters: {parameters}")

            # Handle system-level commands
            if action == "unknown":
                response = "Sorry, I didn't understand that command."
                logger.warning(f"Unknown command: {command_text}")
            elif action == "no_action":
                response = parameters.get("message", "Command not recognized")
            else:
                # Execute command and get response
                response = self.command_handler.execute_command(action, parameters)

            # Speak response
            if response:
                self.voice_engine.speak(response)

        except Exception as e:
            logger.error(f"Error processing command: {str(e)}")
            error_response = "There was an error processing your command."
            self.voice_engine.speak(error_response)

    @staticmethod
    def _is_wake_word(text):
        """Check if text contains wake word."""
        wake_words = ["hello lucius", "hey lucius"]
        text_lower = text.lower().strip()
        return any(wake in text_lower for wake in wake_words)

    @staticmethod
    def _is_exit_command(text):
        """Check if text is an exit command."""
        exit_words = ["exit", "quit", "goodbye", "bye"]
        text_lower = text.lower().strip()
        return any(word in text_lower for word in exit_words)

    def shutdown(self):
        """Gracefully shutdown LUCIUS."""
        logger.info("\n" + "=" * 60)
        logger.info("🛑 LUCIUS is shutting down...")
        logger.info("=" * 60)

        self.is_running = False

        try:
            self.voice_engine.speak("Goodbye!")
            self.voice_engine.cleanup()
        except Exception as e:
            logger.error(f"Error during shutdown: {str(e)}")

        logger.info("✓ LUCIUS shutdown complete")
        sys.exit(0)


def main():
    """Entry point for LUCIUS."""
    try:
        assistant = LuciusAssistant()
        assistant.start()
    except Exception as e:
        logger.critical(f"Fatal error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
