import streamlit as st
from huggingface_hub import InferenceClient


# MUST SET HF_TOKEN IN STREAMLIT SETTINGS IN HUGGINGFACE REPO SECRETS
HF_TOKEN = st.secrets["HF_TOKEN"]



# INIT THE INFERENCE CLIENT WITH YOUR HF TOKEN
client = InferenceClient(
    provider="hf-inference",
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
    model="HuggingFaceH4/zephyr-7b-beta",
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
## THESE WILL TRY AND DOWNLOAD AND LOAD THE MODEL EVERY TIME SOMEONE VISITS THE APP

### PIPELINE WAY
# from transformers import pipeline
# messages = [
#     {"role": "user", "content": "Who are you?"},
# ]
# pipe = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta")
# pipe(messages)

### DIRECT WAY
# Load model directly
# from transformers import AutoTokenizer, AutoModelForCausalLM

# tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-Prover-V2-671B", trust_remote_code=True)
# model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-Prover-V2-671B", trust_remote_code=True)