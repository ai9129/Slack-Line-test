# Slack-LINE連携ボット

このプログラムは、Slackチャンネルのメッセージを監視し、新しいメッセージを要約してLINEに送信するボットです。

## 機能

- Slackチャンネルのメッセージを定期的に監視
- 新しいメッセージをOpenAIを使用して要約
- 要約したメッセージをLINEに送信

## セットアップ

1. 必要なパッケージをインストール:
```bash
pip install -r requirements.txt
```

2. `.env`ファイルを作成し、以下の環境変数を設定:
```
SLACK_BOT_TOKEN=your_slack_bot_token
SLACK_CHANNEL_ID=your_channel_id
LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
LINE_USER_ID=your_line_user_id
OPENAI_API_KEY=your_openai_api_key
```

## 使用方法

以下のコマンドでプログラムを実行:
```bash
python slack_line_bot.py
```

## 注意事項

- Slackボットには`channels:history`スコープが必要です
- LINEボットはプッシュ通知を送信できるように設定する必要があります
- OpenAI APIキーが必要です 