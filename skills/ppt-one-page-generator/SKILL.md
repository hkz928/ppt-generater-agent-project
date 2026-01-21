---
name: "ppt-one-page-generator"
description: "Generates image generation prompts for single-page technical PPT reports. Invoke when user wants to design a PPT slide, technical summary, or visual report."
---

# PPT Single Page Technical Report Generator

This skill generates professional technical report PPT slide visual content prompts based on user input. It constructs a detailed image generation prompt that describes the layout, content, visuals, and style of a technical presentation slide.

## Function Description
Automatically builds professional standard PPT layouts and generates clear, beautiful, and information-complete technical report image prompts based on provided technical content.

## Input Parameters

### Required Parameters
| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `page_title` | String | PPT Page Title | "Knowledge Base Core Performance Optimization" |
| `main_topic` | String | Main Technical Topic | "Query Performance Optimization" |
| `problem_description` | String | Problem Description | "Long query latency affecting user experience" |
| `solution_summary` | String | Solution Overview | "Index optimization and query refactoring" |
| `key_results` | String | Key Results | "Performance up 90%, response time 10s -> 1s" |

### Optional Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `layout_type` | Enum | "three_column" | `two_column`, `three_column`, `comparison`, `flow`, `architecture` |
| `text_ratio` | Integer | 30 | Top text area percentage (20-40) |
| `visual_style` | Enum | "technical" | `technical`, `business`, `modern`, `minimal` |
| `color_scheme` | String | "blue_professional" | `blue_professional`, `green_tech`, `orange_warm`, or custom |
| `language` | Enum | "chinese" | `chinese`, `english`, `bilingual` |
| `include_metrics` | Boolean | true | Include data visualization |
| `problem_points` | Array | [] | List of specific problem points |
| `solution_steps` | Array | [] | List of solution steps |
| `optimization_items` | Array | [] | List of optimization items |
| `before_metrics` | Object | {} | Metrics before optimization |
| `after_metrics` | Object | {} | Metrics after optimization |

## Processing Logic (Mental Model)

When this skill is invoked, you should act as an engine that executes the following logic to produce the **final image generation prompt**.

