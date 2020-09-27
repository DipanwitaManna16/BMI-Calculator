
#importing the libraries
import streamlit as st
from PIL import Image

#title
st.title('*Welcome to BMI Calculator*')

#Image
img = Image.open('bmi.jpg')
st.image(img , width=800)

#information
st.info('Information : The Body Mass Index (BMI) Calculator can be used to calculate BMI value and corresponding weight and height status .')



h_mode = 0

#weight as input
weight = st.number_input('Enter your weight (in Kgs):')

#height as input
status = st.radio('Select your height format',('cms','mts','feet'))

if status == 'cms':
    h_mode = 0
    height = st.number_input('Centimeters')
elif status == 'mts':
    h_mode = 1
    height = st.number_input('Meters')
else:
     h_mode = 2
     height = st.number_input('Feet')
    
#Calculating the BMI
  
if st.button('Calculate BMI'):
     if(h_mode == 0):
         bmi = weight / (height ** 2)
        
     elif(h_mode == 1):
         bmi = weight / ((height/100)**2)
        
     else:
         # 1 meter = 3.28 feet
         bmi = weight / ((height/3.28)**2)
     if(bmi < 16):
        st.error("You are Extremely Underweight")
     elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
     elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
        st.balloons()
        
     elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
     elif(bmi >= 30):
        st.error("Extremely Overweight")
               
        
      
    
  
    
    
  
    