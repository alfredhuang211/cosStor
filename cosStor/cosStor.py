# -*- coding: utf8 -*-

import os
import json

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

class cosStor:

    def __init__(self, cosBucket="cosStor",cosFile="cosStor.json"):
        self.cosBucket = cosBucket
        self.cosFile = cosFile
        self.storageData = None

    def config(self, secretId=None, secretKey=None, region=None, token=None, appid=None):
        self.secretId = secretId if secretId is not None else os.environ.get("TENCENTCLOUD_SECRETID", None)
        self.secretKey = secretKey if secretKey is not None else os.environ.get("TENCENTCLOUD_SECRETKEY", None)
        self.region = region if region is not None else os.environ.get("TENCENTCLOUD_REGION", "ap-guangzhou")
        self.token = token if token is not None else os.environ.get("TENCENTCLOUD_SESSIONTOKEN", None)
        self.appid = appid

        self.cosConfig = CosConfig(Region=self.region, Appid=self.appid , Secret_id=self.secretId, Secret_key=self.secretKey, Token=self.token, Scheme='https')
        self.cosClient = CosS3Client(self.cosConfig)


    def load(self):
        response = self.cosClient.get_object(
            Bucket=self.cosBucket,
            Key=self.cosFile,
        )
        data = response['Body'].get_raw_stream().read()
        self.storageData = json.loads(data)

    def save(self):
        self.cosClient.put_object(
            Bucket=self.cosBucket,
            Key=self.cosFile,
            Body=json.dumps(self.storageData),
            EnableMD5=False
        )

    def set(self, key, value):
        self.load()
        if self.storageData is None:
            self.storageData = dict()
        self.storageData[key] = value
        self.save()

    def get(self, key):
        self.load()
        return self.storageData[key]

    def flush(self):
        self.save()