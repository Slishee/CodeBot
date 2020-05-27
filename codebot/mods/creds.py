#!/usr/bin/env python3

"""
Chatbot for Messenger Groups to Compile
and reply code-status.

The bot currently works as a facebook user

Depends on:
	- GeekForGeeks (website) - for code execution
	- fbchat (module) - to interact with facebook
	- json (module) - json data
	- threading (module) - for multithreading 
	- requests (module) - for http requests

Author: Rakibul Yeasin
	- Github: dreygur
	- Facebook: dreygur
	- Twitter: drreygur
"""

import os
import json
from typing import Dict

# Bot's Status (Down or Up)
botState = False

# Facebook User Details
user = "01647561445"
password = "798193274622"
cookieFile = os.path.realpath(os.path.join(os.getcwd(), "cookies.json"))

# User-Agent
agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"

# Ubuntu-Paste cookie
ubuntuPastebinCookie: str = "45jgnmetiw3qjbq2f49x06hd8h8bi3vy"

def getfbCookie() -> Dict:
	"""
	Retrieves saved Cookie from cookies.json file

	Args:
		None

	Returns:
		cookies 	A dictionary containing facebook cookie

	Raises:
		None
	"""

	# Use Old Cookie
	cookies: dict = {}

	try:
		with open(cookieFile, "r") as cookie:
			cookies = json.load(cookie)
	except: pass

	return cookies

def setfbCookie(cookies: dict):
	"""
	Saves retrievd fb cookie to a json file

	Args:
		cookie 	A Dictionary containing cookies

	Returns:
		None

	Raises:
		None
	"""

	# fbchat Session
	with open(cookieFile, "w") as cookie:
		json.dump(cookies, cookie)