import pandas as pd
import os

# プロジェクトルートの取得
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))

def analyze_sales(clean_file_path):
    df = pd.read_csv(clean_file_path)
    
    # 月別売上集計
    monthly_sales = df.groupby('month')['sales'].sum().reset_index()
    
    # カテゴリ別売上
    category_sales = df.groupby('category')['sales'].sum().reset_index()
    
    # 地域別売上
    region_sales = df.groupby('region')['sales'].sum().reset_index()
    
    return monthly_sales, category_sales, region_sales

if __name__ == "__main__":
    # クリーンデータファイルへの相対パスをプロジェクトルートから構築
    clean_file_path = os.path.join(project_root, 'data', 'clean_sales_data.csv')
    monthly, category, region = analyze_sales(clean_file_path)
    
    # 分析結果の保存パスを構築
    monthly_path = os.path.join(project_root, 'data', 'monthly_sales.csv')
    category_path = os.path.join(project_root, 'data', 'category_sales.csv')
    region_path = os.path.join(project_root, 'data', 'region_sales.csv')
    
    monthly.to_csv(monthly_path, index=False)
    category.to_csv(category_path, index=False)
    region.to_csv(region_path, index=False)
    
    print("Sales analysis completed and CSV files saved.")
