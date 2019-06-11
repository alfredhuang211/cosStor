# COS Storage

使用腾讯云 COS 对象存储的文件存储来进行简单数据的存储。

## 使用方式

'''
from cosStor import cosStor

client = cosStor(secretId=secret_id,secretKey=secret_key,appid=appid)

client.flush()

client.set("testkey","testvalue")

print(client.get("testkey"))
'''

1. 初始化 client，配置认证信息
2. 使用 flush 确保 cos 中文件生成。
3. 使用 set 设置 key-value 对。
4. 使用 get 读取 key 对应的 value。