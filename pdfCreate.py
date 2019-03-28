import os, sys
from fpdf import FPDF

labels = ['Name:', 'ID:', 'Date:', 'Location:', 'Size:', 'Owner:']

with open('Dados.txt', 'r') as f:
    d = f.read().split('\n')
    del d[-1]    

class PDF(FPDF):
    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 12)
        # Title
        self.cell(0, 10, '(Insira Informações aqui)', align='C')
        # Line break
        self.ln(20)


# Instantiation of inherited class
pdf = PDF('L')
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)
pdf.cell(140, 0,'(Insira Informações aqui)', align='C')
pdf.image('arq0.jpg', 20, 35, 120, 120)
pdf.cell(133, 0,'(Insira Informações aqui)',align='C')
pdf.image('arq0.jpg', 297-140, 35, 120, 120)
pdf.ln(135)
pdf.set_draw_color(255,0,0)
pdf.set_line_width(0.6)
pdf.cell(5)
pdf.cell(12, 7, '', 1)
pdf.cell(100, 7, '(Insira Informações aqui)')
pdf.ln(12)
pdf.set_draw_color(0,0,0)
pdf.set_line_width(0.6)
pdf.cell(5)
pdf.cell(12, 7, '', 1)
pdf.cell(100, 7, '(Insira Informações aqui)')
pdf.output('tuto2.pdf', 'F')