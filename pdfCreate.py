import os, sys
from fpdf import FPDF

folders = [folder for folder in os.listdir('.') if os.path.isdir(os.path.join('.',folder))]

for i in range(len(folders)):
    path_dados = './' + folders[i] + '/Dados.txt'
    path_relatorio = './' + folders[i] + '/relatorio.pdf'
    path_antes = './' + folders[i] + '/Antes.png'
    path_depois = './' + folders[i] + '/Depois.png'
    path_mini = './' + folders[i] + '/Mini.png'

    with open(path_dados, 'r') as f:
        d = f.read().split('\n')
        del d[-1]    
        
    titulo = 'PRODES' + '-' + d[5]
    local = d[5]
    car = "CAR: " + d[7]
    sigef = "SIGEF: " + d[6] + ' - ' + "Área desmatada do Sigef: " + d[0]+ ' - ' + "Porcentagem: " + d[1]
    snci = "SNCI: " + d[8]
    regul_sigef = "REGULARIZAÇÃO SIGEF: " + d[9]
    titulo_imgs_antes = 'PLANET - ' + d[3]
    titulo_imgs_depois = 'PLANET - ' + d[4]
    titulo_imgs_mini = d[0] + '-' + d[6]
    territorio_desmatado = "Área desmatada: " + d[2] + 'Km² '
    
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
    pdf.ln(100)
    pdf.set_font('Times', '', 10)
    pdf.cell(215, 75,'(Insira Informações aqui)', align='R')
    pdf.cell(12)
    pdf.set_font('Times', '', 10)
    pdf.cell(40, 15,local, align='C')
    
    #Line Breaker
    pdf.ln(12)
    
    #Território Desmatado
    pdf.set_draw_color(255,0,0)
    pdf.set_line_width(0.6)
    pdf.cell(5)
    pdf.cell(12, 0, '', 1)
    pdf.set_font('Times', '', 10)
    pdf.cell(1)
    pdf.multi_cell(80, 0, territorio_desmatado)
    pdf.cell(117)
    pdf.set_font('Times', '', 8)
    pdf.multi_cell(43.49, 3, 'Sistema de coordenadas geodésico Datum Horizontal: WGS-84 Cálculo da Área: Projeção Sinusoidal', align='C')
    
    #Line Breaker
    pdf.ln(-3)
    
    #CAR
    pdf.set_draw_color(255, 0, 255)
    pdf.set_line_width(0.6)
    pdf.cell(5)
    pdf.cell(12, 2.5, '', 'B')
    pdf.cell(1)
    pdf.set_font('Times', '', 10)
    pdf.multi_cell(80, 5, car)
    
    #Line Breaker
    pdf.ln(3)
    
    #Sigef
    pdf.set_draw_color(0, 255, 0)
    pdf.set_line_width(0.6)
    pdf.cell(5)
    pdf.cell(12, 5, '', 'B')
    pdf.cell(1)
    pdf.set_font('Times', '', 10)
    pdf.multi_cell(80, 5, sigef)
    
    #Line Breaker
    pdf.ln(3)
    
    #SNCI
    pdf.set_draw_color(255, 255, 0)
    pdf.set_line_width(0.6)
    pdf.cell(5)
    pdf.cell(12, 2.5, '', 'B')
    pdf.cell(1)
    pdf.set_font('Times', '', 10)
    pdf.multi_cell(80, 5, snci)
    #Line Breaker
    pdf.ln(3)
    
    #Regularização SIGEF
    pdf.set_draw_color(96, 255, 0)
    pdf.set_line_width(0.6)
    pdf.cell(5)
    pdf.cell(12, 2.5, '', 'B')
    pdf.cell(1)
    pdf.set_font('Times', '', 10)
    pdf.multi_cell(80, 5, regul_sigef)
    
    #Default Author
    pdf.set_font('Times', 'B', 10)
    pdf.cell(123)
    pdf.cell(30, -45, 'Elaborado por:', align='C')
    
    #Line Breaker
    pdf.ln(25)
    
    
    pdf.image('logo-imazon_transp.png',x=130, y=160 ,w=33, h=12)
    
    #Mini Image
    pdf.image(path_mini, 297-60,y= 135, w=40, h=40)
    pdf.output(path_relatorio )