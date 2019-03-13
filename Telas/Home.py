from tkinter import *

class Home:

    def __init__(self, master = None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text='Primeiro Widget')
        self.msg["font"] = ('Verdana', '10', 'italic', 'bold')
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair['text'] = 'Clique Aqui'
        self.sair['font'] = ('Calibri', '9')
        self.sair['width'] = 10
        self.sair["command"] = self.mudarTexto
        self.sair.pack()

    def mudarTexto(self):
        if self.msg["text"] == "Primeiro Widget":
            self.msg["text"] = "O Botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro Widget"

root = Tk()
root.title('Tela Sorteio')
Home(root)
root.mainloop()