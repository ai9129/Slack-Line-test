import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from openai import OpenAI
from config import *
from linebot.v3.messaging import MessagingApi, Configuration, PushMessageRequest, TextMessage

# Slackクライアントの初期化
slack_client = WebClient(token=SLACK_BOT_TOKEN)

# LINEクライアントの初期化（v3系対応）
configuration = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)
messaging_api = MessagingApi(configuration)

# OpenAIクライアントの初期化
client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://api.openai.com/v1"
)

def get_slack_messages():
    """Slackチャンネルから最新のメッセージを取得"""
    try:
        result = slack_client.conversations_history(
            channel=SLACK_CHANNEL_ID,
            limit=10  # 最新10件のメッセージを取得
        )
        return result["messages"]
    except SlackApiError as e:
        print(f"Slack API エラー: {e}")
        return []

def summarize_text(text):
    """OpenAIを使用してテキストを要約"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "以下のテキストを簡潔に要約してください。"},
                {"role": "user", "content": text}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API エラー: {e}")
        return text

def send_to_line(message):
    """LINEにメッセージを送信（v3系対応）"""
    try:
        req = PushMessageRequest(
            to=LINE_USER_ID,
            messages=[TextMessage(text=message)]
        )
        messaging_api.push_message(req)
    except Exception as e:
        print(f"LINE API エラー: {e}")

def main():
    """メイン処理"""
    print("Slack-LINE連携ボットを開始します...")
    
    # 前回取得したメッセージのタイムスタンプを保存
    last_ts = None
    
    while True:
        try:
            messages = get_slack_messages()
            
            if messages and (last_ts is None or messages[0]["ts"] != last_ts):
                # 新しいメッセージがある場合
                latest_message = messages[0]
                message_text = latest_message.get("text", "")
                
                # メッセージを要約
                summary = summarize_text(message_text)
                
                # LINEに送信
                send_to_line(f"新しいSlackメッセージの要約:\n{summary}")
                
                # タイムスタンプを更新
                last_ts = latest_message["ts"]
            
            # 5分待機
            time.sleep(300)
            
        except Exception as e:
            print(f"エラーが発生しました: {e}")
            time.sleep(60)  # エラー時は1分待機

if __name__ == "__main__":
    main() 