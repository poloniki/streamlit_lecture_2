import streamlit as st
from openai import OpenAI

st.balloons()
client = OpenAI(api_key=st.secrets["API_KEY"])

st.title("Angry investor: GPT powered")

if prompt := st.chat_input("Pitch"):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("ai"):
        placeholder = st.empty()
        message = ""

        for response in client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are angry investor. Give me ironic evaluation of my pitch. Be brief and sarcastic.",
                },
                {"role": "user", "content": prompt},
            ],
            model="gpt-4",
            stream=True,
        ):
            message += response.choices[0].delta.content or ""
            placeholder.markdown(message)
