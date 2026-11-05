# Experiment 001 — What AI can actually run in 4 GB of RAM?

**Question:** A 4 GB RAM box is what a cheap VPS gives you. Which LLMs genuinely run on it — and what are they good (and bad) at?

**Why it matters:** "AI features" for small products die on hosting costs. If a 3B-class model on a $5 VPS can draft product descriptions, summarize, and classify, a whole class of tiny products becomes viable.

## Method

- Runtime: [Ollama](https://ollama.com) (llama.cpp under the hood)
- Models: `qwen2.5:3b` and `llama3.2:3b`, Q4 quantization (~2 GB on disk)
- Machine: *(record CPU / RAM / OS when run)*
- Script: [`bench.py`](bench.py) — warms the model up, then times a fixed generation and reports tokens/second from Ollama's own counters
- Prompts: one short factual prompt, one product-description prompt, one summarization prompt

## Results

| Model | Load time | Tokens/sec | Peak RAM | Notes |
|---|---|---|---|---|
| qwen2.5:3b (Q4) | TBD | TBD | TBD | |
| llama3.2:3b (Q4) | TBD | TBD | TBD | |

*(Filled in after the first run — real numbers only.)*

## Early expectations (to be tested)

- Both 3B Q4 models should fit beside a small web service; a 7B model should not.
- CPU inference will be fine for background jobs (descriptions, summaries) and too slow for live chat.
- Output quality at 3B is "useful draft," not "publish as-is."

## Run it yourself

```bash
ollama pull qwen2.5:3b
ollama serve        # in one terminal
python3 bench.py    # in another
```
