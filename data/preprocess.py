import pandas as pd
from sklearn.model_selection import train_test_split

def prepare_data(csv_path="clinvar_data.csv"):
    """
    تقسیم داده به Train, Validation, Test
    """
    df = pd.read_csv(csv_path)
    print(f"📊 Total samples: {len(df)}")
    
    # حذف موارد خالی
    df = df.dropna()
    df = df[df["input"].str.strip() != ""]
    df = df[df["output"].str.strip() != ""]
    
    # تقسیم
    train_df, temp_df = train_test_split(df, test_size=0.2, random_state=42)
    val_df, test_df = train_test_split(temp_df, test_size=0.5, random_state=42)
    
    # ذخیره
    train_df.to_csv("train_data.csv", index=False)
    val_df.to_csv("val_data.csv", index=False)
    test_df.to_csv("test_data.csv", index=False)
    
    print(f"✅ Train: {len(train_df)}")
    print(f"✅ Validation: {len(val_df)}")
    print(f"✅ Test: {len(test_df)}")
    
    return train_df, val_df, test_df

if __name__ == "__main__":
    prepare_data()
