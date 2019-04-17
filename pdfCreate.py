import os, sys
from fpdf import FPDF

folders = [folder for folder in os.listdir('.') if os.path.isdir(os.path.join('.',folder))]

for i in range(len(folders)):
    path_dados = './' + folders[i] + '/Dados.txt'
    path_relatorio = './' + folders[i] + '/relatorio.pdf'
    path_antes = './' + folders[i] + '/Antes.png'
    path_depois = './' + folders[i] + '/Depois.png'

    with open(path_dados, 'r') as f:
        d = f.read().split('\n')
        del d[-1]    
        
    titulo = 'PRODES' + '-' + d[12]
    
    titulo_imgs_antes = 'SENTINEL - ' + d[9] + ' - ' + d[8]
    titulo_imgs_depois = 'SENTINEL - ' + d[11] + ' - ' + d[10]
        
    territorio_desmatado = d[7] + 'Km² '
    
    if (d[13] == "N/P" or d[13] == "none"):
        sigef = "N/P*"
    else:
        sigef = "N°: " + d[13] + '\n' + "Área desmatada do Sigef: " + d[4]+ 'Km² \n' + "Porcentagem: " + d[5]
    
    if (d[14] == "N/P" or d[14] == "none"):
        regul_sigef = "N/P*"
    else:
        regul_sigef = "N°: " + d[14] + '\n' + "Área desmatada do Sigef: " + d[6]+ 'Km² \n' + "Porcentagem: " + d[7]
    
    if (d[1] == "N/P" or d[1] == "none"):
        car = "N/P*"
    else:
        car = "N°: " + d[0] + '\n' + "Área desmatada do CAR: " + d[1]+ 'Km² \n' + "Porcentagem: " + d[2]   
        
    snci = "N/P*"
    
    
    
    class PDF(FPDF):
        def header(self):
            # Arial bold 15
            self.set_font('Arial', 'B', 12)
            # Title
            self.cell(0, 10, titulo, align='C')
            # Line break
            self.ln(15)
    
    
    # Instantiation of inherited class
    pdf = PDF('L')
    pdf.set_auto_page_break(True, margin=0.0)
    pdf.alias_nb_pages()
    pdf.add_page()
    #Setting Images
    pdf.set_font('Times', 'b', 10)
    pdf.cell(140, 0,titulo_imgs_antes, align='C')
    pdf.image(path_antes, 20, 30, 120, 100)
    pdf.cell(133, 0,titulo_imgs_depois,align='C')
    pdf.image(path_depois, 297-140, 30, 120, 100)
    
    #Line Breaker
    pdf.ln(115)
    
    #Território Desmatado
    pdf.set_draw_color(255,0,0)
    pdf.set_line_width(0.6)
    pdf.cell(50)
    pdf.cell(12, 0, '', 1)
    pdf.set_font('Times', '', 10)
    pdf.cell(1)
    pdf.multi_cell(80, 0, "ÁREA DESMATADA", 'R')

    
    #Sigef
    pdf.cell(117)
    pdf.set_draw_color(0, 255, 0)
    pdf.set_line_width(0.6)
    pdf.cell(5)

    pdf.cell(12, 0, '', 1)
    pdf.cell(1)
    pdf.set_font('Times', '', 10)
    pdf.multi_cell(80, 0, "SIGEF")
    
    #Regularização SIGEF
    pdf.cell(170)
    pdf.set_draw_color(96, 255, 0)
    pdf.set_line_width(0.6)
    pdf.cell(5)

    pdf.cell(12, 0, '', 1)
    pdf.cell(1)
    pdf.set_font('Times', '', 10)
    pdf.multi_cell(80, 0, "REGULARIZAÇÃO SIGEF")
        
    #Line Breaker
    pdf.ln(13)
    
    #CAR
    pdf.set_draw_color(255, 0, 255)
    pdf.set_line_width(0.6)
    pdf.cell(50)
    pdf.cell(12, 0, '', 1)
    pdf.cell(1)
    pdf.set_font('Times', '', 10)
    pdf.multi_cell(80, 0, "CAR")
    
    #SNCI
    pdf.cell(170)
    pdf.set_draw_color(255, 255, 0)
    pdf.set_line_width(0.6)
    pdf.cell(5)
    pdf.cell(12, 0, '', 1)
    pdf.cell(1)
    pdf.set_font('Times', '', 10)
    pdf.multi_cell(80, 0, "SNCI")
    
    
    pdf.image('mpf.png',x=120, y=170 ,w=50, h=30)
    
    pdf.add_page(orientation='L')
    
    pdf.cell(12)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_fill_color(255,0,0)
    pdf.set_font('Times', 'b', 14)
    pdf.cell(250, 10, "Área desmatada", 1, align='C', fill=True)
    pdf.set_font('Times', '', 12)
    pdf.ln(10)
    pdf.cell(12)
    pdf.multi_cell(250, 8, territorio_desmatado, 1, align='C')
    
    pdf.ln(5)
    
    pdf.cell(12)
    pdf.set_fill_color(0, 255, 0)
    pdf.set_font('Times', 'b', 14)
    pdf.cell(250, 10, "SIGEF", 1, align='C', fill=True)
    pdf.set_font('Times', '', 12)
    pdf.ln(10)
    pdf.cell(12)
    pdf.multi_cell(250, 8, sigef, 1, align='C')
    
    pdf.ln(5)
    
    pdf.cell(12)
    pdf.set_font('Times', 'b', 14)
    pdf.set_fill_color(96, 255, 0)
    pdf.cell(250, 10, "REGULARIZAÇÃO SIGEF", 1, align='C', fill=True)
    pdf.set_font('Times', '', 12)
    pdf.ln(10)
    pdf.cell(12)
    pdf.multi_cell(250, 8, regul_sigef, 1, align='C')
    
    pdf.ln(5)
    
    pdf.cell(12)
    pdf.set_font('Times', 'b', 14)
    pdf.set_fill_color(255, 0, 255)
    pdf.cell(250, 10, "CAR", 1, align='C', fill=True)
    pdf.set_font('Times', '', 12)
    pdf.ln(10)
    pdf.cell(12)
    pdf.multi_cell(250, 8, car, 1, align='C')
    
    pdf.ln(5)
    
    pdf.cell(12)
    pdf.set_font('Times', 'b', 14)
    pdf.set_fill_color(255, 255, 0)
    pdf.cell(250, 10, "SNCI", 1, align='C', fill=True)
    pdf.set_font('Times', '', 12)
    pdf.ln(10)
    pdf.cell(12)
    pdf.multi_cell(250, 8, snci, 1, align='C')
    
    pdf.output(path_relatorio)