<div align="center">

# 🧬 BioGPT-ClinVar
 
## A Reproducible Framework for Parameter-Efficient Adaptation of Biomedical Large Language Models for Genomic Variant Interpretation
---
**Year:** 2024–2025  
**License:** MIT  
**Author:** Sepideh Moafi
---

**Technologies:**  
Python • PyTorch • Hugging Face Transformers • BioGPT • PEFT/LoRA • ClinVar • GPU Computing

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


📄 **Preprint in Preparation**  
🤗 **Hugging Face Model Available**  
🔬 **Fully Reproducible Research Pipeline**  
⚡ **Single-GPU Biomedical LLM Adaptation**  
🧪 **Independent Biomedical AI Research**

**Biomedical AI • Computational Genomics • Biomedical Large Language Models • Precision Medicine • Open Science**



</div>

---

> **Biomedical AI • Precision Medicine • Genomic LLMs • Open Science**

This repository presents a fully reproducible framework for adapting BioGPT to genomic variant interpretation using Low-Rank Adaptation (LoRA) and publicly available ClinVar data.

---


# Overview

BioGPT-ClinVar is a reproducible biomedical AI framework for adapting a pretrained biomedical large language model to genomic variant interpretation using parameter-efficient fine-tuning.

The project explores the application of **Low-Rank Adaptation (LoRA)** to specialize BioGPT, a biomedical autoregressive language model with approximately **150 million parameters**, toward the interpretation of clinically annotated genomic variants from ClinVar.

Rather than focusing only on model optimization, this work develops an end-to-end research framework integrating genomic data processing, instruction dataset construction, efficient model adaptation, evaluation workflows, and reproducible inference.

The framework demonstrates how biomedical large language models can be adapted to specialized genomic tasks using accessible computational resources while maintaining transparent and reproducible research practices.

---

---

# Research Motivation

The rapid growth of sequencing technologies has generated an increasing number of genomic variants requiring interpretation. Although databases such as ClinVar provide valuable clinical annotations, transforming structured genomic information into meaningful biological interpretations remains a challenging computational problem.

Biomedical large language models offer new opportunities for assisting genomic reasoning by leveraging their ability to represent complex biomedical language and domain knowledge. However, adapting large-scale models to specialized biomedical tasks can require substantial computational resources and careful data engineering.

BioGPT-ClinVar investigates whether **parameter-efficient adaptation strategies** can provide an effective and computationally accessible approach for specializing biomedical language models toward genomic variant interpretation.

The project combines:
- biomedical foundation models,
- structured genomic data engineering,
- parameter-efficient fine-tuning,
- and reproducible machine learning workflows

to establish a foundation for future trustworthy biomedical AI systems.

---

# Why This Project Matters

Biomedical AI systems increasingly rely on foundation models, yet reproducible frameworks for adapting these models to specialized scientific domains remain limited.

BioGPT-ClinVar addresses this challenge by providing a complete research pipeline from raw genomic data processing to model deployment.

The project emphasizes:

- efficient adaptation of biomedical large language models,
- transparent preprocessing of genomic resources,
- reproducible training workflows,
- and open dissemination of computational resources.

This framework provides a foundation for future research in genomic reasoning, precision medicine, and trustworthy biomedical artificial intelligence.

---

# Key Contributions

- Developed an end-to-end framework for adapting a biomedical large language model to genomic variant interpretation.

- Built a reproducible ClinVar data processing pipeline converting raw genomic variant records into structured instruction-style training examples.

- Applied **LoRA-based parameter-efficient fine-tuning** to BioGPT, enabling domain adaptation with reduced computational requirements.

- Designed modular components for:
  - genomic data preprocessing,
  - dataset construction,
  - model training,
  - evaluation,
  - and inference.

- Optimized training for single-GPU execution using **NVIDIA Tesla T4 GPU** and **BF16 mixed-precision computation**.

- Released reproducible implementation resources and trained model artifacts through GitHub and Hugging Face.

---

# Repository Highlights

- 🧬 ClinVar-based genomic instruction dataset construction
- 🤖 Biomedical LLM adaptation using BioGPT
- ⚡ LoRA-based efficient fine-tuning
- 💻 Single-GPU mixed-precision training
- 🔄 Reproducible preprocessing and training pipeline
- 🧪 Evaluation and inference workflow
- 🤗 Public model release through Hugging Face
- 🔬 Open-source biomedical AI research framework

