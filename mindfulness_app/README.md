# Mindfulness Mobile Application

A Python-based mobile application focused on mindfulness and stress relief to support users in managing anxiety, improving focus, and maintaining emotional well-being.

## Features

- User Authentication
  - Secure login and registration
  - Password hashing for security
  
- Meditation Sessions
  - Guided meditation audio sessions
  - Breathing exercises
  - Daily affirmations
  
- Mood Tracking
  - Daily mood logging
  - Personal notes
  - Mood history visualization
  - Personalized wellness tips
  
- Chatbot Assistant
  - Conversational support
  - Guided mindfulness routines
  - Emotional support responses
  
## Installation

1. Clone the repository
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Requirements

- Python 3.7+
- Kivy 2.2.1
- Passlib 1.7.4
- SQLite3

## Project Structure

- `main.py`: Main application file with UI screens
- `auth.py`: User authentication management
- `meditation.py`: Meditation sessions and exercises
- `mood_tracker.py`: Mood tracking and history
- `chatbot.py`: Chatbot assistant functionality
- `mindfulness.kv`: Kivy UI design file

## Usage

1. Register a new account or login
2. Access meditation sessions from the home screen
3. Track your daily mood and view history
4. Chat with the mindfulness assistant for support

## Note

This application uses SQLite for data storage and includes sample meditation audio files. For production use, you should:

1. Add proper error handling
2. Implement session management
3. Add proper audio files in the meditation_audio directory
4. Implement a more sophisticated chatbot system