import tkinter as tk

class CriarToolTip(object):
    def __init__(page, widget, text='widget info'):
        page.tempo_espera = 500    
        page.wraplength = 180       
        page.widget = widget
        page.text = text
        page.widget.bind("<Enter>", page.entrar)
        page.widget.bind("<Leave>", page.sair)
        page.widget.bind("<ButtonPress>", page.sair)
        page.id = None
        page.tw = None

    def entrar(page, event=None):
        page.agendar()

    def sair(page, event=None):
        page.desagendar()
        page.esconder_tool_tip()

    def agendar(page):
        page.desagendar()
        page.id = page.widget.after(page.tempo_espera, page.exibir)

    def desagendar(page):
        id = page.id
        page.id = None
        if id:
            page.widget.after_cancel(id)

    def exibir(page, event=None):
        x = y = 0
        x, y, cx, cy = page.widget.bbox("insert")
        x += page.widget.winfo_rootx() + 25
        y += page.widget.winfo_rooty() + 20

        page.tw = tk.Toplevel(page.widget)
        
        page.tw.wm_overrideredirect(True)
        page.tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(page.tw, 
                        text = page.text, 
                        justify = 'left',
                        background = "#ffffff", 
                        relief = 'solid', 
                        borderwidth = 1,
                        wraplength = page.wraplength)
        label.pack(ipadx=1)

    def esconder_tool_tip(page):
        tw = page.tw
        page.tw= None
        if tw:
            tw.destroy()
