from wechatpy import WeChatClient

client = WeChatClient('wxcc5c9fadb81c03fb', '2c8a5d964d4838b2dbcf9239893ab24d')
client.menu.create({
    "button":[
        {
            "type":"click",
            "name":"今日歌曲",
            "key":"V1001_TODAY_MUSIC"
        },
        {
            "type":"click",
            "name":"歌手简介",
            "key":"V1001_TODAY_SINGER"
        },
        {
            "name":"菜单",
            "sub_button":[
                {
                    "type":"view",
                    "name":"搜索",
                    "url":"http://www.soso.com/"
                },
                {
                    "type":"view",
                    "name":"视频",
                    "url":"http://v.qq.com/"
                },
                {
                    "type":"click",
                    "name":"赞一下我们",
                    "key":"V1001_GOOD"
                }
            ]
        }
    ]
})