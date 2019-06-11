# -*- coding: utf8 -*-


appid = 'your appid'
secret_id = 'your secret id'
secret_key = 'your secret key'

from cosStor import cosStor

client = cosStor(secretId=secret_id,secretKey=secret_key,appid=appid)

client.flush()

client.set("testkey","testvalue")

print(client.get("testkey"))

client.set("testkey","testvalue2")

print(client.get("testkey"))