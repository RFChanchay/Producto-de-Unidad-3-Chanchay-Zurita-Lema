import time #Importacion de libreria time
import RPi.GPIO as GPIO#Importacion de libreria GPIO

# Clase Bomba para el sistema de riego
class Bomba():
    estado=0#atributo

    def __init__(self, estado):#CONSTRUCTOR
        self.estado = estado

    def apagado(self):#FUNCION PARA APAGAR LA BOMBA
        GPIO.output(8,GPIO.LOW)

    def encendido(self):#FUNCION PARA ENCENDER LA bOMBA
        GPIO.output(8,GPIO.HIGH)

    def analizar(self):# FUNCION PARA ANALIZAR EL ESTADO DE NUESTRAS ENTRADAS
        #AL USAR LOGICA BOOLEANA DEBEMOS CREAR UNA FUNCION QUE LEA NUESTRAS ENTRADAS Y LES ASUMA VALORES REALES
        #EN ESTE CASO LE DAREMOS VALORES DE ENTEROS A CADA ENTRADA RELACIONANDOLO CON CADA VALOR DE BIT EN UN SISTEMA POSICIONAL
        #PARA EL MENOS SIGNIFICATIVO SERA 1 Y PARA EL MAS SIGNIFICATIVO 8 SEGUN EL VALOR DE BIT 2^N
        #SI SE DETECTA UNA ENTRADA ALTA SE IRAN SUMANDO VALORES A LA VARIABLE SELECCIONADOR QUE SERA ENVIADA A OTRA FUNCION
        seleccionador=0
        if GPIO.input(7) == GPIO.HIGH:
            seleccionador= seleccionador+1
        if GPIO.input(11) == GPIO.HIGH:
            seleccionador= seleccionador+2
        if GPIO.input(13) == GPIO.HIGH:
            seleccionador= seleccionador+4
        if GPIO.input(15) == GPIO.HIGH:
            seleccionador= seleccionador+8
        return seleccionador #retorno

    def casos(self,caso):#SELECCIONADOR DE CASOS
    #LA FUNCION RECIBIRA UN PARAMETRO DEL CASO BOOLEANO ANTERIORMENTE ANALIZADO SEGUN EL ESTADO DE LOS PINES
    #MEDIANTE LA FUNCION MENSAJE IMPRIMIRA EL ESTADO EN EL QUE SE ENCUENTRA CADA SENSOR
    #SEGUN EL CASO ENCENDERA O APAGARA NUESTRA SALIDA
    #SE TENDRA UNICAMENTE 16 CASOS DEL 0 AL 15 AL CONTAR UNICAMENTE CON 4 VARIABLES

        if caso==0:
            self.mensaje("Tierra Humeda")
            self.mensaje("Deposito de agua lleno")
            self.mensaje("Calendario sin restricciones")
            self.mensaje("Es de noche")
            self.mensaje("Bomba de riego: Desactivada")
            self.apagado()

        elif caso==1:
            self.mensaje("Tierra Humeda")
            self.mensaje("Deposito de agua lleno")
            self.mensaje("Calendario sin restricciones")
            self.mensaje("Es de dia")
            self.mensaje("Bomba de riego: Desactivada")
            self.apagado()


        elif caso==2:
            self.mensaje("Tierra Humeda")
            self.mensaje("Deposito de agua lleno")
            self.mensaje("Calendario con restricciones")
            self.mensaje("Es de noche")
            self.mensaje("Bomba de riego: Desactivada")
            self.apagado()

        elif caso==3:
            self.mensaje("Tierra Humeda")
            self.mensaje("Deposito de agua lleno")
            self.mensaje("Calendario con restricciones")
            self.mensaje("Es de dia")
            self.mensaje("Bomba de riego: Desactivada")
            self.apagado()

        elif caso==4:
            self.mensaje("Tierra Humeda")
            self.mensaje("Deposito de agua vacio")
            self.mensaje("Calendario sin restricciones")
            self.mensaje("Es de noche")
            self.mensaje("Bomba de riego: Desactivada")
            self.apagado()

        elif caso==5:
            self.mensaje("Tierra Humeda")
            self.mensaje("Deposito de agua vacio")
            self.mensaje("Calendario sin restricciones")
            self.mensaje("Es de dia")
            self.mensaje("Bomba de riego: Desactivada")
            self.apagado()


        elif caso==6:
            self.mensaje("Tierra Humeda")
            self.mensaje("Deposito de agua vacio")
            self.mensaje("Calendario con restricciones")
            self.mensaje("Es de noche")
            self.mensaje("Bomba de riego: Desactivada")
            self.apagado()

        elif caso==7:
            self.mensaje("Tierra Humeda")
            self.mensaje("Deposito de agua vacio")
            self.mensaje("Calendario con restricciones")
            self.mensaje("Es de dia")
            self.mensaje("Bomba de riego: Desactivada")
            self.apagado()


        elif caso==8:
            self.mensaje("Tierra Seca")
            self.mensaje("Deposito de agua lleno")
            self.mensaje("Calendario sin restricciones")
            self.mensaje("Es de noche")
            self.mensaje("Bomba de riego: Activada")
            self.encendido()
        elif caso==9:
            self.mensaje("Tierra Seca")
            self.mensaje("Deposito de agua lleno")
            self.mensaje("Calendario sin restricciones")
            self.mensaje("Es de dia")
            self.mensaje("Bomba de riego: Activada")
            self.encendido()
        elif caso==10:
            self.mensaje("Tierra Seca")
            self.mensaje("Deposito de agua lleno")
            self.mensaje("Calendario con restricciones")
            self.mensaje("Es de noche")
            self.mensaje("Bomba de riego: Activada")
            self.encendido()


        elif caso==11:
            self.mensaje("Tierra Seca")
            self.mensaje("Deposito de agua lleno")
            self.mensaje("Calendario con restricciones")
            self.mensaje("Es de dia")
            self.mensaje("Bomba de riego: Desactivada")
            self.apagado()
        elif caso==12:
            self.mensaje("Tierra Seca")
            self.mensaje("Deposito de agua vacio")
            self.mensaje("Calendario sin restricciones")
            self.mensaje("Es de noche")
            self.mensaje("Bomba de riego: Desactivada")
            self.apagado()

        elif caso==13:
            self.mensaje("Tierra Seca")
            self.mensaje("Deposito de agua vacio")
            self.mensaje("Calendario sin restricciones")
            self.mensaje("Es de dia")
            self.mensaje("Bomba de riego: Desactivada")
            self.apagado()

        elif caso==14:
            self.mensaje("Tierra Seca")
            self.mensaje("Deposito de agua vacio")
            self.mensaje("Calendario con restricciones")
            self.mensaje("Es de noche")
            self.mensaje("Bomba de riego: Desactivada")
            self.apagado()

        elif caso==15:
            self.mensaje("Tierra Seca")
            self.mensaje("Deposito de agua vacio")
            self.mensaje("Calendario con restricciones")
            self.mensaje("Es de dia")
            self.mensaje("Bomba de riego: Desactivada")
            self.apagado()



    def mensaje(self,mens):#FUNCION MENSAJE
    #NOS PERMITE IMPRIMIR UN MENSAJE CUALQUIERA
        print(mens)



