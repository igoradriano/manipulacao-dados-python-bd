from flexx import flx
class Exemplo(flx.Widget):

    def init(self):
        with flx.HBox(): # HBox - distribuem o espaço entre seus filhos de uma maneira mais sensata
            flx.Button(text='hello', flex=1) # Button cria um botão chamado hello
            flx.Button(text='world', flex=2)


if __name__ == '__main__':
    a = flx.App(Exemplo, title='Flexx demonstração') # Para criar um aplicativo real a partir de um widget, basta envolvê-lo em um App.
    m = a.launch()  # Para realmente mostrar o aplicativo, use launch:
    flx.run()  # enter the mainloop

