# AI-code-comment-generator
This is a Streamlit web application designed to compare two AI models for generating code comments: a pre-trained CodeT5-small model and a custom, scratch-built Tiny Transformer.
# 🧠 AI Code Comment Generator (Beginner-Focused Case Study)

 Overview
This project explores **automatic Python code comment generation** using two different Transformer-based approaches:

1. **CodeT5-small (Base Model)** – a pre-trained model evaluated without fine-tuning  
2. **Tiny Transformer** – a custom Transformer trained from scratch on expanded mock data

The goal of this case study is not to achieve production-level performance, but to **analyze model behavior, limitations, and trade-offs** under constrained data settings, while emphasizing **interpretability and transparency** through visualization.

---

## 🎯 Problem Statement
Understanding source code is challenging for beginners due to:
- Missing or unclear comments
- Technical compiler-style error messages
- Difficulty understanding the *intent* behind code logic

This project investigates whether Transformer-based models can help generate readable comments and what factors most strongly influence their effectiveness.

---

## 💡 Project Objectives
- Compare a **pre-trained Transformer** with a **from-scratch Transformer**
- Evaluate performance using **BLEU**, **ROUGE**, and **latency**
- Understand the impact of **dataset size**
- Demonstrate the importance of **model transparency and visualization**

---

## 🛠️ Technologies Used
- Python  
- PyTorch  
- HuggingFace Transformers (CodeT5-small)  
- Custom Transformer implementation  
- Streamlit (visualization and analysis interface)  

---

## 📊 Evaluation Summary

### Comparative Model Performance

| Metric                  | CodeT5-small (Base Model) | Tiny Transformer (Re-trained) |
|-------------------------|---------------------------|--------------------------------|
| Average Latency (s)     | 0.7944                    | 0.7180                         |
| BLEU Score              | 0.0000                    | 0.0000                         |
| ROUGE-1 F1              | 0.1119                    | 0.4330                         |
| ROUGE-2 F1              | 0.0000                    | 0.0326                         |
| ROUGE-L F1              | 0.1119                    | 0.2391                         |

---

## 🧠 Observed Outcomes and Discussion

### BLEU Scores
Both models achieved a BLEU score of **0.0000**, indicating no exact n-gram overlap with reference comments.  
This outcome highlights the unsuitability of BLEU for extremely small datasets and the inability of both models to generate phrasing aligned with reference text under limited data conditions.

### ROUGE Scores
The Tiny Transformer achieved higher ROUGE scores, particularly ROUGE-1 and ROUGE-L.  
This improvement reflects **lexical overlap learned from repeated exposure to a small dataset**, rather than genuine semantic understanding.  
The base CodeT5-small model, evaluated without fine-tuning, remained more generic and showed lower overlap.

### Inference Latency
The Tiny Transformer demonstrated slightly lower inference latency due to its simpler architecture and smaller parameter count.  
CodeT5-small incurred higher latency as expected from a larger, more expressive pre-trained model.

### Qualitative Results
Despite numerical differences, **both models produced largely incoherent and low-quality comments**.  
This confirms that meaningful natural language generation is **not feasible with extremely small training datasets**, regardless of model architecture.

---

## 📌 Key Learnings

### 1️⃣ Data Scale Is Critical
Transformer models require **large, diverse, and high-quality datasets** to learn meaningful language representations.  
The mock datasets used in this project (3 and 50 samples) were insufficient for realistic performance.

### 2️⃣ Power of Pre-trained Models
While building a Transformer from scratch is valuable for learning, **pre-trained models such as CodeT5 provide a far stronger foundation**.  
With proper fine-tuning on sufficient data, pre-trained models dramatically outperform scratch-trained models.

### 3️⃣ Efficiency vs. Practical Quality
Although the Tiny Transformer showed marginal improvements in ROUGE scores and latency on limited data, these gains do not translate into practical usefulness.  
In real-world scenarios, **fine-tuned pre-trained models dominate** in both quality and robustness.

### 4️⃣ Importance of Visualization and Transparency
The Streamlit application played a crucial role in:
- Visualizing preprocessing steps
- Comparing metrics across models
- Making abstract ML concepts understandable

Transparency through visualization is essential when analyzing complex machine learning systems, especially in educational contexts.

---

## 🧪 Streamlit Application
The project includes an interactive **Streamlit dashboard** that:
- Displays preprocessing details
- Shows tokenization statistics
- Compares BLEU, ROUGE, and latency metrics
- Supports qualitative inspection of model outputs

---

## 📂 Project Structure
ai-code-comment-generator/
│
├── app/ # Streamlit application
├── case-study/ # Detailed written analysis
├── examples/ # Sample inputs and outputs
├── screenshots/ # UI visuals
├── requirements.txt
└── README.md



---

## 🚀 Future Work
- Fine-tune CodeT5-small on a large-scale real dataset
- Replace mock data with millions of code–comment pairs
- Improve evaluation with semantic metrics (BERTScore, human evaluation)
- Extend to additional programming languages

---

## 🎓 Academic Relevance
This project is suitable for:
- Machine Learning and NLP coursework
- Case study–based evaluation assignments
- Demonstrations of Transformer limitations
- Educational tools for ML transparency

---

## 👤 Author
Srikar Batthula

---

## 📄 License
MIT License