---

# Framework Overview

The BioGPT-ClinVar framework provides a complete workflow for adapting biomedical large language models to genomic interpretation tasks.

```text
ClinVar Genomic Records
          │
          ▼
Variant Extraction & Filtering
          │
          ▼
Clinical Significance Processing
          │
          ▼
Instruction Dataset Construction
          │
          ▼
Train / Validation / Test Split
          │
          ▼
BioGPT + LoRA Adaptation
          │
          ▼
Model Evaluation
          │
          ▼
Genomic Variant Inference
          │
          ▼
Model Release.

---

Dataset Preparation

## ClinVar Data Engineering Pipeline

BioGPT-ClinVar uses publicly available ClinVar genomic variant annotations to construct a specialized instruction-style dataset for biomedical large language model adaptation.

A custom preprocessing pipeline was developed to transform raw genomic variant records into structured training examples suitable for causal language modeling.

The data processing workflow includes:

- Acquisition of ClinVar genomic variant records
- Extraction of variant-level information
- Parsing of clinical significance annotations
- Label normalization
- Removal of duplicated records
- Construction of instruction-style training examples
- Reproducible dataset partitioning

The objective of this pipeline is to bridge the gap between structured genomic databases and natural-language-based biomedical model training.

---

## Variant Information Extraction

From raw ClinVar records, the preprocessing pipeline extracts relevant genomic information including:

- Chromosome
- Genomic position
- Reference allele
- Alternative allele
- Clinical significance annotation

The extracted genomic information is transformed into instruction-style examples designed for biomedical language model adaptation.

### Example Transformation

**Raw ClinVar Record**
Chromosome: 17
Position: 43071077
Reference: C
Alternative: T
Clinical Significance: Pathogenic

⬇️

**Instruction-Style Training Example**
Instruction: Interpret the clinical significance of this genomic variant.
Input: Variant: 17:43071077 C>T
Output: Clinical Significance: Pathogenic

---

# Clinical Label Processing

To create consistent supervised learning targets, clinical significance annotations were normalized into simplified categories.

The current framework focuses on:

- Pathogenic
- Benign

Variants with unclear, conflicting, or insufficient clinical interpretation were excluded during preprocessing to improve label consistency.

---

# Dataset Statistics

The preprocessing pipeline generated a curated ClinVar subset for biomedical LLM adaptation.

| Processing Stage | Number of Records |
|---|---:|
| Raw ClinVar Variants | 20,000 |
| After Duplicate Removal | ~19,600 |
| Training Set | 16,000 |
| Validation Set | 2,000 |
| Test Set | 2,000 |

Dataset splitting was performed using deterministic partitioning to ensure reproducible experiments.

---

# 🧠 Model Architecture

## Base Biomedical Large Language Model

BioGPT-ClinVar adapts:

## BioGPT

A biomedical autoregressive transformer language model pretrained on biomedical literature.

Model characteristics:

| Component | Description |
|---|---|
| Architecture | Transformer-based Causal Language Model |
| Parameters | ~150M |
| Framework | Hugging Face Transformers |

BioGPT was selected due to its biomedical domain pretraining and suitability for adapting language-based models toward specialized biomedical tasks.

---

# ⚡ Parameter-Efficient Adaptation with LoRA

Instead of updating all parameters of the pretrained model, BioGPT-ClinVar applies:

## Low-Rank Adaptation (LoRA)

LoRA introduces trainable low-rank matrices into selected transformer layers while keeping the majority of pretrained parameters frozen.

This strategy provides:

- Reduced computational requirements
- Faster adaptation
- Lower memory usage
- Preservation of pretrained biomedical knowledge

The approach enables biomedical LLM adaptation using accessible GPU resources.

---

# LoRA Configuration

| Parameter | Value |
|---|---:|
| Adaptation Method | LoRA (PEFT) |
| Rank (r) | 16 |
| Alpha | 32 |
| Dropout | 0.05 |
| Bias | None |
| Target Modules | q_proj, k_proj, v_proj, out_proj |

The LoRA adapters were applied to attention projection layers to efficiently optimize BioGPT for genomic variant interpretation.

---

# ⚙️ Training Configuration

The fine-tuning pipeline was implemented using:

- PyTorch
- Hugging Face Transformers
- PEFT library
- Hugging Face Trainer API

## Training Setup

| Parameter | Value |
|---|---|
| Base Model | BioGPT |
| Fine-Tuning Strategy | LoRA-based PEFT |
| Objective | Causal Language Modeling |
| Epochs | 3 |
| Learning Rate | 5e-5 |
| Optimizer | AdamW |
| Weight Decay | 0.01 |
| Batch Size | 4 |
| Gradient Accumulation | 4 |
| Maximum Sequence Length | 128 |
| Precision | BF16 Mixed Precision |

---

# 💻 Computational Resources

Training was performed using:

| Resource | Configuration |
|---|---|
| GPU | NVIDIA Tesla T4 |
| Training Mode | Single-GPU Adaptation |
| Precision | BF16 Mixed Precision |
| Framework | PyTorch + Transformers |

The use of LoRA significantly reduced the computational cost compared with full-model fine-tuning, enabling biomedical foundation model adaptation using limited hardware resources.

Training Results

The BioGPT-ClinVar model demonstrated stable optimization during parameter-efficient adaptation using LoRA.

Training dynamics were monitored through training and validation loss across the fine-tuning process.

| Metric | Initial | Final |
|---|---:|---:|
| Training Loss | 1.49 | 1.39 |
| Validation Loss | 1.45 | 1.40 |

The close alignment between training and validation loss trajectories suggests stable convergence during adaptation, with limited evidence of overfitting under the current experimental setting.

These results demonstrate the feasibility of adapting a biomedical large language model to genomic variant interpretation using parameter-efficient methods and accessible computational resources.

---

# 🔬 Evaluation Framework

A modular evaluation workflow was developed to assess the behavior of the adapted BioGPT model on held-out genomic variants.

The evaluation pipeline includes:

1. Loading the LoRA-adapted BioGPT model
2. Preparing unseen genomic variant inputs
3. Generating model interpretations
4. Comparing generated outputs with reference ClinVar annotations
5. Saving prediction outputs for further analysis

Evaluation workflow:

```text
Held-Out ClinVar Variants
          │
          ▼