```python
def generate_ppt_slide(
    page_title: str,
    main_topic: str,
    problem_description: str,
    solution_summary: str,
    key_results: str,
    layout_type: str = "three_column",
    text_ratio: int = 30,
    visual_style: str = "technical",
    color_scheme: str = "blue_professional",
    language: str = "chinese",
    include_metrics: bool = True,
    problem_points: list = None,
    solution_steps: list = None,
    optimization_items: list = None,
    before_metrics: dict = None,
    after_metrics: dict = None
) -> str:
    """
    Generates the prompt for the PPT slide image.
    """
    
    # 1. Build Base Layout
    prompt = f"Create a professional PPT slide layout with {language} text.\n\n"
    
    # 2. Define Layout Structure
    prompt += f"**Layout Structure:**\n"
    prompt += f"- Top Section: Professional Header with Title + Horizontal Summary Strip.\n"
    visual_ratio = 100 - text_ratio
    prompt += f"- Main Section: {get_layout_description(layout_type)} using distinct cards with header bars.\n\n"
    
    # 3. Add Content Details
    prompt += f"**Content Details:**\n"
    prompt += f"Title: {page_title}\n"
    prompt += f"Topic: {main_topic}\n\n"
    
    prompt += f"Summary Strip Content:\n"
    prompt += f"- {problem_description}\n"
    prompt += f"- {solution_summary}\n"
    prompt += f"- {key_results}\n\n"
    
    # 4. Build Visual Section
    prompt += build_visual_section(
        layout_type, 
        problem_points, 
        solution_steps, 
        optimization_items, 
        before_metrics, 
        after_metrics
    )
    
    # 5. Add Visual Elements (Concise)
    prompt += "**Visual Elements:**\n"
    prompt += "Icons: Warning/alert (Problem), Tool/gear (Solution), Checkmark/success (Results)\n"
    if visual_style == "technical":
        prompt += "Diagrams: Technical flow, Architecture, System component diagrams\n"
    else:
        prompt += "Diagrams: Process flow, Simple connection diagrams\n"
    
    if include_metrics:
        prompt += "Metrics: Bar charts, Large bold numbers, Percentage indicators\n"
        
    prompt += "Indicators: Directional arrows, Status colors, Highlight boxes\n\n"
    
    # 6. Set Color Scheme (Concise)
    prompt += build_color_scheme(color_scheme)
    
    # 7. Define Style Guidelines (Concise)
    prompt += f"**Style:** {visual_style.title()} design, High contrast, Clear hierarchy, Professional aesthetic. Text must be rendered in Chinese characters as specified in Content Details.\n"
    prompt += "**Typography:** Title and prominent text in 'SimHei' (黑体); Body content in 'Microsoft YaHei' (微软雅黑).\n"
    
    return prompt

def get_layout_description(layout_type: str) -> str:
    layouts = {
        "two_column": "Two-column (Before/After) clean card layout",
        "three_column": "Three distinct cards (Problem -> Solution -> Results) with colored header bars",
        "comparison": "Comparison with arrow",
        "flow": "Horizontal flow diagram",
        "architecture": "Architecture diagram"
    }
    return layouts.get(layout_type, layouts["three_column"])

def build_visual_section(layout_type, problem_points, solution_steps, optimization_items, before_metrics, after_metrics) -> str:
    section = "**Visual Content (Cards):**\n"
    
    if layout_type == "three_column":
        section += "Card 1 (Problem): Header='问题'. Content="
        if problem_points:
            section += "\\n".join([f"- {p}" for p in problem_points])
        else:
            section += "Key issues list"
        section += "\\n[Warning icons]\\n"
        
        section += "Card 2 (Solution): Header='解决方案'. Content="
        if solution_steps:
            section += "\\n".join([f"- {s}" for s in solution_steps])
        else:
            section += "Optimization steps"
        section += "\\n[Process arrows]\\n"
        
        section += "Card 3 (Results): Header='结果'. Content="
        if after_metrics:
             section += format_metrics(after_metrics)
        else:
             section += "Performance gains"
        section += "\\n[Success checkmarks]\\n\n"
    
    elif layout_type == "comparison":
        section += "Left (Before): " + (", ".join(problem_points) if problem_points else "Issues") + "\n"
        section += "Center: Transformation Arrow\n"
        section += "Right (After): " + (", ".join(solution_steps) if solution_steps else "Improvements") + "\n\n"
    
    return section

def build_visual_elements(visual_style, include_metrics, before_metrics, after_metrics) -> str:
    # Deprecated in favor of inline concise generation
    return ""

def build_color_scheme(color_scheme: str) -> str:
    schemes = {
        "blue_professional": "Primary: Blue, Success: Green, Problem: Red",
        "green_tech": "Primary: Green, Success: Bright Green, Problem: Red",
        "orange_warm": "Primary: Orange, Success: Green, Problem: Red"
    }
    colors = schemes.get(color_scheme, schemes["blue_professional"])
    return f"**Colors:** {colors}, Neutral Gray text, White BG. Do not render HEX codes as text.\n\n"

def build_style_guidelines(visual_style: str) -> str:
    # Deprecated in favor of inline concise generation
    return ""

def format_metrics(metrics: dict) -> str:
    return ", ".join([f"{k}: {v}" for k, v in metrics.items()])
```

## Output Format

The output must be a single block of text representing the **Image Generation Prompt**, containing:
1.  **Layout Structure**: Layout definition (Top text, bottom visual).
2.  **Content Details**: Title, Topic, Summary (Problem, Solution, Results).
3.  **Visual Section Content**: Detailed description of the visual elements in each column/section.
4.  **Visual Elements**: Icons, Diagrams, Metrics Display, Indicators.
5.  **Color Scheme**: Specific color codes and usage.
6.  **Style Guidelines**: Design style instructions.

## Example Usage

**User Input:**
"Create a slide for Knowledge Base Optimization. Problem: Slow queries. Solution: Indexing. Result: 10x faster."

**Skill Execution:**
1.  Parse input into parameters (`page_title`, `problem_description`, etc.).
2.  Apply defaults for missing parameters (`layout_type="three_column"`, `visual_style="technical"`).
3.  Run the logic (mental or actual) to generate the prompt string.

**Final Output:**
```text
Create a professional PPT slide layout with chinese text.

**Layout Structure:**
- Top 30%: Single paragraph summary
- Bottom 70%: Three-column layout showing problem -> solution -> results

**Content Details:**
Title: Knowledge Base Optimization
Topic: Performance Optimization

Top Section Summary:
Problem: Slow queries
Solution: Indexing
Results: 10x faster

**Visual Section Content:**
Column 1 - Problem Analysis:
- Warning icons and alert symbols

Column 2 - Optimization Solution:
- Process arrows and transformation indicators

Column 3 - Optimization Results:
- Success indicators and checkmarks

**Visual Elements:**
Icons:
- Warning/alert icons for problems
- Tool/gear icons for solutions
- Checkmark/success icons for results
...
```
