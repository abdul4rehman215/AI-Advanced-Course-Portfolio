# RAG Overview and Document Loading

This note covers the start of the RAG section.

RAG stands for Retrieval-Augmented Generation. The core idea is that instead of relying only on a model’s internal knowledge, I can connect the model to external documents and make it answer using that retrieved context.

That makes RAG especially useful for private knowledge, company documents, legal material, course notes, and any domain where freshness or traceability matters.

The lecture also made LangChain easier to understand. Instead of thinking of it as “the magic AI framework,” I understood it as an orchestration layer that helps connect loaders, splitters, retrievers, vector stores, prompts, and models into one workflow.

A big part of the lecture focused on document loaders. I studied how the system can ingest:
- PDFs
- text files
- URLs
- web pages

One especially useful point was metadata. The loaders do not only extract text. They can also preserve information like source file names and page numbers. That matters a lot because grounded AI answers are more trustworthy when I can trace where the answer came from.

My biggest takeaway from this topic is that RAG starts with data ingestion quality. If documents are loaded poorly, everything later in the pipeline becomes weaker.
