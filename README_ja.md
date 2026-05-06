# 🚀 VIRAKKO - コンテンツ作成自動化スキル

![VIRAKKO Logo](https://img.shields.io/badge/VIRAKKO-v1.0.0-purple)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**VIRAKKO**は、アイデアの生成から最終ビデオの制作まで、ビデオコンテンツ作成プロセスを完全に自動化する革命的なスキルです。

## ✨ 主な機能

- 🎯 **コマンドアクティベーション**: "VIRAKKO" + コンテンツを入力して開始
- 🤖 **アイデア生成**: AIが3つの創造的なアイデアを生成（Google Gemini）
- 📜 **スクリプト作成**: 8秒のシーンを含む完全なスクリプト
- 🎙️ **音声合成**: ElevenLabsでプロフェッショナルなオーディオを生成
- 🖼️ **画像生成**: 各シーンの初期画像と最終画像
- 🎬 **ビデオ制作**: Google FLOWを使用して完全なビデオを制作
- 🌐 **ローカルウェブ**: プロジェクト全体を視覚化するウェブインターフェース
- 🌍 **多言語**: スペイン語、英語、日本語、中国語

## 🎥 ワークフロー

1. **アクティベーション**: "VIRAKKO <コンテンツ>"と入力
2. **アイデア**: 3つのスクリプトアイデアが生成されます
3. **選択**: 最も気に入ったアイデアを選択
4. **スクリプト**: 8秒のシーンを含むスクリプトが作成されます（ウルグアイスペイン語）
5. **オーディオ**: 各シーンの音声が生成されます
6. **画像**: 初期画像と最終画像が作成されます
7. **ビデオ**: 最終ビデオが制作されます
8. **ウェブ**: すべてのコンテンツを含むローカルウェブページが生成されます

## 📦 インストール

### 前提条件

- Python 3.8以上
- Chromeブラウザ（Selenium用）
- ElevenLabs APIキー
- Google Gemini APIキー（オプション）

### 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 設定

1. 設定テンプレートをコピー：
```bash
cp config/settings.json.template config/credentials.json
```

2. `config/credentials.json`を編集してAPIキーを追加：
```json
{
  "elevenlabs": {
    "api_key": "YOUR_ELEVENLABS_API_KEY"
  },
  "gemini": {
    "api_key": "YOUR_GEMINI_API_KEY"
  }
}
```

## 🚀 使用方法

### スキルを実行

```bash
python src/main.py
```

### コマンド例

```
VIRAKKO 教育におけるAIの利点についてのビデオを作成
```

## 📁 プロジェクト構造

```
VIRAKKO/
├── PLAN.md                          # 開発計画
├── README.md                        # このファイル
├── README_en.md                     # 英語のREADME
├── README_ja.md                     # 日本語のREADME
├── README_zh.md                     # 中国語のREADME
├── .gitignore                       # Gitで無視されるファイル
├── requirements.txt                 # 依存関係
├── config/
│   ├── settings.json.template       # 設定テンプレート
│   └── credentials.json             # あなたの認証情報（Gitから除外）
├── src/
│   ├── __init__.py                  # パッケージ初期化
│   ├── main.py                      # メインスクリプト
│   ├── gemini_integration.py        # Gemini統合
│   ├── elevenlabs_integration.py    # ElevenLabs統合
│   ├── file_manager.py              # ファイル管理
│   └── web_generator.py             # ウェブジェネレーター
├── templates/
│   └── index.html                   # ウェブテンプレート
├── projects/                        # 生成されたプロジェクト
│   └── IDEA_YYYYMMDD_HHMMSS/
│       ├── Escena1/
│       │   ├── guion_escena1.txt
│       │   ├── audio_escena1.mp3
│       │   ├── imagen_inicial_escena1.png
│       │   ├── imagen_final_escena1.png
│       │   └── video_escena1.mp4
│       └── index.html               # プロジェクトウェブページ
└── docs/                            # 追加のドキュメント
```

## 🔑 必要なAPIキー

### ElevenLabs

1. [ElevenLabs](https://elevenlabs.io/)にサインアップ
2. コントロールパネルからAPIキーを取得
3. `config/credentials.json`に追加

### Google Gemini（オプション）

1. [Google AI Studio](https://makersuite.google.com/)にサインアップ
2. APIキーを取得
3. `config/credentials.json`に追加

## 🌐 使用技術

- **Python 3.8+**: メイン言語
- **Selenium**: ウェブ自動化
- **Google Gemini**: アイデア、スクリプト、画像生成
- **ElevenLabs**: 音声合成
- **Google FLOW**: ビデオ生成
- **HTML/CSS/JS**: ローカルウェブ

## 🤝 貢献

貢献を歓迎します。以下の手順に従ってください：

1. プロジェクトをフォーク
2. 機能用のブランチを作成（`git checkout -b feature/NewFeature`）
3. 変更をコミット（`git commit -m 'Add new feature'`）
4. ブランチにプッシュ（`git push origin feature/NewFeature`）
5. プルリクエストを開く

## 📄 ライセンス

このプロジェクトはMITライセンスの下です - 詳細は[LICENSE](LICENSE)ファイルを参照してください

## ❤️ プロジェクトをサポート

VIRAKKOが気に入り、開発をサポートしたい場合は、寄付をご検討ください：

[🎁 PayPalで寄付](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ramiro.silva.1993@gmail.com&item_name=VIRAKKO+Donation&currency_code=USD)

## 👤 作成者

**Ramiro Fernando Silva Berrutti**

## 🌐 ソーシャルメディアでフォロー

- 🐱 [GitHub](https://github.com/RakkoTV)
- 💼 [LinkedIn](https://www.linkedin.com/in/ramiro-silva/)
- 📸 [Instagram](https://www.instagram.com/Rakko.Tech)
- 👾 [Twitch](https://www.twitch.com/RakkoTech)
- ✖️ [X (Twitter)](https://www.x.com/RakkoTech)
- 🧵 [Threads](https://www.threads.net/@rakko.tech)
- 🦋 [BlueSky](https://bsky.app/profile/rakkotech.bsky.social)
- 📘 [Facebook](https://www.facebook.com/RakkoTech)
- 📺 [YouTube](https://www.youtube.com/@RakkoTech)
- 🎵 [TikTok](https://www.tiktok.com/RakkoTech)
- 🟩 [Kick](https://kick.com/rakkotech/about)

## 📞 連絡先

- **Email**: ramiro.silva.1993@gmail.com
- **GitHub**: [RakkoTV](https://github.com/RakkoTV)

## 🙏 謝辞

- GeminiとFLOWのGoogle
- 音声合成APIのElevenLabs
- オープンソースコミュニティ

---

**VIRAKKOをご利用いただきありがとうございます！ 🚀**

Ramiro Fernando Silva Berruttiが ❤️ で作成