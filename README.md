RunPod RAG Pipeline

Complete Retrieval-Augmented Generation (RAG) system using RunPod Serverless for LLM and Embeddings.


- ✅ RunPod Serverless LLM (vLLM) for text generation
- ✅ RunPod Infinity Embedding Worker for embeddings
- ✅ PDF document processing
- ✅ FAISS vector store with persistence
- ✅ Source attribution in answers
- ✅ LangChain orchestration
- ✅ Jupyter notebook interface

pip install langchain langchain-runpod langchain-community langchain-classic faiss-cpu requests pypdf

### 2. Add Your PDFs

Place your PDF documents in the `data/` folder:

bash
cp your_document.pdf data/


### 3. Configure API Keys

Open `runpod_rag_pdf.ipynb` and update:
- `RUNPOD_API_KEY` - Your RunPod API key
- `RUNPOD_LLM_ENDPOINT_ID` - Your vLLM endpoint ID
- `RUNPOD_EMBEDDING_ENDPOINT_ID` - Your Infinity Embedding endpoint ID

### 4. Run the Notebook

bash
jupyter notebook runpod_rag_pdf.ipynb


Run all cells sequentially and start asking questions about your documents!


### `runpod_rag_pdf.ipynb`
**Full-featured RAG pipeline with PDF support**
- Loads PDFs from `data/` folder
- Saves vector store to disk for fast reloading
- Comprehensive comments and explanations
- Production-ready code

## 🔧 How It Works

### 1. Document Loading
- PDFs are loaded from `data/` folder using PyPDFLoader
- Each page is extracted as a separate document
- Metadata (filename, page number) is preserved

### 2. Text Chunking
- Documents are split into chunks using RecursiveCharacterTextSplitter
- Chunk size: 800 characters (configurable)
- Overlap: 150 characters to preserve context

### 3. Embedding Generation
- Each chunk is sent to RunPod Infinity Embedding worker
- Returns 384-dimensional vectors (BAAI/bge-small-en-v1.5)
- Uses OpenAI-compatible API format

### 4. Vector Storage
- FAISS index stores embeddings for fast similarity search
- Saved to `vector_store/` folder for persistence
- Loads instantly on subsequent runs (no re-embedding needed)

### 5. Question Answering
- User question is embedded using the same model
- FAISS finds top-k most similar document chunks
- Chunks + question are sent to RunPod LLM
- LLM generates answer grounded in retrieved context



### Adjust Chunk Size
python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,      # Increase for more context per chunk
    chunk_overlap=300,    # Increase to preserve more context
)


### Change Number of Retrieved Documents
python
retriever=vectorstore.as_retriever(
    search_kwargs={"k": 5}  # Retrieve top 5 instead of 3
)


### Modify LLM Parameters
python
llm = ChatRunPod(
    endpoint_id=RUNPOD_LLM_ENDPOINT_ID,
    model_kwargs={
        "temperature": 0.5,    # Lower = more deterministic
        "max_tokens": 3000,    # Longer responses
    }
)


When you add new PDFs or modify existing ones:

Delete the `vector_store/` folder:
bash
   rm -rf vector_store/


When using `similarity_search_with_score()`:
- **0.0 - 0.3**: Highly relevant (very similar to query)
- **0.3 - 0.5**: Moderately relevant
- **0.5+**: Less relevant

Lower scores = better match (it's a distance metric, not similarity score)

### "No PDF files found"
- Make sure PDFs are in the `data/` folder
- Check file extensions are `.pdf` (lowercase)

### "Vector store loading error"
- Delete `vector_store/` folder and rebuild
- Ensure embeddings object uses same model



# Test embedding endpoint
python embed_api_test.py

# Test LLM endpoint
python llm_api_test.py

Update the `EMBEDDING_ENDPOINT_ID`, `LLM_ENDPOINT_ID`, and `API_KEY` variables in each script before running.


1. **vLLM Endpoint** (for text generation)
   - Model: Any supported LLM (e.g., Llama, Mistral)
   - Get endpoint ID from RunPod dashboard

2. **Infinity Embedding Endpoint** (for embeddings)
   - Worker: `runpod-workers/worker-infinity-embedding`
   - Model: BAAI/bge-small-en-v1.5
   - Get endpoint ID from RunPod dashboard

### API Key:
- Get from: RunPod Dashboard → Settings → API Keys


