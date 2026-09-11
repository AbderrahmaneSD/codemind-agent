# CodeMind

> An AI coding agent built with LangGraph that reviews code, debugs errors, generates tests, and explains logic — using a multi-tool agentic loop with self-reflection.

---

## What it does

Give CodeMind a Python file, a GitHub PR URL, or an error traceback and it will:

- **Review** — find bugs, style issues, and improvement opportunities
- **Debug** — trace errors and suggest fixes with code examples  
- **Test** — generate pytest unit tests for your functions
- **Explain** — break down complex code in plain English

---

## How it works

CodeMind is a [LangGraph](https://langchain-ai.github.io/langgraph/) `StateGraph` with four nodes and a self-reflection retry loop:

```
User input
    │
    ▼
[Planner]   classifies intent: review / debug / test / explain
    │
    ▼
[Router]    selects 1–3 tools based on intent + plan
    │
    ▼
[Executor]  calls tools, synthesises answer
    │
    ▼
[Critic]    scores answer 1–5 → retry if score < 3, else done
```

### Tools

| Tool | What it does |
|---|---|
| `code_reader` | Semantic search over a local codebase using FAISS (reuses [ml-research-assistant](https://github.com/AbderrahmaneOd/ml-research-assistant) embeddings stack) |
| `github_tool` | Fetches PR diffs via the GitHub REST API |
| `repl_tool` | Executes Python in a subprocess to verify fixes or run tests |
| `doc_search` | RAG over Python/framework docs (reuses ml-research-assistant RAG pipeline) |

---


## Quickstart

```bash
git clone https://github.com/AbderrahmaneSD/codemind-agent
cd codemind-agent
pip install -r requirements.txt
cp .env.example .env   # add your GROQ_API_KEY
python app.py
```

Get a free Groq API key at [console.groq.com](https://console.groq.com).

---

## Run in Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](notebooks/codemind_demo.ipynb)

---

## Stack

`Python` · `LangGraph` · `LangChain` · `Groq (LLaMA 3.1)` · `FAISS` · `sentence-transformers` · `Gradio` · `GitHub Actions`

---

## Project structure

```
codemind-agent/
├── agent/
│   ├── state.py          # AgentState TypedDict — shared memory
│   ├── graph.py          # LangGraph StateGraph — node wiring
│   ├── nodes/
│   │   ├── planner.py    # Classifies intent, writes plan
│   │   ├── router.py     # Selects tools per intent
│   │   ├── executor.py   # Calls tools, synthesises answer
│   │   └── critic.py     # Scores answer, triggers retry
│   └── tools/
│       ├── code_reader.py
│       ├── github_tool.py
│       ├── repl_tool.py
│       └── doc_search.py
├── app.py                # Gradio UI
├── config.py             # Env vars + constants
├── tests/
│   └── test_graph.py
├── notebooks/
│   └── codemind_demo.ipynb
├── .github/workflows/ci.yml
└── requirements.txt
```
