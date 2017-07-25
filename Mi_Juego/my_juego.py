import pilasengine
import random

pilas = pilasengine.iniciar()
# CREAR EL MENU DEL JUEGO
class EscenaMenu(pilasengine.escenas.Escena):
	def iniciar(self):
		self.fondo_menu = pilas.fondos.Tarde()
		
		##############################################
		self.Mi_Menu = pilas.actores.Menu(
			[
				(u'IR  AL JUEGO', self.Ir_al_juego),
				(u'SALIR ', self.Salir_de_Pilas)
			])
		##############################################
		
		Nombre_de_mi_juego = pilas.actores.Texto(u'RECOGE MONEDAS')
		Nombre_de_mi_juego.color = pilas.colores.rojo
		Nombre_de_mi_juego.y = 170
		
				
	def actualizar(self):
		pass
		
	def Salir_de_Pilas(self): 
		pilas.terminar()	
		
	def Ir_al_juego(self): 
		pilas.escenas.EscenaPrincipal()		

# codigo del juego
class Protagonista(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = "aceituna.png"
        self.figura = pilas.fisica.Circulo(self.x, self.y, 17,
            friccion=0, restitucion=0)

        self.figura.sin_rotacion = True
        self.figura.escala_de_gravedad = 2

        self.sensor_pies = pilas.fisica.Rectangulo(self.x, self.y, 20, 5, sensor=True, dinamica=False)
        self.contador_puede_disparar = 0
        self.direccion = 1

    def actualizar(self):
        velocidad = 10
        salto = 15
        self.x = self.figura.x
        self.y = self.figura.y


        if self.pilas.control.derecha:
            self.figura.velocidad_x = velocidad
            self.rotacion -= velocidad
            self.direccion = 1
        elif self.pilas.control.izquierda:
            self.figura.velocidad_x = -velocidad
            self.rotacion += velocidad
            self.direccion = -1
        else:
            self.figura.velocidad_x = 0

      
        if self.esta_pisando_el_suelo():
            if self.pilas.control.arriba and int(self.figura.velocidad_y) <= 0:
                self.figura.impulsar(0, salto)

        self.sensor_pies.x = self.x
        self.sensor_pies.y = self.y - 20

        if self.esta_pisando_el_suelo():
            self.imagen = "aceituna.png"
        else:
            self.imagen = "aceituna_risa.png"

    def esta_pisando_el_suelo(self):
        return len(self.sensor_pies.figuras_en_contacto) > 0

class Enemigo(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "bomba.png"
        self.escala = 0.3
        self.aprender( pilas.habilidades.PuedeExplotarConHumo )
        self.y = pilas.azar(-200, 200)
        self.x = 290
        self.velocidad = pilas.azar(10, 40) / 10.0

    def actualizar(self):
        self.rotacion += 10
        self.x -= self.velocidad

        # Elimina el objeto cuando sale de la pantalla.
        if self.y < -300:
            self.eliminar()

class Moneda(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "estrella.png"
        self.escala = 0.3
        self.aprender( pilas.habilidades.PuedeExplotarConHumo )
        self.x = pilas.azar(-180, 180)
        self.y = pilas.azar(-180, 180)
        self.velocidad = 0
        self.radio_de_colision = 30

    def actualizar(self):
        self.rotacion += 10
        self.y -= self.velocidad

       

class EscenaPrincipal(pilasengine.escenas.Escena):

    def iniciar(self):

        mapa = pilas.actores.Mapa()
        fondo = pilas.fondos.Tarde()

        #### Hacer Mundo#####
        #bloque1
        mapa.pintar_bloque(12, 3, 1,es_bloque_solido=True)
        mapa.pintar_bloque(12, 4, 1,es_bloque_solido=True)
        mapa.pintar_bloque(12, 5, 1,es_bloque_solido=True)
        mapa.pintar_bloque(12, 6, 1,es_bloque_solido=True)
        # bloque 2
        mapa.pintar_bloque(11, 12, 1, es_bloque_solido=True)
        mapa.pintar_bloque(11, 13, 1, es_bloque_solido=True)
        mapa.pintar_bloque(11, 14, 1, es_bloque_solido=True)
        mapa.pintar_bloque(11, 15, 1, es_bloque_solido=True)
        # bloque 3
        mapa.pintar_bloque(8, 5, 1, es_bloque_solido=True)
        mapa.pintar_bloque(8, 6, 1, es_bloque_solido=True)
        mapa.pintar_bloque(8, 7, 1, es_bloque_solido=True)
        mapa.pintar_bloque(8, 8, 1, es_bloque_solido=True)
        #bloque 4
        mapa.pintar_bloque(6, 12, 1,es_bloque_solido=True)
        mapa.pintar_bloque(6, 13, 1, es_bloque_solido=True)
        mapa.pintar_bloque(6, 14, 1, es_bloque_solido=True)
        mapa.pintar_bloque(6, 15, 1, es_bloque_solido=True)
        # piso de juego
        for columna in range(20):
            mapa.pintar_bloque(17, columna, 1,es_bloque_solido=True)

        #Creacion de p(Protagonista), enemigos y puntos    
        p = self.pilas.actores.Protagonista() 
 
        enemigos = pilas.actores.Grupo()
        monedas = pilas.actores.Grupo()
                        
        #Letrero con puntaje obtenido
        puntos = pilas.actores.Puntaje(x=230, y=200, color=pilas.colores.blanco)
        texto = (puntos.obtener())
        puntos.magnitud = 40

        def crear_enemigo():
            actor = Enemigo(pilas)
            enemigos.agregar(actor)
        #Creacion de enemigos cada 1 segundo
        pilas.tareas.siempre(1, crear_enemigo)

        def crear_moneda():
            actor = Moneda(pilas)
            monedas.agregar(actor)
        #Creacion de monedas cada segundo 
        for x in range (0,10):     
            pilas.tareas.una_vez(1,crear_moneda)
        #evento cuando colisiona p con moneda
        def eliminar_moneda(p, monedas):
            monedas.eliminar()
            puntos.escala = 1
            puntos.aumentar(1)
            
            if puntos.obtener()==10:
                gano()
                
                
      
        #evento cuando colisionan p con enemigos
        def eliminar_enemigo(p, enemigos):
            p.eliminar()
            global fin_de_juego               
            pilas.avisar("GAME OVER. Conseguiste %d puntos" %(puntos.obtener()))
        def gano():
            pilas.avisar(" FELICIDADES GANASTE")
            p.eliminar()
            
                #cuando p colisiona llama un evento para que se produsca
        pilas.colisiones.agregar(p, monedas, eliminar_moneda)
        pilas.colisiones.agregar(p, enemigos, eliminar_enemigo)

pilas.actores.vincular(Protagonista)
pilas.actores.vincular(Enemigo)

pilas.escenas.vincular(EscenaPrincipal)
pilas.escenas.EscenaPrincipal()

pilas.escenas.vincular(EscenaMenu)

pilas.escenas.EscenaMenu()


pilas.ejecutar()
