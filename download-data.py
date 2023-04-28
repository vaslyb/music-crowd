#!/bin/bash

import math
import json
import requests
import csv
import os

endpoint1 = 'https://api.europeana.eu/set/4457?wskey=apidemo&profile=standard'
endpoint2 = 'https://api.europeana.eu/set/4417?wskey=apidemo&profile=standard'
endpoint3 = 'https://api.europeana.eu/set/4388?wskey=apidemo&profile=standard'
endlist = [endpoint1,endpoint2,endpoint3]

path = './data'
if not os.path.exists(path):
    os.mkdir(path)

for endpoint in endlist:
	try:
		response = requests.get(endpoint)
		response.raise_for_status()
		# If successful, access the json content
		jsonResponse = response.json()
	except HTTPError as http_err:
		print(f'HTTP error occurred: {http_err}')
		sys.exit(1)
	except Exception as err:
		print(f'Other error occurred: {err}')
		sys.exit(1)

	items = jsonResponse['items']
	index = 1
	total = len(items)
	todownload = list()

	for item in items:

		flag=-2
		try:
			recordEndpoint = "https://api.europeana.eu/record/v2/" + item.split('http://data.europeana.eu/item')[1] + ".json?wskey=apidemo"
			recordResponse = requests.get(recordEndpoint)
			recordResponse.raise_for_status()
			# If successful, access the json content
			jsonRecordResponse = recordResponse.json()
		except HTTPError as http_err:
			print(f'HTTP error occurred: {http_err}')
			sys.exit(1)
		except Exception as err:
			print(f'Other error occurred: {err}')
			sys.exit(1)


		# Europeana ID
		try:
			url = jsonRecordResponse['object']['aggregations'][0]['edmIsShownBy']
			europeana_id = jsonRecordResponse['object']['about']
			# print(url)
			print(europeana_id)
			line = europeana_id[1:8]+"_"+ europeana_id[8:]+".mp3"
			print(line)
			os.system("wget '" +url+"' -O "+ "./data/" + line.replace('/',''))
			index += 1
		except KeyError:
			line = europeana_id[5:]+".mp3"
			todownload.append(item)
	print(todownload)
