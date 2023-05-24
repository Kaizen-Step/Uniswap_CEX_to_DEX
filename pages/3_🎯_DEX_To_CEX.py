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
st.set_page_config(page_title='DEX To CEX - CEX to DEX and DEX to CEX',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🎯 DEX To CEX')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'DEX_To_CEX':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/9aecba57-c6af-4b35-8d09-fa569418cd42/data/latest')
    elif query == 'DEX_To_CEX_Overview':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/d13df68c-7857-4e7a-bc03-3c3ede798064/data/latest')
    elif query == 'DEX_To_CEX_Daily':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/48149c44-4aa8-4509-891f-3d2c6bb47b80/data/latest')
    elif query == 'DEX_To_CEX_weekly':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/a408c759-99c4-462d-8108-5d77618bc826/data/latest')
    elif query == 'DEX_to_CEX_HeatMap':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/3570909c-6b8f-46f2-baa9-976cd57a7af5/data/latest')
    return None


DEX_To_CEX = get_data('DEX_To_CEX')
DEX_To_CEX_Overview = get_data('DEX_To_CEX_Overview')
DEX_To_CEX_Daily = get_data('DEX_To_CEX_Daily')
DEX_To_CEX_weekly = get_data('DEX_To_CEX_weekly')
DEX_to_CEX_HeatMap = get_data('DEX_to_CEX_HeatMap')


df = DEX_To_CEX
df2 = DEX_To_CEX_Overview
df3 = DEX_To_CEX_Daily
df4 = DEX_To_CEX_weekly
df5 = DEX_to_CEX_HeatMap
#################################################################################################
st.write(""" ### Uniswap Token DEX to CEX Transactions ##  """)

st.write(""" 
Uniswap is a popular decentralized exchange protocol built on the Ethereum blockchain that enables users to trade tokens directly from their wallets without the need for an intermediary. In contrast, centralized exchanges are operated by a centralized entity that manages the trading platform. When it comes to token transactions between DEXs like Uniswap and CEXs, there are a few key differences to consider.
  """) 


st.info(""" ##### In This DEX to CEX Transactions you can find: ####

* DEX to CEX Overview 
* DEX to CEX Popular Platforms    
* DEX to CEX Transactions on the Time Span  
* Transaction Daily and Hourly Patterns


""")
#########################################################################
st.write(""" ## UNI Token DEX to CEX Flow Overview  """)

st.write("""  In a DEX like Uniswap, users have full control and ownership of their funds. They interact with the exchange directly through smart contracts, which execute trades based on predefined rules. On the other hand, CEXs require users to deposit their funds into centralized wallets owned and managed by the exchange. This means users do not have direct control over their tokens during trading, as they rely on the exchange to facilitate transactions.
    """)