BioGPT-ClinVar Inference
          │
          ▼
Generated Variant Interpretation
          │
          ▼
Comparison with Reference Annotation
          │
          ▼
Performance Analysis
The current framework establishes the infrastructure for future benchmarking using additional evaluation metrics and external genomic interpretation resources.
🧪 Model Inference
A lightweight inference workflow was developed to enable researchers to apply the adapted model to genomic variant interpretation tasks.
The inference module provides a simple interface for generating predictions from variant descriptions.
Example Usage
from inference import GenomicVariantInterpreter

interpreter = GenomicVariantInterpreter(
    model_path="./biogpt_final_model"
)

result = interpreter.interpret(
    "BRCA1 c.68_69delAG"
)

print(result)
Example variants explored during inference:
BRCA1 c.68_69delAG
CFTR F508del
TP53 R175H
The inference workflow supports GPU-accelerated execution when CUDA resources are available.
🔄 Reproducible Research Pipeline
The repository provides a modular and reproducible implementation covering the complete model development lifecycle.
Data Acquisition
        │
        ▼
ClinVar Data Processing
        │
        ▼
Instruction Dataset Construction
        │
        ▼
Train / Validation / Test Split
        │
        ▼
LoRA Fine-Tuning
        │
        ▼
Model Evaluation
        │
        ▼
Inference Pipeline
        │
        ▼
