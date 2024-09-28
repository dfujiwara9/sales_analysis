import pandas as pd
import os

# プロジェクトルートの取得
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))

def load_and_clean_data(file_path):
    # CSVファイルの読み込み
    df = pd.read_csv(file_path)
    
    # データの基本情報確認
    print(df.head())
    print(df.info())
    
    # データのクリーニング（例: 欠損値の処理）
    df = df.dropna()
    
    # 日付データの形式変換
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')
    
    return df

if __name__ == "__main__":
    # データファイルへの相対パスをプロジェクトルートから構築
    file_path = os.path.join(project_root, 'data', 'sales_data.csv')
    df = load_and_clean_data(file_path)
    
    # クリーンデータの保存パスを構築
    output_path = os.path.join(project_root, 'data', 'clean_sales_data.csv')
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
