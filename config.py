import os

class Config:
    # ===== NCBI =====
    NCBI_EMAIL = os.getenv("NCBI_EMAIL", "public@example.com")
    NCBI_TOOL = "BioGPT_Finetuning"
    
    # ===== مدل =====
    MODEL_NAME = "microsoft/biogpt"
    
    # ===== LoRA =====
    LORA_R = 16
    LORA_ALPHA = 32
    LORA_DROPOUT = 0.05
    TARGET_MODULES = ["q_proj", "v_proj", "k_proj", "out_proj"]
    
    # ===== Hyperparameters =====
    BATCH_SIZE = 4
    GRADIENT_ACCUMULATION = 4
    EPOCHS = 3
    LEARNING_RATE = 5e-5
    WEIGHT_DECAY = 0.01
    MAX_LENGTH = 128
    LOGGING_STEPS = 20
    
    # ===== مسیرها =====
    DATA_DIR = "./data"
    OUTPUT_DIR = "./biogpt_clinvar_results"
    
    # ===== تعداد داده =====
    MAX_RECORDS = 20000
    
    @classmethod
    def validate(cls):
        print(f"✅ NCBI Email: {cls.NCBI_EMAIL}")
        print(f"✅ Model: {cls.MODEL_NAME}")
        print(f"✅ Output: {cls.OUTPUT_DIR}")
        return True

config = Config()
