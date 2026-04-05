"""
Voice Engine Module
Handles speech recognition (STT) and text-to-speech (TTS)
Uses SpeechRecognition for microphone input and pyttsx3 for voice output
"""

import speech_recognition as sr
import pyttsx3
import logging
from logger_config import setup_logger

logger = setup_logger("VoiceEngine")


class VoiceEngine:
    """
    Manages all voice-related operations.
    - Speech-to-Text (listening and transcription)
    - Text-to-Speech (spoken responses)
    """

    def __init__(self):
        """Initialize speech recognizer and TTS engine."""
        logger.info("Initializing Voice Engine...")

        # Initialize speech recognizer
        try:
            self.recognizer = sr.Recognizer()
            self.microphone = sr.Microphone()

            # Adjust recognizer settings for better accuracy
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                logger.info("✓ Microphone calibrated")

        except Exception as e:
            logger.critical(f"Failed to initialize recognizer/microphone: {str(e)}")
            raise

        # Initialize TTS engine
        try:
            self.tts_engine = pyttsx3.init()
            self._configure_tts()
            logger.info("✓ Text-to-Speech engine initialized")
        except Exception as e:
            logger.critical(f"Failed to initialize TTS: {str(e)}")
            raise

    def _configure_tts(self):
        """Configure TTS engine for optimal performance."""
        try:
            # Set speech rate (words per minute)
            self.tts_engine.setProperty("rate", 150)

            # Set volume (0.0 to 1.0)
            self.tts_engine.setProperty("volume", 0.9)

            # Get and set voice (prefer female voice if available)
            voices = self.tts_engine.getProperty("voices")
            if len(voices) > 1:
                self.tts_engine.setProperty("voice", voices[1].id)
            else:
                self.tts_engine.setProperty("voice", voices[0].id)

            logger.debug(f"TTS voice set to: {self.tts_engine.getProperty('voice')}")
        except Exception as e:
            logger.warning(f"Could not fully configure TTS: {str(e)}")

    def listen_for_audio(self, timeout=10):
        """
        Listen for audio input from microphone.

        Args:
            timeout (int): Seconds to listen (default: 10)

        Returns:
            AudioData object or None if no speech detected
        """
        try:
            with self.microphone as source:
                logger.debug("Listening for audio...")
                try:
                    audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=10)
                    logger.debug("Audio captured successfully")
                    return audio
                except sr.UnknownValueError:
                    logger.debug("No speech detected in the audio")
                    return None
                except sr.RequestError as e:
                    logger.warning(f"Could not request results: {str(e)}")
                    return None

        except Exception as e:
            logger.error(f"Error while listening: {str(e)}")
            return None

    def transcribe_audio(self, audio):
        """
        Convert audio to text using Google Speech Recognition.

        Args:
            audio (AudioData): Audio data to transcribe

        Returns:
            str: Transcribed text or empty string if failed
        """
        if audio is None:
            return ""

        try:
            logger.debug("Transcribing audio...")
            # Use Google Speech Recognition API
            text = self.recognizer.recognize_google(audio, language="en-US")
            logger.info(f"Transcribed: {text}")
            return text

        except sr.UnknownValueError:
            logger.warning("Could not understand audio")
            return ""
        except sr.RequestError as e:
            logger.error(f"Could not request results from Google STT: {str(e)}")
            return ""
        except Exception as e:
            logger.error(f"Unexpected error during transcription: {str(e)}")
            return ""

    def speak(self, text):
        """
        Convert text to speech and play it.

        Args:
            text (str): Text to speak
        """
        if not text or not isinstance(text, str):
            logger.warning("Invalid text provided to speak()")
            return

        try:
            logger.info(f"Speaking: {text}")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
            logger.debug("Speech completed")

        except Exception as e:
            logger.error(f"Error during text-to-speech: {str(e)}")

    def cleanup(self):
        """Clean up resources."""
        try:
            if self.tts_engine:
                self.tts_engine.stop()
            logger.info("Voice engine cleaned up")
        except Exception as e:
            logger.warning(f"Error during cleanup: {str(e)}")
