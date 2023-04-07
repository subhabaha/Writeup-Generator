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
# Set your Stripe API key

def main():
    st.title("Research Writer")
    st.subheader('This app has been developed and maintained by InstaDataHelp Analytics Services')
    st.write('This app is supposed to help in writing literature review and writeup on any topic. The write-up includes in-text citations and references')
    st.write('Please mail to info@instadatahelp.com for suggestions and improvements. Per write-up cost is INR 50 currently. The articles generated are plag-free.')
    st.write('Please write any topic of interest in the below box to get detailed writeup.')
    st.write('This is for reference purpose only.')
    st.write('Please Note: The write-up generated are for references and researchers may use it in their manuscript with or without modification.')
    st.write('We charge a nominal fee of INR 50.00 (0.65 USD) for each literature review.')
    st.write('Please enter your topic and click Pay INR 50. Once payment ID is generated, please put that in the below box and generate blog writeup.')
    st.write('Please Whatsapp or call at +91 9903726517 if you face any issue after payment. Currently accepting payments from India only.')
    st.write('It is secure RazorPay Payment Gateway and your payment details will not be stored anywhere.')

    notes = st.text_area("Enter Topic Information:")
    
    st.subheader('Free Tool to generate writeup')
    if st.button("Pay INR 50"):
        
         #First Payment will happen and then once it happen following code should run
        order = client.order.create({
            "amount": int(5000),
            "currency": "INR",
            
        })
        paymentId = order['id']
        st.experimental_set_query_params(
        order_id=paymentId
        )
        p = open("./test.html")
        components.html(p.read(),height=800,width=500)

    id = st.text_input('Enter Payment Id Generated After Making Payment')  
        
    if st.button("Generate Writeup"):
        payment = client.payment.fetch(id)
        
        if payment['status'] == 'captured' or payment['status'] == 'authorized':
            st.write("Payment successful")
            with st.spinner("Generating Writeup ..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{'role':'user','content':f'You act as reseracher. Write research paper with more than 3000 words. Include real references. Include in-text citations. Write on topic \n\n{notes}\n\nDescription:'}]
             
                 )
            description = response['choices'][0]['message']['content'] 
            st.subheader("Generated Literature Review")
            st.write(description)    
        
        else:
            st.write("Payment failed")
       

if __name__ == '__main__':
   main()



        