class Alarma():# Clase Bomba para el sistema de riego
    estado=0#ATRIBUTO ESTADO

    def __init__(self, estado):#CONSTRUCTOR
        self.estado = estado

    def apagado(self):#FUNCION PARA APAGAR LA BOMBA
        GPIO.output(8,GPIO.LOW)

    def encendido(self):#FUNCION PARA ENCENDER LA bOMBA
        GPIO.output(8,GPIO.HIGH)

    def analizar(self):# FUNCION PARA ANALIZAR EL ESTADO DE NUESTRAS ENTRADAS
        #AL USAR LOGICA BOOLEANA DEBEMOS CREAR UNA FUNCION QUE LEA NUESTRAS ENTRADAS Y LES ASUMA VALORES REALES
        #EN ESTE CASO LE DAREMOS VALORES DE ENTEROS A CADA ENTRADA RELACIONANDOLO CON CADA VALOR DE BIT EN UN SISTEMA POSICIONAL
        #PARA EL MENOS SIGNIFICATIVO SERA 1 Y PARA EL MAS SIGNIFICATIVO 8 SEGUN EL VALOR DE BIT 2^N
        #SI SE DETECTA UNA ENTRADA ALTA SE IRAN SUMANDO VALORES A LA VARIABLE SELECCIONADOR QUE SERA ENVIADA A OTRA FUNCION
        seleccionador=0
        if GPIO.input(7) == GPIO.HIGH:
            seleccionador= seleccionador+1
        if GPIO.input(11) == GPIO.HIGH:
            seleccionador= seleccionador+2
        if GPIO.input(13) == GPIO.HIGH:
            seleccionador= seleccionador+4
        if GPIO.input(15) == GPIO.HIGH:
            seleccionador= seleccionador+8
        return seleccionador

    def casos(self,caso):#SELECCIONADOR DE CASOS
    #LA FUNCION RECIBIRA UN PARAMETRO DEL CASO BOOLEANO ANTERIORMENTE ANALIZADO SEGUN EL ESTADO DE LOS PINES
    #MEDIANTE LA FUNCION MENSAJE IMPRIMIRA EL ESTADO EN EL QUE SE ENCUENTRA CADA SENSOR
    #SEGUN EL CASO ENCENDERA O APAGARA NUESTRA SALIDA
    #SE TENDRA UNICAMENTE 16 CASOS DEL 0 AL 15 AL CONTAR UNICAMENTE CON 4 VARIABLES
        if caso==0:
            self.mensaje("Sin gases")
            self.mensaje("Sin humo")
            self.mensaje("Temperatura inferior a 45 grados")
            self.mensaje("Alarma: Desactivada")
            self.apagado()

        elif caso==1:
            self.mensaje("Se detectaron gases")
            self.mensaje("Sin humo")
            self.mensaje("Temperatura inferior a 45 grados")
            self.mensaje("Alarma: Desactivada")
            self.apagado()


        elif caso==2:
            self.mensaje("Sin gases")
            self.mensaje("Se detecto humo")
            self.mensaje("Temperatura inferior a 45 grados")
            self.mensaje("Alarma: Desactivada")
            self.apagado()

        elif caso==3:
            self.mensaje("Se detectaron gases")
            self.mensaje("Se detecto humo")
            self.mensaje("Temperatura inferior a 45 grados")
            self.mensaje("Alarma: Activada")
            self.encendido()

        elif caso==4:
            self.mensaje("Sin gases")
            self.mensaje("Sin humo")
            self.mensaje("Temperatura superior a 45 grados")
            self.mensaje("Temperatura inferior a 60 grados")
            self.mensaje("Alarma: Desactivada")
            self.apagado()

        elif caso==5:
            self.mensaje("Se detectaron gases")
            self.mensaje("Sin humo")
            self.mensaje("Temperatura superior a 45 grados")
            self.mensaje("Temperatura inferior a 60 grados")
            self.mensaje("Alarma: Activada")
            self.encendido()


        elif caso==6:
            self.mensaje("Sin gases")
            self.mensaje("Se detecto humo")
            self.mensaje("Temperatura superior a 45 grados")
            self.mensaje("Temperatura inferior a 60 grados")
            self.mensaje("Alarma: Activada")
            self.encendido()

        elif caso==7:
            self.mensaje("Se detectaron gases")
            self.mensaje("Se detecto humo")
            self.mensaje("Temperatura superior a 45 grados")
            self.mensaje("Temperatura inferior a 60 grados")
            self.mensaje("Alarma: Activada")
            self.encendido()


        elif caso==8:
            self.mensaje("Sin gases")
            self.mensaje("Sin humo")
            self.mensaje("Temperatura superior a 60 grados")
            self.mensaje("Alarma: Activada")
            self.encendido()
        elif caso==9:
            self.mensaje("Se detectaron gases")
            self.mensaje("Sin humo")
            self.mensaje("Temperatura superior a 60 grados")
            self.mensaje("Alarma: Activada")
            self.encendido()
        elif caso==10:
            self.mensaje("Sin gases")
            self.mensaje("Se detecto humo")
            self.mensaje("Temperatura superior a 60 grados")
            self.mensaje("Alarma: Activada")
            self.encendido()


        elif caso==11:
            self.mensaje("Se detectaron gases")
            self.mensaje("Se detecto humo")
            self.mensaje("Temperatura superior a 60 grados")
            self.mensaje("Alarma: Activada")
            self.encendido()
        elif caso==12:
            self.mensaje("Sin gases")
            self.mensaje("Sin humo")
            self.mensaje("Temperatura superior a 60 grados")
            self.mensaje("Alarma: Activada")
            self.encendido()

        elif caso==13:
            self.mensaje("Se detectaron gases")
            self.mensaje("Sin humo")
            self.mensaje("Temperatura superior a 60 grados")
            self.mensaje("Alarma: Activada")
            self.encendido()

        elif caso==14:
            self.mensaje("Sin gases")
            self.mensaje("Se detecto humo")
            self.mensaje("Temperatura superior a 60 grados")
            self.mensaje("Alarma: Activada")
            self.encendido()

        elif caso==15:
            self.mensaje("Se detectaron gases")
            self.mensaje("Se detecto humo")
            self.mensaje("Temperatura superior a 60 grados")
            self.mensaje("Alarma: Activada")
            self.encendido()



    def mensaje(self,mens):#FUNCION MENSAJE
    #NOS PERMITE IMPRIMIR UN MENSAJE CUALQUIERA
        print(mens)


