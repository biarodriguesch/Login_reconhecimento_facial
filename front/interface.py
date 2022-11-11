import sys

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import IntVar

from .tooltip import CriarToolTip

class Interface:
    def __init__(page):
        page.top = tk.Tk()

        page._bgcolor = '#339933' # background texto,verde
        page._fgcolor = '#000000'  # cor do texto, preto
        page._compcolor = '#d9d9d9' # borta do botao 
        page._ana2color = '#d9d9d9' # sombra do click do botão, verde
        page.font9 = "-family {Segoe UI Light} -size 12 -weight bold"
        page.continuar_mostrando_webcam = True

        page.style = ttk.Style()
        if sys.platform == "win32":
            page.style.theme_use('winnative')
        page.style.configure('.',background = page._bgcolor)
        page.style.configure('.',foreground = page._fgcolor)
        page.style.configure('.',font = "TkDefaultFont")
        page.style.map('.',background = [('selected', page._compcolor), ('active',page._ana2color)])

        X = int(page.top.winfo_screenwidth() / 2 - page.top.winfo_reqwidth() / 2)
        Y = int(page.top.winfo_screenheight() / 3 - page.top.winfo_reqheight() / 2)
        X = int(X * 0.8)
        Y = int(Y * 0.8)

        page.top.geometry(f"634x536+{X}+{Y}")
        page.top.minsize(120, 1)
        page.top.maxsize(3844, 1061)
        page.top.resizable(1, 1)
        page.top.title("Login Ministério do Meio Ambiente")
        page.top.configure(background="#339933")

        page.texto_bemvindo = ttk.Label(page.top)
        page.texto_bemvindo.place(relx=0.325, rely=0.12, height=49, width=205)
        page.texto_bemvindo.configure(font="-family {Yu Mincho Demibold} -size 24 -weight bold ")
        page.texto_bemvindo.configure(relief="flat")
        page.texto_bemvindo.configure(anchor='w')
        page.texto_bemvindo.configure(justify='center')
        page.texto_bemvindo.configure(text='''Bem vindo(a)''')
        page.texto_bemvindo.configure(compound='top')

        page.texto_msg_inicio = ttk.Label(page.top)
        page.texto_msg_inicio.place(relx=0.228, rely=0.320, height=99, width=325)
        page.texto_msg_inicio.configure(font="TkDefaultFont")
        page.texto_msg_inicio.configure(borderwidth="5")
        page.texto_msg_inicio.configure(relief="ridge")
        page.texto_msg_inicio.configure(anchor='center')
        page.texto_msg_inicio.configure(justify='center')
        page.texto_msg_inicio.configure(text='''Login e registro Ministério do meio Ambiente.''')
        page.texto_msg_inicio.configure(wraplength = 300)

        page.botao_login = ttk.Button(page.top, text = "Login", command = page._botao_login_clicado)
        page.botao_login.place(relx=0.252, rely=0.877, height=35, width=86)
        page.botao_login.configure(cursor="hand2")
        button1_ttp = CriarToolTip(page.botao_login, \
            "Clique para fazer login caso você já esteja registrado.")

        page.botao_registrar = ttk.Button(page.top, text = "Registrar", command = page._botao_registrar_clicado)
        page.botao_registrar.place(relx=0.426, rely=0.877, height=35, width=96)
        page.botao_registrar.configure(cursor="hand2")
        button2_ttp = CriarToolTip(page.botao_registrar, \
            "Clique para se registrar caso não possua registro, antes de poder fazer login.")

        page.botao_sair = ttk.Button(page.top, text = "Sair", command = page._botao_sair_clicado)
        page.botao_sair.place(relx=0.615, rely=0.877, height=35, width=86)
        page.botao_sair.configure(cursor="hand2")
        button3_ttp = CriarToolTip(page.botao_sair, \
            "Clique para sair e encerrar o programa.")

        page.top.mainloop()
    
    def _tela_de_aviso(page, msg):
        """Exibe uma tela de aviso, com uma mensagem, em cima do resto do programa."""
        page.frame_tela_aviso = ttk.Frame(page.top)
        page.frame_tela_aviso.place(relx=0.014, rely=0.017, relheight=0.96, relwidth=0.97)
        page.frame_tela_aviso.configure(relief='groove')
        page.frame_tela_aviso.configure(borderwidth="2")
        page.frame_tela_aviso.configure(relief="groove")

        page.texto_mensagem = tk.Message(page.frame_tela_aviso)
        page.texto_mensagem.place(relx = 0.325, rely = 0.285, relheight = 0.292, relwidth = 0.341)
        page.texto_mensagem.configure(background = "#d9d9d9")
        page.texto_mensagem.configure(font = page.font9)
        page.texto_mensagem.configure(highlightbackground = "#d9d9d9")
        page.texto_mensagem.configure(highlightcolor = "black")
        page.texto_mensagem.configure(text = msg)
        page.texto_mensagem.configure(anchor='center')
        page.texto_mensagem.configure(justify='center')
        page.texto_mensagem.configure(width = 210)

        page.botao_ok = ttk.Button(page.frame_tela_aviso, text = "Ok", command = page.frame_tela_aviso.destroy)
        page.botao_ok.place(relx=0.400, rely=0.870, height=35, width=116)

    def _exibir_dados_confidenciais(page, nome, num):
        """Exibe os dados baseado no cargo que dada pessoa registrada tem."""
        page.style.configure('TNotebook.Tab', background = page._bgcolor)
        page.style.configure('TNotebook.Tab', foreground = page._fgcolor)
        page.style.map('TNotebook.Tab', background = [('selected', page._compcolor), ('active', page._ana2color)])

        page.TNotebook1 = ttk.Notebook(page.frame_login)
        page.TNotebook1.place(relx=0.016, rely=0.060, relheight=0.835, relwidth=0.967)
        page.TNotebook1.configure(takefocus="")

        if num >= 1:
            page.TNotebook1_t1 = tk.Frame(page.TNotebook1)
            page.TNotebook1.add(page.TNotebook1_t1, padding = 5)
            page.TNotebook1.tab(0, text = "Funcionários", compound = "left", underline = "-1",)
            page.TNotebook1_t1.configure(background="#339933")
            page.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
            page.TNotebook1_t1.configure(highlightcolor="black")
        if num >= 2:
            page.TNotebook1_t2 = tk.Frame(page.TNotebook1)
            page.TNotebook1.add(page.TNotebook1_t2, padding=5)
            page.TNotebook1.tab(1, text="Diretores",compound="left",underline="-1",)
            page.TNotebook1_t2.configure(background="#339933")
            page.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
            page.TNotebook1_t2.configure(highlightcolor="black")
        if num >= 3:
            page.TNotebook1_t3 = tk.Frame(page.TNotebook1)
            page.TNotebook1.add(page.TNotebook1_t3, padding = 5)
            page.TNotebook1.tab(2, text = "CEO", compound = "left", underline = "-1",)
            page.TNotebook1_t3.configure(background = "#339933")
            page.TNotebook1_t3.configure(highlightbackground = "#d9d9d9")
            page.TNotebook1_t3.configure(highlightcolor = "black")

        page.label_cargo = tk.Label(page.frame_login)
        page.label_cargo.place(relx = 0.010, rely = 0, height = 31, width = 500)
        page.label_cargo.configure(anchor = 'w')
        page.label_cargo.configure(background = "#339933")
        page.label_cargo.configure(disabledforeground = "#a3a3a3")
        page.label_cargo.configure(font = page.font9)
        page.label_cargo.configure(foreground = "#000000")

        if num == 0:
            page.label_cargo.configure(text=f"Seja bem-vindo(a), {nome}.")
        elif num == 1:
            page.label_cargo.configure(text=f"Seja bem-vindo(a), diretor(a) {nome}.")
        elif num == 2:
            page.label_cargo.configure(text=f"Seja bem-vindo(a), ministro(a) {nome}.")

    def _criar_interface_login(page):
        """Chamado caso haja alguém registrado, para iniciar o login de alguém."""
        page.frame_login = ttk.Frame(page.top)
        page.frame_login.place(relx=0.014, rely=0.017, relheight=0.96, relwidth=0.97)
        page.frame_login.configure(relief='groove')
        page.frame_login.configure(borderwidth="2")
        page.frame_login.configure(relief="groove")

        page.frame_feed_webcam = tk.Frame(page.frame_login)
        page.frame_feed_webcam.place(relx=0.150, rely=0.195, relheight=0.65, relwidth=0.70)
        page.frame_feed_webcam.configure(relief='groove')
        page.frame_feed_webcam.configure(borderwidth="2")
        page.frame_feed_webcam.configure(relief="groove")
        page.frame_feed_webcam.configure(background="#d9d9d9")

        page.texto_validando = ttk.Label(page.frame_login)
        page.texto_validando.configure(background="#339933")
        page.texto_validando.configure(foreground="#000000")
        page.texto_validando.configure(font="TkDefaultFont")
        page.texto_validando.configure(relief="flat")
        page.texto_validando.configure(anchor='w')
        page.texto_validando.configure(justify='left')

        page.titulo_login = ttk.Label(page.frame_login)
        page.titulo_login.place(relx = 0.095, rely = 0.010, height = 40, width = 500)
        page.titulo_login.configure(font = '-family {Segoe UI} -size 23 -weight bold')
        page.titulo_login.configure(anchor = 's')
        page.titulo_login.configure(justify = 'center')
        page.titulo_login.configure(text = 'Verificação biométrica')

        page.mensagem_tela_login = ttk.Label(page.frame_login)
        page.mensagem_tela_login.place(relx = 0.095, rely = 0.1, height = 20, width = 500)
        page.mensagem_tela_login.configure(font = '-family {Segoe UI} -size 11')
        page.mensagem_tela_login.configure(anchor = 's')
        page.mensagem_tela_login.configure(justify = 'center')
        page.mensagem_tela_login.configure(text = 'Por favor, fique parado em frente a câmera.')

        page.botao_retornar = ttk.Button(page.frame_login, text = "Voltar", command = page.frame_login.destroy)
        page.botao_retornar.place(relx=0.875, rely=0.915, height=35, width=70)
        page.botao_retornar.configure(takefocus="")
        page.botao_retornar.configure(cursor="hand2")

    def _criar_frame_webcam(page):
        if page.frame_feed_webcam.winfo_exists():
            page.webcam_frame = tk.Label(page.frame_feed_webcam)
            page.webcam_frame.pack() # Tem que dar 'pack()' aqui, senão não aparece o label na GUI.

    def _botao_registrar_clicado(page):
        """Chamado pelo botão 'Registrar' na tela principal do programa."""
        page.frame_registro = ttk.Frame(page.top)
        page.frame_registro.place(relx=0.014, rely=0.017, relheight=0.96, relwidth=0.97)
        page.frame_registro.configure(relief='groove')
        page.frame_registro.configure(borderwidth="2")
        page.frame_registro.configure(relief="groove")

        page.texto_nome = tk.Entry(page.frame_registro)
        page.texto_nome.place(relx=0.325, rely=0.047,height=20, relwidth=0.461)
        page.texto_nome.configure(background="white")
        page.texto_nome.configure(disabledforeground="#a3a3a3")
        page.texto_nome.configure(font="TkFixedFont")
        page.texto_nome.configure(foreground="#000000")
        page.texto_nome.configure(highlightbackground="#d9d9d9")
        page.texto_nome.configure(highlightcolor="black")
        page.texto_nome.configure(insertbackground="black")
        page.texto_nome.configure(selectbackground="#c4c4c4")
        page.texto_nome.configure(selectforeground="black")
        page.texto_nome.configure(takefocus="0")

        page.label_nome = tk.Label(page.frame_registro)
        page.label_nome.place(relx=0.195, rely=0.047, height=22, width=65)
        page.label_nome.configure(activebackground="#f9f9f9")
        page.label_nome.configure(activeforeground="black")
        page.label_nome.configure(anchor='se')
        page.label_nome.configure(background="#339933")
        page.label_nome.configure(disabledforeground="#a3a3a3")
        page.label_nome.configure(font="-family {Segoe UI} -size 12")
        page.label_nome.configure(foreground="#000000")
        page.label_nome.configure(highlightbackground="#d9d9d9")
        page.label_nome.configure(highlightcolor="black")
        page.label_nome.configure(justify='right')
        page.label_nome.configure(text='''Nome:''')

        page.style.map('TRadiobutton',background=[('selected', page._bgcolor), ('active', page._ana2color)])

        # Faz a opção 'opc_diretor' ser o valor default; 'page.cargo_selecionado' guarda qual radiobutton foi selecionado, via os valores deles.
        page.cargo_selecionado = IntVar()
        page.cargo_selecionado.set(1)

        page.opc_funcionario = ttk.Radiobutton(page.frame_registro, variable = page.cargo_selecionado, value = 1)
        page.opc_funcionario.place(relx=0.265, rely=0.115, relwidth=0.170, relheight=0.0, height=30)
        page.opc_funcionario.configure(text='''Funcionário(a)''')
        page.opc_funcionario.configure(cursor="hand2")

        page.opc_diretor = ttk.Radiobutton(page.frame_registro, variable = page.cargo_selecionado, value = 2)
        page.opc_diretor.place(relx=0.460, rely=0.115, relwidth=0.140, relheight=0.0, height=30)
        page.opc_diretor.configure(text='''Diretor(a)''')
        page.opc_diretor.configure(cursor="hand2")

        page.opc_ministro = ttk.Radiobutton(page.frame_registro, variable = page.cargo_selecionado, value = 3)
        page.opc_ministro.place(relx=0.610, rely=0.115, relwidth=0.140, relheight=0.0, height=30)
        page.opc_ministro.configure(text='''Ministro(a)''')
        page.opc_ministro.configure(cursor="hand2")

        page.frame_feed_webcam = tk.Frame(page.frame_registro)
        page.frame_feed_webcam.place(relx=0.160, rely=0.195, relheight=0.65, relwidth=0.70)
        page.frame_feed_webcam.configure(relief='groove')
        page.frame_feed_webcam.configure(borderwidth="2")
        page.frame_feed_webcam.configure(relief="groove")
        page.frame_feed_webcam.configure(background="#d9d9d9")

        page.botao_confirmar_registro = ttk.Button(page.frame_registro, text = "Confirmar registro", command = page._botao_confirmar_registro_clicado)
        page.botao_confirmar_registro.place(relx=0.400, rely=0.892, height=35, width=116)
        page.botao_confirmar_registro.configure(takefocus="")
        page.botao_confirmar_registro.configure(cursor="hand2")

        page.botao_tirar_foto = ttk.Button(page.frame_registro, text = "Tirar foto", command = page._botao_tirar_foto_clicado)
        page.botao_tirar_foto.place(relx=0.400, rely=0.892, height=35, width=116)
        page.botao_tirar_foto.configure(takefocus="")
        page.botao_tirar_foto.configure(cursor="hand2")      

        page.botao_retornar = ttk.Button(page.frame_registro, text = "Voltar", command = page.frame_registro.destroy)
        page.botao_retornar.place(relx=0.875, rely=0.915, height=35, width=70)
        page.botao_retornar.configure(takefocus="")
        page.botao_retornar.configure(cursor="hand2")

        page.continuar_mostrando_webcam = True

        page._webcam_durante_registro()

    def _botao_tirar_foto_clicado(page):
        """Chamado pelo botão 'Tirar foto', dentro da interface de registro de novo usuário."""
        page.continuar_mostrando_webcam = False
        page.botao_confirmar_registro.lift()

    def _botao_confirmar_registro_clicado(page):
        """Chamado pelo botão 'Confirmar', dentro da interface de registro de novo usuário."""
        nome = page.texto_nome.get()
        page._salvar_database(nome, page.cargo_selecionado.get()) if nome != "" else page._tela_de_aviso("Você não inseriu um nome.")

    def _botao_sair_clicado(page):
        """Chamado pelo botão 'Sair' na tela principal do programa."""
        sys.exit(0)