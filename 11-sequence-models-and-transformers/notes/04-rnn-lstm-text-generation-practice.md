# RNN and LSTM Text Generation Practice

This note covers the practical sequence-model notebook from the course.

The lecture walked through a text-generation workflow that included:
- tokenizing text
- assigning integer indices to words
- creating n-gram style training sequences
- applying padding so all inputs have consistent length
- using embeddings to turn tokens into richer vector representations
- training recurrent models to predict the next word

This was helpful because it showed how raw text becomes model-ready data. Before this, next-word prediction felt abstract. After this practice, I could see the full preparation pipeline more clearly.

The lecture also compared a simple RNN to an LSTM. That comparison mattered because it linked the theory of memory control to actual training behavior. LSTMs are better suited when the model needs stronger sequence memory.

Another useful detail was the use of argmax during prediction. The model outputs probabilities across the vocabulary, and the token with the highest score is selected as the next predicted word.

What I liked about this notebook is that it made language-model behavior easier to imagine. Even though it was a smaller-scale example, it clearly pointed toward the logic behind larger text-generation systems.

My takeaway is that modern LLM ideas become easier to understand after seeing a smaller text-generation pipeline from scratch.
