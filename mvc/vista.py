
from tkinter import *
from tkinter import messagebox

class vista_ejercicios:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Área de figuras geométricas")
        self.ventana.config(bg="cyan")
        self.ventana.geometry("400x300")

        # Frame para rectángulo
        rectangulo_frame = LabelFrame(self.ventana, text="Área de un rectángulo", padx=30, pady=10)
        rectangulo_frame.config(bg='deep sky blue')
        rectangulo_frame.grid(row=0, column=0, padx=10, pady=10)

        labealtura = Label(rectangulo_frame, text="Ingrese la altura", width=13)
        labealtura.grid(row=0, column=0, padx=10, pady=10)
        self.altura = Entry(rectangulo_frame)
        self.altura.grid(row=0, column=1, padx=10, pady=10)

        labebase = Label(rectangulo_frame, text="Ingrese la base", width=13)
        labebase.grid(row=1, column=0, padx=10, pady=10)
        self.base = Entry(rectangulo_frame)
        self.base.grid(row=1, column=1, padx=10, pady=10)

        self.boton_rectangulo = Button(rectangulo_frame, text="Calcular área")
        self.boton_rectangulo.grid(row=2, columnspan=2, padx=10, pady=10)

        # Frame para círculo
        circulo_frame = LabelFrame(self.ventana, text="Área de un círculo", padx=30, pady=10)
        circulo_frame.config(bg='deep sky blue')
        circulo_frame.grid(row=1, column=0, padx=10, pady=10)

        laberadio = Label(circulo_frame, text="Ingrese el radio", width=13)
        laberadio.grid(row=0, column=0, padx=10, pady=10)
        self.radio = Entry(circulo_frame)
        self.radio.grid(row=0, column=1, padx=10, pady=10)

        self.boton_circulo = Button(circulo_frame, text="Calcular área")
        self.boton_circulo.grid(row=2, columnspan=2, padx=10, pady=10)
        
        
        #frame celcius a faheren

        celsius_frame=LabelFrame(self.ventana,text="celsius a Fahrenheit",padx=30,pady=10)
        celsius_frame.config(bg='deep sky blue')
        celsius_frame.grid(row=2,column=0,padx=10,pady=10)

        labecelsius=Label(celsius_frame,text="ingrese el numero de ceslsuis",width=27)
        labecelsius.grid(row=0,column=0)
        self.celsiu= Entry(celsius_frame)
        self.celsiu.grid(row=0,column=1,padx=10,pady=10)

        self.boton_celsius= Button(celsius_frame,text="calcular a faherent")
        self.boton_celsius.grid(row=2,columnspan=2,padx=10,pady=10)

        #frame trapecio
        trapecio_frame=LabelFrame(self.ventana,text="calcular area del trapecio",padx=30,pady=10)
        trapecio_frame.config(bg='deep sky blue')
        trapecio_frame.grid(row=3,column=0,padx=10,pady=10)

        labemenor = Label(trapecio_frame, text="Ingrese la base menor", width=16)
        labemenor.grid(row=0, column=0, padx=10, pady=10)
        self.basemenor = Entry(trapecio_frame)
        self.basemenor.grid(row=0, column=1, padx=10, pady=10)

        labemayor = Label(trapecio_frame, text="Ingrese la base mayor", width=16)
        labemayor.grid(row=1, column=0, padx=10, pady=10)
        self.basemayor = Entry(trapecio_frame)
        self.basemayor.grid(row=1, column=1, padx=10, pady=10)

        labealturas = Label(trapecio_frame, text="Ingrese la altura", width=16)
        labealturas.grid(row=2, column=0, padx=10, pady=10)
        self.alturas = Entry(trapecio_frame)
        self.alturas.grid(row=2, column=1, padx=10, pady=10)

        self.boton_trapecio= Button(trapecio_frame,text="calcular trapecio")
        self.boton_trapecio.grid(row=3,columnspan=2,padx=10,pady=10)

        #frame kilometro a millas
        kilometro_frame=LabelFrame(self.ventana,text="conversion de kilometros a millas",padx=30,pady=10)
        kilometro_frame.config(bg='deep sky blue')
        kilometro_frame.grid(row=4,column=0,padx=10,pady=10)

        labelkilometros=Label(kilometro_frame,text="ingrese la cantidad de km",width=20)
        labelkilometros.grid(row=0,column=0,padx=10,pady=10)
        self.kilometro=Entry(kilometro_frame)
        self.kilometro.grid(row=0,column=1,padx=10,pady=10)
        self.boton_milla=Button(kilometro_frame,text="converetir")
        self.boton_milla.grid(row=1,columnspan=2,padx=10,pady=10)

        #frame piramede
        pirademe_frame=LabelFrame(self.ventana,text="area de la piramede",padx=30,pady=10)
        pirademe_frame.config(bg='deep sky blue')
        pirademe_frame.grid(row=0,column=1,padx=10,pady=10)

        labeareapiramede=Label(pirademe_frame,text="ingrese la area",width=16)
        labeareapiramede.grid(row=0,column=0,padx=10,pady=10)
        self.area_piramede=Entry(pirademe_frame)
        self.area_piramede.grid(row=0,column=1,padx=10,pady=10)

        labebasepiramede=Label(pirademe_frame,text="ingrese la base",width=16)
        labebasepiramede.grid(row=1,column=0,padx=10,pady=10)
        self.base_piramede=Entry(pirademe_frame)
        self.base_piramede.grid(row=1,column=1,padx=10,pady=10)

        labealturapiramede=Label(pirademe_frame,text="ingrese la altura")
        labealturapiramede.grid(row=2,column=0,padx=10,pady=10)
        self.altura_piramede=Entry(pirademe_frame)
        self.altura_piramede.grid(row=2,column=1,padx=10,pady=10)

        self.boton_piramede=Button(pirademe_frame,text="calcular")
        self.boton_piramede.grid(row=3,columnspan=2,padx=10,pady=10)

        #frame paralelogramo
        piralelogramo_frame=LabelFrame(self.ventana,text="area del parealelogramo",padx=30,pady=10)
        piralelogramo_frame.config(bg='deep sky blue')
        piralelogramo_frame.grid(row=1,column=1,padx=10,pady=10)

        labebaseparalelogramo=Label(piralelogramo_frame,text="ingrese la base",width=16)
        labebaseparalelogramo.grid(row=0,column=0,padx=10,pady=10)
        self.base_paralelogramo=Entry(piralelogramo_frame)  
        self.base_paralelogramo.grid(row=0,column=1,padx=10,pady=10)

        labealturaparalelogramo=Label(piralelogramo_frame,text="ingrese la altura",width=16)
        labealturaparalelogramo.grid(row=1,column=0,padx=10,pady=10)
        self.altura_paralelogramo=Entry(piralelogramo_frame)
        self.altura_paralelogramo.grid(row=1,column=1,padx=10,pady=10)

        self.boton_paralelogramo=Button(piralelogramo_frame,text="calcular")
        self.boton_paralelogramo.grid(row=2,columnspan=2,padx=10,pady=10)

        #frame libra-kilogramo
        libra_frame=LabelFrame(self.ventana,text="convercion de lb a kg",padx=30,pady=10)
        libra_frame.config(bg='deep sky blue')
        libra_frame.grid(row=2,column=1,padx=10,pady=10)

        labelibra=Label(libra_frame,text="ingrese la cantida de lb",width=16)
        labelibra.grid(row=0,column=0,padx=10,pady=10)
        self.libra=Entry(libra_frame)
        self.libra.grid(row=0,column=1,padx=10,pady=10)

        self.boton_libra=Button(libra_frame,text="convertir")
        self.boton_libra.grid(row=1,columnspan=2,padx=10,pady=10)

        #frame prisma
        prisma_frame=LabelFrame(self.ventana,text="voluemen de un prisma",padx=30,pady=10)
        prisma_frame.config(bg='deep sky blue')
        prisma_frame.grid(row=3,column=1,padx=10,pady=10)

        labeareaprisma=Label(prisma_frame,text="ingrese la area",width=16)
        labeareaprisma.grid(row=0,column=0,padx=10,pady=10)
        self.area_prisma=Entry(prisma_frame)
        self.area_prisma.grid(row=0,column=1,padx=10,pady=10)

        labebaseprisma=Label(prisma_frame,text="ingrese la base",width=16)
        labebaseprisma.grid(row=1,column=0,padx=10,pady=10)
        self.base_prisma=Entry(prisma_frame)
        self.base_prisma.grid(row=1,column=1,padx=10,pady=10)

        labealturaprisma=Label(prisma_frame,text="ingrese la altura")
        labealturaprisma.grid(row=2,column=0,padx=10,pady=10)
        self.altura_prisma=Entry(prisma_frame)
        self.altura_prisma.grid(row=2,column=1,padx=10,pady=10)

        self.boton_prisma=Button(prisma_frame,text="calcular")
        self.boton_prisma.grid(row=3,columnspan=2,padx=10,pady=10)

        #frame suma de dos numeros
        suma_frame=LabelFrame(self.ventana,text="suma",padx=30,pady=10)
        suma_frame.config(bg='deep sky blue')
        suma_frame.grid(row=0,column=2,padx=10,pady=10)

        labeprimernumero=Label(suma_frame,text="ingrese un numero",width=16)
        labeprimernumero.grid(row=0,column=0,padx=10,pady=10)
        self.primernumero=Entry(suma_frame)
        self.primernumero.grid(row=0,column=1,padx=10,pady=10)

        labesegundonumero=Label(suma_frame,text="ingrese otro numero",width=16)
        labesegundonumero.grid(row=1,column=0,padx=10,pady=10)
        self.segundonumero=Entry(suma_frame)
        self.segundonumero.grid(row=1,column=1,padx=10,pady=10)

        self.boton_suma=Button(suma_frame,text="sumar")
        self.boton_suma.grid(row=2,columnspan=2,padx=10,pady=10)

        #frame division

        division_frame=LabelFrame(self.ventana,text="division",padx=30,pady=10)
        division_frame.config(bg='deep sky blue')
        division_frame.grid(row=1,column=2,padx=10,pady=10)

        labenumerouno=Label(division_frame,text="ingrese un numero",width=16)
        labenumerouno.grid(row=0,column=0,padx=10,pady=10)
        self.numerouno=Entry(division_frame)
        self.numerouno.grid(row=0,column=1,padx=10,pady=10)
        labenumerodos=Label(division_frame,text="ingrese el segundo numero",width=16)
        labenumerodos.grid(row=1,column=0,padx=10,pady=10)
        self.numerodos=Entry(division_frame)
        self.numerodos.grid(row=1,column=1,padx=10,pady=10)

        self.boton_division=Button(division_frame,text="calcular")
        self.boton_division.grid(row=2,columnspan=2,padx=10,pady=10)

        #frame
        raiz_frame=LabelFrame(self.ventana,text="raiz cuasdrada",padx=30,pady=10)
        raiz_frame.config(bg='deep sky blue')
        raiz_frame.grid(row=2,column=2,padx=10,pady=10)
        labenumerouno=Label(raiz_frame,text="ingrese un numero",width=16)
        labenumerouno.grid(row=0,column=0,padx=10,pady=10)
        self.numuno=Entry(raiz_frame)
        self.numuno.grid(row=0,column=1,padx=10,pady=10)

        self.raiz_division=Button(raiz_frame,text="calcular")
        self.raiz_division.grid(row=2,columnspan=2,padx=10,pady=10)

        #frame circuferencia
        circuferencia_frame=LabelFrame(self.ventana,text="circuferencia",padx=30,pady=10)
        circuferencia_frame.config(bg='deep sky blue')
        circuferencia_frame.grid(row=3,column=2,padx=10,pady=10)
        labenumerounocircu=Label(circuferencia_frame,text="ingrese el radio",width=16)
        labenumerounocircu.grid(row=0,column=0,padx=10,pady=10)
        self.numunocircu=Entry(circuferencia_frame)
        self.numunocircu.grid(row=0,column=1,padx=10,pady=10)

        self.circuferencia=Button(circuferencia_frame,text="calcular")
        self.circuferencia.grid(row=2,columnspan=2,padx=10,pady=10)

        #frame  hora a minutos
        hora_frame=LabelFrame(self.ventana,text="horas a minutos",padx=30,pady=10)
        hora_frame.config(bg='deep sky blue')
        hora_frame.grid(row=4,column=2,padx=10,pady=10)
        labehora=Label(hora_frame,text="ingrese la horas",width=16)
        labehora.grid(row=0,column=0,padx=10,pady=10)
        self.hora=Entry(hora_frame)
        self.hora.grid(row=0,column=1,padx=10,pady=10)

        self.minutos=Button(hora_frame,text="calcular")
        self.minutos.grid(row=2,columnspan=2,padx=10,pady=10)

        # multiplo uno con otro
        multiplo_frame=LabelFrame(self.ventana,text="multiplo",padx=30,pady=10)
        multiplo_frame.config(bg='deep sky blue')
        multiplo_frame.grid(row=0,column=3,padx=10,pady=10)

        labenuno=Label(multiplo_frame,text="ingrese un numero",width=16)
        labenuno.grid(row=0,column=0,padx=10,pady=10)
        self.nuuno=Entry(multiplo_frame)
        self.nuuno.grid(row=0,column=1,padx=10,pady=10)
        labenudos=Label(multiplo_frame,text="ingrese el segundo numero",width=16)
        labenudos.grid(row=1,column=0,padx=10,pady=10)
        self.nudos=Entry(multiplo_frame)
        self.nudos.grid(row=1,column=1,padx=10,pady=10)

        self.boton_multiplo=Button(multiplo_frame,text="calcular")
        self.boton_multiplo.grid(row=2,columnspan=2,padx=10,pady=10)

        #promedio de dos numeros
        promedio_frame=LabelFrame(self.ventana,text="promedio",padx=30,pady=10)
        promedio_frame.config(bg='deep sky blue')
        promedio_frame.grid(row=1,column=3,padx=10,pady=10)

        labenuno=Label(promedio_frame,text="ingrese un numero",width=16)
        labenuno.grid(row=0,column=0,padx=10,pady=10)
        self.numunoprom=Entry(promedio_frame)
        self.numunoprom.grid(row=0,column=1,padx=10,pady=10)
        labenudos=Label(promedio_frame,text="ingrese el segundo numero",width=16)
        labenudos.grid(row=1,column=0,padx=10,pady=10)
        self.nudosprom=Entry(promedio_frame)
        self.nudosprom.grid(row=1,column=1,padx=10,pady=10)

        self.boton_promedio=Button(promedio_frame,text="calcular")
        self.boton_promedio.grid(row=2,columnspan=2,padx=10,pady=10)

        



       

    #ractangulo

    def obtener_datos(self):
        altura = int(self.altura.get())
        base = int(self.base.get())
        return [altura, base]

    def mostrar_resultado(self, area):
        messagebox.showinfo("Resultado", f"El área del rectángulo es {area}")



    #circulo
    def obtenerdatoscirculo(self):
        radio=int(self.radio.get())
        return [radio]  
    
    def mostrar_rasultadocirculo(self,area_circulo):
        messagebox.showinfo("resulatado", f"el area del circulo es {area_circulo} cm2")  

    #faherent
    def obtenerdatosfaherent(self):
        celsiu=int(self.celsiu.get())
        return [celsiu]
    def mostrar_resusltado_faherent(self,faherent):
        messagebox.showinfo("resultado", f"en faherent es {faherent}  ")       

    #area trapecio
    def obtenerdatos_trapecio(self):
        basemenor=int(self.basemenor.get())
        basemayor=int(self.basemayor.get())
        altura=int(self.alturas.get())
        return [basemenor,basemayor,altura]
    def mostrar_trapecio(self,trapecio):
        messagebox.showinfo("resusltador", f"el area del trapecio es {trapecio} cm2")

    #kilometro-millas
    def obtener_datoskilometros(self):
        kilometro=int(self.kilometro.get())
        return[kilometro]
    def mostrar_millas(self,milla):
        messagebox.showinfo("resulatado", f"en millas son {milla} millas")
    
    #area de la piramede
    def obtener_datos_piramede(self):
        area=int(self.area_piramede.get())
        base=int(self.base_piramede.get())
        altura=int(self.altura_piramede.get())
        return[area,base,altura]
    def mostrar_piramede(self,piramede):
        messagebox.showinfo("resulatado", f"el area de la piramede es {piramede} cm3")

    #area paralelogramo
    def obtener_datosparalelogramo(self):
        base=int(self.base_paralelogramo.get()) 
        altura=int(self.altura_paralelogramo.get())
        return[base,altura]
    def mostrar_paralelogramo(self,paralelogramo):
        messagebox.showinfo("resulatado", f"el area del paralelogramo es {paralelogramo}")   

    def obtener_datoslibra(self):
        libra=int(self.libra.get())
        return[libra]
        
    def mostrar_kilogramo(self,kilogramo):
        messagebox.showinfo("resultado", f"en libras son {kilogramo} kg") 
    
    #valumen de un prisma   
    def obtener_datos_prisma(self):
        area=int(self.area_prisma.get())
        base=int(self.base_prisma.get())
        altura=int(self.altura_prisma.get())
        return[area,base,altura]
    def mostrar_prisma(self,prisma):
        messagebox.showinfo("resultado", f"el volumen del prisma es {prisma} cm3")

    #suma de dos numeros
    def obtener_datossuma(self):
        numerouno=int(self.primernumero.get())  
        numerodos=int(self.segundonumero.get())
        return[numerouno,numerodos]  
    def mostrar_suma(self,suma):
        messagebox.showinfo("resusltado", f"la sumas de los  numeros es {suma}")

    #division    


    def obtebnerdatos_division(self):
        numerouno=int(self.numerouno.get())
        numerodos=int(self.numerodos.get())
        return[numerouno,numerodos]
    def mostrar_datosdivison(self,division):
        messagebox.showinfo("resusltado", f" la division es {division}")  

    # raiz de un numero    

    def obtenerdatosraiz(self):
        numuno=int(self.numuno.get())
        return[numuno]
    def mostrar_datoraiz(self,raiz):
        messagebox.showinfo("resultado", f"la raiz caudrada es {raiz}")

    #circuferencia 

    def obtener_datocircuferencia(self):
        numero=int(self.numunocircu.get())
        return [numero]
    def mostrar_circufrencia(self,circuferencia):
        messagebox.showinfo("resualtado", f" la circuferencia es {circuferencia}")

    # horas a minutos

    def obtener_dato_hora(self):
        hora=int(self.hora.get())
        return[hora]  
    def mostrar_hora(self,minuto):
        messagebox.showinfo("resulatado", f"en minustos son {minuto} minutos")  

    #multiplo
    def obtner_dato_multiplo(self):
        nuuno=int(self.nuuno.get()) 
        nudos=int(self.nudos.get())
        return[nuuno,nudos]
    def mostrar_multiplo(self,multiplo):
        messagebox.showinfo("resultado", f"los dos numeros  {multiplo}")

    #promedio de dos numeros
    def obtner_dato_promedio(self):
        nuunoprom=int(self.numunoprom.get())
        nudosprm=int(self.nudosprom.get()) 
        return [nuunoprom,nudosprm]
    def mostrar_promedio(self,promedio):
        messagebox.showinfo("resulatado", f"el promedio de los dos numeros es  {promedio}")  

    
             

    def inicio(self):
        self.ventana.mainloop()