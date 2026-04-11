# LLM Selection, Cost, and Capability Tradeoffs

This note comes from the retrieval lecture and my supporting notes on model choice.

One of the strongest ideas from this topic is that choosing a model is part of the system design, not an afterthought.

In a RAG system, the model does not always need massive built-in world knowledge. Its job is often to read the retrieved context carefully, reason over it, and produce a good answer. That is why smaller or “mini” models can sometimes be a very strong option.

The lecture and notes also pushed me to think about tradeoffs:
- reasoning quality
- coding ability
- multimodal support
- context window size
- embedding support
- cost per request
- latency
- client budget

This was an important professional lesson. A good developer should be able to justify model selection instead of choosing blindly based on popularity.

Another useful takeaway was that I should stay updated. Model ecosystems change quickly, and client-facing credibility depends partly on knowing which tools are current and where each one is strong or weak.

My biggest lesson here is that model selection is part of product thinking. The best model is not always the largest one. It is the one that fits the use case, the quality requirement, and the budget.
