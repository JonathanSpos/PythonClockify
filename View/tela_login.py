import tkinter

# Criando a janela_login
janela_login = tkinter.Tk()
janela_login.title("Formulário de Autenticação")
janela_login.geometry('340x440')
janela_login.configure(bg='#333333')

moldura = tkinter.Frame(bg='#333333')

# Criando widgets
login_label = tkinter.Label(moldura, text="Login", bg='#333333', fg='#FFFFFF', font=("Arial, 30"))
chaveapi_label = tkinter.Label(moldura, text="Chave API", bg='#333333', fg='#FFFFFF', font=("Arial, 20"))
chaveapi_entry = tkinter.Entry(moldura, font=("Arial, 16"))
chaveapi_entry = tkinter.Entry(moldura, show="*", font=("Arial, 16"))
botao_login = tkinter.Button(moldura, text="Entrar", font=("Arial, 16"))

# Posicionando os widgets
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=35)
chaveapi_label.grid(row=1, column=0)
chaveapi_entry.grid(row=1, column=1, pady=15)
botao_login.grid(row=3, column=0, columnspan=2, pady=25)


moldura.pack()

janela_login.mainloop()