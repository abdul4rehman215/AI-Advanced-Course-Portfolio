# Generative AI Overview

This note brings together the part of the course where the focus shifted from classification-oriented thinking toward Generative AI.

The first important distinction I learned was between discriminative and generative systems.

## Discriminative AI
Discriminative systems focus on separation, classification, or prediction. Their job is usually to decide which category an input belongs to or to distinguish between options.

## Generative AI
Generative systems create new outputs. Depending on the model, that output may be text, code, images, summaries, responses, or other content.

This difference is important because it changes the way we think about model behavior. A classifier answers “what is this?” while a generative model answers “what can I produce based on this input?”

The course also introduced the idea of Large Language Models and transformer-based systems. These models process text using tokens rather than treating whole sentences as single units. I learned that context windows define how much input a model can consider at once, and that larger context windows can help with more complex tasks but also affect cost and performance.

Another major takeaway was that prompt quality matters because prompts guide the model’s task, role, and expected output. Generative AI is not only about model size or architecture. It is also about how clearly the user defines the task.

This part of the course made Generative AI feel more understandable and less mysterious. It showed that behind text generation or image generation there are concrete ideas such as:
- model architecture
- tokenization
- context handling
- instruction design
- output control

That understanding later becomes useful in API usage and Hugging Face work.
