# import pandas as pd
# import streamlit as st
# import yfinance as yf


# st.write(
#     """
#     # Stock Price Analyser

#     Shown are the stock prices of Apple
#     """
# )

# ticker_symbol="AAPL"  #This is the stock price symbol of Aaple company


# # Now how to capture stock data for that go to yfinance package

# ticker_data=yf.Ticker(ticker_symbol)   # this will generally make a object ready

# # From this object , I need historical data for apple stock price.

# ticker_df=ticker_data.history(period="1d",
#                               start="2019-01-01",
#                               end="2022-12-31")


# #In order to show entire data i.e ticker_df in our case in webapplication you can use st.dataframe()

# st.dataframe(ticker_df)

# st.write("""
# ## Daily Closing Price Chart
# """)

# #Showcasing the line chart.Go visit streamlit api refrence and find line chart example and implement it below

# #Closing price and volume are important in stock price 
# st.line_chart(ticker_df.Close)

# st.write("""
# ## Volume of Shares traded each day
# """)

# st.line_chart(ticker_df.Volume)


#======================================================================

#Now I want to give user flexibility to choose date 
import pandas as pd
import streamlit as st
import yfinance as yf
import datetime


st.write(
    """
    # Stock Price Analyser

    Shown are the stock prices of Apple
    """
)

ticker_symbol=st.text_input(
                            "Enter the stock symbol",
                            "AAPL",
                            key="placeholder")

col1, col2, col3 = st.columns(3)

with col1:
   #start date of analysis
    start_date=st.date_input("Input starting date" , 
    datetime.date(2019, 1, 1))

with col2:
   #end date
    end_date=st.date_input("Input starting date" , 
    datetime.date(2020, 12, 31))
   

# Now how to capture stock data for that go to yfinance package

ticker_data=yf.Ticker(ticker_symbol)   # this will generally make a object ready

# From this object , I need historical data for apple stock price.



ticker_df=ticker_data.history(period="1d",
                              start=f"{start_date}",
                              end=f"{end_date}")



st.write(f"""
        ### {ticker_symbol}'s EOD prices """)

#In order to show entire data i.e ticker_df in our case in webapplication you can use st.dataframe()
st.dataframe(ticker_df)

st.write("""
## Daily Closing Price Chart
""")

#Showcasing the line chart.Go visit streamlit api refrence and find line chart example and implement it below

#Closing price and volume are important in stock price 
st.line_chart(ticker_df.Close)

st.write("""
## Volume of Shares traded each day
""")

st.line_chart(ticker_df.Volume)