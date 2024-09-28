import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.font_manager import FontProperties

# プロジェクトルートの取得
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))

# 日本語フォントの設定
font_path = os.path.join(project_root, 'fonts', 'NotoSansJP-Regular.ttf')
font_prop = FontProperties(fname=font_path)

def set_font():
    plt.rcParams['font.family'] = font_prop.get_name()
    plt.rcParams['axes.unicode_minus'] = False  # マイナス記号の表示

def plot_monthly_sales(file_path, output_path):
    monthly_sales = pd.read_csv(file_path)

    plt.figure(figsize=(10,6))
    sns.lineplot(data=monthly_sales, x='month', y='sales', marker='o')
    plt.title('月別売上トレンド', fontproperties=font_prop)
    plt.xlabel('月', fontproperties=font_prop)
    plt.ylabel('売上', fontproperties=font_prop)
    plt.xticks(rotation=45, fontproperties=font_prop)
    plt.yticks(fontproperties=font_prop)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Monthly sales trend plot saved to {output_path}")

def plot_category_sales(file_path, output_path):
    category_sales = pd.read_csv(file_path)

    plt.figure(figsize=(8,6))
    sns.barplot(data=category_sales, x='category', y='sales')
    plt.title('カテゴリ別売上', fontproperties=font_prop)
    plt.xlabel('カテゴリ', fontproperties=font_prop)
    plt.ylabel('売上', fontproperties=font_prop)
    plt.xticks(rotation=45, fontproperties=font_prop)
    plt.yticks(fontproperties=font_prop)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Category sales plot saved to {output_path}")

def plot_region_sales(file_path, output_path):
    region_sales = pd.read_csv(file_path)

    plt.figure(figsize=(8,6))
    sns.barplot(data=region_sales, x='region', y='sales')
    plt.title('地域別売上', fontproperties=font_prop)
    plt.xlabel('地域', fontproperties=font_prop)
    plt.ylabel('売上', fontproperties=font_prop)
    plt.xticks(rotation=45, fontproperties=font_prop)
    plt.yticks(fontproperties=font_prop)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    print(f"Region sales plot saved to {output_path}")

if __name__ == "__main__":
    # グローバルフォント設定
    set_font()

    # 分析結果ファイルへの相対パスをプロジェクトルートから構築
    monthly_sales_path = os.path.join(project_root, 'data', 'monthly_sales.csv')
    category_sales_path = os.path.join(project_root, 'data', 'category_sales.csv')
    region_sales_path = os.path.join(project_root, 'data', 'region_sales.csv')

    # グラフ画像の保存パスを構築
    monthly_plot_path = os.path.join(project_root, 'images', 'monthly_sales_trend.png')
    category_plot_path = os.path.join(project_root, 'images', 'category_sales.png')
    region_plot_path = os.path.join(project_root, 'images', 'region_sales.png')

    # 各プロットを作成
    plot_monthly_sales(monthly_sales_path, monthly_plot_path)
    plot_category_sales(category_sales_path, category_plot_path)
    plot_region_sales(region_sales_path, region_plot_path)
