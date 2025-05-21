import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# Slack設定
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
SLACK_CHANNEL_ID = os.getenv('SLACK_CHANNEL_ID')

# LINE設定
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
LINE_USER_ID = os.getenv('LINE_USER_ID')

# OpenAI設定
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY') 