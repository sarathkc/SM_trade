import requests

url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/op/option/NIFTY"

querystring = {"expiration":"1705622400"}

headers = {
	"X-RapidAPI-Key": "bdac2c12b5mshf2789d8e1032a5ep114a01jsn969e71e9566c",
	"X-RapidAPI-Host": "yahoo-finance15.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)