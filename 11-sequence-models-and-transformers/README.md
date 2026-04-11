# 🔁 Sequence Models and Transformers

### My sequence-learning block covering time-aware neural networks, attention, text generation, and transformer foundations  
### Focused on how AI models process ordered information across time, language, and context

<div align="center">

<p>
  <img src="https://img.shields.io/badge/Section-Sequence%20Models%20%26%20Transformers-3949AB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Lectures-32--35-5C6BC0?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Studied%20and%20Practiced-00C853?style=for-the-badge" />
</p>

<p>
  <img src="https://img.shields.io/badge/Topics-Time%20Series%20%7C%20RNN%20%7C%20GRU%20%7C%20LSTM-303F9F?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Topics-Seq2Seq%20%7C%20Attention%20%7C%20Text%20Generation-512DA8?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Topics-Transformers%20%7C%20BERT%20%7C%20GPT-7E57C2?style=for-the-badge" />
</p>

</div>

---

# 📌 Section Overview

This section captures the part of the course where deep learning moved from static inputs into ordered data and language-oriented architectures.

Earlier sections focused mostly on images and tabular learning. This block introduced a different challenge: sequence matters. In time-series data and natural language, one element depends on what came before it. That requires architectures with memory, context handling, and later attention-based reasoning.

The section covers a clear progression:
- time series and sequential data
- RNN fundamentals
- GRU and LSTM as memory-improved recurrent models
- Seq2Seq architecture
- attention mechanism
- practical RNN/LSTM text generation
- transformer architecture
- BERT vs GPT

This was one of the most important conceptual blocks in the whole course because it leads directly into modern language models.

---

# 🎯 Lecture Coverage In This Section

| Lecture | Topic |
|--------|------|
| 32 | RNN and LSTM |
| 33 | Transformers |
| 34 | RNN and LSTM Code Practice |
| 35 | Transformers |

---

# 🧠 What I Studied In This Section

This section helped me understand:

- what makes sequential data different from ordinary input data
- why memory matters in time-series and language tasks
- how recurrent neural networks process one step at a time
- why vanishing memory becomes a problem in long sequences
- how GRU and LSTM improve memory control
- how sequence-to-sequence models work
- the bottleneck issue in standard Seq2Seq
- why attention was introduced
- how text is tokenized, padded, and converted into trainable sequences
- how transformer models use self-attention and positional encoding
- the difference between BERT and GPT

This section gave me a much more practical mental model of how large language model ideas evolved historically.

---

# 🧪 Notebook Coverage

```text
11-sequence-models-and-transformers/notebooks/
└── 01_rnn_lstm_text_generation_basics.ipynb
```

This notebook reflects my practice with recurrent sequence modeling and next-word style text generation workflows.

---

# 📝 Notes Included In This Section

```text
11-sequence-models-and-transformers/notes/
├── 01-time-series-and-sequential-data.md
├── 02-rnn-gru-and-lstm-basics.md
├── 03-seq2seq-and-attention-mechanism.md
├── 04-rnn-lstm-text-generation-practice.md
└── 05-transformer-architecture-bert-vs-gpt.md
```

---

# 🧩 Portfolio Placement In This Section

This section currently acts as a concept-and-practice block without a separate assignment folder in my repo structure.

Its portfolio role is major because it connects:
- deep learning foundations
- language modeling basics
- transformer theory
- the later RAG section

In other words, this section builds the conceptual bridge from neural networks into modern LLM understanding.

---

# 💡 Why This Section Matters

This section matters because it explains how AI systems work when order, sequence, and context are essential.

That matters for:
- forecasting
- translation
- summarization
- next-word prediction
- chat systems
- modern LLMs

It also helped me understand why transformers were such a major shift. They solved important weaknesses in recurrent processing and created the foundation for the most powerful language models used today.

This block is one of the most strategically important sections in the whole portfolio because it ties together deep learning history and current AI practice.

---

# 🔗 Connection To The Next Stage

After this sequence-model block, the course moves into Retrieval-Augmented Generation and LangChain-based system building.

That transition made a lot of sense:
- sequence models explained language processing history
- transformers explained the foundation of modern LLMs
- RAG then explained how those LLMs are connected to external knowledge in real applications

So this section is the final architecture foundation before the course enters applied LLM systems.

Next stage in the course: **RAG and LangChain Pipeline**.
