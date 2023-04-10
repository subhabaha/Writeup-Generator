import openai
import streamlit as st
#from charset_normalizer import md__mypyc
import config
#import requests
import razorpay
client = razorpay.Client(auth=("rzp_live_ccdgxUrjuwvI5O", "lHxlvFXCwt8qz6StKedTMab2"))
client.set_app_details({"title" : "Streamlit App", "version" : "1.0.0"})
import streamlit.components.v1 as components
from streamlit_javascript import st_javascript
import time
from streamlit.components.v1 import html

def get_from_local_storage(k):
    v = st_javascript(
        f"JSON.parse(localStorage.getItem('{k}'));"
    )
    return v or {}


def set_to_local_storage(k, v):
    jdata = json.dumps(v)
    st_javascript(
        f"localStorage.setItem('{k}', JSON.stringify({jdata}));"
    )

openai.api_key=config.api_key

def main():
    st.title("Summarizer")
    st.subheader('This app has been developed and maintained by InstaDataHelp Analytics Services')
    notes = st.text_area("Enter Text to summarize:")
    
    st.subheader('Payment for Summary Generation')
    if st.button("Pay INR 25"):
        
         #First Payment will happen and then once it happen following code should run
        order = client.order.create({
            "amount": int(2500),
            "currency": "INR",
            
        })
        paymentId = order['id']
        st.experimental_set_query_params(
        order_id=paymentId
        )
        p = open("./test1.html")
        components.html(p.read(),height=800,width=500)

    id = st.text_input('Enter Payment Id Generated After Making Payment')      
    
    
    if st.button("Generate Writeup"):
        
        payment = client.payment.fetch(id)
        
        if payment['status'] == 'captured' or payment['status'] == 'authorized':
            st.write("Payment successful")
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
            #myobj = {'input': response['choices'][0]['message']['content'], 'email': config.email, 'key':config.wordai_api_key }
            #x = requests.post(config.wordai_url, json = myobj)


            description = response['choices'][0]['message']['content'] 
            st.subheader("Generated Summarized Writeup")
            st.write(description)
       # st.subheader("Modified Content with WordAI to avoid AI Tool Detection")
       # st.write(x.json()['text'])
        else:
            st.write("Payment failed")


if __name__ == '__main__':
   main()
