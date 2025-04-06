from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from auth import AuthManager
from mood_tracker import MoodTracker
from kivy.properties import StringProperty
from meditation import MeditationManager
from chatbot import ChatbotAssistant

class MindfulnessApp(App):
    def build(self):
        self.screen_manager = ScreenManager()
        
        # Initialize managers
        self.auth_manager = AuthManager()
        self.mood_tracker = MoodTracker()
        self.meditation_manager = MeditationManager()
        self.chatbot = ChatbotAssistant()
        
        # Add screens
        self.screen_manager.add_widget(LoginScreen(name='login'))
        self.screen_manager.add_widget(HomeScreen(name='home'))
        self.screen_manager.add_widget(MeditationScreen(name='meditation'))
        self.screen_manager.add_widget(MoodTrackerScreen(name='mood'))
        self.screen_manager.add_widget(ChatbotScreen(name='chatbot'))
        
        return self.screen_manager

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(layout)
        
        layout.add_widget(Label(text='Mindfulness App'))
        layout.add_widget(Button(text='Login', on_press=self.login))
        layout.add_widget(Button(text='Register', on_press=self.register))
    
    def login(self, instance):
        # Implement login logic
        self.manager.current = 'home'
    
    def register(self, instance):
        # Implement registration logic
        pass

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(layout)
        
        layout.add_widget(Label(text='Welcome to Mindfulness'))
        layout.add_widget(Button(text='Meditation Sessions', on_press=self.goto_meditation))
        layout.add_widget(Button(text='Mood Tracker', on_press=self.goto_mood))
        layout.add_widget(Button(text='Chat with Assistant', on_press=self.goto_chatbot))
        layout.add_widget(Button(text='Logout', on_press=self.logout))
    
    def goto_meditation(self, instance):
        self.manager.current = 'meditation'
    
    def goto_mood(self, instance):
        self.manager.current = 'mood'
    
    def goto_chatbot(self, instance):
        self.manager.current = 'chatbot'
    
    def logout(self, instance):
        self.manager.current = 'login'

class MeditationScreen(Screen):
    current_affirmation = StringProperty("You are calm, strong, and capable.")  # <-- This is the key addition

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(layout)

        layout.add_widget(Label(text='Meditation Sessions'))

        # Add meditation session buttons
        for session in App.get_running_app().meditation_manager.get_available_sessions():
            session_info = App.get_running_app().meditation_manager.get_session_info(session)
            btn = Button(
                text=f"{session}\n{session_info['description']}\nDuration: {session_info['duration']}s",
                size_hint_y=None,
                height='100dp'
            )
            btn.bind(on_press=lambda x, s=session: self.start_session(s))
            layout.add_widget(btn)

        layout.add_widget(Button(text='Back to Home', on_press=self.goto_home))

    def start_session(self, session_name):
        App.get_running_app().meditation_manager.play_session(session_name)

    def goto_home(self, instance):
        self.manager.current = 'home'


class MoodTrackerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(layout)
        
        layout.add_widget(Label(text='How are you feeling today?'))
        
        self.mood_slider = Slider(min=1, max=5, value=3, step=1)
        layout.add_widget(self.mood_slider)
        
        self.mood_note = TextInput(
            hint_text='Add any notes about your mood...',
            multiline=True,
            size_hint_y=None,
            height='100dp'
        )
        layout.add_widget(self.mood_note)
        
        layout.add_widget(Button(text='Save Mood', on_press=self.save_mood))
        layout.add_widget(Button(text='View History', on_press=self.show_history))
        layout.add_widget(Button(text='Back to Home', on_press=self.goto_home))
    
    def save_mood(self, instance):
        mood_level = int(self.mood_slider.value)
        notes = self.mood_note.text
        # In a real app, you'd get the user_id from the session
        App.get_running_app().mood_tracker.record_mood(1, mood_level, notes)
        # Show the wellness tip
        tip = App.get_running_app().mood_tracker.get_wellness_tips(mood_level)
        self.mood_note.text = ''  # Clear the note field
        # You might want to show the tip in a popup or label
    
    def show_history(self, instance):
        # In a real app, you'd get the user_id from the session
        history = App.get_running_app().mood_tracker.get_mood_history(1)
        # You might want to show this in a popup or new screen
    
    def goto_home(self, instance):
        self.manager.current = 'home'

class ChatbotScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(layout)
        
        layout.add_widget(Label(text='Chat with your Mindfulness Assistant'))
        
        self.chat_history = TextInput(
            readonly=True,
            multiline=True,
            size_hint_y=0.7
        )
        layout.add_widget(self.chat_history)
        
        self.user_input = TextInput(
            hint_text='Type your message here...',
            size_hint_y=0.1,
            multiline=False
        )
        self.user_input.bind(on_text_validate=self.send_message)
        layout.add_widget(self.user_input)
        
        layout.add_widget(Button(text='Send', on_press=self.send_message))
        layout.add_widget(Button(text='Back to Home', on_press=self.goto_home))
    
    def send_message(self, instance):
        user_message = self.user_input.text
        if user_message.strip():
            response = App.get_running_app().chatbot.get_response(user_message)
            self.chat_history.text += f"\nYou: {user_message}\nAssistant: {response}\n"
            self.user_input.text = ''  # Clear the input field
    
    def goto_home(self, instance):
        self.manager.current = 'home'

if __name__ == '__main__':
    MindfulnessApp().run()