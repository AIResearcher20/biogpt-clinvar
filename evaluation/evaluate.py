import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM
from tqdm import tqdm

def load_model(model_path):
    tokenizer = AutoTokenizer.from_pretrained("microsoft/biogpt")
    tokenizer.pad_token = tokenizer.eos_token
    
    model = AutoModelForCausalLM.from_pretrained(model_path)
    model.eval()
    
    if torch.cuda.is_available():
        model = model.to("cuda")
    
    return tokenizer, model

def predict_variant(tokenizer, model, variant):
    prompt = f"Interpret the clinical significance of this variant: {variant}"
    inputs = tokenizer(prompt, return_tensors="pt")
    
    if torch.cuda.is_available():
        inputs = {k: v.to("cuda") for k, v in inputs.items()}
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=20,
            temperature=0.1,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    if "Pathogenic" in response:
        return "Pathogenic"
    elif "Benign" in response:
        return "Benign"
    else:
        return "Unknown"

def evaluate(model_path, test_file):
    tokenizer, model = load_model(model_path)
    test_df = pd.read_csv(test_file)
    
    print(f"📊 Evaluating on {len(test_df)} samples...")
    
    correct = 0
    total = 0
    results = []
    
    for _, row in tqdm(test_df.iterrows(), total=len(test_df)):
        variant = row['input'].replace("Variant: ", "")
        true_label = row['output'].replace("Significance: ", "")
        
        pred = predict_variant(tokenizer, model, variant)
        
        total += 1
        if pred == true_label:
            correct += 1
        
        results.append({
            "variant": variant,
            "true": true_label,
            "predicted": pred
        })
    
    accuracy = correct / total * 100 if total > 0 else 0
    
    print(f"\n✅ Accuracy: {accuracy:.2f}% ({correct}/{total})")
    return pd.DataFrame(results)

if __name__ == "__main__":
    results = evaluate("./biogpt_final_model", "test_data.csv")
    results.to_csv("evaluation_results.csv", index=False)
    print("✅ Results saved to evaluation_results.csv")
