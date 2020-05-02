#!/bin/env python3
import requests, math

def get_price():
	try:
		r = requests.get('https://www.bitstamp.net/api/ticker/',timeout=3)
		obj = r.json()

		if obj:
			price=float(obj.get("last"))
			high=float(obj.get("high"))
			low=float(obj.get("low"))
			diff = (price-low)/low if math.fabs((price-low)/low)>math.fabs((high-price)/high) else (high-price)/high;
			return f"{price:.1f}$ <span color='{'red' if diff<0 else 'green'}'>{diff:+.2%}</span>"
	except Exception as e:
		return f"<span color='yellow'>{e}</span>"

	
print(get_price())