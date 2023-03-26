import openai
import streamlit as st
#from charset_normalizer import md__mypyc
import config
import requests
import stripe

openai.api_key=config.api_key
# Set your Stripe API key
stripe.api_key = config.stripe_api_key

def main():
    st.title("Automated Writeup Generator")
    st.subheader('This app has been developed by :red[Dr. Subhabaha Pal].')
    st.write('This app is supposed to help in writing literature review and writeup on any topic. The background AI model used is ChatGPT model developed by OpenAI. ')
    st.write('Please mail to subhabaha@msn.com for suggestions and improvements.')
    st.write('Please write any topic of interest in the below box to get detailed writeup.')
    st.write('This is for reference purpose only.')
    st.write('Please Note: The researcher is suggested to cross-check validity of the generated content before final use in any manuscript.')
    st.write('We charge a nominal fee of INR 50.00 (0.65 USD) for each literature review which is transformed into Human writing form using WordAI Avoid AI Detection Tool Makeover so that you can use the content without much effort.')
    st.write('Please enter the topic on which you want writeup and put your Card Details in the below boxes and proceed. It is Secure Site and your information will not be stored anywhere.')
    notes = st.text_area("Enter Topic Information:")
    
    st.subheader('Free Tool to generate writeup')
    if st.button("Generate Writeup without Avoid AI Detection Tool"):
        with st.spinner("Generating Writeup ...."):
            response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[{'role':'user','content':f'You act as reseracher. Write research paper with more than 3000 words and include real references and in-line citations on topic \n\n{notes}\n\nDescription:'}]
              #temperature=0.7,
              #max_tokens=3000,
              #top_p=1,
              #frequency_penalty=0,
              #presence_penalty=0
            )
            #myobj = {'input': response['choices'][0]['message']['content'], 'email': config.email, 'key':config.wordai_api_key }
            #x = requests.post(config.wordai_url, json = myobj)

        description = response['choices'][0]['message']['content'] 
        
        st.subheader("Generated Writeup")
        st.write(description)
        #st.subheader("Modified Writeup with WordAI to avoid AI Tool Detection")
        #st.write(x.json()['text'])
     
    st.subheader('Please include card payment information to generate writeup modified by Avoid AI Detection tool')
    st.write("Enter payment information:")
    name = st.text_input("Name on card")
    card_number = st.text_input("Card number")
    exp_month = st.selectbox("Expiration month", range(1, 13))
    exp_year = st.selectbox("Expiration year", range(2022, 2030))
    cvc = st.text_input("CVC")    
    
    
    if st.button("Pay INR 50 and Generate Writeup with Avoid AI Detection Tool Modification"):
        
        
        payment_intent = stripe.PaymentIntent.create(
            amount=100,
            currency="inr",
            #payment_method_types=['card'],

            automatic_payment_methods={
                'enabled': True,
            },
            payment_method_options={"card": {"request_three_d_secure": "any"}},
            
        )
        
        try:
            payment_method = stripe.PaymentMethod.create(
                type="card",
                card={
                    "number": card_number,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "cvc": cvc,
                    },
                )

            # Confirm the PaymentIntent with the payment method
            stripe.PaymentIntent.confirm(
                payment_intent.id,
               # payment_method=payment_method.id,
                return_url = 'https://subhabaha-writeup-generator-literature-review-writer-0t4ldh.streamlit.app/',
                payment_method.id,

            )

            # Display a success message
            st.success("Payment was successful!")

      
            with st.spinner("Generating Writeup ...."):
                
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{'role':'user','content':f'You act as reseracher. Write research paper with more than 3000 words and include real references and in-line citations on topic \n\n{notes}\n\nDescription:'}]
                    #temperature=0.7,
                    #max_tokens=3000,
                    #top_p=1,
                    #frequency_penalty=0,
                    #presence_penalty=0
                )
                myobj = {'input': response['choices'][0]['message']['content'], 'email': config.email, 'key':config.wordai_api_key }
                x = requests.post(config.wordai_url, json = myobj)
                
                #myobj1 = {'input': response['choices'][0]['message']['content'], 'email': config.email, 'key':config.wordai_api_key, 'output': 'json','rewrite_num' : 1, 'uniqueness': 2, 'return_rewrites':2,}
                #x1 = requests.post(config.wordai_url1, json = myobj1)


                description = response['choices'][0]['message']['content'] 
        
                st.subheader("Generated Writeup")
                st.write(description)
                st.subheader("Modified Writeup with WordAI to avoid AI Tool Detection")
                st.write(x.json()['text']) 
                #st.subheader("Modified Writeup with WordAI Normal Paraphraser")
                #st.write(x1.json()['text'])     
            
        except stripe.error.CardError as e:
            # Display an error message for card errors
            st.error(f"Error: {e.error.message}")
        
        except stripe.error.StripeError as e:
            # Display an error message for other Stripe errors
            st.error(f"Error: {e.error.message}")

if __name__ == '__main__':
   main()



        
