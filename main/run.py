from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import re
import os
import subprocess  #他のpythonファイルを実行する

SLACK_BOT_TOKEN="xoxb-4395843400308-4400294354372-QCzh2A8lIizvv1xw4kmBd6zc"
SLACK_APP_TOKEN="xapp-1-A04B98BJK5M-4401321535252-627d24072fb24e2d9f38260fc98d5a25f0007b9b4aa93c4d6914b6727a7acdca"


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
                    "text": {"type": "plain_text", "text":"scheduleを呼び出す"},
                    "action_id": "schedule"
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

@app.action("schedule")
def action_button_click(message, ack, body, say):
    # アクションを確認したことを即時で応答します
    ack()
    # チャンネルにメッセージを投稿します
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there in block1 <@{body['user']['id']}!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text":"予定を追加する"},
                    "action_id": "add_schedule"
                }
            }
        ],
        text=f"Hey there !"
    )
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there in block2 <@{body['user']['id']}!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text":"予定を削除する"},
                    "action_id": "delete_schedule"
                }
            }
        ],
        text=f"Hey there !"
    )

@app.action("add_schedule")
def add_schedule(message, ack, say, body, event):
    # アクションを確認したことを即時で応答します
    ack()
    #チャンネルにメッセージを送信
    #say(f"<@{body['user']['id']}> add new schedule")
    say(f"<@{body['user']['id']}>")
    say(os.getcwd())
    name = f"<@{body['user']['id']}>"
    path_w = './'+name[2:-1] + 'schedule.txt'
    with open(path_w, mode='w', encoding='UTF-8') as f:
         f.write("aaa")


@app.action("delete_schedule")
def delete_schedule(message, ack, say, body):
    # アクションを確認したことを即時で応答します
    ack()
    #チャンネルにメッセージを送信
    say(f"<@{body['user']['id']}> adelete new schedule")





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