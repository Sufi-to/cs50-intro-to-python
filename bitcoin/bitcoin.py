import requests
import sys
import json

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("enter a number")



try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    v= response.json()
    x = v["bpi"]["USD"]["rate_float"] *n
    print(f"${x:,.4f}")
except requests.RequestException:
    pass
