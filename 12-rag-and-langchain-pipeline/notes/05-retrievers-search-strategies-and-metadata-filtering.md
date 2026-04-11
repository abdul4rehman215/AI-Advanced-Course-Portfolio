# Retrievers, Search Strategies, and Metadata Filtering

This note covers how the system actually finds relevant information after the data has already been embedded and stored.

The course explained that a retriever is like the interface used to query the vector store. That helped me separate the storage layer from the retrieval layer in my mind.

The lecture covered multiple retrieval ideas:
- semantic similarity search
- cosine similarity
- dot product
- maximum marginal relevance (MMR)
- metadata filtering
- keyword-oriented alternatives such as TF-IDF and SVM

MMR was especially interesting because it tries to reduce redundancy in results. Instead of returning many nearly identical chunks, it encourages more diverse but still relevant retrieval.

Metadata filtering felt even more practical. In large real-world systems, searching everything is often inefficient. Filtering by source, page range, or category can make the system faster and more trustworthy.

Another major point was validation. Retrieval should not only return context. It should return context that can be traced back to a source. That is what makes RAG useful in serious environments.

My biggest takeaway is that retrieval quality is not only about “finding something similar.” It is about finding the right evidence in a controllable and explainable way.
