
from modelo import modelo_area
from vista import vista_ejercicios
import math
class controlador_ejercicio:
    def __init__(self,objmodelo,objvista) :
        self.objmodelo=objmodelo
        self.objvista=objvista
    def tomar_datos(self):    
        datos_rectangulo=self.objvista.obtener_datos()
        self.objmodelo.set_altura(datos_rectangulo[1])
        self.objmodelo.set_base(datos_rectangulo[0])
        self.calcular_area(datos_rectangulo[0],datos_rectangulo[1])   


    def calcular_area(self,altura,base):
        area= base*altura 
        self.objmodelo.set_area(area)
        self.objvista.mostrar_resultado(area)
        return True
    

    # controlador area del circulo
    def tomar_datoscirculo(self):
        datos_circulo=self.objvista.obtenerdatoscirculo()
        self.objmodelo.set_radio(datos_circulo[0])
      
        self.calcular_areacirculo(datos_circulo[0])
    
    def calcular_areacirculo(self,radio):
        area_circulo= 3.1416 * radio ** 2
        self.objmodelo.set_areacirculo(area_circulo)
        self.objvista.mostrar_rasultadocirculo(area_circulo)
        return True
    

    #controlador celsius a faherent
    def tomar_datocelsius(self):
        datos_celsius=self.objvista.obtenerdatosfaherent()
        self.objmodelo.set_faherent(datos_celsius[0])
        self.calcular_afaherent(datos_celsius[0])
        
   
    def calcular_afaherent(self,celsiu):
        faherent=1.8 * celsiu +32
        self.objmodelo.set_faherent(faherent)
        self.objvista.mostrar_resusltado_faherent(faherent)
        return True
    
    #controlador area trapecio
    def tomar_datos_trapecio(self):
        datos_trapecio=self.objvista.obtenerdatos_trapecio()
        self.objmodelo.set_basemenor(datos_trapecio[2])
        self.objmodelo.set_basemayor(datos_trapecio[1])
        self.objmodelo.set_altura(datos_trapecio[0])
        self.calcular_trapecio(datos_trapecio[0],datos_trapecio[1],datos_trapecio[2])
   
    def calcular_trapecio(self,basemenor,basemayor,alturas):
        trapecio= (basemenor+basemayor)*alturas/2
        self.objmodelo.set_area_trapecio(trapecio)
        self.objvista. mostrar_trapecio(trapecio)
        return True
    
    #controlador kilometros-milla
    def tomar_datos_millas(self):
        datos_millas=self.objvista.obtener_datoskilometros()
        self.objmodelo.set_kilometros(datos_millas[0])
        self.calcilar_milla(datos_millas[0])
    
    def calcilar_milla(self,kilometro):
        milla=kilometro/1.60934
        self.objmodelo.set_milla(milla)
        self.objvista.mostrar_millas(milla)
        return True
    
    #controlador piramede
    def tomar_datos_piramede(self):
        datos_piramede=self.objvista.obtener_datos_piramede()
        self.objmodelo.set_area(datos_piramede[2])
        self.objmodelo.set_base(datos_piramede[1])
        self.objmodelo.set_altura(datos_piramede[0])
        self.calcular_piramede(datos_piramede[0],datos_piramede[1],datos_piramede[2])
   
        
    def calcular_piramede(self,area,base,altura):
        piramede= int(area*base)*altura/3
        self.objmodelo.set_piramede(piramede)
        self.objvista.mostrar_piramede(piramede)
        return True
    
    #controlador paralelogramo
    def tomar_datos_paralelogramo(self):
        datos_paralelgramo=self.objvista.obtener_datosparalelogramo()
        self.objmodelo.set_base(datos_paralelgramo[1])
        self.objmodelo.set_altura(datos_paralelgramo[0])
        self.calcular_datosparalelogramo(datos_paralelgramo[0],datos_paralelgramo[1])
        
    
    def calcular_datosparalelogramo(self,base,altura):
        paralelogramo=base*altura
        self.objmodelo.set_paralelogramo(paralelogramo)
        self.objvista.mostrar_paralelogramo(paralelogramo)
        return True
    
    #conrolador libra-kilogramo
    def tomar_datos_libra(self):
        dato_kilogramo=self.objvista.obtener_datoslibra()
        self.objmodelo.set_libra(dato_kilogramo[0])
        self.calcular_kilogramo(dato_kilogramo[0])
    

    def calcular_kilogramo(self,libra):
        kilogramo=libra/2.2046
        self.objmodelo.set_kilogramo(kilogramo)
        self.objvista.mostrar_kilogramo(kilogramo)  
        return True
    
    #controlador primsa
    def tomar_dato_prisma(self):
        dato_prisma=self.objvista.obtener_datos_prisma()
        self.objmodelo.set_base(dato_prisma[2])
        self.objmodelo.set_area(dato_prisma[1])
        self.objmodelo.set_altura(dato_prisma[0])
        self.calcualr_prisma(dato_prisma[0],dato_prisma[1],dato_prisma[2])
   
    def calcualr_prisma(self,base,area,altura):
        prisma=(base*area)*altura/2
        self.objmodelo.set_prisma(prisma)
        self.objvista.mostrar_prisma(prisma)
        return True
    
    #controlador suma
    def tomar_dato_suma(self):
        dato_suma=self.objvista.obtener_datossuma()
        self.objmodelo.set_numerouno(dato_suma[1])
        self.objmodelo.set_numerodos(dato_suma[0])
        self.calcular_suma(dato_suma[0],dato_suma[1])
   
    def calcular_suma(self,numerouno,numerodos):
        suma=numerouno+numerodos
        self.objvista.mostrar_suma(suma)
        self.objmodelo.set_suma(suma)   
        return True
    
    #controlador division
    def tomar_datodivision(self):
        dato_suma=self.objvista.obtebnerdatos_division()
        self.objmodelo.set_numerouno(dato_suma[1])
        self.objmodelo.set_numerodos(dato_suma[0])
        self.calcular_division(dato_suma[0],dato_suma[1])
       
   
    def calcular_division(self,numerouno,numerodos):
        division=numerouno/numerodos
        self.objvista.mostrar_datosdivison(division)
        self.objmodelo.set_division(division)
        return True
    
    #controlador raiz
    def tomar_dato_raiz(self):
        dato_raiz=self.objvista.obtenerdatosraiz()
        self.objmodelo.set_numerouno(dato_raiz[0])
        self.calcular_raiz(dato_raiz[0])
   
        
    def calcular_raiz(self,raiz):
        raiz_cuadrada=math.sqrt(raiz) 
        self.objvista.mostrar_datoraiz(raiz_cuadrada)
        self.objmodelo.set_raiz(raiz_cuadrada)
        return True   
    
    #controlador circuferencia
    def tomar_dato_circuferencia(self):
        dato_curcuferencia=self.objvista.obtener_datocircuferencia()
        self.objmodelo.set_numerouno(dato_curcuferencia[0])
        self.calcular_circuferencia(dato_curcuferencia[0])
   
    def calcular_circuferencia(self,numerouno):
        circuferencia=3.1416 * (numerouno*2)    
        self.objvista.mostrar_circufrencia(circuferencia)
        self.objmodelo.set_circuferencia(circuferencia)
        return True
    
    #controlador hora a minutos
    def tomar_dato_hora(self):
        dato_minuto=self.objvista.obtener_dato_hora()
        self.objmodelo.set_hora(dato_minuto[0])
        self.calcular_minutos(dato_minuto[0])

   
    def calcular_minutos(self,hora):
        minu=hora*60
        self.objvista.mostrar_hora(minu)
        self.objmodelo.set_minuto(minu)
        return True
    
    #controlador multiplo
    def tomar_daro_multiplo(self):
        dato_multiplo=self.objvista.obtner_dato_multiplo()
        self.objmodelo.set_numerouno(dato_multiplo[1])
        self.objmodelo.set_numerodos(dato_multiplo[0])
        self.calcular_multiplo(dato_multiplo[0],dato_multiplo[1])

    
    def calcular_multiplo(self,nuuno,nudos):
        nuuno=self.objmodelo.get_numuno()
        nudos=self.objmodelo.get_nudos()
        multiplo=self.sisonmultiplo(nuuno,nudos)
        self.objmodelo.set_multiplo(multiplo)
        self.objvista.mostrar_multiplo(multiplo)
        return True



    def sisonmultiplo(self,nuuno,nudos):
       if nuuno % nudos == 0 or nudos % nuuno == 0:
            return "son múltiplos"
       else:
            return "no son múltiplos"
            

    #controlador promedio
    def tomar_dato_promedio(self):
        dato_promeido=self.objvista.obtner_dato_promedio()
        self.objmodelo.set_numerouno(dato_promeido[1])  
        self.objmodelo.set_numerodos(dato_promeido[0])
        self.calcular_promedio(dato_promeido[0],dato_promeido[1])

    def calcular_promedio(self,nuuno,nudos):
        promedio=(nuuno+nudos)/2
        self.objvista.mostrar_promedio(promedio)
        self.objmodelo.set_promedio(promedio)
        return True  
      
     

