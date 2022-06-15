#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 01:29:10 2022

@author: deepak-vlit
"""

import streamlit as st
import helper
import pickle

model = pickle.load(open('/home/deepak-vlit/Desktop/home/Thesis_Files/nlp/nlp_project/model.pkl', 'rb'))

st.header('Welcome to App for Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]
    
    if result:
        
        st.header('Duplicate')
        
    else:
        
        st.header('Not Duplicate')

