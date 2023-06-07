from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
import os

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,  
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

cwd = os.getcwd()
report = SimpleDocTemplate(f"{cwd}/resources/report.pdf")
styles = getSampleStyleSheet()

report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
report.build([report_title])