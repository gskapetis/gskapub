import requests

url = "https://coinranking1.p.rapidapi.com/coin/1/history/7d"

headers = {
    'x-rapidapi-host': "coinranking1.p.rapidapi.com",
    'x-rapidapi-key': "811d0d04ebmshe3a0af52ecc2cc7p137404jsn0d808175d0f3"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)