import subprocess
import os
import sys

# プロジェクトルートの取得
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(current_dir)

def run_script(script_path):
    try:
        subprocess.run(["python", script_path], check=True)
        print(f"Executed {script_path} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_path}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # スクリプトの相対パスをプロジェクトルートから構築
    scripts = [
        os.path.join(project_root, 'scripts', 'data_processing.py'),
        os.path.join(project_root, 'scripts', 'data_analysis.py'),
        os.path.join(project_root, 'scripts', 'visualization.py'),
        os.path.join(project_root, 'scripts', 'report_generation.py'),
        # オプションでデータベース連携を実行
        # os.path.join(project_root, 'scripts', 'database_integration.py')
    ]
    
    for script in scripts:
        run_script(script)
    
    print("All scripts executed successfully.")
