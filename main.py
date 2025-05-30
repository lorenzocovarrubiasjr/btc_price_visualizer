from pycoingecko import CoinGeckoAPI
import plotly
import plotly.graph_objects as go
import pandas as pd

cg = CoinGeckoAPI()
btc_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

# Using Pandas to format the data
btc_df = pd.DataFrame(btc_data['prices'], columns=['TimeStamp', 'Price'])
btc_df['Date'] = pd.to_datetime(btc_df['TimeStamp'], unit='ms')
btc_candlestick_data = btc_df.groupby(btc_df.Date.dt.date).agg(
    {
        'Price': ['min', 'max', 'first', 'last']
    })

# Using Plotly to visualize the data
plotlyfig = go.Figure(data=[go.Candlestick(
    x = btc_candlestick_data.index,
    open = btc_candlestick_data['Price']['first'],
    high = btc_candlestick_data['Price']['max'],
    low = btc_candlestick_data['Price']['min'],
    close = btc_candlestick_data['Price']['last']
)])

plotlyfig.update_layout(
    xaxis_rangeslider_visible=False,
    xaxis_title='Date',
    yaxis_title='Price',
    title='BTC Candlestick Chart (30 Days)'
    )

plotly.offline.plot(plotlyfig, filename='./btc_candlestick_chart.html')