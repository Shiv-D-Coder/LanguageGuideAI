#  🤖 LanguageGuideAI

Welcome to **LanguageGuideAI**! This application serves as a personalized language learning assistant, offering support in various languages. You can interact with the app to practice conversations, ask questions about grammar and vocabulary, and more.

##  🚀 Features

- **Multilingual Support:** Practice and learn languages such as Spanish, French, German, Italian, Japanese, Chinese, and Russian.
- **Personalized Interaction:** Receive tailored responses to help you learn and practice your target language.
- **Conversation History:** Keep track of your interactions with the assistant.
- **User-Friendly Interface:** A clean and intuitive interface for a smooth learning experience.

## 📍 Deployed App

Explore the live app here: [LanguageGuideAI](https://languageguideai.streamlit.app/)

##  🛠️ Installation

To run the application locally, follow these steps:


1. **Clone the Repository**

   ```bash
   git clone https://github.com/Shiv-D-Coder/ManhwaChatbot/
   cd LanguageGuideAI
   ```
   
2. **Install Dependencies**
Make sure you have Python 3.7 or higher installed. Then, create a virtual environment and install the required packages:

   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
3. **Run the app**

   ```bash
   streamlit run app.py --server.port 8051
   ```

Open your web browser and go to http://localhost:8051 to view the app.

## 🐳 Running with Docker

You can also run the app using Docker. Here’s how:

1. Build the Docker Image

   ```bash
   docker build -t lang_app:latest .
   ```
2. Run the Docker Container
   
   ```bash
   docker run -p 8051:8051 lang_app:latest
   ```
   The app will be available at http://localhost:8051.

You can also pull images directly from my Dockerhub to do that run below command

   ```bash
   docker login
   docker pull shiv37/languageguideai:latest
   ```
   
Enjoy using Manhwa Chatbot! If you have any suggestions or issues, please let me know. Happy chatting! 😊
   
