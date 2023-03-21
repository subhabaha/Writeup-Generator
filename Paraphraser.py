import openai
import streamlit as st
#from charset_normalizer import md__mypyc
import config
import requests

openai.api_key=config.api_key

def main():
    st.title("Summarizer")
    st.subheader('This app has been developed by :red[Dr. Subhabaha Pal].')
    notes = st.text_area("Enter Text to summarize:")
    if st.button("Generate Writeup"):
        with st.spinner("Generating Writeup ..."):
            response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[{'role':'user','content':f'Paraphrase the text \n\n{notes}\n\nDescription:'}]
              #temperature=0.7,
              #max_tokens=3000,
              #top_p=1,
              #frequency_penalty=0,
              #presence_penalty=0
            )
            myobj = {'input': response['choices'][0]['message']['content'], 'email': config.email, 'key':config.wordai_api_key }
            x = requests.post(config.wordai_url, json = myobj)


        description = 'AI-Generated Content\n\n\n' + response['choices'][0]['message']['content'] + '\n\n\n\n' + 'Modified Content with WordAI to avoid AI Tool Detection'+'\n\n\n\n'+x.json()['text']
        st.subheader("Generated Writeup:")
        st.write(description)


if __name__ == '__main__':
   main()