class Seleccion():#CLASE SELECCION PARA ELEGIR EL MODO DE FUNCIONAMIENTO
    seleccion=0#ATRIBUTO

    def __init__(self, seleccion):#CONSTRUCTOR
        self.seleccion = seleccion

    def iniciarGPIO(self):#FUNCION PARA INICIAR LA GPIO
        GPIO.setmode(GPIO.BOARD)#ACTIVAR GPIO
        #ENTRADAS
        GPIO.setup(7,GPIO.IN)
        GPIO.setup(11,GPIO.IN)
        GPIO.setup(13,GPIO.IN)
        GPIO.setup(15,GPIO.IN)
        GPIO.setup(19,GPIO.IN)
        #SALIDA
        GPIO.setup(8,GPIO.OUT)

    def tempo(self):#FUNCION PARA MOSTRAR UN MENSAJE INICIAL
    #CADA MENSAJE SE MOSTRARA CON UN TIEMPO DE 1 SEGUNDO
    #ESTE TIEMPO SERA PARA QUE EL USUARIO PUEDA ESCOJER EL MODO DE FUNCIONAMIENTO ADECUADO
        print("****Bienvenido*****")
        time.sleep(1)
        print("****Sistema Automatico de Alarma*****")
        time.sleep(1)
        print("Selecione metodo de operacion en el interruptor (GPIO19)")
        time.sleep(1)
        print("Bombas de Agua (0) ")
        print("Alarma contra incendios (1)")
        time.sleep(1)
        print("Dispone de 15 segundos ")
        time.sleep(1)
        #CONTADOR REGRESIVO PARA SELECCIONAR EL MODO DE OPERACION
        for i in range(15):
            print(15-i)
            time.sleep(1)


    def elegir(self):#FUNCION PARA SELECCIONAR EL MODO DE OPERACION
    #LA VARIABLE SELECT NOS SABER QUE MODO DE OPERACION ESCOJIO EL USUARIO
    #SE LEERA EL PUERTO 13 Y DEPENDIENDO DE SU ESTADO SE ALMACENARA UN VALOR DE 1 O 0 EN SELECT PARA QUE SE EJECUTE UNO DE LOS 2 PROGRAMAS
        select=0
        if GPIO.input(19) == GPIO.HIGH:
            select=0
        if GPIO.input(19) == GPIO.HIGH:
            select=1
        return select

