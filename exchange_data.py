import json
import pandas as pd
import requests  # to make HTTP calls to the API

# function that brings in Tickers, Stock Type, Exchanges
# puts them in a Pandas DataFrame
# creates a new File with a new TimeStamp to save the Pandas DF in that file

"""
def return_exchange_data(key, exchange_code='NYSE'):
    API_Call = "https://eodhistoricaldata.com/api/exchange-symbol-list/"
    API_Call += f"{exchange_code}?api_token={key}&delisted=1"
    print("Exchange MetaData Downloading")
    # getting data and converting it into text format
    call = requests.get(API_Call).text
    exchange_data = pd.DataFrame(json.loads(call))
    print("Finished")
    print(exchange_data.head())
    return exchange_data
"""


def Return_List_Of_Exchanges(key):
    API_CALL = "https://eodhistoricaldata.com/api/exchanges-list/?api_token={key}}&fmt=json"
    print("Exchange Lists being downloaded")
    call = requests.get(API_CALL).text
    Exchange_List = pd.DataFrame(json.loads(call))
    print("Finished Loading Exchange List")
    print(Exchange_List.head())
    return Exchange_List


def main():
    key = "62f9fa8999db62.45214477"
    print(Return_List_Of_Exchanges())


if __name__ == '__main__':
    main()