objmodelo=modelo_area()
objvista=vista_ejercicios()
objcontrolador=controlador_ejercicio(objmodelo,objvista)
objvista.boton_rectangulo.config(command=objcontrolador.tomar_datos)
objvista.boton_circulo.config(command=objcontrolador.tomar_datoscirculo)
objvista.boton_celsius.config(command=objcontrolador.tomar_datocelsius)
objvista.boton_trapecio.config(command=objcontrolador.tomar_datos_trapecio)
objvista.boton_milla.config(command=objcontrolador.tomar_datos_millas)
objvista.boton_piramede.config(command=objcontrolador.tomar_datos_piramede)
objvista.boton_paralelogramo.config(command=objcontrolador.tomar_datos_paralelogramo)
objvista.boton_libra.config(command=objcontrolador.tomar_datos_libra)
objvista.boton_prisma.config(command=objcontrolador.tomar_dato_prisma)
objvista.boton_suma.config(command=objcontrolador.tomar_dato_suma)
objvista.boton_division.config(command=objcontrolador.tomar_datodivision)
objvista.raiz_division.config(command=objcontrolador.tomar_dato_raiz)
objvista.circuferencia.config(command=objcontrolador.tomar_dato_circuferencia)
objvista.minutos.config(command=objcontrolador.tomar_dato_hora)
objvista.boton_multiplo.config(command=objcontrolador.tomar_daro_multiplo)
objvista.boton_promedio.config(command=objcontrolador.tomar_dato_promedio)

objvista.inicio()


    

        





