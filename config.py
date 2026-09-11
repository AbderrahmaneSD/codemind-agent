import os
from dotenv import load_dotenv

load_dotenv()

# API keys
GROQ_API_KEY    = os.getenv("GROQ_API_KEY", "")
GITHUB_TOKEN    = os.getenv("GITHUB_TOKEN", "")

# Model
GROQ_MODEL      = "llama-3.1-8b-instant"
EMBED_MODEL     = "all-MiniLM-L6-v2"
MAX_TOKENS      = 1500

# Retrieval
TOP_K           = 4

# Paths
CODEBASE_PATH   = os.getenv("CODEBASE_PATH",   "data/codebase_index")
DOCS_INDEX_PATH = os.getenv("DOCS_INDEX_PATH",  "data/docs_index")

# Agent
MAX_RETRIES     = 2
