# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='CEX to DEX and DEX to CEX',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' Uniswap CEX to DEX and DEX to CEX ')
st.text(" \n")
# Content
c1, c2, c3 = st.columns(3)


with c1:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/DEX1.jpg'))

with c2:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/Uniswap3.jpg'))
with c3:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/DEX2.jpg'))


st.write("""


### How Exchange Tokens Work ###  
Exchange tokens function just like any other cryptocurrency token. You can trade them on secondary markets or hold them for speculative purposes. Examples of exchange tokens include FTX’s FTT token, Binance’s BNB, Huobi’s HT and WazirX’s WRX.     
These exchange tokens are minted by the cryptocurrency exchange itself. The term is usually reserved for tokens issued by a **centralized cryptocurrency exchange** – a company with an executive team and structure similar to a traditional finance company, that maintains an order book of buyers and sellers.Exchange tokens generally refer to volatile cryptocurrencies issued by the exchanges; stablecoin tokens issued by exchanges, like BUSD, HUSD, and Coinbase (and Circle’s) USDC are not generally called exchange tokens, and are simply referred to as stablecoins.[[1]](https://www.coindesk.com/learn/what-is-an-exchange-token/)       

### Centralized  and Decentralized Exchanges ###
Decentralized exchanges, like Uniswap and SushiSwap, also have their own tokens, although these are usually separated into their own categories, like “DeFi tokens” or “DEX tokens.” These tokens are used in governance; stakers pledge them within various decentralized finance protocols to alter the parameters that define the platforms.
You can usually buy exchange tokens directly from the cryptocurrency exchange – which will often pay you in the token as a reward for completing tasks or trading certain coins. Some exchanges, like WazirX, airdrop, or give away, tokens to holders to kickstart the market.    
Exchange tokens do not equate to stock in the company, and do not usually confer governance rights over the exchange. However, exchange token markets often work quite a bit like equity markets; their price is a function of the belief that the exchange will become successful, making its exchange token valuable to hold; the more activity there is on the exchange, the thinking goes, the more demand there will be for the exchange token.For traders, the main benefit is a reduction in trading fees. Holders of WRX are entitled to discounts of up to 50% when they pay fees in WRX, and FTX offers those that hold more than \$100 worth of FTT a 3% discount when trading on the exchange.[[2]](https://www.coindesk.com/learn/centralized-exchange-cex-vs-decentralized-exchange-dex-whats-the-difference/ )     
### Decentralized Exchanges Goals ###     
DEXs aim to complete transactions more quickly and cheaply than their centralized counterparts. They do this by cutting out the intermediary entities that take a cut of transaction fees on CEXs. The 2018 whitepaper of the world’s largest DEX, Uniswap, proclaims "zero rent extraction." It aims to protect its users from the additional costs entailed in generating profit for the intermediaries that run CEXs. Bancor, which launched in 2017 and describes itself as the first DEX, advocates for the decentralized approach like this:
“Liquidity on traditional asset exchanges has historically been provided by a small handful of professional trading firms with permissioned access and specialized tools. This concentrates liquidity in the hands of a few actors who can withdraw their assets during periods of volatility and restrict trading of an asset when users need it the most.”
In late 2021, the leading DEX Uniswap was charging a 0.05% transaction fee on the $100,000 trade sampled by global accountancy KPMG. CEXs Binance, Coinbase and Kraken were charging 0.1%, 0.2% and 0.2%, respectively.[[3]](https://cryptopotato.com/what-is-the-ethereum-shanghai-shapella-upgrade-everything-you-need-to-know/)

      


""")


st.write("""
## Methodology ##  

Using the flipside database, we go in-depth on the UNI token DEX to CEX and CEX to DEX flow in this dashboard. We created a complete main table with contract labels using the "ethereum.core.ez_token_transfers" table and the "ethereum.core.dim_labels," "LABEL_TYPE," and "LABEL" columns defined from and to contract addresses of each transaction on the token transfer table. This allowed us to easily filter the source and destination of each UNI transaction. The additional transactions were then removed, and the rows with null labels were given undefined contract addresses as names. We examine the amount of USD and UNI, the number of users, and the number of transactions going from CEX to DEX using this table. Finally, we look into the relationship between the price of these UNI tokens and their pricing.


""")


st.text(" \n")
st.write("""   
#### Sources ####  """)
st.write("""   
        1.https://www.coindesk.com/learn/what-is-an-exchange-token/    
        2.https://www.salomonstore.sk/what-is-the-difference-between-dex-and-cex/   
        3.https://www.coindesk.com/learn/centralized-exchange-cex-vs-decentralized-exchange-dex-whats-the-difference/   
        4.[Image-Source] (https://twitter.com/Uniswap)
            """)


st.text(" \n")
c1, c2 = st.columns(2)
with c1:
    st.info(
        '**Twitter:  [Ludwig.1989](https://twitter.com/Ludwig_1989)**', icon="🕊️")
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.xyz/app/market/0x3e4f7978447e354E832D38363e927231e518e33a/request/155)**', icon="👨🏻‍💼")


with c2:
    st.info(
        '**Project Github:  [Uniswap CEX to DEX and DEX to CEX ](https://github.com/Kaizen-Step/Russia_Ukraine_Conflict)**', icon="💻")
    st.info(
        '**Data Set:  [Flipsidecrypto](https://flipsidecrypto.xyz/)**', icon="🧠")
