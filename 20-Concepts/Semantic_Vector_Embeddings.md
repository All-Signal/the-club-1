---
id: concept-embeddings
type: concept
category: vector-search
created_at: 2026-09-16T09:45:00+05:30
tags:
  - embeddings
  - vector-search
  - qdrant
---

# 📐 Semantic Vector Embeddings

## Local High-Speed Vectorization
Rather than sending knowledge to cloud APIs, the ULTRON unified memory core uses local, fast embeddings (ONNX / FastEmbed / BGE-small) running locally on the Intel CPU or NVIDIA dGPU.

## Hybrid Search Architecture
To achieve 100% recall precision, retrieval blends:
- **Dense Vectors (Cosine Distance)**: Semantic meaning, conceptual parallels.
- **Sparse BM25 (Keyword Match)**: Exact symbol names, function signatures, command flags.
- **Graph Reranking**: Distance in the [[Bi-Temporal_Knowledge_Graphs]] network.
