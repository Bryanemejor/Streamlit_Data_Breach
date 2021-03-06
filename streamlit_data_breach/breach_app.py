
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
import joblib


# In[2]:


st.markdown('## Data Breach Incident')
affected_state = st.number_input('Enter State')
method_breach = st.text_input('Enter Method of Breach')

model = joblib.load('streamlit_data_breach/security_incident.pkl')
#Predict button

inputs = [[affected_state]]

if st.button('Predict'):
   result = model.predict(inputs)
   #updated_res = result.flatten().astype(float)
   st.success('The Probability data breach in this city is {}'.format(result))
   #st.success('The Probability of ', method_breach , 'in this city {}' .format(result))


