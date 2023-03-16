import openai
import streamlit as st
#from charset_normalizer import md__mypyc
import config

openai.api_key=config.api_key

def main():
    st.title("Paraphraser")
    notes = st.text_area("Enter Text to Paraphrase:")
    if st.button("Generate Writeup"):
        with st.spinner("Generating Writeup ..."):
            response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[{"role":"user","content"="write long literature review with references and in-line citations on topic \n\n{notes}\n\nDescription:"}]
              #temperature=0.7,
              #max_tokens=3000,
              #top_p=1,
              #frequency_penalty=0,
              #presence_penalty=0
            )
        description = response['choices'][0]['message']['content']
        st.subheader("Generated Writeup:")
        st.write(description)


if __name__ == '__main__':
   main()
