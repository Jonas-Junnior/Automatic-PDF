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
    
    titulo_imgs_antes = 'PLANET - ' + d[9] + ' - ' + d[8]
    titulo_imgs_depois = 'PLANET - ' + d[11] + ' - ' + d[10]
        
    territorio_desmatado = "Área desmatada: " + d[7] + 'Km² '
    
    if (d[13] == "N/P" or d[13] == "none"):
        sigef = "SIGEF: " + "N/P*"
    else:
        sigef = "SIGEF: " + d[13] + ' - ' + "Área desmatada do Sigef: " + d[4]+ ' - ' + "Porcentagem: " + d[5]
    
    if (d[14] == "N/P" or d[14] == "none"):
        regul_sigef = "REGULARIZAÇÃO SIGEF: " + "N/P*"
    else:
        regul_sigef = "REGULARIZAÇÃO SIGEF: " + d[14] + ' - ' + "Área desmatada do Sigef: " + d[6]+ ' - ' + "Porcentagem: " + d[7]
    
    if (d[1] == "N/P" or d[1] == "none"):
        car = "CAR: " + "N/P*"
    else:
        car = "CAR: " + d[0] + ' - ' + "Área desmatada do CAR: " + d[1]+ ' - ' + "Porcentagem: " + d[2]   
    snci = "SNCI: N/P*"
    
    
    
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
    pdf.set_font('Times', 'b', 12)
    pdf.cell(140, 0,titulo_imgs_antes, align='C')
    pdf.image(path_antes, 20, 30, 120, 100)
    pdf.cell(133, 0,titulo_imgs_depois,align='C')
    pdf.image(path_depois, 297-140, 30, 120, 100)
    
    #Line Breaker
    pdf.ln(115)
    
    #Território Desmatado
    pdf.set_draw_color(255,0,0)
    pdf.set_line_width(0.6)
    pdf.cell(5)
    pdf.cell(12, 0, '', 1)
    pdf.set_font('Times', '', 8)
    pdf.cell(1)
    pdf.multi_cell(80, 0, territorio_desmatado, 'R')

    
    #Sigef
    if (sigef == "SIGEF: N/P*"):
        pdf.cell(117)
        pdf.set_draw_color(0, 255, 0)
        pdf.set_line_width(0.6)
        pdf.cell(5)
    
        pdf.cell(12, 0, '', 1)
        pdf.cell(1)
        pdf.set_font('Times', '', 8)
        pdf.multi_cell(80, 0, sigef)
    else:
        pdf.cell(107)
        pdf.set_draw_color(0, 255, 0)
        pdf.set_line_width(0.6)
        pdf.cell(5)
        pdf.cell(12, 5, '', 'T')
        pdf.cell(1)
        pdf.set_font('Times', '', 8)
        pdf.multi_cell(70, 3, sigef)
    
    #Regularização SIGEF
    if (regul_sigef == "REGULARIZAÇÃO SIGEF: N/P*"):
        pdf.cell(210)
        pdf.set_draw_color(96, 255, 0)
        pdf.set_line_width(0.6)
        pdf.cell(5)
    
        pdf.cell(12, 0, '', 1)
        pdf.cell(1)
        pdf.set_font('Times', '', 8)
        pdf.multi_cell(80, 0, regul_sigef)
    else:
        pdf.cell(200)
        pdf.set_draw_color(96, 255, 0)
        pdf.set_line_width(0.6)
        pdf.cell(5)
        pdf.cell(12, 5, '', 'T')
        pdf.cell(1)
        pdf.set_font('Times', '', 8)
        pdf.multi_cell(80, 3, regul_sigef)
        
    #Line Breaker
    pdf.ln(7)
    
    #CAR
    pdf.set_draw_color(255, 0, 255)
    pdf.set_line_width(0.6)
    pdf.cell(5)
    if (car == "CAR: N/P*"):
        pdf.cell(12, 0, '', 1)
        pdf.cell(1)
        pdf.set_font('Times', '', 8)
        pdf.multi_cell(80, 0, car)
    else:
        pdf.cell(12, 5, '', 'B')
        pdf.cell(1)
        pdf.set_font('Times', '', 8)
        pdf.multi_cell(80, 3, car)
    
    #SNCI
    pdf.cell(210)
    pdf.set_draw_color(255, 255, 0)
    pdf.set_line_width(0.6)
    pdf.cell(5)
    if (snci == "SNCI: N/P*"):
        pdf.cell(12, 0, '', 1)
        pdf.cell(1)
        pdf.set_font('Times', '', 8)
        pdf.multi_cell(80, 0, snci)
    else:
        pdf.cell(12, 5, '', 'B')
        pdf.cell(1)
        pdf.set_font('Times', '', 8)
        pdf.multi_cell(80, 5, snci)
        
    #Line Breaker
    pdf.ln(5)
    pdf.cell(115)
    pdf.set_font('Times', '', 8)
    pdf.multi_cell(43.49, 3, 'Sistema de coordenadas geodésico Datum Horizontal: WGS-84 Cálculo da Área: Projeção Sinusoidal', align='C')
    
    
    #Default Author
    pdf.set_font('Times', 'B', 10)
    pdf.cell(123)
    pdf.cell(30, 10, 'Elaborado por:', align='C')
    
    #Line Breaker
    pdf.ln(25)
    
    
    pdf.image('mpf.png',x=133, y=182 ,w=27, h=10)
    
    pdf.output(path_relatorio)