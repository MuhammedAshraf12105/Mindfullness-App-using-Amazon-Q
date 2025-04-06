from kivy.core.audio import SoundLoader
import os

class MeditationManager:
    def __init__(self):
        self.meditation_sessions = {
            'Breathing': {
                'duration': 300,  # 5 minutes
                'description': 'Focus on your breath with this guided breathing exercise',
                'audio_file': 'meditation_audio/breathing.mp3'
            },
            'Body Scan': {
                'duration': 600,  # 10 minutes
                'description': 'Progressive relaxation through body awareness',
                'audio_file': 'meditation_audio/body_scan.mp3'
            },
            'Loving Kindness': {
                'duration': 900,  # 15 minutes
                'description': 'Develop compassion for yourself and others',
                'audio_file': 'meditation_audio/loving_kindness.mp3'
            }
        }
    
    def get_available_sessions(self):
        return list(self.meditation_sessions.keys())
    
    def get_session_info(self, session_name):
        return self.meditation_sessions.get(session_name)
    
    def play_session(self, session_name):
        session = self.meditation_sessions.get(session_name)
        if session and os.path.exists(session['audio_file']):
            sound = SoundLoader.load(session['audio_file'])
            if sound:
                sound.play()
                return True
        return False
    
    def get_breathing_exercise(self):
        return {
            'inhale': 4,  # seconds
            'hold': 4,    # seconds
            'exhale': 4,  # seconds
            'cycles': 5   # number of repetitions
        }
    
    def get_daily_affirmation(self):
        affirmations = [
            "I am calm and centered",
            "I choose to be present in this moment",
            "I am worthy of peace and happiness",
            "I release all tension and anxiety",
            "I am becoming more mindful each day"
        ]
        from random import choice
        return choice(affirmations)