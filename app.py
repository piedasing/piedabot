from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from weather import weather

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('uyu+7tMPiGmv7tdwgnFnHgb6qkrrTKjBXlvIiCOoqCQnpF2KV5FCUUcFB63kQymzoEiJxA+QKltfAojwQ4MN3OLWbom90pC9qvpL3B9xbXJ5dwv2b0zBAxpPBE0soIYcFinB39QkINAHbL7BVnWl/gdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fe395aaba407f803a7a71709e7749f45')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
