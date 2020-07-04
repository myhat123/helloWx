使用 python 3

pip国内镜像
==========

设置pip.conf

> $ mkdir .pip  

建立 pip.conf

```conf
[global]
index-url=https://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
```