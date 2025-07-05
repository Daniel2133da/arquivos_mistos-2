import sys
from classes import Info, Planilha, MainWindow, setupTheme, Grades, Valor, Usuario
from PySide6.QtWidgets import QApplication



planilha = Planilha()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    setupTheme(app)
    

    info = Info('CLIENTE')
    window.addObjetoLayout(info)
    comprador = Usuario()
    window.addObjetoLayout(comprador)
    
    info1 = Info('VALOR')
    window.addObjetoLayout(info1)
    valor = Valor()
    window.addObjetoLayout(valor)

    grades1 = Grades(planilha, comprador, valor, info1)
    window.vLayout.addLayout(grades1)


    window.adjustFixedSize()

    window.show()   
    app.exec() 
    planilha.salvar()   
