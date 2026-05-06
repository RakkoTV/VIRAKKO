# 🚀 VIRAKKO - 内容创作自动化技能

![VIRAKKO Logo](https://img.shields.io/badge/VIRAKKO-v1.0.0-purple)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**VIRAKKO** 是一项革命性的技能，它完全自动化视频内容创作过程，从想法生成到最终视频制作。

## ✨ 主要功能

- 🎯 **命令激活**: 输入"VIRAKKO" + 您的内容开始
- 🤖 **想法生成**: AI生成3个创意想法（Google Gemini）
- 📜 **脚本创建**: 包含8秒场景的完整脚本
- 🎙️ **语音合成**: 使用ElevenLabs生成专业音频
- 🖼️ **图像生成**: 每个场景的初始图像和最终图像
- 🎬 **视频制作**: 使用Google FLOW制作完整视频
- 🌐 **本地网页**: 网页界面可视化整个项目
- 🌍 **多语言**: 西班牙语、英语、日语、中文

## 🎥 工作流程

1. **激活**: 输入"VIRAKKO <您的内容>"
2. **想法**: 生成3个脚本想法
3. **选择**: 选择您最喜欢的想法
4. **脚本**: 创建包含8秒场景的脚本（乌拉圭西班牙语）
5. **音频**: 为每个场景生成语音
6. **图像**: 创建初始图像和最终图像
7. **视频**: 制作最终视频
8. **网页**: 生成包含所有内容的本地网页

## 📦 安装

### 先决条件

- Python 3.8或更高版本
- Chrome浏览器（用于Selenium）
- ElevenLabs API密钥
- Google Gemini API密钥（可选）

### 安装依赖项

```bash
pip install -r requirements.txt
```

### 配置

1. 复制配置模板：
```bash
cp config/settings.json.template config/credentials.json
```

2. 编辑`config/credentials.json`并添加您的API密钥：
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

### 运行技能

```bash
python src/main.py
```

### 命令示例

```
VIRAKKO 创建一个关于教育中人工智能好处的视频
```

## 📁 项目结构

```
VIRAKKO/
├── PLAN.md                          # 开发计划
├── README.md                        # 此文件
├── README_en.md                     # 英文README
├── README_ja.md                     # 日文README
├── README_zh.md                     # 中文README
├── .gitignore                       # Git忽略的文件
├── requirements.txt                 # 依赖项
├── config/
│   ├── settings.json.template       # 配置模板
│   └── credentials.json             # 您的凭据（从Git中排除）
├── src/
│   ├── __init__.py                  # 包初始化
│   ├── main.py                      # 主脚本
│   ├── gemini_integration.py        # Gemini集成
│   ├── elevenlabs_integration.py    # ElevenLabs集成
│   ├── file_manager.py              # 文件管理
│   └── web_generator.py             # 网页生成器
├── templates/
│   └── index.html                   # 网页模板
├── projects/                        # 生成的项目
│   └── IDEA_YYYYMMDD_HHMMSS/
│       ├── Escena1/
│       │   ├── guion_escena1.txt
│       │   ├── audio_escena1.mp3
│       │   ├── imagen_inicial_escena1.png
│       │   ├── imagen_final_escena1.png
│       │   └── video_escena1.mp4
│       └── index.html               # 项目网页
└── docs/                            # 额外文档
```

## 🔑 所需的API密钥

### ElevenLabs

1. 在[ElevenLabs](https://elevenlabs.io/)注册
2. 从控制面板获取您的API密钥
3. 将其添加到`config/credentials.json`

### Google Gemini（可选）

1. 在[Google AI Studio](https://makersuite.google.com/)注册
2. 获取您的API密钥
3. 将其添加到`config/credentials.json`

## 🌐 使用的技术

- **Python 3.8+**: 主要语言
- **Selenium**: 网页自动化
- **Google Gemini**: 想法、脚本和图像生成
- **ElevenLabs**: 语音合成
- **Google FLOW**: 视频生成
- **HTML/CSS/JS**: 本地网页

## 🤝 贡献

欢迎贡献。请：

1. 分叉项目
2. 为您的功能创建分支（`git checkout -b feature/NewFeature`）
3. 提交您的更改（`git commit -m 'Add new feature'`）
4. 推送到分支（`git push origin feature/NewFeature`）
5. 打开拉取请求

## 📄 许可证

此项目在MIT许可证下 - 有关详细信息，请参阅[LICENSE](LICENSE)文件

## ❤️ 支持项目

如果您喜欢VIRAKKO并希望支持其开发，请考虑捐款：

[🎁 通过PayPal捐款](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ramiro.silva.1993@gmail.com&item_name=VIRAKKO+Donation&currency_code=USD)

## 👤 作者

**Ramiro Fernando Silva Berrutti**

## 🌐 在社交媒体上关注我

- 🐱 [GitHub](https://github.com/RakkoTV) (3 ⭐)
- 💼 [LinkedIn](https://www.linkedin.com/in/ramiro-silva/) (449 个联系人)
- 📸 [Instagram](https://www.instagram.com/Rakko.Tech) (6666 粉丝)
- 👾 [Twitch](https://www.twitch.com/RakkoTech) (8800 粉丝)
- ✖️ [X (Twitter)](https://www.x.com/RakkoTech) (245 粉丝)
- 🧵 [Threads](https://www.threads.net/@rakko.tech) (125 粉丝)
- 🦋 [BlueSky](https://bsky.app/profile/rakkotech.bsky.social) (2 粉丝)
- 📘 [Facebook](https://www.facebook.com/RakkoTech) (2100 粉丝)
- 📺 [YouTube](https://www.youtube.com/@RakkoTech) (131 订阅者)
- 🎵 [TikTok](https://www.tiktok.com/RakkoTech) (35 粉丝)
- 🟩 [Kick](https://kick.com/rakkotech/about) (0 粉丝)

## 📞 联系方式

- **Email**: ramiro.silva.1993@gmail.com
- **GitHub**: [RakkoTV](https://github.com/RakkoTV)

## 🙏 致谢

- Google的Gemini和FLOW
- ElevenLabs的语音合成API
- 开源社区

---

**感谢使用VIRAKKO！ 🚀**

由Ramiro Fernando Silva Berrutti用 ❤️ 制作