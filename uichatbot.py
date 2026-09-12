import os
import streamlit as st
from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

token = os.getenv("HF_TOKEN")

if not token:
    raise ValueError("HF_TOKEN not found in .env")

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    huggingfacehub_api_token=token,
)

model = ChatHuggingFace(llm=llm)


st.set_page_config(
    page_title="Pink AI Chat",
    page_icon="🌸",
    layout="centered"
)


st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(
            135deg,
            #fff6fa,
            #ffe8f1,
            #fff8fb
        );
    }

    .block-container {
        max-width: 850px;
        padding-top: 2rem;
        padding-bottom: 7rem;
    }

    h1 {
        text-align: center;
        color: #8f2857;
        font-weight: 700;
        text-shadow: 0 1px 0 #ffffff;
    }

    .subtitle {
        text-align: center;
        color: #633047;
        margin-bottom: 30px;
        font-size: 16px;
    }

    [data-testid="stChatMessage"] {
        background-color: rgba(255, 255, 255, 0.75);
        border-radius: 18px;
        padding: 12px 18px;
        margin-bottom: 12px;
        border: 1px solid #f6cfdf;
        box-shadow: 0 3px 10px rgba(220, 120, 160, 0.08);
    }

    [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"],
    [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] p {
        color: #2f2430;
    }

    [data-testid="stChatInput"] {
        background-color: white;
        border-radius: 25px;
        border: 1px solid #efb8cf;
    }

    [data-testid="stChatInput"] textarea {
        color: #333333;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #6f5a66;
        opacity: 1;
    }

    .mode-box {
        background-color: rgba(255,255,255,0.65);
        padding: 15px 20px;
        border-radius: 18px;
        border: 1px solid #f3c7d8;
        margin-bottom: 25px;
    }

    div[data-testid="stCheckbox"] label {
        color: #633047;
        font-weight: 500;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.title("🌸 Pink AI Chat")

st.markdown(
    '<div class="subtitle">Choose a personality and start chatting</div>',
    unsafe_allow_html=True
)


st.markdown('<div class="mode-box">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    funny = st.checkbox("😂 Funny")

with col2:
    sad = st.checkbox("😢 Sad")

with col3:
    sarcastic = st.checkbox("😏 Sarcastic")

st.markdown("</div>", unsafe_allow_html=True)


selected_modes = sum([funny, sad, sarcastic])

if selected_modes == 0:
    st.info("Choose one chatbot personality to start chatting.")
    st.stop()

if selected_modes > 1:
    st.warning("Please select only one personality.")
    st.stop()


if funny:
    mode = "funny"
    system_prompt = "You are a funny AI agent."

elif sad:
    mode = "sad"
    system_prompt = "You are a sad AI agent."

else:
    mode = "sarcastic"
    system_prompt = "You are a sarcastic AI agent."


if "mode" not in st.session_state:
    st.session_state.mode = mode


if st.session_state.mode != mode:
    st.session_state.mode = mode
    st.session_state.messages = [
        SystemMessage(content=system_prompt)
    ]


if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=system_prompt)
    ]


for message in st.session_state.messages:

    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)


prompt = st.chat_input("Message your AI...")


if prompt:

    user_message = HumanMessage(content=prompt)

    st.session_state.messages.append(user_message)

    with st.chat_message("user"):
        st.markdown(prompt)


    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = model.invoke(
                st.session_state.messages
            )

        st.markdown(response.content)


    st.session_state.messages.append(
        AIMessage(content=response.content)
    )