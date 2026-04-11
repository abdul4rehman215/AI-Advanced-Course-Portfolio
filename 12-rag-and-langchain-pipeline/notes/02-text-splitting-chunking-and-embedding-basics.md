# Text Splitting, Chunking, and Embedding Basics

This note covers the second major step in the RAG pipeline: preparing loaded text so it becomes retrievable.

Large language models cannot consume unlimited context. That means documents need to be split into smaller chunks before they can be embedded and retrieved effectively.

The lecture explained different chunking strategies, especially:
- fixed-size character splitting
- recursive character splitting
- overlap between chunks

The idea of overlap was important. If chunks are cut too sharply, meaning can break across boundaries. Overlap helps preserve continuity between neighboring chunks.

The lecture then connected chunking to embeddings. Embeddings convert text into numerical vectors so the system can compare meaning rather than just exact keywords. That was a major concept because it explains how semantic retrieval becomes possible.

I also liked the distinction between the raw text world and the vector world. Humans read words. Retrieval systems compare vectors. Chunking is what makes that transition manageable.

My takeaway is that chunking is not just a preprocessing detail. It directly affects retrieval quality, context preservation, and the final usefulness of the RAG answer.
