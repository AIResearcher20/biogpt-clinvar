import os
import pandas as pd
import gzip
import re

def process_clinvar_data(file_path, max_records=20000):
    """
    پردازش فایل VCF ClinVar و استخراج داده‌های آموزشی
    """
    print(f"📥 Processing ClinVar data from: {file_path}")
    
    data = []
    with gzip.open(file_path, 'rt') as f:
        for line in f:
            if line.startswith('#'):
                continue
            
            parts = line.strip().split('\t')
            if len(parts) < 8:
                continue
            
            chrom = parts[0]
            pos = parts[1]
            ref = parts[3]
            alt = parts[4]
            info = parts[7]
            
            if "CLNSIG=" not in info:
                continue
            
            raw_sig = info.split("CLNSIG=")[1].split(";")[0]
            
            # نرمال‌سازی Significance
            if "Pathogenic" in raw_sig:
                sig = "Pathogenic"
            elif "Benign" in raw_sig:
                sig = "Benign"
            else:
                continue
            
            variant = f"{chrom}:{pos} {ref}>{alt}"
            data.append({
                "input": f"Variant: {variant}",
                "output": f"Significance: {sig}"
            })
            
            if len(data) >= max_records:
                break
    
    df = pd.DataFrame(data)
    df = df.drop_duplicates(subset=["input"])
    
    print(f"✅ Loaded {len(df)} unique variants")
    print(df.head())
    
    return df

if __name__ == "__main__":
    # دانلود فایل اگر وجود نداشت
    if not os.path.exists("clinvar.vcf.gz"):
        print("📥 Downloading ClinVar data...")
        !wget -q https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar.vcf.gz
        print("✅ Download complete!")
    
    df = process_clinvar_data("clinvar.vcf.gz")
    df.to_csv("clinvar_data.csv", index=False)
    print(f"✅ Saved to clinvar_data.csv")
