# chatbot-skincare
A simple Python chatbot that gives personalized skincare advice based on your skin type.

##  How It Works
The user answers a few questions about their skin type (oily, dry, combination, sensitive),
and the chatbot recommends a skincare routine and tips tailored to their profile.

##  Features
- Skin type detection through conversation
- Personalized skincare advice
- Lightweight and easy to use
- No internet connection required

##  Tech Stack
- Python
- JSON (for storing advice/responses)
- ChatterBot library

##  How to Run
1. Clone the repository
   git clone https://github.com/wala-boubaker/chatbot-skincare.git

2. Install dependencies
   pip install chatterbot

3. Run the chatbot
   python using_chatterbot.py

##  Project Structure
chatbot-skincare/
├── chat/                  # Chat logic
├── report/                # Reports
├── training_pairs.json    # Q&A training data
├── using_chatterbot.py    # Main file
├── interface.py           # User interface
└── exp.py                 # Experiments

