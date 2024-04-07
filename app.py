import streamlit as st
from transformers import pipeline

model_name = "gpt2"
text_generator = pipeline("text-generation", model=model_name)

def main():
    st.title("Hugging Face LLM Chatbot")

    st.write(
        "Welcome to the Hugging Face LLM Chatbot! Enter a prompt below and see how the model responds."
    )

    prompt = st.text_input("Enter your prompt here:", "")

    if st.button("Generate"):
        if prompt:
            generated_text = text_generator(prompt, max_length=150, do_sample=True)[0][
                "generated_text"
            ]
            st.write("Generated Text:")
            st.write(generated_text)
        else:
            st.error("Please enter a prompt.")

if __name__ == "__main__":
    main()
