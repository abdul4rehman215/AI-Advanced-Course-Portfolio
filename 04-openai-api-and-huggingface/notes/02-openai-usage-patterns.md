# OpenAI Usage Patterns

This note captures the practical OpenAI-related ideas introduced in the course.

The course demonstrated how a language model can be used through code by defining a task, preparing input, and sending it to the model through an API client. One of the key examples used in the course was sentiment analysis, where text is analyzed and categorized based on emotional tone.

This made two things clear to me.

First, language models are very flexible. They can perform different tasks depending on the prompt and system instructions.

Second, the quality of the interaction depends not only on the model, but also on:
- prompt clarity
- role definition
- task framing
- output expectations
- model settings

I also learned that model selection matters. Different models can vary in cost, speed, reasoning strength, and context window size. That means choosing a model is not only a technical decision. It is also a practical decision related to project needs.

Another important point from this lecture is API key handling. Keys are sensitive credentials and should never be exposed publicly. This is one of the most important practical lessons from the notebook section because it directly affects safe GitHub publishing.

Overall, this topic helped me understand how LLM functionality can be wrapped inside a notebook workflow and turned into a usable application pattern instead of remaining a black box.
