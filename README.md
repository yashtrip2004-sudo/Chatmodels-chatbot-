# ChatModels

A collection of conversational AI chat models built with LangChain, HuggingFace, and Streamlit. This project includes both terminal-based chatbots and a dynamic graphical user interface app.

## Features
- **Pink AI Chat (UI)**: A beautifully designed Streamlit interface offering different conversational personalities (Funny, Sad, Sarcastic).
- **CLI Chatbots**: Multiple terminal-based chatbot variants (standard, huggingface direct, and a local tiny-llama implementation).

## Getting Started

### Prerequisites
- Python 3.8+
- HuggingFace API Token

### Installation
1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your HuggingFace API Token:
   ```
   HF_TOKEN=your_token_here
   ```

### Usage
- **Run the Streamlit UI:**
  ```bash
  streamlit run uichatbot.py
  ```
- **Run the CLI Chatbots:**
  ```bash
  python chatbot.py
  # or
  python huggingface.py
  # or
  python localmodel.py
  ```
