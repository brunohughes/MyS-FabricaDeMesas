class Variable:
    def __init__(self):        
        self.stockM4=0
        self.stockM6=0
        self.minutosRestantes=0 #Contador de minutos restantes en un dia 
        self.minutosXdia = 60*8
        self.mesasConstruidasM4=[]
        self.mesasConstruidasM6=[]
        self.tiemposOperarios=[]
        self.solicitudesAtendidasXMes=[]
        self.solicitudesSinAtenderXMes=[]
        self.solicitudesSinAtender=0
        self.solicitudesAtendidas=0
        self.minutosRestantes=0        
        #Parametros
        self.MES = 0
        self.DIAS = 0
        self.incrementoStockM4 = 0
        self.incrementoStockM6 = 0
        self.velOperM4 = 0
        self.velOperM6 = 0
        self.cantidadM4 = 0
        self.cantidadM6 = 0        
        self.cantDiasProduccion = 0