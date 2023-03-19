import openai
import streamlit as st
#from charset_normalizer import md__mypyc
import config

openai.api_key=config.api_key

def main():
    st.title("Automated Writeup Generator")
    st.subheader('This app has been developed by :red[Dr. Subhabaha Pal].')
    st.text('This app is supposed to help in writing literature review and writeup on any topic.')
    st.text('The background AI model used is ChatGPT model developed by OpenAI.') 
    st.text('Please mail to subhabaha@msn.com for suggestions and improvements.')
    st.text('Please write any topic of interest in the below box to get detailed writeup.')
    st.text('This is for reference purpose only.')
    st.text('Please Note: The researcher is suggested to cross-check validity of the generated content before final use in any manuscript.')
    notes = st.text_area("Enter Topic Information:")
    if st.button("Generate Writeup"):
        with st.spinner("Generating Writeup ...."):
            response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[{'role':'user','content':f'You act as reseracher. Write research review of more than 2000 words and include real references and in-line citations on topic \n\n{notes}\n\nDescription:'}]
              #temperature=0.7,
              #max_tokens=3000,
              #top_p=1,
              #frequency_penalty=0,
              #presence_penalty=0
            )
        description = response['choices'][0]['text']
        st.subheader("Generated Writeup:")
        st.write(description)


if __name__ == '__main__':
   main()
