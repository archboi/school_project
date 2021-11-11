import json
import requests 

def korona():
	data = requests.get("https://api.apify.com/v2/key-value-stores/GlTLAdXAuOz6bLAIO/records/LATEST?disableRedirect=true")
	return data.json()


