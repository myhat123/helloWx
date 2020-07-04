微信主动调用接口使用
=================

client = WeChatClient('app_id', 'secret')

单独运行程序，发送消息等操作

client.message.send_text(openid, '你好中国')

获取关注者

client.user.iter_followers()

被动调用接口
==========

消息格式是xml

<xml>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[hi]]></Content>
<FromUserName><![CDATA[gh_9e5af8f72f7e]]></FromUserName>
<ToUserName><![CDATA[oSOaDuJJD0EcvyLVnXRKFzT7accw]]></ToUserName>
<CreateTime>1593868008</CreateTime>
</xml>
