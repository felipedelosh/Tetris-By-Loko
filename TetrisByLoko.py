"""
@FelipedelosH
05 / 31 / 2019

Procedo a crear un tetris

"""

from tkinter import *
import threading
import time
from random import randint

class SW:
    def __init__(self):
        self.pantalla = Tk()
        # Muestra las estadisticas
        self.telaInformacion = Canvas(self.pantalla, width=480, height=90, bg="snow")
        self.puntaje = 0
        self.lblPuntaje = Label(self.telaInformacion, text="Puntaje: "+str(self.puntaje))
        self.nivel = 1
        self.lblNivel = Label(self.telaInformacion, text="Nivel: "+str(self.nivel))
        # Muestra el tablero de juego
        self.telaGame = Canvas(self.pantalla, width=480, height=540, bg="white")
        # Se vincula el presionar una tecla con el canvas
        self.telaGame.bind_all("<Key>", self.presionaTecla)
        # Se crea Un Label De informacion del juego
        self.lblInformacion = Label(self.telaGame, text="Pressiona Space para iniciar")
        # Se generan las piezas
        self.listaDePiezas = []
        self.listaDePiezas = self.generarListaDePiezas()
        # Se captura la informacion de la pieza actual
        self.piezaActual = []
        self.piezaActual_x = 0
        self.piezaActual_y = 0

        # Control Del Juego
        # Controla si el juego ha empezado
        self.starGame = False
        # Hilo controla el juego
        self.game = threading.Thread(target=self.run)
        # Control de retardo del juego
        # Mientas mas avanza el nivel menor es el retardo del juego
        self.retardo = 1
        self.lanzarPantalla()
    
    # Se procede a configurar y mostrar los elementos de la pantalla
    def lanzarPantalla(self):
        # Configuracion de la pantalla
        self.pantalla.geometry("480x640")
        self.pantalla.title("Tetris by Loko")
        # Se configura la tela de informacion
        self.telaInformacion.place(x=0, y=0)
        self.lblPuntaje.place(x=10, y=20)
        self.lblNivel.place(x=200, y=20)
        # Se crea la matricita que muesta la sig pieza
        # Esta matrix se asocia a sig pieza
        for i in range(0, 4):
            for j in range(0, 4):
                x0 = 380 + (j*20) 
                y0 = 5 + (i*20)
                self.telaInformacion.create_rectangle(x0, y0, x0+20, y0+20, tag="sigpieza")
        # Se pinta la tela de juego
        self.telaGame.place(x=0, y=93)
        # Se pinta el mensaje de press space para iniciar
        self.lblInformacion.place(x=160, y=100)
        # Modo De juego
        # 0 significa que estamos sin iniciar el juego
        # Por ello se procede a pintar la pantalla
        # 1 significa que estamos jugando
        self.modoJuego = 0
        # Esta Matrix controla que pasa con el tablero
        self.matrixTablero = []
        # Esta variable controla si la pieza esta callendo
        self.piezaCallendo = False
        # Esta variable controla cual es la siguiente pieza que cae
        self.IDsigPieza = 0
        self.pantalla.mainloop()

    # Se Actualiza la informacion del juego
    def actualizarInformacion(self):
        # Se actualiza el puntaje
        self.lblPuntaje['text'] = "Puntaje: "+str(self.puntaje)
        # Se Actualiza el nivel
        self.lblNivel['text'] = "Nivel: "+str(self.nivel)

    # Este metodo me dice cual sera la sigPieza
    def cualSigPieza(self):
        # Se procede a escoger la pieza actual
        self.IDsigPieza = randint(0, len(self.listaDePiezas)-1)
        self.piezaActual = self.listaDePiezas[self.IDsigPieza]

    # Este metodo procede a poner la pieza en el tablero 
    # en la pos x, y
    def ponerPieza(self):
        # Dependiendo de que tan larga sea la pieza empiezo a pintar
        aux_x = self.piezaActual_x
        aux_y = self.piezaActual_y
        for i in self.piezaActual:
            for j in i:
                self.matrixTablero[aux_x][aux_y] = j
                aux_y = aux_y + 1
            aux_y = self.piezaActual_y
            aux_x = aux_x + 1

    # Este metodo mueve la pieza a la derecha


    # Este metodo mueve la pieza a la Izquierda
    # 1ro se comprueba que no se salga del tablero
    def mov_izq(self):
        if self.piezaActual_x > 0:
            # Procedo a borrar la pieza
            # Dependiendo de que tan larga sea la pieza empiezo a pintar
            aux_x = self.piezaActual_x
            aux_y = self.piezaActual_y
            for i in self.piezaActual:
                for j in i:
                    self.matrixTablero[aux_x][aux_y] = 0
                    aux_y = aux_y + 1
                aux_y = self.piezaActual_y
                aux_x = aux_x + 1

            # Procedo a decrementar x
            self.piezaActual_x = self.piezaActual_x - 1

    # Este metodo mueve la pieza a la derecha
    # 1ro se comprueba que no se salga del tablero
    def mov_der(self):
        pass

        
        

    # Se actualiza la miniatura de la sigPieza
    def actualizarMiniatura(self):
        # Se procede a borrar la pieza anterior
        for i in self.telaInformacion.find_withtag("sigpieza"):
            self.telaInformacion.itemconfig(i, fill='white')

        # Se procede a pintar la nueva pieza
        # Pintar el cuadrado
        if self.IDsigPieza == 0:
            self.telaInformacion.itemconfig(6, fill='black')
            self.telaInformacion.itemconfig(7, fill='black')
            self.telaInformacion.itemconfig(10, fill='black')
            self.telaInformacion.itemconfig(11, fill='black')

        if self.IDsigPieza == 1:
            self.telaInformacion.itemconfig(2, fill='black')
            self.telaInformacion.itemconfig(6, fill='black')
            self.telaInformacion.itemconfig(10, fill='black')
            self.telaInformacion.itemconfig(14, fill='black')

        if self.IDsigPieza == 2:
            self.telaInformacion.itemconfig(5, fill='black')
            self.telaInformacion.itemconfig(6, fill='black')
            self.telaInformacion.itemconfig(7, fill='black')
            self.telaInformacion.itemconfig(10, fill='black')

        if self.IDsigPieza == 3:
            self.telaInformacion.itemconfig(5, fill='black')
            self.telaInformacion.itemconfig(6, fill='black')
            self.telaInformacion.itemconfig(7, fill='black')
            self.telaInformacion.itemconfig(11, fill='black')

        if self.IDsigPieza == 4:
            self.telaInformacion.itemconfig(5, fill='black')
            self.telaInformacion.itemconfig(6, fill='black')
            self.telaInformacion.itemconfig(7, fill='black')
            self.telaInformacion.itemconfig(9, fill='black')

        if self.IDsigPieza == 5:
            self.telaInformacion.itemconfig(7, fill='black')
            self.telaInformacion.itemconfig(10, fill='black')
            self.telaInformacion.itemconfig(11, fill='black')
            self.telaInformacion.itemconfig(14, fill='black')

        if self.IDsigPieza == 6:
            self.telaInformacion.itemconfig(6, fill='black')
            self.telaInformacion.itemconfig(10, fill='black')
            self.telaInformacion.itemconfig(11, fill='black')
            self.telaInformacion.itemconfig(15, fill='black')

    # Se actualiza la pantalla
    def refrescarPantalla(self):
        # Contador que ayuda a vincular la matrix con el juego
        contador = 1
        for i in self.matrixTablero:
            for j in i:
                if j == 0:
                    self.telaGame.itemconfig(contador, fill='white')
                else:
                    self.telaGame.itemconfig(contador, fill='black')
                contador = contador + 1

    # Este metodo es el encargado de pintar la pantalla de juego
    def pintarLaPantallaJuego(self):
        # Se borra el texto de press barra espaciadora para empezar
        # Se tagea como tablerojuego
        self.lblInformacion.destroy()
        # Se pinta la matrix del tablero
        for i in range(0, 10):
            self.matrixTablero.append([])
            for j in range(0, 20):
                x0 = 100 + (i*25)
                y0 = 10 + (j*25)
                self.telaGame.update()
                self.telaGame.create_rectangle(x0, y0, x0+25, y0+25, tag="tablerojuego")
                # Se actualiza la matrix que controla el juego
                self.matrixTablero[i].append(0)
                
        # La pantalla se pinto por ello se puede jugar ahora
        self.modoJuego = 1

    # Se procede a insertar las piezas del juego
    def generarListaDePiezas(self):
        a = [[1,1],[1,1]]
        b = [[1,1,1,1]]
        c = [[1,1,1], [0,1,0]]
        d = [[1,1,1], [0,0,1]]
        e = [[1,1,1], [1,0,0]]
        f = [[0,1], [1,1], [1,0]]
        g = [[1,0], [1,1], [0,1]]

        return [a, b, c, d, e, f]

    def presionaTecla(self, Event):
        if Event.keysym == "Up":
            print('Arriba')
        if Event.keysym == "Down":
            print('Abajo')
        if Event.keysym == "Right":
            print('Derecha')
        if Event.keysym == "Left":
           self.mov_izq()

        if Event.keysym == "space":
            if not self.starGame:
                self.starGame = True
                self.game.start()
                print('Empieza el Juego')

    # Hilo de ejecucion
    def run(self):
        while self.starGame:

            if self.modoJuego == 0:
                self.pintarLaPantallaJuego()

            if self.modoJuego == 1:
                # Se procede a refrescar lo que hay en pantalla
                self.refrescarPantalla()
                # Si la pieza no esta callendo se procede a actualizar
                if not self.piezaCallendo:
                    # Se actualiza cual sera la sig pieza
                    self.cualSigPieza()
                    # Se procede a actualizar la miniatura
                    self.actualizarMiniatura()
                    # Se proce a ponerla en el tablero
                    self.piezaActual_x = 4
                    self.piezaActual_y = 0
                    self.piezaActual = self.listaDePiezas[self.IDsigPieza]
                    # Procede a pintar esa pieza
                    self.ponerPieza()
                    # Se procede a ponerla como callendo
                    self.piezaCallendo = True
                else:
                    self.ponerPieza()


            time.sleep(0)

# Instancia
sw = SW()