<div align="center">

# 🧬 BioGPT-ClinVar

### Fine-Tuning a Biomedical Large Language Model for Genomic Variant Interpretation Using Parameter-Efficient LoRA

#### Vania Karimi · Independent Researcher

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)]()
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0-red?style=for-the-badge&logo=pytorch)]()
[![Transformers](https://img.shields.io/badge/HuggingFace-Transformers-yellow?style=for-the-badge)]()
[![BioGPT](https://img.shields.io/badge/BioGPT-Microsoft-purple?style=for-the-badge)]()
[![LoRA](https://img.shields.io/badge/PEFT-LoRA-green?style=for-the-badge)]()
[![ClinVar](https://img.shields.io/badge/Dataset-ClinVar-orange?style=for-the-badge)]()
[![GPU](https://img.shields.io/badge/GPU-Tesla_T4-76B900?style=for-the-badge&logo=nvidia)]()
[![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)]()

### 🧬 Biomedical Large Language Models for Genomic Variant Interpretation

**Parameter-Efficient Fine-Tuning of BioGPT on ClinVar Variants**

📄 Preprint in Preparation  
🤗 Hugging Face Model Available  
🔬 Fully Reproducible Pipeline  
⚡ Single-GPU Training  
🧪 Independent Biomedical AI Research

</div>

---

> **Biomedical AI • Precision Medicine • Genomic LLMs • Open Science**

This repository presents a fully reproducible framework for adapting BioGPT to genomic variant interpretation using Low-Rank Adaptation (LoRA) and publicly available ClinVar data.

---

# 📖 Overview

Clinical interpretation of genomic variants remains one of the major bottlenecks in precision medicine. Public resources such as ClinVar contain thousands of clinically annotated variants, yet manual interpretation is labor-intensive and difficult to scale.

This project investigates the adaptation of BioGPT, a biomedical large language model trained on PubMed literature, to genomic variant interpretation using parameter-efficient fine-tuning.

The entire pipeline is reproducible, computationally accessible, and designed for independent biomedical AI research.

---

# 🚀 Project Highlights

- 🧬 Fine-tuned BioGPT on approximately 20,000 ClinVar variants
- ⚡ Parameter-efficient LoRA adaptation
- 🔬 BF16 mixed-precision training
- 💻 Trained on a single NVIDIA Tesla T4 GPU
- 📊 Stable optimization and convergence
- 🔁 Fully reproducible training pipeline
- 🤗 Public model release on Hugging Face
- 🧪 Independent biomedical AI research

---

# 🏗️ Architecture

```text
ClinVar Dataset
        │
        ▼
Data Collection
        │
        ▼
Preprocessing Pipeline
        │
        ▼
Prompt Construction
        │
        ▼
BioGPT (150M)
        │
        ▼
LoRA Fine-Tuning
        │
        ▼
Validation
        │
        ▼
Model Deployment

---

📂 Repository Structure

biogpt-clinvar/
│
├── data/
│   ├── download_clinvar.py
│   └── preprocess.py
│
├── finetune/
│   └── train.py
│
├── evaluation/
│
├── models/
│
├── config.py
├── inference.py
├── requirements.txt
├── README.md
└── LICENSE

---

📊 Dataset

The study utilizes publicly available ClinVar records.

Stage| Number of Records
Raw ClinVar Records| 20,000
After Duplicate Removal| ~19,600
Training Set| 16,000
Validation Set| 2,000
Reserved Test Set| 2,000

Variants with conflicting or uncertain interpretations were excluded.

---

⚙️ Training Configuration

Parameter| Value
Base Model| BioGPT
Parameters| 150M
Fine-Tuning Method| LoRA
LoRA Rank| 16
LoRA Alpha| 32
Epochs| 3
Learning Rate| 5e-5
Optimizer| AdamW
Precision| BF16
Hardware| Tesla T4
Framework| Hugging Face Transformers

---

📈 Training Results

Metric| Initial| Final
Training Loss| 1.49| 1.39
Validation Loss| 1.45| 1.40

The small divergence between training and validation losses suggests stable optimization and limited overfitting.

---

🔬 Key Findings

- BioGPT can be successfully adapted to genomic variant interpretation.
- LoRA enables efficient fine-tuning with minimal computational cost.
- Stable convergence was achieved during optimization.
- Validation loss closely followed training loss.
- The workflow is fully reproducible.

---

🧪 How to Use the Model

from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Sepideh2027/biogpt-clinvar-finetuned"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def interpret_variant(variant):
    prompt = f"Interpret the clinical significance of this variant: {variant}"

    inputs = tokenizer(
        prompt,
        return_tensors="pt"
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=50
    )

    return tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

print(interpret_variant("BRCA1 c.68_69delAG"))

---

💻 Installation

git clone https://github.com/YOUR_USERNAME/biogpt-clinvar.git

cd biogpt-clinvar

pip install -r requirements.txt

---

📥 Download Data

python data/download_clinvar.py

---

🔄 Data Preprocessing

python data/preprocess.py

---

🚀 Fine-Tuning

python finetune/train.py

---

📊 Computational Resources

Training was performed on a single NVIDIA Tesla T4 GPU using BF16 mixed-precision training.

The use of LoRA significantly reduced the number of trainable parameters, enabling efficient adaptation using modest hardware resources.

---

🔁 Reproducibility

- Public ClinVar dataset
- Open-source code
- Public model weights
- Fixed configuration files
- Documented preprocessing pipeline
- Reproducible training workflow

---

⚠️ Limitations

- Moderate dataset size (~20,000 variants).
- Limited representation of structural variants.
- External benchmark evaluation has not yet been performed.
- Model explainability methods were not incorporated.
- Quantitative evaluation metrics (accuracy, precision, recall, and F1-score) are currently under investigation and will be reported in future updates.

---

🔮 Future Directions

- Larger genomic datasets.
- Retrieval-Augmented Generation.
- Explainable genomic AI.
- Multi-agent biomedical systems.
- Clinical decision-support applications.
- Prospective real-world evaluation.

---

🤗 Model Availability

Hugging Face Model:

https://huggingface.co/Sepideh2027/biogpt-clinvar-finetuned

---

📄 Preprint

A preprint describing the methodology and experimental findings is currently in preparation.

---

🏛 Affiliation

Independent Researcher

This study was conducted independently using publicly available datasets, open-source software, and accessible computational resources.

---

📚 Citation

@article{Moafi2026biogpt,
  title={BioGPT-ClinVar: Fine-Tuning a Biomedical Large Language Model for Genomic Variant Interpretation Using Parameter-Efficient LoRA},
  author={Moafi , Sepideh},
  journal={Preprint},
  year={2026}
}

---

🙏 Acknowledgements

The author thanks:

- ClinVar contributors
- BioGPT developers
- Hugging Face community
- Open-source biomedical AI researchers

---

👩‍🔬 Author

Sepideh Moafi 
Independent Researcher

Research Interests:

- Biomedical Large Language Models
- Genomic Artificial Intelligence
- Computational Biology
- Precision Medicine
- AI for Healthcare

---

📜 License

This project is released under the MIT License.

---

<div align="center">⭐ If you find this work useful, please consider starring the repository.

🧬 Biomedical AI • Genomic Medicine • Open Science

</div>
```
