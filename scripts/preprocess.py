import os
import pandas as pd

def main():
    # Buat folder output jika belum ada
    os.makedirs('../data/processed', exist_ok=True)
    
    try:
        # Baca data mentah
        raw_path = '../data/raw/gb1.csv'
        df = pd.read_csv(raw_path)
        
        # Proses data
        df = df[['sequence', 'fitness']].dropna()
        df['sequence'] = df['sequence'].str.upper()
        
        # Simpan hasil
        output_path = '../data/processed/gb1_processed.csv'
        df.to_csv(output_path, index=False)
        
        # Beri laporan
        print(f"✅ Data berhasil diproses!")
        print(f"File input: {raw_path}")
        print(f"File output: {output_path}")
        print(f"Jumlah data: {len(df)} baris")
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()