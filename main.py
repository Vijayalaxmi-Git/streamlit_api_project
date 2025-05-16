# Streamlit app
import streamlit as st
from utils import StockAPI

# Set page config
st.set_page_config(page_title="Stock App", layout="wide")

# Get the stockapi
client = StockAPI()

# Add a title to web app
st.title("Stock Market App")

# Add a subheading
st.subheader("By Vijaylaxmi")

# Take text input from user
company = st.text_input("Company Name :")

# If company name is entered show some stock symbols and information
if company:
    r1 = client.symbol_search(company)
    dropdown = st.selectbox("Symbol", options=r1["1. symbol"].tolist())
    company_details = r1[r1["1. symbol"] == dropdown]
    st.dataframe(company_details)


    # Create a submit button
    submit = st.button("Submit", type="primary")

    # If submit button clicked plot the chart
    if submit:
        df = client.stock_data(dropdown)
        fig = client.plot_chart(df)
        st.plotly_chart(fig)