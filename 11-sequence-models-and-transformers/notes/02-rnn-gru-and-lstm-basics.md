# RNN, GRU, and LSTM Basics

This note covers the main recurrent architectures from the section.

A recurrent neural network processes sequence data step by step while carrying a hidden state that acts like memory. That hidden state lets the model keep some summary of earlier information and use it when producing the current output.

This was a useful conceptual shift because it showed how neural networks can move from static pattern recognition to time-aware reasoning.

However, the lecture also explained a major weakness of simple RNNs: long-term dependencies are hard to preserve. As sequences grow longer, earlier information can fade away. That is the vanishing memory problem.

To address that, the course introduced two stronger variants:

## GRU
A gated recurrent unit uses gating logic to decide how much information should be updated or preserved.

## LSTM
A long short-term memory network adds a more explicit memory-control mechanism and is especially useful when older context must be retained across longer spans.

This made it clear that sequence learning is really a memory-management problem. The architecture must decide what to keep, what to forget, and what to emphasize at each step.

My main takeaway is that LSTMs and GRUs were not random upgrades. They were responses to a real weakness in basic recurrent networks.