Model Release
The repository structure separates data processing, model adaptation, evaluation, and inference components to improve reproducibility and future extension.
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
├── inference.py
│
├── config.py
│
├── requirements.txt
│
└── README.md
🤗 Model Availability
The adapted BioGPT resources are publicly released through Hugging Face.
Available components include:
LoRA-adapted model weights
Model configuration
Tokenizer resources
Reproducible inference workflow
The released resources allow researchers to reproduce experiments and further investigate biomedical large language models for genomic interpretation tasks.
🌐 Open Science & Accessibility
BioGPT-ClinVar was developed following open and reproducible research principles:
✅ Public biomedical dataset (ClinVar)
✅ Open-source implementation
✅ Documented preprocessing pipeline
✅ Reproducible training configuration
✅ Public model availability
The project demonstrates how biomedical large language models can be adapted efficiently through parameter-efficient approaches while maintaining accessibility for independent research environments.
⚠️ Limitations
Although BioGPT-ClinVar demonstrates the feasibility of adapting biomedical large language models for genomic variant interpretation, several limitations remain.
The current study uses a curated subset of ClinVar variants.
The training objective focuses on simplified clinical significance categories.
Variants with uncertain or conflicting annotations were excluded during preprocessing.
External benchmarking against established variant interpretation tools has not yet been performed.
Additional explainability and uncertainty estimation analyses are required.
Evaluation on larger and more diverse genomic resources represents an important future direction.


Future Directions

BioGPT-ClinVar establishes a foundation for future development of more reliable and evidence-aware genomic AI systems.

Several research directions can further extend this framework:

---

## 1. Large-Scale Genomic Foundation Model Adaptation

Future work may investigate adaptation using larger and more diverse genomic resources, including:

- Expanded ClinVar releases
- Additional variant databases
- Broader genomic annotation sources
- More complex variant interpretation tasks

These extensions could improve model generalization across diverse genomic contexts.

---

## 2. Evidence-Grounded Genomic Reasoning

A natural extension of this framework is integrating external biomedical knowledge sources to improve evidence-based interpretation.

Potential directions include:

- Retrieval-Augmented Generation (RAG)
- Biomedical literature retrieval
- Functional annotation databases
- Knowledge graph integration

Such approaches may enable models to generate more transparent and evidence-supported genomic interpretations.

---

## 3. Explainable and Trustworthy Biomedical Language Models

Future investigations may focus on improving model transparency through:

- Attribution methods
- Attention analysis
- Uncertainty estimation
- Evidence tracing
- Calibration analysis

These approaches are essential for developing trustworthy AI systems in biomedical applications.

---

## 4. Multimodal Biomedical AI

Future versions of the framework may integrate multiple biological data modalities, including:

- Genomic variants
- Transcriptomic information
- Biomedical literature
- Molecular features
- Clinical annotations

Such multimodal approaches could enable richer representations of genotype–phenotype relationships.

---

# 🧬 Research Impact

BioGPT-ClinVar demonstrates an accessible approach for adapting biomedical large language models to specialized genomic tasks.

The project highlights how the combination of:

- biomedical foundation models,
- parameter-efficient learning,
- genomic data engineering,
- and reproducible open-source workflows

can support independent research in computational genomics.

By reducing computational barriers to biomedical LLM adaptation, this framework contributes toward more accessible and reproducible development of AI methods for precision medicine and biological discovery.

---

# 🏛 Research Profile

**Independent Biomedical AI Research Project**

This work was conducted independently using:

- Public biomedical datasets
- Open-source machine learning frameworks
- Accessible GPU computing resources

The project reflects an interest in developing reliable computational methods at the intersection of:

- Artificial Intelligence
- Computational Biology
- Genomics
- Precision Medicine

---

📌 Project Summary
BioGPT-ClinVar provides an end-to-end framework for adapting biomedical large language models to genomic variant interpretation through:
🧬 Genomic Data Engineering
Transforming ClinVar genomic records into structured instruction datasets.
🤖 Biomedical LLM Adaptation
Applying LoRA-based parameter-efficient fine-tuning to BioGPT.
⚡ Efficient Computing
Enabling biomedical foundation model adaptation using a single NVIDIA Tesla T4 GPU.
🔬 Reproducible Research
Providing documented workflows, open-source implementation, and model resources.
The project bridges:
🧬 Genomics
🤖 Biomedical Artificial Intelligence
⚡ Foundation Model Adaptation
🔬 Open Science
toward future development of reliable AI systems for biomedical discovery.












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

git clone https://github.com/AIResearcher20/biogpt-clinvar.git

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

@article{Moafi2025biogpt,
  title={BioGPT-ClinVar: Fine-Tuning a Biomedical Large Language Model for Genomic Variant Interpretation Using Parameter-Efficient LoRA},
  author={Moafi , Sepideh},
  journal={Preprint},
  year={2025},
  journal={Research Square},
  doi={10.21203/rs.3.rs-10196893/v1}
}
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
