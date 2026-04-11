# Seq2Seq and Attention Mechanism

This note covers the progression from recurrent sequence models into sequence-to-sequence learning and attention.

A Seq2Seq model takes a sequence as input and produces another sequence as output. Translation is the classic example, but the same idea also applies to summarization and other text tasks.

The basic structure includes:
- an encoder
- a decoder
- a context representation between them

The encoder reads the input sequence and compresses it into a fixed representation. The decoder uses that representation to generate the output sequence.

The lecture explained why this becomes difficult for long sequences. If the whole meaning of a long sentence has to be compressed into one fixed vector, important information can get lost. That is the bottleneck problem.

Attention solves that by letting the decoder focus on different parts of the input at different moments. Instead of depending on one frozen summary, the model dynamically looks back at the most relevant tokens.

That made attention feel less mysterious to me. I understood it as a mechanism for selective focus. The model does not treat all input positions as equally important at every output step.

My biggest takeaway is that attention was a major conceptual breakthrough because it reduced the burden on a single fixed context vector and made long-range sequence modeling far stronger.
