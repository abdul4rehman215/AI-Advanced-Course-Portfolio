# Vector Databases and Ingestion Pipelines

This note covers the stage where chunks and embeddings become searchable infrastructure.

A vector database stores embeddings and makes similarity-based retrieval fast and scalable. This is very different from a traditional relational database. In a relational database, data is usually organized in rows and columns. In a vector database, the main goal is semantic proximity search.

The lecture discussed systems like Qdrant and Pinecone, which made the topic feel relevant to actual production work.

Another important idea was the ingestion pipeline:
- load raw data
- split it into chunks
- generate embeddings
- attach metadata
- push everything into the vector store

The metadata part was especially valuable. Page numbers, source names, and custom tags make later filtering and traceability much stronger.

I also liked the discussion around avoiding duplicate insertion. Re-running ingestion carelessly can waste money, increase latency, and clutter the database with redundant vectors.

My takeaway is that vector storage is not only about saving embeddings. It is about building a clean, repeatable ingestion system that can scale without becoming messy or expensive.
