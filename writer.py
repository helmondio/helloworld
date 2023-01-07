# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 15:40:52 2023

@author: Helmond
"""

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.writer')

st.write('Hello , *world* :sunglasses:')

st.write(1234, "Hello")



df = pd.DataFrame({
    '1st':['a',1,2,3,4],
    '2nd':[22,11,33,44,55]
    })

st.write(df)



df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)