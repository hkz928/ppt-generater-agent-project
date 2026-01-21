# PPT Generation Agent (智能 PPT 生成助手)

[English](./README.md) | 简体中文

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Trae](https://img.shields.io/badge/IDE-Trae-green.svg)

**基于 AI 的自动化技术演示文稿生成系统**

这是一个基于 Trae Agent 的综合解决方案，实现了自动化创建专业技术 PPT 的全流程：从智能规划、内容生成，到视觉渲染和演讲稿撰写，一气呵成。

## 🚀 核心特性

1.  **智能编排**：自动分析用户意图，生成结构清晰的演示文稿大纲。
2.  **多模态生成**：并发生成用于图像生成的视觉提示词（Prompts）和用于汇报的专业演讲稿（Scripts）。
3.  **高质量视觉**：集成火山引擎 Ark (Doubao Seedream) 模型，产出高质量、技术准确的幻灯片图片。
4.  **端到端自动化**：仅需一句自然语言指令，即可完成从构思到全套 PPT 图片及演讲稿的交付。

## 📂 项目结构

```
ppt-agent-project/
├── skills/                  # Trae Skills 技能定义
│   ├── ppt-planning-generator/  # 编排器技能 (负责大纲规划与流程控制)
│   ├── ppt-one-page-generator/  # 执行器技能 (负责单页视觉提示词生成)
│   └── ppt-script-generator/    # 撰稿人技能 (负责单页演讲稿生成)
├── scripts/                 # Python 执行脚本
│   └── generate_ppt_images.py   # 调用 API 生成并保存图片的脚本
├── requirements.txt         # Python 依赖列表
└── README_cn.md             # 本文件
```

## 🛠️ 环境配置

### 前置条件

1.  **Trae IDE**：本项目技能专为 Trae 环境设计（同时支持claude-code、iflow等cli工具）。
2.  **火山引擎 Ark API Key**：你需要一个 API Key 来访问图像生成模型。
    *   点击此处申请 Key：[https://www.volcengine.com/product/ark](https://www.volcengine.com/product/ark)
3.  **Python 3.x**：用于运行生成脚本。

### 安装步骤

1.  **安装 Python 依赖**：
    ```bash
    pip install -r requirements.txt
    ```

2.  **配置 API Key**：
    将你的火山引擎 API Key 设置为环境变量：
    ```bash
    # Windows (PowerShell)
    $env:ARK_API_KEY="your_api_key_here"
    
    # Linux/Mac
    export ARK_API_KEY="your_api_key_here"
    ```

## 🚀 使用指南

1.  **导入技能**：确保 `skills` 文件夹位于你的 Trae 工作区的 `.trae/skills` 目录下（或 Trae 指定的自定义技能目录）。
2.  **调用 Agent**：
    *   打开 Trae。
    *   告诉 Agent：**“帮我规划一个关于 [主题] 的 PPT”**。
    *   跟随 Agent 的引导：
        1.  **规划**：确认生成的 PPT 大纲。
        2.  **内容**：确认生成的图像提示词和演讲稿。
        3.  **生成**：Agent 将自动填充 `generate_ppt_images.py` 脚本并运行，为你生成最终的 PPT 图片。

## 🌟 工作流演示

| 规划阶段 (Planning) | 提示词生成 (Prompt Gen) | 图像生成 (Image Gen) |
|-------------------|-----------------------|--------------------|
| 分析主题 -> 创建大纲 | 生成视觉提示词 & 演讲稿 | 调用 API -> 保存图片 |

## 🤝 贡献指南

欢迎提交 Issues 和 Pull Requests，帮助我们改进这个项目！

## 📄 许可证

本项目基于 [MIT License](LICENSE) 开源。

## 🎉 致谢

感谢 [火山引擎 (Volcengine)](https://www.volcengine.com/) 提供 Doubao Seedream 模型支持。
