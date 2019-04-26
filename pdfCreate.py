import os
from fpdf import FPDF
import pygame

folders = [folder for folder in os.listdir('.') if os.path.isdir(os.path.join('.',folder))]

for i in range(len(folders)):
    path_dados = './' + folders[i] + '/Dados.txt'
    path_relatorio = './' + folders[i] + '/relatorio.pdf'
    path_antes = './' + folders[i] + '/Antes.png'
    path_depois = './' + folders[i] + '/Depois.png'

    img1 = pygame.image.load(path_antes)
    img2 = pygame.image.load(path_depois)
    
    width1 = img1.get_width() / 4.5
    width2 = img2.get_width() / 4.5
    height1 = img1.get_height() / 4.5
    height2 = img2.get_height() / 4.5


    with open(path_dados, 'r') as f:
        d = f.read().split('\n')
        del d[-1]    
        
    titulo = 'PRODES' + '-' + d[18]
    
    data_antes = d[14]
    titulo_imgs_antes = 'SENTINEL - ' + d[15] 
    data_depois = d[16]
    titulo_imgs_depois = 'SENTINEL - ' + d[17]
        
    territorio_desmatado = d[13] + ' ha'
    
    
    #Dados
    if (d[0] == "N/P"):
        car = "N/P*"
    else:
        if(d[0] == "N/P"):
            car = "N°: Não presente" + '\n' + "Área desmatada do CAR: " + d[1] + 'ha' + '\n' + "Porcentagem: " + d[2] + '%'
        else:
            car = "N°: " + d[0] + '\n' + "Área desmatada do CAR: " + d[1] + 'ha' + '\n' + "Porcentagem: " + d[2] + '%'
        
    if (d[19] == "N/P" and d[3] == "N/P" and d[4] == "N/P"):
        sigef = "N/P*"
    else:
        if(d[19] == "N/P"):
            sigef = "N°: Não presente" + '\n' + "Área desmatada do Sigef: " + d[3]+ 'ha \n' + "Porcentagem: " + d[4] + '%'
        else:
            sigef = "N°: " + d[19] + '\n' + "Área desmatada do Sigef: " + d[3]+ 'ha \n' + "Porcentagem: " + d[4] + '%'
    
    if (d[20] == "N/P" and d[5] == "N/P" and d[6] == "N/P"):
        regul_sigef = "N/P*"
    else:
        if(d[20] == "N/P"):
            regul_sigef = "N°: Não presente" + '\n' + "Área desmatada do Sigef: " + d[5]+ 'ha \n' + "Porcentagem: " + d[6] + '%'
        else:
            regul_sigef = "N°: " + d[20] + '\n' + "Área desmatada do Sigef: " + d[5]+ 'ha \n' + "Porcentagem: " + d[6] + '%'
    
    if(d[21] == "N/P" and d[7] == "N/P" and d[8] == "N/P"):
        snci = "N/P*"
    else:
        if(d[21] == "N/P"):
            snci = "N°: Não presente" + '\n' + "Área desmatada do Snci: " + d[7] + 'ha \n' + "Porcentagem: " + d[8] + '%'
        else:
            snci = "N°: " + d[21] + '\n' + "Área desmatada do Snci: " + d[7] + 'ha \n' + "Porcentagem: " + d[8] + '%'
        
    if(d[22] == "N/P" and d[9] == "N/P" and d[10] == "N/P"):
        UC = "N/P*"
    else:
        if (d[22] == "N/P"):
            UC = "N°: N/P* " + '\n' + "Área desmatada da unidade de conservação: " + d[9] + "ha" + '\n' + "Porcentagem: " + d[10] + '%' 
        else:
            UC = "N°: " + d[22] + '\n' + "Área desmatada da unidade de conservação: " + d[9] + "ha" + '\n' + "Porcentagem: " + d[10] + '%' 
    
    if(d[23] == "N/P" and d[11] == "N/P" and d[12] == "N/P"):
        TL = "N/P*"
    else:
        if (d[23] == "N/P"):
            TL = "N°: N/P* " + '\n' + "Área desmatada em Terras Legais: " + d[11] + "ha" + '\n' + "Porcentagem: " + d[12] + '%' 
        else:
            TL = "N°: " + d[23] + '\n' + "Área desmatada em Terras Legais: " + d[11] + "ha" + '\n' + "Porcentagem: " + d[12] + '%' 
    
    if(d[26] == "N/P" and d[24] == "N/P" and d[25] == "N/P"):
        EM = "N/P*"
    else:
        if (d[26] == "N/P"):
            EM = "N°: Não presente " + '\n' + "Área desmatada em embargo: " + d[24] + "ha" + '\n' + "Porcentagem: " + d[25] + '%' 
        else:
            EM = "N°: " + d[26] + '\n' + "Área desmatada em embargo: " + d[24] + "ha" + '\n' + "Porcentagem: " + d[25] + '%' 
    
    #Células Padrões
    def inicio(x):
        return pdf.cell(x)
    
    class PDF(FPDF):
        def header(self):
            # Arial bold 15
            self.set_font('Arial', 'B', 12)
            # Title
            self.cell(270, 10, titulo, align='C')
            # Line break
            self.ln(15)
            
        def footer(self):
            if (self.page_no() == 1):
                self.image('mpf.png',x=175, y=150 ,w=60, h=35)
            else:
                self.set_font('Times', 'b', 10)
                self.cell(10)
                self.image('mpf.png',x=125, y=170 ,w=50, h=30)
    
    
    # Instantiation of inherited class
    pdf = PDF('L')
    pdf.alias_nb_pages()
    pdf.add_page()
    #Setting Images
    pdf.set_font('Times', 'b', 12)
    pdf.cell(140, 0, data_antes, align='C')
    pdf.cell(133, 3, data_depois, align='C')
    pdf.ln(5)
    pdf.set_font('Times', '', 8)
    pdf.cell(140, 0,titulo_imgs_antes, align='C')
    pdf.image(path_antes, 20, 35, width1, height1)
    pdf.cell(133, 0,titulo_imgs_depois,align='C')
    pdf.image(path_depois, 297-140, 35, width2, height2)
    
    #Line Breaker
    pdf.ln(117)
        
    #Território Desmatado 
    pdf.cell(30)
    pdf.set_draw_color(255,0,0)
    pdf.set_line_width(0.6)
    pdf.cell(12, 5, '', 1)
    pdf.set_font('Times', '', 10)
    pdf.cell(1)
    pdf.cell(35, 7, "ÁREA DESMATADA")

    #Sigef
    if (sigef != "N/P*"):
        pdf.ln(7)
        pdf.cell(20)
        pdf.cell(10)
        pdf.set_draw_color(1, 111, 144)
        pdf.set_line_width(0.6)
    
        pdf.cell(12, 5, '', 1)
        pdf.cell(1)
        pdf.set_font('Times', '', 10)
        pdf.cell(15, 7, "SIGEF")
    else:
        pdf.cell(1)
        
    #Regularização SIGEF
    
    if(regul_sigef != "N/P*"):
        pdf.ln(7)
        pdf.cell(20)
        pdf.cell(10)
        pdf.set_draw_color(244, 119, 6)
        pdf.set_line_width(0.6)
    
        pdf.cell(12, 5, '', 1)
        pdf.cell(1)
        pdf.set_font('Times', '', 10)
        pdf.cell(45, 7, "REGULARIZAÇÃO SIGEF")
    else:
        pdf.cell(1)
    
    #CAR
    if(car != "N/P*"):
        pdf.ln(7)
        pdf.cell(20)
        pdf.set_draw_color(150, 150, 150)
        pdf.set_line_width(0.6)
        pdf.cell(10)
        pdf.cell(12, 5, '', 1)
        pdf.cell(1)
        pdf.set_font('Times', '', 10)
        pdf.cell(10, 7, "CAR")
    else:
        pdf.cell(1)
    
    #SNCI
    if(snci != "N/P*"):
        pdf.ln(7)
        pdf.cell(20)
        pdf.cell(10)
        pdf.set_draw_color(255, 255, 0)
        pdf.set_line_width(0.6)
        pdf.cell(12, 5, '', 1)
        pdf.cell(1)
        pdf.set_font('Times', '', 10)
        pdf.cell(15, 7, "SNCI")
    else:
        pdf.cell(0)
        
    #UC
    if(UC != "N/P*"):
        pdf.ln(7)
        pdf.cell(20)
        pdf.cell(10)
        pdf.set_draw_color(0, 255, 0)
        pdf.set_line_width(0.6)
        pdf.cell(12, 5, '', 1)
        pdf.cell(1)
        pdf.set_font('Times', '', 10)
        pdf.cell(15, 7, "UC")
    else:
        pdf.cell(0)
    
    #Terras Legais
    
    if(TL != "N/P*"):
        pdf.ln(7)
        pdf.cell(20)
        pdf.cell(10)
        pdf.set_draw_color(0, 255, 255)
        pdf.set_line_width(0.6)
    
        pdf.cell(12, 5, '', 1)
        pdf.cell(1)
        pdf.set_font('Times', '', 10)
        pdf.cell(45, 7, "TERRAS LEGAIS")
    else:
        pdf.cell(1)
        
    #Terras Legais
    
    if(EM != "N/P*"):
        pdf.ln(7)
        pdf.cell(20)
        pdf.cell(10)
        pdf.set_draw_color(13, 118, 224)
        pdf.set_line_width(0.6)
    
        pdf.cell(12, 5, '', 1)
        pdf.cell(1)
        pdf.set_font('Times', '', 10)
        pdf.cell(45, 7, "EMBARGO")
    else:
        pdf.cell(1)
    
    
    pdf.add_page(orientation='L')
    pdf.set_auto_page_break(True, margin = 60.0)
    
    pdf.set_fill_color(188, 188, 188)
    
    pdf.cell(12)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_font('Times', 'b', 14)
    pdf.cell(250, 10, "Área desmatada", 1, align='C', fill=True)
    pdf.set_font('Times', '', 12)
    pdf.ln(10)
    pdf.cell(12)
    pdf.multi_cell(250, 8, territorio_desmatado, 1, align='C')
    
    pdf.ln(0)
    
    if(sigef != "N/P*"):
        pdf.ln(0)
        pdf.cell(12)
        pdf.set_font('Times', 'b', 14)
        pdf.cell(250, 10, "SIGEF", 1, align='C', fill=True)
        pdf.set_font('Times', '', 12)
        pdf.ln(10)
        pdf.cell(12)
        pdf.multi_cell(250, 8, sigef, 1, align='C')
        
        pdf.ln(0)
    else:
        pdf.cell(0)
    
    if(regul_sigef != "N/P*"):
        pdf.ln(0)
        pdf.cell(12)
        pdf.set_font('Times', 'b', 14)
        pdf.cell(250, 10, "REGULARIZAÇÃO SIGEF", 1, align='C', fill=True)
        pdf.set_font('Times', '', 12)
        pdf.ln(10)
        pdf.cell(12)
        pdf.multi_cell(250, 8, regul_sigef, 1, align='C')
        
        pdf.ln(0)
    else:
        pdf.cell(0)
    
    if(car != "N/P*"):
        pdf.ln(0)
        pdf.cell(12)
        pdf.set_font('Times', 'b', 14)
        pdf.cell(250, 10, "CAR", 1, align='C', fill=True)
        pdf.set_font('Times', '', 12)
        pdf.ln(10)
        pdf.cell(12)
        pdf.multi_cell(250, 8, car, 1, align='C')
        
        pdf.ln(0)
    else:
        pdf.cell(0)
    
    if(snci != "N/P*"):
        pdf.ln(0)
        pdf.cell(12)
        pdf.set_font('Times', 'b', 14)
        pdf.cell(250, 10, "SNCI", 1, align='C', fill=True)
        pdf.set_font('Times', '', 12)
        pdf.ln(10)
        pdf.cell(12)
        pdf.multi_cell(250, 8, snci, 1, align='C')
    else:
        pdf.cell(0)
        
    if(UC != "N/P*"):
        pdf.ln(0)
        pdf.cell(12)
        pdf.set_font('Times', 'b', 14)
    
        pdf.cell(250, 10, "Unidade de Conservação", 1, align='C', fill=True)
        pdf.set_font('Times', '', 12)
        pdf.ln(10)
        pdf.cell(12)
        pdf.multi_cell(250, 8, UC, 1, align='C')
    else:
        pdf.cell(0)
        
    if(TL != "N/P*"):
        pdf.ln(0)
        pdf.cell(12)
        pdf.set_font('Times', 'b', 14)
    
        pdf.cell(250, 10, "Terras Legais", 1, align='C', fill=True)
        pdf.set_font('Times', '', 12)
        pdf.ln(10)
        pdf.cell(12)
        pdf.multi_cell(250, 8, TL, 1, align='C')
    else:
        pdf.cell(0)
        
    if(EM != "N/P*"):
        pdf.ln(0)
        pdf.cell(12)
        pdf.set_font('Times', 'b', 14)
    
        pdf.cell(250, 10, "Embargo", 1, align='C', fill=True)
        pdf.set_font('Times', '', 12)
        pdf.ln(10)
        pdf.cell(12)
        pdf.multi_cell(250, 8, EM, 1, align='C')
    else:
        pdf.cell(0)
    
    pdf.output(path_relatorio)