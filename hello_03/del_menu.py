from wechatpy import WeChatClient

client = WeChatClient('wxcc5c9fadb81c03fb', '2c8a5d964d4838b2dbcf9239893ab24d')
res = client.menu.delete()