# Week 1 — Python + LLM fundamentals, first local model

**Goal:** go from "platform engineer who calls LLM APIs" to "engineer who has run a model himself, measured it, and can explain what the numbers mean."

## Sessions

- [ ] **Session 1 — First local model.** Install [Ollama](https://ollama.com), pull a small model (`qwen2.5:3b`), run [Experiment 001](../experiments/001-llm-on-4gb-ram/) and record real numbers.
- [ ] **Session 2 — Python for ML, the 20%.** numpy arrays & broadcasting, pandas DataFrames, loading a CSV and answering three questions from it. Notes in `notes/`.
- [ ] **Session 3 — An LLM call from Java.** Spring AI "hello world": one controller that sends a prompt and returns the answer — the on-ramp to Build #1 (StackTrace AI).

## Concepts to be able to explain by Friday

- Tokens, context windows, and why generation speed is measured in tokens/second
- Quantization (what Q4 does to a model, and why it fits in 4 GB)
- Temperature and top-p, in one sentence each
- Embedding vs. generation models

## How sessions get logged

**The pipeline:** stream the session live on **Twitch** from OBS — while OBS
also records a clean local copy at the same time. The local recording goes to
**YouTube** (*AI Journey* playlist on @bishowpandey); the Twitch VOD is just a
backup, so its 7-day expiry doesn't matter. The YouTube link goes in the table
below; the written entry is built from the video — what was run, what the
numbers were, what broke. Video = the proof, this page = the searchable record.

OBS notes for Rabison (i7-1255U): recording quality "Same as stream" costs no
extra CPU; Intel Quick Sync handles the stream encode.

## Log

| Date | Session | What happened | Video |
|---|---|---|---|
| — | — | Journey starts this week | — |
