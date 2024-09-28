# 売上データ分析ツール

## 概要
このプロジェクトは、CSV形式の売上データを自動的に収集、整理、分析し、月次レポートを生成するツールです。Visual Studio Codeを開発環境として使用しています。

## 機能
- データの読み込みとクリーニング
- 売上データの分析（月別、カテゴリ別、地域別）
- データの可視化（グラフの生成）
- PDF形式のレポート自動生成
- オプションでデータベースとの連携

## 使用技術
- Python
- pandas, matplotlib, seaborn, sqlalchemy, fpdf
- Visual Studio Code

## セットアップ
1. リポジトリをクローン
   git clone https://github.com/yourusername/sales_analysis.git
   cd sales_analysis

2. 仮想環境の作成と有効化
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows

3. 必要なパッケージのインストール
   pip install -r requirements.txt

4. データの配置
   data/sales_data.csv に売上データを配置します。

## 実行方法
以下のコマンドで一連の分析プロセスを実行します。

   python run_analysis.py

## 結果
reports/monthly_sales_report.pdf に生成されたレポートが保存されます。
images/ フォルダに各種グラフが保存されます。