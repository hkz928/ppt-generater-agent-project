---
name: "ppt-planning-generator"
description: "Plans PPT structure and orchestrates content generation. Invoke when user wants to create a full PPT deck from a topic or document."
---

# PPT Planning & Generation Orchestrator

This skill plans a complete PowerPoint presentation outline based on user input and then orchestrates the detailed generation of each slide using the `ppt-one-page-generator` standards.

## Function Description
1.  **Planning Phase**: Analyzes user input to create a structured PPT outline (Chapters, Pages, Key Content).
2.  **Execution Phase**: Upon user confirmation, generates the detailed image generation prompts for *every* page defined in the plan. **Simultaneously**, it invokes the `ppt-script-generator` logic to generate a speech draft for each slide.
3.  **Generation Phase**: Upon user confirmation of the prompts, invokes the image generation tool (e.g. `seedream-prompt-generator` or custom script) to produce the final images.

## Input Parameters

| Parameter | Description |
|-----------|-------------|
| `topic` | Main topic or title of the presentation |
| `source_content` | (Optional) Raw text or document content to base the PPT on |
| `slide_count` | (Optional) Target number of slides (approximate) |
| `audience` | (Optional) Target audience (Technical, Executive, General) |
| `style` | (Optional) Visual style (Technical, Business, Modern) |

## Processing Logic

When this skill is invoked, follow this multi-step process:

### Step 1: Outline Planning
Generate a structured plan based on user input.

**Output Format:**
```json
{
  "ppt_title": "My Presentation",
  "visual_style": "technical",
  "color_scheme": "blue_professional",
  "slides": [
    {
      "page_num": 1,
      "type": "Title Slide",
      "title": "Presentation Title",
      "key_points": ["Subtitle", "Presenter Name"]
    },
    {
      "page_num": 2,
      "type": "Content",
      "layout": "three_column",
      "title": "Problem Statement",
      "content_summary": "Description of current bottlenecks...",
      "main_topic": "Current Issues",
      "problem_description": "...",
      "solution_summary": "...",
      "key_results": "..."
    }
    // ... more slides
  ]
}
```
**Action**: *Pause and ask the user to confirm the outline.*

### Step 2: Content Generation (Prompts & Scripts)
Once the user confirms the outline, you must generate the full content for **ALL** slides.

1.  **Image Prompts**: Apply `ppt-one-page-generator` logic to create visual prompts.
2.  **Speech Scripts**: Apply `ppt-script-generator` logic to create a speech draft for each slide.

**Crucial Naming Requirement**:
For each slide, you must specify the output filename:
`{ppt_title}_Page{page_num}_{safe_slide_title}`

**Final Output Format for Step 2**:
Present the result as a series of code blocks or clearly separated sections. For the script, include it as a comment or separate field associated with each page.

**Example Output:**
```python
PPT_PAGES = [
    {
        "filename": "Optimization_Page01_Title.png",
        "prompt": "Create a professional PPT slide layout...",
        "script": "**Slide:** Optimization Title\n**Audience:** Executive\n\n(Opening)\nGood morning everyone..."
    },
    {
        "filename": "Optimization_Page02_Problem.png",
        "prompt": "Create a professional PPT slide layout...",
        "script": "**Slide:** Problem Statement\n**Audience:** Executive\n\n(Body)\nAs you can see..."
    }
]
```
**Action**: *Pause and ask the user to confirm the prompts and scripts.*

### Step 3: Image Generation (After Confirmation)
Once the user confirms the content, you must use the `Write` tool to create or update a python script (e.g., `generate_ppt_images.py`) with the `PPT_PAGES` data from Step 2, and then use the `RunCommand` tool to execute it.

**Script Template**:
The script should import `OpenAI` (or compatible client), iterate through `PPT_PAGES`, generate images using the provided prompts, and save them to the specified filenames. Optionally, it can save the scripts to text files alongside the images.

## Orchestration Instructions for the Agent
- **Do not** skip steps. You must drive the user to confirm at each stage (Outline -> Content -> Generation).
- **Parallelism**: When generating content in Step 2, generate BOTH prompts and scripts for all slides in one go.
- **Consistency**: Ensure the `visual_style` and `color_scheme` chosen in the plan are applied consistently. Ensure the script tone matches the target audience.
