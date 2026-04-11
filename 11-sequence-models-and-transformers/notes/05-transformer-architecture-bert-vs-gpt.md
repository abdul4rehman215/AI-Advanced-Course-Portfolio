# Transformer Architecture, BERT, and GPT

This note covers the transformer part of the section.

The transformer was presented as the architecture that solved major limitations of recurrent sequence processing. Instead of reading input one step at a time, transformers process tokens in parallel and use attention to model relationships across the sequence.

That parallelism is one reason transformers became so important. They handle long-range relationships more efficiently and scale much better than earlier recurrent approaches.

The main concepts I studied were:
- encoder and decoder blocks
- positional encoding
- self-attention
- multi-head attention
- masked attention

Positional encoding is especially important because parallel token processing would otherwise lose sequence order information.

Self-attention helped me understand how each word can weigh its relationship to other words in the sentence. Multi-head attention extends that by allowing multiple perspectives on those relationships at the same time.

The BERT versus GPT distinction was also very valuable:
- BERT is encoder-based and bidirectional, which makes it strong for understanding context
- GPT is decoder-based and autoregressive, which makes it strong for generation

This topic tied together many earlier ideas from the course and gave me a clearer mental model of why modern LLMs are built the way they are.
