#!/bin/env python3
import requests

def print_ip():
	try:
		r = requests.get('http://ipinfo.io/json',timeout=3)
		obj = r.json()

		if obj:
			ip=obj.get("ip","")
			if ip:
				country=obj.get("country","")
				if country:
					return "<span color='yellow'>{}</span> - {}".format(ip,country)
				else:
					return "<span color='yellow'>{}</span>".format(ip)
	except:
		return "<span color='red'>fail</span>"

	
print(print_ip())