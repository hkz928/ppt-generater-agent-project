# PPT Generation Agent

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Trae](https://img.shields.io/badge/IDE-Trae-green.svg)

**An Automated Technical Presentation Generation System Powered by AI**

A comprehensive Trae Agent solution that automates the entire workflow of creating professional technical PPTs: from intelligent planning and content generation to visual rendering and speech script drafting.

## 🚀 Core Features

1.  **Intelligent Orchestration**: Automatically analyzes user intent to generate structured presentation outlines.
2.  **Multimodal Generation**: Concurrently generates visual prompts for image generation and professional speech scripts for presentation.
3.  **High-Quality Visualization**: Integrates with Volcengine Ark (Doubao Seedream) to produce high-quality, technically accurate slide images.
4.  **End-to-End Automation**: Seamless workflow from a single natural language command to a complete set of slide images and scripts.

## 📂 Project Structure

```
ppt-agent-project/
├── skills/                  # Trae Skills definitions
│   ├── ppt-planning-generator/  # Orchestrator skill (Plans outline & prompts)
│   ├── ppt-one-page-generator/  # Worker skill (Generates visual prompts per slide)
│   └── ppt-script-generator/    # Script writer skill (Generates speech drafts)
├── scripts/                 # Python scripts for execution
│   └── generate_ppt_images.py   # Script to call API and save images
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## 🛠️ Environment Setup

### Prerequisites

1.  **Trae IDE**: These skills are designed to work within the Trae environment.
2.  **Volcengine Ark API Key**: You need an API key to access the image generation models.
    *   Apply for a key here: [https://www.volcengine.com/product/ark](https://www.volcengine.com/product/ark)
3.  **Python 3.x**: For running the generation script.

### Installation

1.  **Install Python Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure API Key**:
    Set your Volcengine API key as an environment variable:
    ```bash
    # Windows (PowerShell)
    $env:ARK_API_KEY="your_api_key_here"
    
    # Linux/Mac
    export ARK_API_KEY="your_api_key_here"
    ```

## 🚀 Usage Guide

1.  **Import Skills**: Ensure the `skills` folder is placed in your Trae workspace's `.trae/skills` directory (or wherever Trae looks for custom skills).
2.  **Invoke the Agent**:
    *   Open Trae.
    *   Tell the agent: **"Help me plan a PPT about [Topic]"**.
    *   Follow the agent's guidance:
        1.  **Plan**: Confirm the generated outline.
        2.  **Content**: Confirm the generated image prompts and speech scripts.
        3.  **Generate**: The agent will populate the `generate_ppt_images.py` script and run it to generate your slides.

## 🌟 Workflow Demonstration

| Planning Phase | Prompt Generation | Image Generation |
|----------------|-------------------|------------------|
| Analyzes topic -> Creates Outline | Generates Visual Prompts & Scripts | Calls API -> Saves Images |

## 🤝 Contribution

Welcome to submit Issues and Pull Requests to improve the project together!

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🎉 Acknowledgments

Thanks to [Volcengine](https://www.volcengine.com/) for providing the Doubao Seedream model support.
