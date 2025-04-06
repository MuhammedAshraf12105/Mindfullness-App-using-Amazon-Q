import json
from datetime import datetime

class ChatbotAssistant:
    def __init__(self):
        self.conversation_history = []
        self.mindfulness_responses = self.load_responses()
    
    def load_responses(self):
        # In a real implementation, this would integrate with Amazon Q
        # For now, we'll use a simple dictionary of responses
        return {
            "stress": [
                "Let's try a simple breathing exercise together. Breathe in for 4 counts, hold for 4, and release for 4.",
                "Would you like to try a quick meditation session to help reduce stress?",
                "Remember that stress is temporary. Let's focus on what you can control right now."
            ],
            "anxiety": [
                "I hear that you're feeling anxious. Let's ground ourselves with a simple exercise.",
                "Can you name 5 things you can see right now? This can help bring you to the present moment.",
                "Would you like to try a guided relaxation exercise?"
            ],
            "meditation": [
                "What type of meditation interests you? We have breathing exercises, body scans, and loving-kindness meditations.",
                "Even a few minutes of meditation can make a difference. Shall we start with a 5-minute session?",
                "Remember, there's no 'right' way to meditate. It's about being present with whatever arises."
            ]
        }
    
    def get_response(self, user_input):
        # Simple keyword matching for demo purposes
        user_input = user_input.lower()
        response = "I'm here to support your mindfulness journey. Would you like to try a meditation or breathing exercise?"
        
        for key in self.mindfulness_responses:
            if key in user_input:
                from random import choice
                response = choice(self.mindfulness_responses[key])
        
        self.conversation_history.append({
            'user': user_input,
            'bot': response,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
        return response
    
    def get_conversation_history(self):
        return self.conversation_history
    
    def clear_conversation(self):
        self.conversation_history = []