import tkinter as tk 
contador= 0
def contador_label(lblRotulo): # recebe o Label
    def funcao_contar():
        global contador
        contador = contador + 1
        lblRotulo.config(text=str(contador))
        lblRotulo.after(1000, funcao_contar) # a cada 1000ms ou 1 s chama recursivamente a funcao contar
    funcao_contar() # chama a funcao contar dentro da fucao_label
#after(parent, ms, function = None, *args)
"""Parâmetros:
parent : é o objeto do widget ou janela principal, o que quer que esteja usando esta função.
ms : é o tempo em milissegundos.
function : que deve ser chamada.
* args : outras opções."""

janela = tk.Tk()  # cria a janela tkinter
janela.title('Contagem dos Segundos') #coloca o titulo na janela
lblRotulo = tk.Label(janela, fg='green')# Cria uma Label #foreground - cor do primeiro plano para o widget. Isso também pode ser representado como fg .
lblRotulo.pack() #Este gerenciador de geometria organiza widgets em blocos antes de colocá-los no widget pai.
#--------------------------------------------fim do primeiro pack() onde ira ficar o contador
contador_label(lblRotulo) #Chamada para a função “contador_label”, que é a função que faz a contagem dos segundos e a atualização dos dados do componente “label”
btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy) #Criação de uma instância do componente “botão” com uma mensagem, largura do componente e o estabelecimento de um comportamento, no caso, fechar a janela, quando o usuário pressionar o botão.
btnAcao.pack()
#---------------------------------------------fim do segundo pack() onde ficará o botao
janela.mainloop()