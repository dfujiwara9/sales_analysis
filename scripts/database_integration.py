from sqlalchemy import create_engine
import pandas as pd
import os

# プロジェクトルートの取得
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))

def save_to_database(csv_file_path, db_path):
    engine = create_engine(db_path)
    df = pd.read_csv(csv_file_path)
    df.to_sql('sales', engine, if_exists='replace', index=False)
    print(f"データベースに保存しました: {db_path}")

def load_from_database(db_path):
    engine = create_engine(db_path)
    query = "SELECT * FROM sales"
    df = pd.read_sql(query, engine)
    print(df.head())
    return df

if __name__ == "__main__":
    # データファイルとデータベースファイルへの相対パスをプロジェクトルートから構築
    csv_file_path = os.path.join(project_root, 'data', 'clean_sales_data.csv')
    db_path = f"sqlite:///{os.path.join(project_root, 'data', 'sales_data.db')}"
    
    save_to_database(csv_file_path, db_path)
    load_from_database(db_path)
