import openai
import streamlit as st
#from charset_normalizer import md__mypyc

openai.api_key=config.api_key

def main():
    st.title("Topic Writeup and References Generator")
    notes = st.text_area("Enter Topic Information:")
    if st.button("Generate Writeup and References"):
        with st.spinner("Generating Writeup and References..."):
            response = openai.Completion.create(
              model="text-davinci-003",
              prompt=f"I want you to write short literature review on below topic.\n\n{notes}\n\nDescription:",
              temperature=0.7,
              max_tokens=256,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
            )
        description = response['choices'][0]['text']
        st.subheader("Generated Writeup:")
        st.write(description)


if __name__ == '__main__':
   main()
