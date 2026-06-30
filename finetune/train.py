import torch
import pandas as pd
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from peft import LoraConfig, get_peft_model, TaskType
from datasets import Dataset
from config import config

def tokenize_fn(tokenizer, examples):
    return tokenizer(
        examples["text"],
        truncation=True,
        padding="max_length",
        max_length=config.MAX_LENGTH
    )

def prepare_dataset(df, tokenizer):
    texts = [f"{row['input']} {row['output']}" for _, row in df.iterrows()]
    dataset = Dataset.from_dict({"text": texts})
    dataset = dataset.map(
        lambda x: tokenize_fn(tokenizer, x),
        batched=True
    )
    return dataset

def main():
    print("🧬 BioGPT Fine-tuning Pipeline")
    
    # 1. بارگذاری داده
    train_df = pd.read_csv("train_data.csv")
    val_df = pd.read_csv("val_data.csv")
    test_df = pd.read_csv("test_data.csv")
    
    print(f"📊 Train: {len(train_df)}, Val: {len(val_df)}, Test: {len(test_df)}")
    
    # 2. بارگذاری مدل
    print("🔄 Loading BioGPT...")
    tokenizer = AutoTokenizer.from_pretrained(config.MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token
    
    model = AutoModelForCausalLM.from_pretrained(
        config.MODEL_NAME,
        torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
        device_map="auto" if torch.cuda.is_available() else None
    )
    
    # 3. LoRA
    print("🔧 Applying LoRA...")
    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=config.LORA_R,
        lora_alpha=config.LORA_ALPHA,
        lora_dropout=config.LORA_DROPOUT,
        target_modules=config.TARGET_MODULES,
        bias="none"
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    
    # 4. آماده‌سازی داده
    print("📦 Preparing datasets...")
    train_ds = prepare_dataset(train_df, tokenizer)
    val_ds = prepare_dataset(val_df, tokenizer)
    
    # 5. تنظیمات آموزش
    training_args = TrainingArguments(
        output_dir=config.OUTPUT_DIR,
        num_train_epochs=config.EPOCHS,
        per_device_train_batch_size=config.BATCH_SIZE,
        per_device_eval_batch_size=config.BATCH_SIZE,
        gradient_accumulation_steps=config.GRADIENT_ACCUMULATION,
        learning_rate=config.LEARNING_RATE,
        weight_decay=config.WEIGHT_DECAY,
        logging_steps=config.LOGGING_STEPS,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        fp16=False,
        bf16=torch.cuda.is_bf16_supported() if torch.cuda.is_available() else False,
        report_to="none",
        save_total_limit=3,
    )
    
    # 6. Data Collator
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )
    
    # 7. Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        data_collator=data_collator,
    )
    
    # 8. آموزش
    print("🚀 Starting training...")
    trainer.train()
    
    # 9. ارزیابی نهایی
    print("\n📊 Final evaluation on Test set...")
    test_ds = prepare_dataset(test_df, tokenizer)
    test_results = trainer.evaluate(test_ds)
    print(f"✅ Test Results: {test_results}")
    
    # 10. ذخیره مدل
    print("\n💾 Saving final model...")
    final_path = "./biogpt_final_model"
    model.save_pretrained(final_path)
    tokenizer.save_pretrained(final_path)
    print(f"✅ Model saved to {final_path}")

if __name__ == "__main__":
    config.validate()
    main()
