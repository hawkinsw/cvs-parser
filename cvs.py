#!/bin/env python3

from bs4 import BeautifulSoup
import requests

class CvsQuery:
	def __init__(self, latitude: float, longitude: float):
		self.latitude = latitude
		self.longitude = longitude

	def __repr__(self):
		return '{"requestMetaData":,"requestPayloadData":}'

class Cvs:
	def __init__(self, soup: BeautifulSoup):
		self.soup = soup

class CvsQueryDownloader:
	def __init__(self, query: CvsQuery):
		self.cookies = {}
		self.query = {}
		self.headers = {}
		self.query["requestMetaData"] = '{"appName":"CVS_WEB","lineOfBusiness":"RETAIL","channelName":"WEB","deviceType":"DESKTOP","deviceToken":"7777","apiKey":"a2ff75c6-2da7-4299-929d-d670d827ab4a","source":"ICE_WEB","securityType":"apiKey","responseFormat":"JSON","type":"cn-dep"}'
		self.query["requestPayloadData"] = '{"selectedImmunization":["CVD"],"distanceInMiles":35,"imzData":[{"imzType":"CVD","ndc":["59267100002","59267100003","59676058015","80777027399"],"allocationType":"1"}],"searchCriteria":{"addressLine":"45230"}}'
		self.url = 'https://www.cvs.com/Services/ICEAGPV1/immunization/1.0.0/getIMZStores'

	def post(self):
		safety_response = requests.post("https://www.cvs.com/vaccine/intake/store/covid-screener/covid-qns")
		return requests.post(self.url, cookies = safety_response.cookies, data=self.query, headers = self.headers)

if __name__ == "__main__":
	# First, do the download.

	geq = CvsQuery(40.4172871, -82.90712300000001)
	geqd = CvsQueryDownloader(geq)

	print(str(geqd.post()))
