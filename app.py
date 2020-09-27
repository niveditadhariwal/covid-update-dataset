import streamlit as st
import pandas as pd
import numpy as np
import requests
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px
from pandas.io.json import json_normalize
from streamlit.ScriptRunner import StopException, RerunException

hide_streamlit_style = """
        <style>
        footer {visibility: hidden;}
        .sidebar .sidebar-content {background-image: linear-gradient(180deg,#00d00982,#20b9d2);}
        .st-b9 {background-color: rgb(47 38 47 / 76%);}
        .st-b4 {color: rgb(111 235 255);}
        .btn-outline-secondary {
        border-color: #09ab3b85;
        color: #f9f9f9;
        }
        body {color: #000000;text-align: left;background-color: #ffffff;}
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.write("""
# COVID 19 Live Update 🚨
[Coronavirus COVID19 API](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest#81447902-b68a-4e79-9df9-1b371905e9fa) is used to get the data in this app.
""")

st.write('''
The coronavirus COVID-19 pandemic is the defining global health crisis of our time and the greatest challenge we have faced since World War Two.
Since its emergence in Asia late last year, the virus has spread to every continent except Antarctica.

But the pandemic is much more than a health crisis, it is also an unprecedent socio-economic crisis.

Stressing every one of the countries it touches, it has the potential to create devastating social,
economic and political effects that will leave deep and longstanding scars.''')

# st.markdown('<iframe src="https://datawrapper.dwcdn.net/WIdnc/5/" style="height:400px;width:800px;" title="Iframe Example"></iframe>', unsafe_allow_html=True)
st.markdown('<iframe src="https://datawrapper.dwcdn.net/JjgUp/2/" style="height:450px;width:700px;" title="Iframe Example"></iframe>', unsafe_allow_html=True)

st.sidebar.subheader("""🤖 [Niveditadhariwal](https://www.linkedin.com/in/nivedita-dhariwal-86186019b/)""")
