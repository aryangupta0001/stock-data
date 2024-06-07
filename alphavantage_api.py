import requests


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SBIN.BSE&apikey=5H2Z5JSEFQOP038O'
r = requests.get(url)

data = r.json()

# print(data)

time_series = data.get("Time Series (Daily)", {})


for date in iter(time_series):
    daily_data = time_series[date]
    print(f"\nDate: {date}")
    print("Data:")
    print(daily_data.get("1. open"), end="\t")
    print(daily_data.get("4. close"))
