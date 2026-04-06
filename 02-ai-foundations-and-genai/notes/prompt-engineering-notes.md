# Prompt Engineering Notes

Prompt engineering was presented in the course as a structured skill rather than a casual habit. The key lesson was that better prompts usually produce better outputs because they give the model a clearer frame to work inside.

The prompt structure taught in the course can be broken into the following parts:

## 1. Persona
This tells the model what role it should adopt. For example, asking the model to act as a teacher, analyst, lawyer, or customer support representative changes the style and focus of the response.

## 2. Task
This is the actual job to be done. A task should be direct, specific, and unambiguous.

## 3. Step-by-step instructions
For more complex requests, breaking the task into steps helps the model produce more organized and reliable outputs.

## 4. Context and constraints
This tells the model the boundaries of the task. It can include the domain, audience, tone, limits, or rules the answer should follow.

## 5. Output format
This defines how the final response should be structured, such as bullet points, JSON, paragraphs, or a table.

The course also introduced model parameters like temperature, frequency penalty, and presence penalty. The main idea is that output quality is not controlled only by the words in the prompt, but also by these settings.

- **Temperature** affects creativity and randomness.
- **Frequency penalty** discourages repetition.
- **Presence penalty** encourages introducing new words or ideas.

A useful insight from this lecture is that prompt engineering is close to workflow design. The clearer the task structure, the easier it becomes to use LLMs for real use cases such as support, analysis, summarization, and domain-specific assistance.

This topic matters to me because it connects directly to practical AI workflow building and automation.
