import streamlit as st
from groq import Groq
import time

# Set Streamlit page configuration
st.set_page_config(page_title="Language Learning Assistant", page_icon=":books:")

# Define CSS for styling
st.markdown("""
    <style>
    body {
        color: #333;
        font-family: 'Arial', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #f0f0f0;
    }
    .css-18e3th9 {
        background-color: #e6e6e6;
    }
    .stButton > button {
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .submit-button > button {
        background-color: #4CAF50;
    }
    .submit-button > button:hover {
        background-color: #45a049;
    }
    .end-conversation-button > button {
        background-color: #f44336;
    }
    .end-conversation-button > button:hover {
        background-color: #d32f2f;
    }
    .chat-message {
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
        max-width: 80%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .user-message {
        background-color: #E3F2FD;
        color: #1565C0;
        align-self: flex-end;
        margin-left: 20%;
    }
    .assistant-message {
        background-color: #F5F5F5;
        color: #333;
        align-self: flex-start;
        margin-right: 20%;
    }
    .default-message {
        background-color: #FFF3E0;
        color: #E65100;
        font-style: italic;
        text-align: center;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .stTextInput > div > div > input {
        background-color: #F5F5F5;
        color: #333;
        border: 1px solid #ddd;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Add title and description to the main page
st.title("Language Learning Assistant")
st.write("Welcome to your personal language learning companion! Ask questions about grammar, vocabulary, or practice conversations in your target language.")

# Sidebar for API key and language selection
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter your Groq API key:")
    
    if api_key:
        st.write("**Choose your target language:**")

        target_language = st.selectbox(
            "Select your target language:",
            options=["Spanish", "French", "German", "Italian", "Japanese", "Chinese", "Russian"],
            index=0,
            help="Choose the language you want to learn or practice."
        )

        st.write("**How to use the app:**")
        st.write("1. Enter your Groq API key.")
        st.write("2. Select your target language.")
        st.write("3. Start learning by asking questions or practicing conversations.")
        st.write("4. You can continue your session until you press 'End Conversation'.")

        # Display session duration in sidebar
        if 'start_time' in st.session_state:
            current_time = time.time()
            session_duration = int(current_time - st.session_state.start_time)
            st.write(f"Session duration: {session_duration} seconds")

# Initialize Groq client with API key
if api_key:
    client = Groq(api_key=api_key)

    # Initialize session state for conversation history, current input, and start time
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""
    if 'clear_input' not in st.session_state:
        st.session_state.clear_input = False
    if 'start_time' not in st.session_state:
        st.session_state.start_time = time.time()
    if 'show_default_message' not in st.session_state:
        st.session_state.show_default_message = True

    # Function to clear input
    def clear_input():
        st.session_state.clear_input = True

    # Default message in the selected language
    default_messages = {
        "Spanish": "¡Hola! Estoy aquí para ayudarte a aprender español.",
        "French": "Bonjour ! Je suis là pour vous aider à apprendre le français.",
        "German": "Hallo! Ich bin hier, um Ihnen beim Deutschlernen zu helfen.",
        "Italian": "Ciao! Sono qui per aiutarti a imparare l'italiano.",
        "Japanese": "こんにちは！日本語を学ぶお手伝いをします。",
        "Chinese": "你好！我在这里帮助你学习中文。",
        "Russian": "Привет! Я здесь, чтобы помочь вам выучить русский язык."
    }
    default_message = default_messages.get(target_language, "Hello! I'm here to help you learn.")

    # Display default message
    if st.session_state.show_default_message:
        st.markdown(f"<div class='default-message'>{default_message}</div>", unsafe_allow_html=True)

    # Display conversation history
    st.write("### Learning Session")
    for entry in st.session_state.history:
        st.markdown(f"<div class='chat-message user-message'>{entry['user']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chat-message assistant-message'>{entry['response']}</div>", unsafe_allow_html=True)

    # User input for new message
    if st.session_state.clear_input:
        st.session_state.user_input = ""
        st.session_state.clear_input = False

    user_input = st.text_input(f"Ask a question or practice {target_language}:", key="user_input")

    # Submit button for sending queries
    if st.button("Submit", key="submit", help="Submit your question or phrase"):
        if user_input:
            with st.spinner("Generating response..."):
                # Construct the system message based on the target language
                system_message = f"You are a helpful language learning assistant for {target_language}. Provide explanations, translations, and engage in practice conversations. Always respond in a way that helps the user learn {target_language}."
                
                # API call
                chat_completion = client.chat.completions.create(
                    model="mixtral-8x7b-32768",
                    messages=[
                        {"role": "system", "content": system_message},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.7,
                    max_tokens=2000,
                    response_format={"type": "text"}
                )
                
                # Append user input and response to history
                st.session_state.history.append({
                    'user': user_input,
                    'response': chat_completion.choices[0].message.content
                })

                # Hide default message after first interaction
                st.session_state.show_default_message = False

                # Set flag to clear input on next rerun
                clear_input()
                st.rerun()

    # End Conversation button to clear history
    if st.button("End Conversation", key="end_conversation", help="Clear chat history"):
        st.session_state.history = []
        clear_input()
        st.session_state.start_time = time.time()  # Reset the start time
        st.session_state.show_default_message = True  # Show default message again
        st.rerun()

else:
    st.info("Please enter your Groq API key to start learning languages.")