#PROGRAMA PRINCIPAL

seleccion=Seleccion(0)#INICIAMOS LA CLASE SELECCION
alarma=Alarma(0)#INICIAMOS LA CLASE ALARMA
bomba=Bomba(0)#INICIAMOS LA CLASE ALARMA

seleccion.iniciarGPIO()#LLAMAMOS A LA FUNCION INICIAR GPIO
seleccion.tempo()#MOSTRAMOS EL MENSAJE INICIAL
sele=seleccion.elegir()#MANDAMOS AL PROGRAMA A LEER EL PIN DESTINADO AL MODO DE FUNCIONAMIENTO

if sele==0:#CASO PARA LA BOMBA DE AGUA
    bomba.mensaje("MODO BOMBA DE AGUA")#MOSTRAMOS UN MENSAJE INICIAL
    aux=100#VARIABLE AUXILIAR QUE NOS AYUDARA EN UN CASO INICIAL
    while 1:#BUCLE REPETITIVO
        caso=bomba.analizar()#LLAMAMOS AL ANALISIS DE PUERTOS Y EL VALOR ENTERO DE LOS PUERTOS SE ALMACENA EN LA VARIABLE CASO
        if caso!=aux:#COMPARAMOS EL CASO CON RESPECTO A LA VARIABLE AUXILIAR QUE PARA LA PRIMERA LECTURA SE VA A CUMPLIR
        #ESTA FUNCION NOS SERA UTIL MARA NO MANDAR EXCESIVOS DATOS A LA CONSOLA YA QUE UNICAMENTE EN CASO DE CAMBIAR DE ESTADO LAS ENTRADAS
        #SE CAMBIARA LOS DATOS DE LA CONSOLA Y LA SALIDA
            bomba.mensaje("----------")
            bomba.casos(caso)#LLAMAMOS A LA FUNCION QUE EFECTUARA NUESTRO CASO
        aux=caso#GUARDAMOS A LA VARIABLE AUX EL CASO ACTUAL PARA QUE NUESTRA CONSOLA NO CAMBIE
