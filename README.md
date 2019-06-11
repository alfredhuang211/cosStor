# COS Storage

使用腾讯云 COS 对象存储的文件存储来进行简单数据的存储。

## 使用方式

'''
from cosStor import cosStor

client = cosStor(secretId=secret_id,secretKey=secret_key,appid=appid)

client.set("testkey","testvalue")

print(client.get("testkey"))
'''

1. 初始化 client，配置认证信息，如果在 scf 环境中使用，无需配置 secretId 及 secretKey，需要配置 apppid
2. 使用 set 设置 key-value 对。
3. 使用 get 读取 key 对应的 value。


## 注意事项

1. 默认文件存储在 cosstor 存储桶， cosStor.json 文件，广州区（ap-guangzhou），如果需要修改默认存储桶及存储文件，可以在初始化 client 时指定。
2. 文件不存在时，可以使用 client.flush() 来新建空文件。如果已有文件，使用此方法将清空文件。

