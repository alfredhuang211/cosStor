# -*- coding: utf8 -*-


appid = 'test appid'
secret_id = 'test id'
secret_key = 'test key'


from cosStor import cosStor

client = cosStor(cosBucket="testbucket",secretId=secret_id,secretKey=secret_key,appid=appid)

client.flush()

client.set("testkey","testvalue")

print(client.get("testkey"))

client.set("testkey","testvalue2")

print(client.get("testkey"))