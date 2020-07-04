import os

from flask import Flask, request, abort, render_template
from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
from wechatpy.exceptions import (
    InvalidSignatureException,
    InvalidAppIdException,
)

# set token or get from environments
TOKEN = os.getenv("WECHAT_TOKEN", "jxepost")
AES_KEY = os.getenv("WECHAT_AES_KEY", "2c8a5d964d4838b2dbcf9239893ab24d")
APPID = os.getenv("WECHAT_APPID", "wxcc5c9fadb81c03fb")

app = Flask(__name__)


@app.route("/")
def index():
    host = request.url_root
    return render_template("index.html", host=host)


@app.route("/wechat", methods=["GET", "POST"])
def wechat():
    signature = request.args.get("signature", "")
    timestamp = request.args.get("timestamp", "")
    nonce = request.args.get("nonce", "")
    msg_signature = request.args.get("msg_signature", "")
    
    try:
        check_signature(TOKEN, signature, timestamp, nonce)
    except InvalidSignatureException:
        abort(403)

    if request.method == "GET":
        echo_str = request.args.get("echostr", "")
        return echo_str

    # POST request
    # plaintext mode
    msg = parse_message(request.data)
    if msg.type == "text":
        reply = create_reply(msg.content, msg)
        print(reply)
    else:
        reply = create_reply("Sorry, can not handle this for now", msg)
    return reply.render()
    