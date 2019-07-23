"""
FelipedelosH

//Procedo a empezar de nuevo el teris.
+ La pantalla se refrescara automaticamente
+ El vector sera horientado deacuerdo a la realidad "gravedad"
"""

from tkinter import *
from threading import Thread
import time
import random

class Tetris():
    def __init__(self):
        # Pantalla Principal
        self.pantalla = Tk()
        # Zona de graficas
        self.tela = Canvas(self.pantalla, width=480, height=640, bg="white")
        self.tela.bind_all("<Key>", self.presionaTecla)

        # Piezas
        self.todasLasPiezas = []
        self.todasLasPiezas = self.construirPiezas()
        self.PIEZAS_DE_JUEGO = len(self.todasLasPiezas)
        
        

        # Variables
        self.puntaje = 0 # Indica el puntaje del jugador
        self.nivel = 1 # Indica el nivel deljugador
        self.tablero = [] # Aqui estara contenido el juego en binario
        self.piezaActual = [] # Aqui se controla cual es la pieza actual
        self.rotacionActual = 0 # Aqui se controla la rotacion de la pieza
        self.IDsigPieza = random.randint(0, (self.PIEZAS_DE_JUEGO-1)) # Aqui se pone la siguiente pieza que va a caer
        self.pox = 4 # Aqui se controla la Pos X de la pieza
        self.poy = 2 # Aqui se controla la pos y de la pieza

        # Zona de labels
        self.lblMensajes = Label(self.tela, text="Presiona Space para Iniciar")
        self.lblPuntaje = Label(self.tela, text=str(self.puntaje))
        """
        La siguiente variable controla animaciones
        0: el juego no ha empezado esta en la pantalla de carga
        """
        self.Tipo_de_juego = 0  
        # Hilo
        self.hilo = Thread(target=self.run)
        """
        Esta variable controla que se debe de mostrar en pantalla
        0 : animacion de cargando
        """
        self.tipoDeAnimacion = 0 


        self.visualizarInterfaz()


    def visualizarInterfaz(self):
        self.pantalla.title("tetris by loko v2.0")
        self.pantalla.geometry("480x640")
        self.tela.place(x=0, y=0)
        self.lblMensajes.place(x=100, y=300)
        self.lblPuntaje.place(x=400, y=20)
        self.construirMiniatura()
        # Procedo a iniciar el hilo
        self.hilo.start()
        # Procedo a invocar inmediatamente 0ms el refresco de la pantalla
        self.pantalla.after(0, self.refrescarPantalla)
        self.pantalla.mainloop()


   # este metodo refresca la pantalla cada 30 ms
    def refrescarPantalla(self):
        self.pantalla.after(30, self.refrescarPantalla)

    """Aqui se construyen todas las piezas y sus rotaciones"""
    def construirPiezas(self):
        piezas = []

        """
           1111
        """

        a = [[1,1,1,1]]
        b = [[1],[1],[1],[1]]
        
        piezas.append([a, b])


        """
           1
           111
        """

        a = [[1,0,0],[1,1,1]]
        b = [[1,1],[1,0],[1,0]]
        c = [[1,1,1], [0,0,1]]
        d = [[0,1],[0,1],[1,1]]


        piezas.append([a, b, c, d])

        """    
              1
            111
        """

        a = [[0,0,1],[1,1,1]]
        b = [[1,0],[1,0],[1,1]]
        c = [[1,1,1], [0,0,1]]
        d = [[1,1],[0,1],[0,1]]


        piezas.append([a, b, c, d])

        """
            11
            11
        """

        a = [[1,1], [1,1]]

        piezas.append([a])

        """
         
        """


        return piezas

    """Este metodo ocurre cuando el jugo no ha iniciado
      self.Tipo_de_juego = 0 >> el mensaje parpadea
    """
    def animcacionEsperandoParaComenzar(self):
        self.lblMensajes.place(x=100, y=300)
        time.sleep(0.2)
        self.lblMensajes.place_forget() # Borra
        time.sleep(0.2)
        



    """Este metodo se encarga de:
    Contruir la mini pantalla que es donde se pone la miniatura de las piezas
    """
    def construirMiniatura(self):
        for i in range(0, 4):
            for j in range(0, 4):
                x0 = 400
                y0 = 150
                self.tela.create_rectangle((x0+(j*14)), (y0+(i*14)), (x0+((j+1))*14), (y0+((i+1))*14), tag="miniatura")
                


    """Este metodo se va a encargar:
    pintar el tablero.
    pintar los indicadores para el jugador
    """
    def construccionPantalla(self):
        self.tablero = []
        for i in range(0, 18):
            self.tablero.append([])
            for j in range(0, 10):
                x0 = 20
                y0 = 50
                self.tela.create_rectangle((x0+(j*30)), (y0+(i*30)), (x0+((j+1))*30), (y0+((i+1))*30), tag="tablero")
                # Se dispone a construir el tablero
                self.tablero[i].append(0)
        

 

    # Este metodo controla cuando se presiona una tecla que se debe de hacer
    def presionaTecla(self, Event):
        if Event.keysym == "Up":
            pass
        if Event.keysym == "Down":
            pass
        if Event.keysym == "Right":
            pass
        if Event.keysym == "Left":
            pass
           

        """Si se presiona espacio el juego empieza
        1 - Se construye la pantalla de juego
        2 - Se borra el mensaje
        """
        if Event.keysym == "space":
            if self.Tipo_de_juego == 0:
                self.Tipo_de_juego = 1
                self.construccionPantalla()
                self.lblMensajes.place_forget()
                

    # Este metodo edita el self.lblMensaje 
    def editarMSM(self, txt):
        self.lblMensajes['text'] = str(txt)

    # Este metodo pinta la miniatura
    def pintarMiniatura(self):
        m = self.todasLasPiezas[self.IDsigPieza][0]
        minitablero = self.tela.find_withtag("miniatura")
        
        # variable auxiliar para recorrer la min
        aux = 0
        for i in m:
            for j in i:
                if j == 1:
                    self.tela.itemconfig(minitablero[aux], fill="black")

                # Recorro un solo espacio la miniatura para pintar
                aux = aux + 1

            # La pieza termino 1 avanzo 1 nivel de la miniatura
            aux = aux + (4 - len(i))


    # Este metodo despinta la miniatura
    def borrarMiniatura(self):
        for i in self.tela.find_withtag("miniatura"):
            self.tela.itemconfig(i, fill="white")


    # Este metodo se encarga de escoger una pieza de manera aleatorea
    # la pieza es buscada en self.todasLasPiezas
    def newPieza(self):
        self.piezaActual = self.todasLasPiezas[self.IDsigPieza]
        self.IDsigPieza = random.randint(0, (self.PIEZAS_DE_JUEGO-1))
        print(self.IDsigPieza)

    # Este metodo se Encarga de pintar la pieza Actual
    def pintarPieza(self):
        # Que tan ancha es la pieza actual
        ancho = self.anchoPieza()
        print("Ancho:",ancho)
        # Que tan larga es
        larga = self.largoPieza()
        print("Largo:", larga)

                    

        self.representarBinario()


    # este metodo representa lo que este en el tablero binario y lo pinta (refresca)
    def representarBinario(self):
         # Procedo a pintar lo que diga el tablero Binario
        auxx = 0
        auxy = 0
        for i in self.tela.find_withtag("tablero"):
            if auxx > 9:
                auxx = 0
                auxy = auxy + 1

            if self.tablero[auxy][auxx] != 0:
                self.tela.itemconfig(i, fill="black")
            else:
                self.tela.itemconfig(i, fill="white")
            
            auxx = auxx + 1


    # Este metodo retorna el ancho de la pieza actual
    def anchoPieza(self):
        return len(self.piezaActual[self.rotacionActual][0])

    # Este metodo retorna que tan larga es una pieza
    def largoPieza(self):
        return len(self.piezaActual[self.rotacionActual])



    def run(self):
        while True:
            """Se verifica si el juego esta en modo 0: modo carga
                                               modo 1: se esta jugando
            """

            # Modo carga solo parpadea el mensaje
            if self.Tipo_de_juego == 0:
                self.animcacionEsperandoParaComenzar()

            # Modo juego 
            if self.Tipo_de_juego == 1:
                # Hay que escoger una nueva pieza
                self.pintarMiniatura()


# Se lanza el sw
t = Tetris()