c1, c2 = st.columns(2)
with c1:
    st.metric(label='**Number of DEX To CEX Transactions**',
              value=str(df2["COUNT"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Number of DEX To CEX Unique Users**',
              value=str(df2["NUMBER_OF_USERS"].map('{:,.0f}'.format).values[0]))
with c2:
    st.metric(label='**Total USD Volume**',
              value=df2["USD_AMOUNT"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total UNI Token Volume**',
              value=str(df2["UNI_AMOUNT"].map('{:,.0f}'.format).values[0]))










#########################################################################
st.write(""" ## DEX to CEX Platforms  """)

st.write("""  DEXs eliminate the need for a central intermediary, which reduces the counterparty risk associated with trusting a centralized exchange. In Uniswap, transactions are executed peer-to-peer through the use of liquidity pools and automated market-making algorithms. This reduces the risk of hacks or malicious activities that can occur on centralized platforms. CEXs, however, require users to trust the exchange with their funds, which introduces a degree of counterparty risk.    

    """)

c1, c2 = st.columns(2)

with c1:
    # Pie
    fig = px.pie(df, values="USD_AMOUNT",
                names="FROM_PLATFORM", title='DEX to CEX USD Amount Based on DEX Platform')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = px.pie(df, values="USD_AMOUNT",
                names="TO_PLATFORM", title='DEX to CEX USD Amount Based on CEX Platform')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)





st.write(""" ## DEX to CEX Transactions on the Time Span   """)

st.write("""  Centralized exchanges often have higher liquidity due to their ability to aggregate orders from various participants. This liquidity can lead to better prices and faster execution of trades. DEXs like Uniswap, while gaining popularity, may have lower liquidity for certain tokens, resulting in potentially higher slippage or less favorable trading conditions.  
CEXs typically enforce Know Your Customer (KYC) procedures to comply with regulatory requirements. This involves verifying the identity of users and collecting relevant personal information. DEXs like Uniswap, being decentralized, do not impose such requirements, allowing users to trade without going through a formal registration process.  
When transitioning from a DEX like Uniswap to a CEX, or vice versa, it's important to consider these factors and choose the platform that aligns with your preferences and requirements. DEXs offer greater control and privacy, while CEXs often provide higher liquidity and additional features like margin trading or futures contracts. Ultimately, the choice depends on your specific needs as a trader or investor in the cryptocurrency market.

    """)




# Bar Chart Stacked
fig = px.bar(df4, x= 'DATE', y="USD_AMOUNT", color="FROM_PLATFORM",
             title='Daily Number of Distinct Miners Before and After Shanghai Update')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Number of Miners')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Bar Chart Stacked
fig = px.bar(df4, x= 'DATE', y="USD_AMOUNT", color="TO_PLATFORM",
             title='Daily Number of Distinct Miners Before and After Shanghai Update')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Number of Miners')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Normalized area
fig = px.area(df3, x="DATE", y="USD_AMOUNT", color="FROM_PLATFORM",
              title='Top Categories in terms of actions after bridging to Near: Number of transactions, normalised', groupnorm='percent')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title="NUMBER_TRANSACTIONS")
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#################################################################################

st.write(""" ## Transaction Daily and Hourly Patterns """)

st.write("""  Users may choose to move their funds from a CEX to a DEX to take advantage of the unique features offered by decentralized exchanges, such as increased control over funds, access to a wider range of trading pairs, and participation in decentralized finance (DeFi) protocols. The transfer typically involves withdrawing funds from the centralized exchange and depositing them into the user's wallet or smart contract on the decentralized exchange, allowing for trading directly on the DEX platform.  
    """)


c1,c2= st.columns(2)

with c1:

    # Heatmap
    fig = px.density_heatmap(df5, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="transactions per minute on hour of day (UTC)",
                            histfunc='avg', title='Number of Transactions per minute on hour of day (UTC)', nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                    'dtick': 1}, coloraxis_colorbar=dict(title="Transactions per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Heatmap
    fig = px.density_heatmap(df5, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="USD Volume per minute on hour of day (UTC)",
                            histfunc='avg', title='UNI Token Volume Flow per minute on hour of day (UTC)', nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                    'dtick': 1}, coloraxis_colorbar=dict(title="UNI Token Volume per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    
with c2:
    # Heatmap
    fig = px.density_heatmap(df5, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="USD Volume per minute on hour of day (UTC)",
                            histfunc='avg', title='USD Volume per minute on hour of day (UTC)', nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                    'dtick': 1}, coloraxis_colorbar=dict(title="USD Volume per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)   

     # Heatmap
    fig = px.density_heatmap(df5, x="HOUR_OF_DAY", y="DAY_OF_WEEK", z="User per minute on hour of day (UTC)",
                            histfunc='avg', title='Number of User per minute on hour of day (UTC)', nbinsx=24)
    fig.update_layout(legend_title=None, xaxis_title=None, yaxis_title=None, xaxis={
                    'dtick': 1}, coloraxis_colorbar=dict(title="User per minute on hour of day (UTC)"))
    fig.update_yaxes(categoryorder='array')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    