elif sele==1:#CASO PARA LA ALARMA
    alarma.mensaje("MODO ALARMA DE INCENDIOS")#MOSTRAMOS UN MENSAJE INICIAL
    aux=100#VARIABLE AUXILIAR QUE NOS AYUDARA EN UN CASO INICIAL
    while 1:#BUCLE REPETITIVO
        caso=alarma.analizar()#LLAMAMOS AL ANALISIS DE PUERTOS Y EL VALOR ENTERO DE LOS PUERTOS SE ALMACENA EN LA VARIABLE CASO
        if caso!=aux:#COMPARAMOS EL CASO CON RESPECTO A LA VARIABLE AUXILIAR QUE PARA LA PRIMERA LECTURA SE VA A CUMPLIR
        #ESTA FUNCION NOS SERA UTIL MARA NO MANDAR EXCESIVOS DATOS A LA CONSOLA YA QUE UNICAMENTE EN CASO DE CAMBIAR DE ESTADO LAS ENTRADAS
        #SE CAMBIARA LOS DATOS DE LA CONSOLA Y LA SALIDA
            alarma.mensaje("----------")
            alarma.casos(caso)#LLAMAMOS A LA FUNCION QUE EFECTUARA NUESTRO CASO
        aux=caso#GUARDAMOS A LA VARIABLE AUX EL CASO ACTUAL PARA QUE NUESTRA CONSOLA NO CAMBIE
