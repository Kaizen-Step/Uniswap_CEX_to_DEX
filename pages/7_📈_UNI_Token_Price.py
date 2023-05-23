# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image

# Theme
theme_plotly = None  # None or streamlit

# Layout
st.set_page_config(page_title=' Ethereum Price - CEX to DEX and DEX to CEX',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('📈 UNI Token Price')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'UNI_price':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/3f6bae3a-9ad2-4a6e-b296-94b2e4c2a9b8/data/latest')
    elif query == 'CEX_to_DEX_weekly':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/f9e545a0-84ac-4516-8eb5-19c31dbc735f/data/latest')
    elif query == 'DEX_To_CEX_weekly':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/a408c759-99c4-462d-8108-5d77618bc826/data/latest')
    return None



UNI_price = get_data('UNI_price')
CEX_to_DEX_weekly = get_data('CEX_to_DEX_weekly')
DEX_To_CEX_weekly = get_data('DEX_To_CEX_weekly')

df = UNI_price
df2 = CEX_to_DEX_weekly
df3 = DEX_To_CEX_weekly

#################################################################################################
st.write(""" ### About UNI token  ##  """)

st.write("""
 The UNI token is the native cryptocurrency of Uniswap, one of the most popular decentralized exchange protocols built on the Ethereum blockchain. UNI serves as a utility token within the Uniswap ecosystem, enabling users to participate in governance decisions and access various features of the platform. Holders of UNI have the power to propose and vote on protocol upgrades, fee adjustments, and other important decisions. Additionally, UNI tokens can be staked to earn rewards and grants, further incentivizing participation and engagement within the Uniswap community. With its role in governance and utility, the UNI token plays a vital role in shaping the future and success of Uniswap as a decentralized exchange platform.
  """)


st.info(""" ##### In This Ethereum Price Section you can find: ####

* UNI Token Price 
* Corrolation Between UNI Token Price and CEX to DEX Transactions
* DEX to CEX Transactions Correlation with UNI Token Price


""")


#####################################################
st.write(""" ## UNI Token Price  """)

st.write("""  The price of the UNI token, like other cryptocurrencies, can be influenced by a variety of factors. Here are some key factors that can impact the price of the UNI token: Market Demand and Trading Volume, Overall Market Conditions, Platform Adoption and Usage. 
It's important to note that cryptocurrency prices are highly volatile and influenced by a complex interplay of various factors. Understanding and analyzing these factors, along with conducting thorough research, can provide insights into the potential price movements of the UNI token.
 """)

c1,c2 = st.columns(2)

with c1:

    #    ETH Daily chart
    fig = px.area(df, x="DATE", y="UNI_PRICE",
                title='UNI Token Price')
    fig.update_layout(legend_title=None, xaxis_title=None,
                    yaxis_title='UNI PRICE')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:
    # ETH Daily chart
    fig = px.line(df, x="DATE", y="UNI_CHANGE",
                title='UNI Token Price Change Rate')
    fig.update_layout(legend_title=None, xaxis_title=None,
                    yaxis_title='UNI Price Change')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

################################################################################################################
st.write(""" ## Corrolation Between UNI Token Price and CEX to DEX Transactions """)

st.write("""  The price of the UNI token can be influenced by various factors, including the volume and frequency of transactions between decentralized exchanges (DEXs) and centralized exchanges (CEXs). However, it's important to note that the correlation between UNI token price and DEX to CEX transactions is complex and can be influenced by a range of additional factors.  
When there is a significant volume of transactions flowing from DEXs to CEXs or vice versa, it can indicate changing market dynamics and investor preferences. Increased activity and liquidity on DEXs like Uniswap may indicate growing interest in decentralized trading, potentially leading to increased demand for UNI tokens. On the other hand, if there is a surge in transactions from DEXs to CEXs, it might suggest users moving their assets to centralized platforms, which could potentially impact the price of UNI tokens.
the price correlation may also be influenced by market sentiment, overall market conditions, regulatory developments, and the broader adoption of decentralized exchanges. Positive sentiment surrounding DEXs and the decentralized finance (DeFi) ecosystem, in general, can contribute to the appreciation of UNI token price, irrespective of DEX to CEX transactions.  

 """)
# Bar with Lines
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["DATE"], y=df2["USD_AMOUNT"],
                     name='USD Volume'), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["UNI_PRICE"],
                      name='UNI Token Price'), secondary_y=True)
fig.update_layout(
    title_text='Corrolation Between UNI Token Price and CEX to DEX Transactions')
fig.update_yaxes(
    title_text='USD Volume', secondary_y=False)
fig.update_yaxes(title_text='UNI Token Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

##################################################################################################
st.write(""" ##  DEX to CEX Transactions Correlation with UNI Token Price """)

st.write("""  the price correlation may also be influenced by market sentiment, overall market conditions, regulatory developments, and the broader adoption of decentralized exchanges. Positive sentiment surrounding DEXs and the decentralized finance (DeFi) ecosystem, in general, can contribute to the appreciation of UNI token price, irrespective of DEX to CEX transactions.  

 """)
# Bar with Lines
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df3["DATE"], y=df3["USD_AMOUNT"],
                     name='USD Volume'), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["UNI_PRICE"],
                      name='UNI Token Price'), secondary_y=True)
fig.update_layout(
    title_text='Corrolation Between UNI Token Price and DEX to CEX Transactions')
fig.update_yaxes(
    title_text='USD Volume', secondary_y=False)
fig.update_yaxes(title_text='UNI Token Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)  

