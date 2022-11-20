from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import re
import subprocess  #他のpythonファイルを実行する

SLACK_BOT_TOKEN="xoxb-4395843400308-4400294354372-LNlCOg6UCPAzASw0VOZgA0gt"
SLACK_APP_TOKEN="xapp-1-A04B98BJK5M-4397730105715-fc65e82b38f7c6e42d1d1e6f3b0086f8e18b7cafac0cd34727c421c675bef213"


app = App(token=SLACK_BOT_TOKEN)


@app.message("hamabot")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there in block1 <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text":"Click button1"},
                    "action_id": "button_click1"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there in block2 <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text":"Click button2"},
                    "action_id": "button_click2"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )

@app.action("button_click1")
def action_button_click(body, ack, say):
    # アクションを確認したことを即時で応答します
    ack()
    # チャンネルにメッセージを投稿します
    say(f"<@{body['user']['id']}> clicked the button1")

@app.action("button_click2")
def action_button_click(body, ack, say):
    # アクションを確認したことを即時で応答します
    ack()
    # チャンネルにメッセージを投稿します
    say(f"<@{body['user']['id']}> clicked the button2")




@app.message("hello")  # 送信されたメッセージ内に"hello"が含まれていたときのハンドラ
def ask_who(say):
    say("can I help you?")



@app.message("bot_save:")
def write(event,say):
    if event['text'][0:9] == "bot_save:":
        say(event['text'][9::])
    else:
        say("you not write ")

@app.event("app_mention")  # chatbotにメンションが付けられたときのハンドラ
def respond_to_mention(event, say):
    message = re.sub(r'^<.*>', '', event['text'])
    say(message[::-1]) # 文字列を逆順


@app.event("message") # ロギング
def handle_message_events(body, logger):
    logger.info(body)

@app.message(re.compile(r'^<.*>'))
def ask_who(say):
    say("all")







SocketModeHandler(app, SLACK_APP_TOKEN).start()