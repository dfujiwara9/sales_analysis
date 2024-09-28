from fpdf import FPDF
from fpdf.enums import XPos, YPos
import os
import logging

# プロジェクトルートの取得
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))

# ログディレクトリの作成
log_dir = os.path.join(project_root, 'logs')
os.makedirs(log_dir, exist_ok=True)

# ログの設定
logging.basicConfig(
    filename=os.path.join(log_dir, 'report_generation.log'),
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

class PDFReport(FPDF):
    def header(self):
        try:
            self.set_font('NotoSansJP', '', 16)
            self.cell(
                w=0,
                h=10,
                text='月次売上レポート',
                border=0,
                align='C',
                new_x=XPos.LMARGIN,
                new_y=YPos.NEXT
            )
        except Exception as e:
            logging.error(f"Error in header: {e}")
            raise

    def chapter_title(self, title):
        try:
            self.set_font('NotoSansJP', '', 12)
            self.cell(
                w=0,
                h=10,
                text=title,
                border=0,
                align='L',
                new_x=XPos.LMARGIN,
                new_y=YPos.NEXT
            )
            self.ln(5)
        except Exception as e:
            logging.error(f"Error in chapter_title: {e}")
            raise

    def chapter_image(self, image_path):
        try:
            self.image(image_path, w=180)
            self.ln(10)
        except Exception as e:
            logging.error(f"Error in chapter_image: {e}")
            raise

def create_pdf_report():
    try:
        pdf = PDFReport()
        
        # フォントの追加（add_font() を add_page() の前に行う）
        font_path = os.path.join(project_root, 'fonts', 'NotoSansJP-Regular.ttf')
        pdf.add_font('NotoSansJP', '', font_path)
        logging.info("Font 'NotoSansJP' added successfully.")
        pdf.set_font('NotoSansJP', '', 12)
        
        # チャプターの定義（タイトルと画像のパス）
        chapters = [
            ('1. 月別売上トレンド', os.path.join(project_root, 'images', 'monthly_sales_trend.png')),
            ('2. カテゴリ別売上', os.path.join(project_root, 'images', 'category_sales.png')),
            ('3. 地域別売上', os.path.join(project_root, 'images', 'region_sales.png')),
        ]
        
        for title, image_path in chapters:
            pdf.add_page()
            pdf.chapter_title(title)
            pdf.chapter_image(image_path)
            logging.info(f"Added chapter: {title}")
        
        # PDFレポートの保存パスを構築
        report_path = os.path.join(project_root, 'reports', 'monthly_sales_report.pdf')
        pdf.output(report_path)
        logging.info(f"PDF report generated at {report_path}")
        print(f"PDF report generated at {report_path}")
    except Exception as e:
        logging.error(f"Failed to create PDF report: {e}")
        print(f"Failed to create PDF report: {e}")

if __name__ == "__main__":
    create_pdf_report()
