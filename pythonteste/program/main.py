import PySimpleGUI as sg 
from teste import automatico

layout = [

    [sg.Text("Digite a mensagem que quer enviar")],
    [sg.InputText(key="mensagem")],
    [sg.Text("Quantas mensagens")],
    [sg.InputText(key="velocidade")],
    [sg.Button("Enviar"),sg.Button("Parar")],
]

    #Janela
janela = sg.Window("Mensagens automáticas", layout)


    #Lógica
while True: 
    evento, valores = janela.read()


    #Clicar no X para fechar
    if evento == sg.WIN_CLOSED or evento == "Parar" : 

        break

    if evento == "Enviar":
        mensagem = valores["mensagem"]
        velocidade = int(valores["velocidade"])
        if mensagem and velocidade: 
            automatico([mensagem], velocidade)



        
        
        
   
janela.close()
