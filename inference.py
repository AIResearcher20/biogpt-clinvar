import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class GenomicVariantInterpreter:
    def __init__(self, model_path="./biogpt_final_model"):
        self.tokenizer = AutoTokenizer.from_pretrained("microsoft/biogpt")
        self.tokenizer.pad_token = self.tokenizer.eos_token
        
        self.model = AutoModelForCausalLM.from_pretrained(model_path)
        self.model.eval()
        
        if torch.cuda.is_available():
            self.model = self.model.to("cuda")
    
    def interpret(self, variant, max_new_tokens=60):
        prompt = f"Interpret the clinical significance of this variant: {variant}"
        inputs = self.tokenizer(prompt, return_tensors="pt")
        
        if torch.cuda.is_available():
            inputs = {k: v.to("cuda") for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=0.1,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
        
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    interpreter = GenomicVariantInterpreter()
    
    variants = [
        "BRCA1 c.68_69delAG",
        "CFTR F508del",
        "TP53 R175H"
    ]
    
    for v in variants:
        result = interpreter.interpret(v)
        print(f"🔬 {v}")
        print(f"💬 {result}\n")
