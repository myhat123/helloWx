内网穿透
=======

pagekite.py  很早以前使用过  
ngrok  今天用一用

安装
----

https://dashboard.ngrok.com/get-started/setup

下载之后解压 ngrok

获取authtoken
-------------

https://dashboard.ngrok.com/auth/your-authtoken

./ngrok authtoken xxxxxxxxx

运行
----

> $ ./ngrok http 5000

Web Interface  http://127.0.0.1:4040  
Forwarding  http://6196ae7c5adc.ngrok.io -> http://      
localhost:5000  

Forwarding  https://6196ae7c5adc.ngrok.io -> http://localhost:5000   

启动flask web
-------------

```sh
export FLASK_APP=hello.py
export FLASK_ENV=development
flask run
```

外网穿透访问
-----------

http://6196ae7c5adc.ngrok.io

ngrok web界面
-------------

http://127.0.0.1:4040