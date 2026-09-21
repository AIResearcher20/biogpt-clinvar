**Year:** 2024–2025  
**License:** MIT  
**Author:** Sepideh Moafi
---
BioGPT-ClinVar

Parameter-efficient fine-tuning of BioGPT on ClinVar-derived instruction data.

2024–2025 · Python · PyTorch · Hugging Face Transformers · PEFT/LoRA · BioGPT · ClinVar

Model: Sepideh2027/biogpt-clinvar-finetuned
Preprint: Research Square

---

Problem

General language models are not trained on clinical variant data. Full fine-tuning of a 347M-parameter biomedical model is also expensive on limited hardware.

---

Background

Genomic sequencing produces large numbers of variants. Interpreting them requires combining structured genomic data with clinical and biological knowledge. ClinVar provides curated annotations, but converting its records into inputs suitable for language-model training requires additional data engineering.

Biomedical language models are pretrained on biomedical literature and can be adapted to specialized tasks. Full fine-tuning, however, is memory-intensive. LoRA provides a parameter-efficient alternative.

---

What I built

I fine-tuned BioGPT with LoRA on ClinVar-derived instruction data.

· Built an instruction-style dataset of ~20,000 ClinVar-derived examples with a 16k/2k/2k train/validation/test split.
· Used LoRA (r=16, α=32) with BF16 mixed precision on a single NVIDIA T4.
· Kept the base model frozen. Only the adapter weights were trained.

Training loss went from 1.49 to 1.39. Validation loss went from 1.45 to 1.40.

---

Method

· Base model: microsoft/biogpt (~347M parameters, transformer-based causal LM)
· Adaptation: LoRA (r=16, α=32, dropout=0.05, target modules: q/k/v/o_proj)
· Training: 3 epochs, AdamW, learning rate 5e-5, weight decay 0.01, batch size 4, gradient accumulation 4, max sequence length 128
· Precision: BF16 mixed precision
· Hardware: single NVIDIA Tesla T4
· Framework: PyTorch + Hugging Face Transformers + PEFT

---

Data pipeline

The dataset was built from raw ClinVar records.

1. Download ClinVar records.
2. Extract variant-level fields (chromosome, position, reference allele, alternative allele, clinical significance).
3. Normalize clinical significance labels (pathogenic / benign).
4. Remove duplicates.
5. Format as instruction–response examples.
6. Split deterministically into train / validation / test.

Example transformation:

```
Raw ClinVar record:
  Chromosome: 17
  Position: 43071077
  Reference: C
  Alternative: T
  Clinical Significance: Pathogenic

Instruction-style example:
  Instruction: Interpret the clinical significance of this genomic variant.
  Input: Variant: 17:43071077 C>T
  Output: Clinical Significance: Pathogenic
```

Only pathogenic and benign variants were kept. Variants with uncertain or conflicting annotations were excluded. This simplifies the task — it does not represent the full complexity of clinical variant classification.

Dataset summary:

Stage Records
Raw ClinVar variants 20,000
After duplicate removal ~19,600
Training set 16,000
Validation set 2,000
Test set 2,000

---

Evaluation

Training and validation loss were monitored during fine-tuning.

Metric Initial Final
Training loss 1.49 1.39
Validation loss 1.45 1.40

The losses stayed close, which suggests stable optimization. Loss values alone do not establish generalization. Accuracy, precision, recall, and F1 require additional evaluation and are not reported here.

---

Usage

```python
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

base_model = AutoModelForCausalLM.from_pretrained("microsoft/biogpt")
tokenizer = AutoTokenizer.from_pretrained("microsoft/biogpt")

model = PeftModel.from_pretrained(
    base_model,
    "Sepideh2027/biogpt-clinvar-finetuned"
)

inputs = tokenizer("Interpret: BRCA1 c.68_69delAG", return_tensors="pt")
outputs = model.generate(**inputs, max_length=128)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

Reproducibility

```bash
git clone https://github.com/AIResearcher20/biogpt-clinvar.git
cd biogpt-clinvar
pip install -r requirements.txt

python data/download_clinvar.py
python data/preprocess.py
python finetune/train.py
```

Repository layout:

```
biogpt-clinvar/
├── data/
│   ├── download_clinvar.py
│   └── preprocess.py
├── finetune/
│   └── train.py
├── evaluation/
├── models/
├── config.py
├── inference.py
├── requirements.txt
├── LICENSE
└── CITATION.cff
```

---

Released artifacts

· Fine-tuned model: Sepideh2027/biogpt-clinvar-finetuned
· Instruction dataset: Sepideh2027/Agent
· LoRA adapter (standalone): Sepideh2027/PathogenAgentAI-BioGPT-LoRA

---

Limitations

· The task is limited to simplified pathogenic/benign categories.
· Variants with uncertain or conflicting annotations were excluded.
· Accuracy, precision, recall, and F1 were not evaluated in this release.
· The model has not been benchmarked against clinical variant interpretation systems.
· Loss values do not establish clinical performance.

---

Citation

```bibtex
@article{Moafi2025biogptclinvar,
  title={BioGPT-ClinVar: Parameter-Efficient Fine-Tuning of a Biomedical Foundation Model},
  author={Moafi, Sepideh},
  journal={Research Square},
  year={2025},
  doi={10.21203/rs.3.rs-10196893/v1}
}
```

---

License

MIT
