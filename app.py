import streamlit as st
from huggingface_hub import InferenceClient
import os

# MUST SET HF_TOKEN IN STREAMLIT SETTINGS IN HUGGINGFACE REPO SECRETS
HF_TOKEN = os.environ["HF_TOKEN"]

# INIT THE INFERENCE CLIENT WITH YOUR HF TOKEN
client = InferenceClient(
    provider="fireworks-ai",
    api_key=HF_TOKEN,
)

# THIS IS JUST THE streamlit TEXT INPUT WIDGET
user_input = st.text_input(
    "Place your prompt here",
    "This is a placeholder",
    key="placeholder",
)

# THIS IS THE INFERENCE CLIENT CALL
completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
    messages=[
        {
            "role": "user",
            "content": user_input
        }
    ],
    max_tokens=512,
)

# THIS IS THE RESPONSE FROM THE INFERENCE CLIENT
ai_response = completion.choices[0].message.content

# THIS IS THE STREAMLIT TEXT OUTPUT WIDGET WITH THE RESPONSE FROM THE INFERENCE CLIENT
st.text(ai_response)


### WRONG WAY TO TRY AND LOAD MODELS::: 
# Load model directly
# from transformers import AutoTokenizer, AutoModelForCausalLM

# tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-Prover-V2-671B", trust_remote_code=True)
# model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-Prover-V2-671B", trust_remote_code=True)