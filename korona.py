import json
import requests 

def korona():
	data = requests.get("https://korona.gov.sk/koronavirus-na-slovensku-v-cislach/")
	return data.json()


