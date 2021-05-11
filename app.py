import os
import requests
import mysql.connector
import json
# from botocore.vendored import requests
from datetime import datetime
from chalice import Chalice
# import urllib.request

app = Chalice(app_name='DSProject')
app.debug=True

HOST = 'dsproject-rds.c2swyd5wfmpl.us-east-1.rds.amazonaws.com'
USER = 'juliaburek'
PASS = 'password'


def mysql_table(factor, pi, time):
    db = mysql.connector.connect(host=HOST,user=USER,passwd=PASS,database='ds3002')
    c = db.cursor()
    table = """INSERT INTO project (factor, pi, time) VALUES (%s, %s, %s)"""
    print(table)
    names=(factor,pi,time)
    c.execute(table,names)
    db.commit()

@app.schedule('cron(0-59 * ? * * *)')
def cron_tab(event):
    url = "https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi"
    response = requests.get(url)
    data = json.loads(response.text)
    mysql_table(data['factor'],data['pi'],data['time'])
    print(data)
