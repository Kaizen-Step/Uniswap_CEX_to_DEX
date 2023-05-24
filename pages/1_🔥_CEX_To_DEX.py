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
st.set_page_config(page_title='CEX To DEX - CEX to DEX and DEX to CEX',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🔥 CEX To DEX')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache_data()
def get_data(query):
    if query == 'CEX_to_DEX':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/244b0157-7832-4570-8e46-5961c9247bfa/data/latest')
    elif query == 'CEX_to_DEX_Overview':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/eeb6b4ac-1166-4e96-8f2a-90f7dea218d2/data/latest')
    elif query == 'CEX_to_DEX_Daily':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/1d3c20f3-1178-443b-9d39-bdefb61afeee/data/latest')
    elif query == 'CEX_to_DEX_weekly':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/f9e545a0-84ac-4516-8eb5-19c31dbc735f/data/latest')
    elif query == 'CEX_to_DEX_HeatMap':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/033f9994-2dcf-4542-9fa4-e2fdf6a8d540/data/latest')
    return None


CEX_to_DEX = get_data('CEX_to_DEX')
CEX_to_DEX_Overview = get_data('CEX_to_DEX_Overview')
CEX_to_DEX_Daily = get_data('CEX_to_DEX_Daily')
CEX_to_DEX_weekly = get_data('CEX_to_DEX_weekly')
CEX_to_DEX_HeatMap = get_data('CEX_to_DEX_HeatMap')

df = CEX_to_DEX
df2 = CEX_to_DEX_Overview
df3 = CEX_to_DEX_Daily
df4 = CEX_to_DEX_weekly
df5 = CEX_to_DEX_HeatMap
#################################################################################################
st.write(""" ### CEX to DEX Transactions ##  """)

st.write(""" In the realm of cryptocurrencies, centralized exchanges (CEX) and decentralized exchanges (DEX) play pivotal roles in facilitating the trading and exchange of digital assets. While CEX platforms have long been the dominant force, DEXs have emerged as a revolutionary alternative that promises increased security, autonomy, and transparency. One area of great interest within the cryptocurrency community is the growing trend of transactions between CEX and DEX platforms.     
  """)


st.info(""" ##### In This CEX to DEX Transactions you can find: ####

* CEX to DEX Overview
* CEX to DEX Platforms    
* CEX to DEX On Time Line   
* Transaction Patterns




""")
#########################################################################
st.write(""" ## Overview  """)

st.write("""  Understanding CEX to DEX transactions and the underlying dynamics between centralized and decentralized exchanges becomes essential for cryptocurrency enthusiasts and traders alike. By bridging the gap between these two distinct paradigms, users can explore the benefits of both centralized liquidity and decentralized autonomy, adapting their strategies to their specific needs.
    """)


c1, c2 = st.columns(2)
with c1:
    st.metric(label='**Number of CEX to DEX Transactions**',
              value=str(df2["COUNT"].map('{:,.0f}'.format).values[0]))
    st.metric(label='**Number of CEX to DEX Unique Users**',
              value=str(df2["NUMBER_OF_USERS"].map('{:,.0f}'.format).values[0]))
with c2:
    st.metric(label='**Total USD Volume**',
              value=df2["USD_AMOUNT"].map('{:,.0f}'.format).values[0])
    st.metric(label='**Total UNI Token Volume**',
              value=str(df2["UNI_AMOUNT"].map('{:,.0f}'.format).values[0]))





#########################################################################
st.write(""" ## CEX to DEX Platforms  """)

st.write(""" Coinbase becomes the leading source. Coinbase is the source of the vast majority of UNI transactions. These transactions have gained significant attention in recent times due to several factors. First, users who value the security and control offered by DEX platforms may decide to transfer their funds from CEXs to DEXs, seeking a more self-custodial approach to trading. Second, certain tokens or projects may be exclusively available on either CEXs or DEXs, prompting users to navigate between platforms to access specific assets.Users need to evaluate factors such as liquidity, trading volume, fees, user experience, and available trading pairs when choosing between CEX and DEX platforms.   
Let's investigate the DEXs on the destination side. The statistics show that more than 51% of the transferred $UNI tokens have been received by the Uniswap platform from the CEXs.


    """)

c1, c2 = st.columns(2)

with c1:
    # Pie
    fig = px.pie(df, values="USD_AMOUNT",
                names="FROM_PLATFORM", title='CEX to DEX USD Amount Based on CEX Platform')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    fig = px.pie(df, values="USD_AMOUNT",
                names="TO_PLATFORM", title='CEX to DEX USD Amount Based on DEX Platform')
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)



st.write(""" ## CEX to DEX On Time Line  """)

st.write("""  Coinbasedominance has generally not changed over time. Although it is not as dominant as it is in terms of the quantity of UNI transfers, Coinbase still has a sizable share of the market in terms of volume. We see that Coinbase sends UNI tokens to several DEXes, with Uniswap being the main recipient. Transfers to various DEXes can also be facilitated using IDEX. It comes as no surprise that Uniswap is the main beneficiary of transfers from CEXes.
CEXs, often characterized by their user-friendly interfaces and robust liquidity, have traditionally served as go-to platforms for traders seeking speed and convenience. These exchanges operate under a centralized authority, where users deposit their funds into wallets managed by the exchange itself. Consequently, this model grants CEXs control over users' assets and requires placing trust in the exchange's security measures and operational integrity.   
On the other hand, DEXs operate on decentralized networks, utilizing smart contracts and blockchain technology to execute transactions. In contrast to CEXs, DEX platforms enable users to maintain full control over their funds throughout the trading process. By eliminating the need for intermediaries and central authorities, DEXs offer enhanced security, privacy, and resilience against hacking attempts or regulatory interventions. This decentralized nature resonates with the core philosophy of cryptocurrencies, empowering users with financial sovereignty.   
    """)




# Bar Chart Stacked
fig = px.bar(df4, x= 'DATE', y="USD_AMOUNT", color="FROM_PLATFORM",
             title='Weekly CEX to DEX USD Volume Base on CEX Platform')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='USD Amount')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Bar Chart Stacked
fig = px.bar(df4, x= 'DATE', y="USD_AMOUNT", color="TO_PLATFORM",
             title='Weekly USD Volume Base on DEX Platform')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='USD Amount')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1,c2= st.columns(2)

with c1:
    # Bar Chart Stacked
    fig = px.bar(df4, x= 'DATE', y="NUMBER_OF_USERS", color="FROM_PLATFORM",
                title='Number of Users Base on DEX Platform')
    fig.update_layout(legend_title=None, xaxis_title=None,
                    yaxis_title='NUMBER_OF_USERS')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

with c2:    
    # Normalized area
    fig = px.area(df3, x="DATE", y="UNI_AMOUNT", color="TO_PLATFORM",
                title='UNI Amount Transferred Volume Base on DEX Platform', groupnorm='percent')
    fig.update_layout(legend_title=None, xaxis_title=None,
                    yaxis_title="UNI AMOUNT")
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

#################################################################################

st.write(""" ## Transaction Days of Week and Hours of Day Pattern  """)

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
