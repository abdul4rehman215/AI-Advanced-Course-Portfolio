# LCEL and Question-Answering Chains

This note covers the final lecture in the RAG section.

LCEL, or LangChain Expression Language, was introduced as a way to build AI workflows by connecting components into structured chains. That made the whole RAG system feel more modular and engineering-oriented.

The lecture explained different execution methods such as stream, invoke, and batch. That helped me understand that chains are not only conceptual diagrams. They are executable pipelines with different runtime behaviors.

I also studied the main chain types:
- QA chain
- QA retrieval chain
- conversation chain
- conversation retrieval chain

This progression made sense. First comes basic model interaction. Then comes retrieval-aware answering. Then comes memory of prior conversation. Finally comes retrieval plus conversational history together.

Another useful concept was prompt formatting inside the chain. The final answer quality depends not only on retrieved data, but also on how that context is assembled and passed to the model.

My main takeaway is that LCEL turns RAG from a loose collection of notebook steps into a more organized application architecture.
