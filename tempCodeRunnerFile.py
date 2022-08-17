API_Call = "https://eodhistoricaldata.com/api/exchange-symbol-list/{exchange_code}?api_token={key}&delisted=1"
#API_Call += f"{exchange_code}?api_token={key}&delisted=1"
print("Exchange MetaData Downloading")
# getting data and converting it into text format
call = requests.get(API_Call).text