# Results

## Quantitative Evaluation

| Metric                  | CodeT5-small (Base Model) | Tiny Transformer (Re-trained) |
|-------------------------|---------------------------|--------------------------------|
| Average Latency (s)     | 0.7944                    | 0.7180                         |
| BLEU Score              | 0.0000                    | 0.0000                         |
| ROUGE-1 F1              | 0.1119                    | 0.4330                         |
| ROUGE-2 F1              | 0.0000                    | 0.0326                         |
| ROUGE-L F1              | 0.1119                    | 0.2391                         |

## Interpretation of Results

Both models achieved a BLEU score of 0.0000, indicating no exact n-gram overlap
with reference comments. This highlights the unsuitability of BLEU for very
small datasets and the inability of both models to generate reference-aligned
text under data-scarce conditions.

The Tiny Transformer achieved higher ROUGE scores, suggesting improved lexical
overlap with the reference comments. However, this improvement reflects pattern
memorization rather than true semantic understanding.

The Tiny Transformer also showed slightly lower inference latency due to its
simpler architecture and smaller parameter count.

## Qualitative Observations
Despite numerical differences, both models generated largely incoherent and
low-quality comments. Generated outputs often lacked grammatical structure
and meaningful explanations.

## Key Findings
- Extremely small datasets severely limit model performance
- Pre-trained models require fine-tuning to be effective
- From-scratch models can show surface-level improvements but lack robustness
- Visualization tools are essential for understanding and communicating results
