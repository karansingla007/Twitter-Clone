import os
import csv
import sys
import requests
import pandas as pd
import pymysql.cursors
from pandas import DataFrame



db = pymysql.connect(host='10.10.97.191',
                    user='root',
                    password='root',
                    db='sigtrack',
                    charset='utf8mb4',
                    cursorclass=pymysql.cursors.DictCursor)
db.autocommit(True)
sig_cursor = db.cursor()
SignatureQuery = "SELECT av_public_name, mode, userid, state FROM signatures WHERE updated_at >= adddate(now(),-8) and updated_at <= adddate(now(),+1) and (state='Released' or state='QA' or state='Ready Pending') and (engine='TRUE' or engine_gencfc=TRUE)"
try:
    sig_cursor.execute(SignatureQuery)
except:
    print  ("Error in cursor")
	
	
	
	
request = requests.get(f"{api}", params = parameters, allow_redirects=True)

response = requests.get("http://api.open-notify.org/astros.json")
print(response)

query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print(response.json())


#if authentication needed: 
requests.get(
  'https://api.github.com/user', 
  auth=HTTPBasicAuth('username', 'password')
)

#for error handling: 
try:
    response = requests.get('http://api.open-notify.org/astros.json')
    response.raise_for_status()
    # Additional code will only run if the request is successful
except requests.exceptions.HTTPError as error:
    print(error)
    # This code will run if there is a 404 error.
    
    
    
