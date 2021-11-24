
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
import joblib


# In[2]:


st.markdown('## Data Breach Incident')
affected_state = st.text_input('Enter State')
method_breach = st.text_input('Enter Method of Breach')


#Predict button
if st.button('Click to Predict'):
    model = joblib.load('/streamlit_data_breach/security_incident.pkl')
    
    st.markdown(f'### Prediction is {model.predict([[affected_state, method_breach]])[0]}')

