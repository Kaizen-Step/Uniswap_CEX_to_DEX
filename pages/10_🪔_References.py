# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image


# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Aknowledgement - CEX to DEX and DEX to CEX',
                   page_icon=':bar_chart:', layout='wide')
st.title('🪔 References')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# SQL Codes
st.write(""" ## Acknowledgement ## """)

st.write("""
We are grateful to all who helped us develop this project specially [**Mr. Ali Taslimi**](https://twitter.com/AliTslm) with comprehensive streamlit open source project [Cross chain Monitoring](https://github.com/alitslm/cross_chain_monitoring) that provides streamlit functions and tools.
And also ****Flipside**** with massive and practical databases and last but not least ****MetricsDao**** that is the reason behind this project.


""")

st.text(" \n")
st.text(" \n")



# SQL Queries
st.write(""" ## SQL Queries ## """)

c1,c2=st.columns(2)
with c1:
  st.write("""
  you can find SQL queries have used for this dashboard at following:

  """)

  st.write("""  
  1.[Uniswap DEX to CEX Heatmap](https://flipsidecrypto.xyz/edit/queries/3570909c-6b8f-46f2-baa9-976cd57a7af5)      
        
  2.[Uniswap CEX to DEX flow Daily](https://flipsidecrypto.xyz/edit/queries/1d3c20f3-1178-443b-9d39-bdefb61afeee)      
       
  3.[Uniswap CEX to DEX Overview](https://flipsidecrypto.xyz/edit/queries/eeb6b4ac-1166-4e96-8f2a-90f7dea218d2)        
    
  4.[Uniswap DEX to CEX Heatmap](https://flipsidecrypto.xyz/edit/queries/3570909c-6b8f-46f2-baa9-976cd57a7af5)      
    
  5.[UNi Token price](https://flipsidecrypto.xyz/edit/queries/3f6bae3a-9ad2-4a6e-b296-94b2e4c2a9b8)           
      
  6.[DEX to CEX flow Overview](https://flipsidecrypto.xyz/edit/queries/d13df68c-7857-4e7a-bc03-3c3ede798064)      
       
  7.[Uniswap cEX to dEX flow  Origin](https://flipsidecrypto.xyz/edit/queries/ba1cc93f-9fee-44d0-abfc-080e8d9ec2b5)     
           
  8.[DEX to CEX flow Daily](https://flipsidecrypto.xyz/edit/queries/48149c44-4aa8-4509-891f-3d2c6bb47b80)        
      
  9.[DEX to CEX flow Main](https://flipsidecrypto.xyz/edit/queries/9aecba57-c6af-4b35-8d09-fa569418cd42)        
      
  10.[CEX to DEX Heatmap](https://flipsidecrypto.xyz/edit/queries/033f9994-2dcf-4542-9fa4-e2fdf6a8d540)      
      
  11.[DEX to CEX flow Weekly](https://flipsidecrypto.xyz/edit/queries/a408c759-99c4-462d-8108-5d77618bc826)      



  """)

with c2:
   st.image(Image.open('Images/Codes2.jpg'))


   # Sources
st.write(""" ## Sources ## """)

st.write("""
Here are the reference numbers for all of the sources used in this project:
  

""")


st.write("""  
        1.https://www.coindesk.com/learn/what-is-an-exchange-token/      
        2.https://www.salomonstore.sk/what-is-the-difference-between-dex-and-cex/    
        3.https://www.coindesk.com/learn/centralized-exchange-cex-vs-decentralized-exchange-dex-whats-the-difference/     
        4.[Image-Source] (https://twitter.com/Uniswap)     


""")