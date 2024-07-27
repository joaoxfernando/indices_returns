import pandas as pd
import yfinance as yf
import warnings
from datetime import date as dt


warnings.filterwarnings('ignore')

def get_prices(tickers, start_date='2015-01-01', end_date=dt.today):
    df_price = pd.DataFrame()
    for t in tickers:
        opendf = yf.download(t, start=start_date, period='1d')[['Open']]
        opendf['Ticker'] = t

        closedf = yf.download(t, start=start_date, period='1d')[['Adj Close']]
        closedf['Ticker'] = t

        prices = pd.concat([opendf, closedf['Adj Close']], axis='columns', join='inner').reset_index()
        prices = prices.melt(id_vars=['Ticker', 'Date'], value_name='Preço', var_name='Pregão')

        prices_open = prices[prices['Pregão'] == 'Open'].iloc[[0]]
        prices_close = prices[prices['Pregão'] == 'Adj Close'].iloc[1:]

        prices_df = pd.concat([prices_open, prices_close])
        prices_df['Normalizado'] = (prices_df['Preço'] / prices_df['Preço'].iloc[0])

        df_price = pd.concat([df_price, prices_df])
        df_price = df_price.drop(columns=['Pregão'])
    df_price.rename(columns={'Ticker': 'Índice'}, inplace=True)
    df_price.reset_index(drop=True, inplace=True)
    return df_price