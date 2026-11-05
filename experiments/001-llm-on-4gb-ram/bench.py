#!/usr/bin/env python3
"""Benchmark a local Ollama model: warm-up, then a timed generation.

Reports tokens/second using Ollama's own eval counters.
Pure stdlib — no pip installs needed.
"""
import json
import sys
import time
import urllib.request

OLLAMA = "http://localhost:11434/api/generate"
MODEL = sys.argv[1] if len(sys.argv) > 1 else "qwen2.5:3b"
PROMPT = (
    "In about 80 words, describe a stainless steel water bottle "
    "for a product page. Be specific and upbeat."
)


def generate(prompt: str) -> dict:
    body = json.dumps({"model": MODEL, "prompt": prompt, "stream": False}).encode()
    req = urllib.request.Request(OLLAMA, data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as resp:
        return json.loads(resp.read())


def main() -> None:
    try:
        print(f"Warming up {MODEL} (first load into memory)...")
        t0 = time.time()
        generate("Say 'ready'.")
        print(f"  load + first reply: {time.time() - t0:.1f}s")

        print("Benchmarking generation...")
        t0 = time.time()
        result = generate(PROMPT)
        wall = time.time() - t0
    except Exception as exc:  # Ollama not running / model not pulled
        print(f"\nCould not reach Ollama at {OLLAMA}: {exc}")
        print("Fix: run `ollama serve` in one terminal and `ollama pull "
              f"{MODEL}` once, then re-run this script.")
        sys.exit(1)

    eval_count = result.get("eval_count", 0)
    eval_secs = result.get("eval_duration", 0) / 1e9
    tps = eval_count / eval_secs if eval_secs else 0.0
    print(f"\nModel:        {MODEL}")
    print(f"Tokens out:   {eval_count}")
    print(f"Eval time:    {eval_secs:.1f}s  ({tps:.1f} tokens/sec)")
    print(f"Wall clock:   {wall:.1f}s (incl. prompt processing)")
    print(f"\nSample output:\n{result.get('response', '').strip()}")


if __name__ == "__main__":
    main()
