from wechatpy import WeChatClient

client = WeChatClient('wxcc5c9fadb81c03fb', '2c8a5d964d4838b2dbcf9239893ab24d')
user = client.user.get('oSOaDuJJD0EcvyLVnXRKFzT7accw')
print(user)

menu = client.menu.get()

for openid in client.user.iter_followers():
    client.message.send_text(openid, '你好中国')