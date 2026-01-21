# PPT Generation Agent Project

This project contains a set of **Trae Skills** and helper scripts to automate the creation of professional technical PPT slides using AI image generation (Volcengine Ark / Doubao Seedream).

## Project Structure

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

## Prerequisites

1.  **Trae IDE**: These skills are designed to work within the Trae environment.
2.  **Volcengine Ark API Key**: You need an API key to access the image generation models.
    *   Apply for a key here: [https://www.volcengine.com/product/ark](https://www.volcengine.com/product/ark)
3.  **Python 3.x**: For running the generation script.

## Setup

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

## Usage (In Trae)

1.  **Import Skills**: Ensure the `skills` folder is placed in your Trae workspace's `.trae/skills` directory (or wherever Trae looks for custom skills).
2.  **Invoke the Agent**:
    *   Open Trae.
    *   Tell the agent: "Help me plan a PPT about [Topic]".
    *   Follow the agent's guidance:
        1.  Confirm the generated outline.
        2.  Confirm the generated image prompts.
        3.  The agent will populate the `generate_ppt_images.py` script and run it to generate your slides.

## Customization

*   **Styles**: You can modify `ppt-one-page-generator/SKILL.md` to adjust default colors, fonts, and layouts.
*   **Model**: You can change the image generation model in `scripts/generate_ppt_images.py` (default: `doubao-seedream-4-5-251128`).

## License

MIT License
