import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()

root.iconbitmap('Sistema/car_ico.ico')
"""Adicionando comentarios para testa"""
class Application():

    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets()
        root.mainloop()

    def tela(self):
        self.root.title("")
        self.root.configure(background="#1e3743")
        self.root.geometry("1280x720")
        self.root.resizable(True, True)
        self.root.maxsize(width=1280, height=720)
        self.root.minsize(width=1280, height=720)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg="#dfe3ee", highlightbackground="#759fe6", highlightthickness=1)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight= 0.9 )

    def recolher(self):
        self.imgrecolher = PhotoImage(file="Sistema/fundo.png")
        self.imgrecolher = self.imgrecolher.subsample(1, 1)
        self.abc = Label(self.root, image=self.imgrecolher)
        self.abc.image = self.imgrecolher
        self.abc.place(relx=0.03, rely=0.62, relwidth=0.2, relheight=0.29)

    def analise(self):
        #Frame de Análise dos Dados
        self.frame_analise = Frame(self.root, bd=4, bg="#dfe3ee", highlightbackground="black", highlightthickness=1.5)
        self.frame_analise.place(relx=0.03, rely=0.62, relwidth=0.2, relheight=0.29)

        #Titulo do Frame
        from datetime import datetime
        hoje = datetime.today().strftime('%Y-%d-%m')
        titulo_analise = Label(self.frame_analise, text=f"Análise: {hoje} ", bg="#dfe3ee", font="-weight bold -size 12" )
        titulo_analise.place(relx=0, rely=0)

        linha_ttanalise = Label(self.frame_analise, text="-"*47, background="#dfe3ee")
        linha_ttanalise.place(relx=0, rely=0.1)

        #Total de Clientes
        total_clientes = self.c
        lb_ttc = Label(self.frame_analise, text="Total De Clientes:", bg="#dfe3ee", font="-weight bold -size 10")
        lb_ttc.place(relx=0, rely=0.2)

        lb_totalclientes = Label(self.frame_analise, text=f"{self.c}", bg="#dfe3ee")
        lb_totalclientes.place(relx=0.48, rely=0.2)

        #Faturamento Total
        faturamento_total = self.faturamento
        lb_faturamento = Label(self.frame_analise, text="Faturamento Total:", bg="#dfe3ee", font="-weight bold -size 10")
        lb_faturamento.place(relx=0, rely=0.35)

        lb_faturamento2 = Label(self.frame_analise, text=f"R$ {self.faturamento:.2f}",  bg="#dfe3ee")
        lb_faturamento2.place(relx=0.55, rely=0.35)

        #Media De Faturamento Por Cliente
        media = self.media
        lb_media = Label(self.frame_analise, text="Ticket Médio:", bg="#dfe3ee",
                               font="-weight bold -size 10")
        lb_media.place(relx=0, rely=0.5)

        lb_media2 = Label(self.frame_analise, text=f"R$ {media:.2F}", bg="#dfe3ee")
        lb_media2.place(relx=0.37, rely=0.5)

        #Média de horas
        media_horas = self.media_horas
        lb_media_horas = Label(self.frame_analise, text="Média de Permanência: ",bg="#dfe3ee",
                               font="-weight bold -size 10")
        lb_media_horas.place(relx=0, rely=0.65)

        lb_media_horas2 = Label(self.frame_analise, text=f"{self.media_horas:.0f} Horas", bg="#dfe3ee",)
        lb_media_horas2.place(relx=0.65, rely=0.65)

        # Recolher Análise
        self.bt_recolher = Button(self.frame_analise, text="Recolher Análise", command=self.recolher, highlightthickness=0)
        self.bt_recolher.place(relx=0.25, rely=0.84)

    def newpage(self):
        self.btclientes = Button(self.frame_1, text="Mostrar Análise", command=self.analise)
        self.btclientes.place(relx=0.08, rely=0.6)
        #Coletando e calculando os dados
        try:
            preco = float(self.preco_entry.get())
            nome = str(self.nome_entry.get()).title().strip()
            nome = " ".join(nome.split())
            nome_separado = str(self.nome_entry.get()).title().strip().split()
            modelo = str(self.modelo_entry.get()).upper().strip()
            modelo = " ".join(modelo.split())
            placa = str(self.placa_entry.get()).upper().strip()

            hora_inicial = int(self.horas1_entry.get())
            hora_final = int(self.horas2_entry.get())

            if hora_inicial > 24 or hora_final > 24:
                hora_inicial = "S"
            if hora_inicial > hora_final:
                hora_inicial = "s"

            horas = hora_final - hora_inicial
            total_preco_cliente = horas * preco

        except:
            messagebox.showerror(title="ERRO", message="DADOS INSERIDOS INCORRETAMENTE")
            self.c = self.c - 1

        #Calculando Dados
        self.c = self.c + 1

        self.faturamento = self.faturamento + total_preco_cliente
        self.total_horas = self.total_horas + horas
        self.media = self.faturamento / self.c
        self.media_horas = self.total_horas / self.c

        #Criação do Novo Frame
        self.frame_impressao = Frame(self.root, bd=4, bg="#dfe3ee",
                                     highlightbackground="#759fe6", highlightthickness=1.5)
        self.frame_impressao.place(relx=0.4, rely=0.1, relwidth=0.5, relheight=0.5)

        self.titulo_impressao = Label(self.frame_impressao, text=f"Ticket Cliente {nome_separado[0]}", bg="#dfe3ee", font="-weight bold -size 13")
        self.titulo_impressao.place(relx=0.38, rely=0.05)

        self.linha = Label(self.frame_impressao, text="-" * 120, bg="#dfe3ee")
        self.linha.place(relx=0.03, rely=0.2)

        #Mostrando Dados
        self.imag2 = PhotoImage(file="")
        self.iamg2_lb = Label(self.frame_impressao, image=self.imag2, bg="#dfe3ee")
        self.iamg2_lb.place(relx=0.76, rely=0.63)

        lbnome1 = Label(self.frame_impressao, text=f"Nome Completo: ", bg="#dfe3ee", font="-weight bold -size 10")
        lbnome1.place(relx=0.03, rely=0.3)
        lbnome2 = Label(self.frame_impressao, text=f"{nome}", bg="#dfe3ee")
        lbnome2.place(relx=0.22, rely=0.3)

        lbmodelo1 = Label(self.frame_impressao, text="Modelo Do Carro: ", bg="#dfe3ee", font="-weight bold -size 10")
        lbmodelo1.place(relx=0.03, rely=0.4)
        lbmodelo2 = Label(self.frame_impressao, text=f"{modelo}", bg="#dfe3ee")
        lbmodelo2.place(relx=0.22, rely=0.4)

        lbplaca1 = Label(self.frame_impressao, text="Placa Do Veículo: ", bg="#dfe3ee", font="-weight bold -size 10" )
        lbplaca1.place(relx=0.03, rely=0.5)
        lbplaca2 = Label(self.frame_impressao, text=f"{placa}", bg="#dfe3ee")
        lbplaca2.place(relx=0.22, rely=0.5)

        lbtempo_total1 = Label(self.frame_impressao, text="Tempo Total: ", bg="#dfe3ee", font="-weight bold -size 10")
        lbtempo_total1.place(relx=0.03, rely=0.6)
        lbtempo_total2 = Label(self.frame_impressao, text=f"{horas} Horas", bg="#dfe3ee")
        lbtempo_total2.place(relx=0.18, rely=0.6)

        lb_hr_entrada = Label(self.frame_impressao, text="Horário de Entrada: ", bg="#dfe3ee", font="-weight bold -size 10")
        lb_hr_entrada.place(relx=0.5, rely=0.3)
        lb_hr_entrada2 = Label(self.frame_impressao, text=f"{hora_inicial} H", bg="#dfe3ee")
        lb_hr_entrada2.place(relx=0.705, rely=0.3)

        lb_hr_entrada = Label(self.frame_impressao, text="Horário de Saída: ", bg="#dfe3ee",
                              font="-weight bold -size 10")
        lb_hr_entrada.place(relx=0.5, rely=0.4)
        lb_hr_entrada2 = Label(self.frame_impressao, text=f"{hora_final} H", bg="#dfe3ee")
        lb_hr_entrada2.place(relx=0.705, rely=0.4)

        lb_linha = Label(self.frame_impressao, text="-"*120, bg="#dfe3ee")
        lb_linha.place(relx=0.03, rely=0.68)

        lbpreco1 = Label(self.frame_impressao, text="PREÇO TOTAL: ", bg="#dfe3ee", font="-weight bold -size 13")
        lbpreco1.place(relx=0.33, rely=0.8)
        lbpreco2 = Label(self.frame_impressao, text=f"R$ {total_preco_cliente:.2f}", bg="#dfe3ee", font="size 12")
        lbpreco2.place(relx=0.55, rely=0.8)

    def widgets(self):
        #Analise
        self.c = 0
        self.faturamento = 0
        self.total_horas = 0

        #Cadastro
        self.titulo = Label(self.frame_1, text="PARKING CONTROL", bg="#dfe3ee", font="-weight bold -size 13")
        self.titulo.place(relx=0.42)


        self.preco = Label(self.frame_1, text="Preço P/ Hora: R$", bg="#dfe3ee", font="-weight bold -size 10")
        self.preco.place(relx=0.001, rely=0.1)
        self.preco_entry = Entry(self.frame_1)
        self.preco_entry.place(relx=0.1, rely=0.1)

        self.titulo2 = Label(self.frame_1, text="Cadastro de Clientes", font="-weight bold -size 12",bg="#dfe3ee")
        self.titulo2.place(relx=0.045, rely=0.18)

        self.nome = Label(self.frame_1, text="Nome Completo", bg="#dfe3ee", font="-weight bold -size 10")
        self.nome.place(relx=0.001, rely=0.25)
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.1, rely=0.25)

        self.modelo = Label(self.frame_1, text="Modelo do Carro ", bg="#dfe3ee", font="-weight bold -size 10")
        self.modelo.place(relx=0.001, rely=0.30)
        self.modelo_entry = Entry(self.frame_1)
        self.modelo_entry.place(relx=0.1, rely=0.30)

        self.placa = Label(self.frame_1, text="Placa Do Veículo", bg="#dfe3ee", font="-weight bold -size 10")
        self.placa.place(relx=0.001, rely=0.35)
        self.placa_entry = Entry(self.frame_1)
        self.placa_entry.place(relx=0.1, rely=0.35)

        self.hora_inicial = Label(self.frame_1, text="Hora De Entrada ", bg="#dfe3ee", font="-weight bold -size 10")
        self.hora_inicial.place(relx=0.001, rely=0.4)
        self.horas1_entry = Entry(self.frame_1)
        self.horas1_entry.place(relx=0.1, rely=0.4)

        self.hora_final = Label(self.frame_1, text="Hora De Saída ", bg="#dfe3ee", font="-weight bold -size 10")
        self.hora_final.place(relx=0.0001, rely=0.45)
        self.horas2_entry = Entry(self.frame_1)
        self.horas2_entry.place(relx=0.1, rely=0.45)

        #Botão Principal
        self.btenviardados = Button(self.frame_1, text="Gerar Ticket", command=self.newpage)
        self.btenviardados.place(relx=0.088, rely=0.54)

        #Carro
        self.estilo = PhotoImage(file="Sistema/car_teste (1).png")
        self.estilo = self.estilo.subsample(1, 1)
        self.abc = Label(self.frame_1, image=self.estilo)
        self.abc.image = self.estilo

        self.bt = Button(self.frame_1, image=self.estilo, bg="#dfe3ee", bd=0, highlightthickness=0)
        self.bt.place(relx=0.7, rely=0.8)

Application()
