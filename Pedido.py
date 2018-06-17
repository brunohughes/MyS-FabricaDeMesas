class Pedido:
    def __init__(self, tipo, velocidad):
        self.tipo = tipo
        self.velocidad = velocidad
        
    def get_tipo(self):
        return self.tipo
    
    def get_vel(self):
        return self.velocidad
    
    def __str__(self):
        return "Pedido - tipo:{}, velocidad: {}".format(self.tipo, self.velocidad)