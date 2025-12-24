# Solution Design

## System Overview
The project implements a comparative framework to evaluate two approaches
to code comment generation:

1. A pre-trained Transformer model (CodeT5-small, base version)
2. A custom Tiny Transformer trained from scratch on mock data

The system focuses on transparency, interpretability, and reproducibility.

## Model Architectures

### CodeT5-small (Base Model)
CodeT5-small is a pre-trained Transformer model designed for code-related
tasks. In this project, the base model is used without fine-tuning to
understand how a generic pre-trained model behaves on a small, task-specific
dataset.

### Tiny Transformer (From Scratch)
The Tiny Transformer is a lightweight custom model trained on an expanded
mock dataset. It is intentionally small to highlight the effects of limited
data and reduced model capacity.

## Data Processing
Raw code–comment pairs were cleaned and filtered to remove noise.
Tokenization was applied with fixed maximum lengths for code and comments
to ensure consistent input formatting.

## Evaluation Metrics
The following metrics were used:
- BLEU: Measures n-gram overlap between generated and reference comments
- ROUGE-1, ROUGE-2, ROUGE-L: Measure lexical overlap and sequence similarity
- Inference Latency: Measures average response time per generation

## Visualization
A Streamlit web application was developed to:
- Display preprocessing steps
- Compare evaluation metrics
- Inspect generated outputs interactively

This visualization layer improves transparency and helps interpret complex
model behavior.
