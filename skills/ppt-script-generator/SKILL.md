---
name: "ppt-script-generator"
description: "Generates presentation scripts (speech drafts) for PPT slides. Invoke when user needs a spoken narrative for a slide."
---

# PPT Presentation Script Generator

This skill generates a professional, engaging, and accessible presentation script (speech draft) for a specific PPT slide. It bridges the gap between technical details and audience understanding.

## Function Description
Takes the content of a slide (Title, Problem, Solution, Results) and transforms it into a spoken narrative. It ensures technical accuracy while using analogies or clear explanations to make the content accessible to a broader audience.

## Input Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `slide_title` | String | Title of the slide |
| `key_points` | List/String | The core content points (Problem, Solution, Results) |
| `audience` | Enum | `technical` (Peers), `executive` (Management), `general` (Public/Clients) |
| `tone` | Enum | `professional`, `enthusiastic`, `storytelling` |
| `duration` | String | Target duration (e.g., "1 minute", "30 seconds") |

## Processing Logic

1.  **Analyze Context**: Determine the appropriate depth based on `audience`.
    *   *Technical*: Focus on metrics, architecture, implementation details.
    *   *Executive*: Focus on business value, ROI, high-level outcomes.
    *   *General*: Focus on the "Why", simple analogies, and user impact.
2.  **Structure the Narrative**:
    *   **Hook**: Start with a sentence that grabs attention or states the core problem clearly.
    *   **Body**: Explain the "Solution" and "Implementation" using transition words. Connect technical points to benefits.
    *   **Conclusion**: Summarize the "Results" and impact.
3.  **Refine Language**:
    *   Use spoken English/Chinese (shorter sentences, active voice).
    *   Add "Stage Directions" (e.g., [Point to the chart], [Pause for effect]).

## Output Format

The output should be a structured script block:

```markdown
**Slide:** [Slide Title]
**Target Audience:** [Audience Type]
**Estimated Time:** [Duration]

---
**(Opening)**
[Speaker]: "Let's look at..." / "Here we encounter a critical challenge..."

**(Body)**
[Speaker]: "As you can see on the left..." / "To solve this, we implemented..."
*(Note: Use simple analogies for complex tech if audience is General)*

**(Closing)**
[Speaker]: "The result? A significant improvement in..."

---
**Key Takeaway for Q&A:** [One sentence summary]
```

## Example Usage

**User Input:**
"Generate a script for the 'Vector Query Optimization' slide. Audience is Executives. Points: Old index slow (15s), New index fast (3s), 80% gain."

**Output:**
```markdown
**Slide:** Vector Query Optimization
**Target Audience:** Executive
**Estimated Time:** 45 seconds

---
**(Opening)**
"Next, I want to highlight one of our biggest performance wins: Vector Search."

**(Body)**
"Previously, our system took about 15 seconds to retrieve complex knowledge—frankly, that's too slow for a smooth user experience. It was like searching for a book in a library without a catalog."

"So, we completely rebuilt the indexing engine. We didn't just patch it; we upgraded the underlying technology."

**(Closing)**
"The impact was immediate. Search time dropped from 15 seconds to just 3 seconds. That's an 80% improvement in speed, meaning our users get answers almost instantly."
---
```
