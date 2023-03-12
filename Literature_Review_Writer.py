import openai
import streamlit as st
#from charset_normalizer import md__mypyc
import config

openai.api_key=config.api_key

def main():
    st.title("Literature Review Writer")
    st.caption('This app has been developed by :red[Dr. Subhabaha Pal].')
    st.text('The background AI model used is ChatGPT model developed by OpenAI.') 
    st.text('Please mail to subhabaha@msn.com for suggestions and improvements.')
    st.text('Please write any topic of interest in the below box to get detailed writeup.')
    notes = st.text_area("Enter Topic Information:")
    if st.button("Generate Literature Review"):
        with st.spinner("Generating Writeup and References..."):
            response = openai.Completion.create(
              model="text-davinci-003",
              prompt=f"I want you to write literature review with references and citations on below topic.\n\n{notes}\n\nDescription:",
              temperature=0.7,
              max_tokens=4000,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
            )
        description = response['choices'][0]['text']
        st.subheader("Generated Writeup:")
        st.write(description)


if __name__ == '__main__':
   main()
