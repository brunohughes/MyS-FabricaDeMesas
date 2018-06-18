#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#== VARIABLES AUXILIARES
pedidos = []
stockM4=0
stockM6=0
pedidosAtendidos=0
pedidosNOatendidos=0
stockM6=0
minutosRestantes=0 #Contador de minutos restantes en un dia 
minutosXdia = 60*8

solicitudesSinAtender=0
solicitudesAtendidas=0
mesasConstruidasM4=[]
mesasConstruidasM6=[]
tiemposOperarios=[]

class Simulacion():
    def __init__(self):
    	pass

def procesar(self, exp, dias, incM4, incM6, velM4, velM6):
	for i in range(exp):
	    for dia in range(dias):
	        minutosRestantes = minutosXdia
	        mesasConstruidasM4.append(0)
	        mesasConstruidasM6.append(0)
	        tiemposOperarios.append(0)
	        
	        #Incremento el stock los primeros N dias
	        if (dia < 10):
	            stockM4=+incrementoStockM4
	            stockM6=+incrementoStockM6
	        
	        #Armo una lista con elemntos M4 y M6
	        for _ in range(50):
	            pedidos.append(Pedido(tipo='M4', velocidad=np.random.poisson(20)))
	        for _ in range(30):    
	            pedidos.append(Pedido(tipo='M6', velocidad=np.random.poisson(10)))
	    
	    
	        #Desordeno lista para no atender siempre las M4 primero
	        np.random.shuffle(pedidos)    
	        
	        #Recorro la lista de solicitudes
	        for item in pedidos:   
	            if (minutosRestantes > 0):
	                if (item.tipo == 'M4'):                
	                    if (stockM4 > 0):
	                        #Decrementar stock M4
	                        stockM4 -= 1
	                        
	                        #Esperar tiempo de Operador. Se resta al tiempo disponible                    
	                        tiempoEspera = np.random.exponential(scale=velOperM4)
	                        minutosRestantes -= tiempoEspera
	                        
	                        #Contabilizar tiempo de Operarios (espera)
	                        tiemposOperarios[dia] += tiempoEspera
	                        
	                        #contabilizar solicitudes atendidas (por dia)
	                        solicitudesAtendidas += 1
	                        
	                        #Incrementamos contador de mesas contruidas M4                
	                        mesasConstruidasM4[dia] += 1 
	                        
	                        #Resto al tiempo restante la velocidad de extraccion M4
	                        minutosRestantes -= item.velocidad
	                    
	                    else:                        
	                        solicitudesSinAtender +=1

	                if (item.tipo == 'M6'):                
	                    if (stockM6 > 0):
	                        #Decrementar stock M4
	                        stockM6 -= 1
	                        
	                        #Esperar tiempo de Operador. se resta al tiempo disponible                    
	                        tiempoEspera = np.random.exponential(scale=velOperM6)
	                        minutosRestantes -= tiempoEspera
	                        
	                        #Contabilizar tiempo de Operarios (espera)
	                        tiemposOperarios[dia] += tiempoEspera
	                        
	                        #contabilizar solicitudes atendidas (por dia)
	                        solicitudesAtendidas += 1
	                        
	                        #Incrementamos contador de mesas contruidas M6                
	                        mesasConstruidasM6[dia] += 1 
	                    
	                        #Resto al tiempo restante la velocidad de extraccion M6
	                        minutosRestantes -= item.velocidad
	                        
	                    else:                        
	                        solicitudesSinAtender +=1
	            else: 
	                #Se terminaron los minutos del dia
	                #contabilizar solicitudes NO atendidas (por dia)
	                solicitudesSinAtender +=1
	                
	#RESULTADOS                
	print('PARAMETRO Minutos totales de trabajo diario: ' + str(minutosXdia))
	print('Solicitudes atendidas: ' + str(solicitudesAtendidas))
	print('Solicitudes NO atendidas: ' + str(solicitudesSinAtender) )

	print('Mesas M4 construidas por dia:')
	for dia in range(DIAS):
	    print('--DIA: %02d' % (dia + 1) + ' cantidad: ' + str(mesasConstruidasM4[dia] )) 

	print('Mesas M6 construidas por dia:')
	for dia in range(DIAS):
	    print('--DIA: %02d' % (dia + 1) + ' cantidad: ' + str(mesasConstruidasM6[dia] )) 

	print('Minutos totales de espera Operarios en Deposito por dia:')
	for dia in range(DIAS):
	    print('--DIA: %02d' % (dia + 1) + ' cantidad: %.0f' % (tiemposOperarios[dia]) ) 
	    