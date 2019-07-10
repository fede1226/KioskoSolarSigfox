from sigfoxapi import Sigfox
import time
s = Sigfox('5d0039c8c563d67583a346ef', 'b3aad36ef40d3a55246f567bc35b4638')#Se define el login y la contraseña de la API.
RESPUESTA=s.device_messages('4D1085') #Se ingresa el ID del dispositivo que se quiere recoger la información.
resp=RESPUESTA[0] # Se revisa el último mensaje.
print(resp['data']) #Último mensaje mandado.
print('time')
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(resp['time']))) #Tiempo del último mensaje mandado.

my_hexdata = resp['data']
scale = 16 ## equals to hexadecimal
num_of_bits = 8
binario=bin(int(my_hexdata, scale))[2:].zfill(num_of_bits*4)
print(binario)
line = binario
n = 8
datos_bytes=[line[i:i+n] for i in range(0, len(line), n)]
ultimaResp=resp
# print('Temperatura: '+str(int(datos_bytes[0],2)))
# print('Velocidad del viento: '+str(int(datos_bytes[1],2)))
# print('Voltaje: '+str(int(datos_bytes[2],2)))
# print('Corriente: '+str(int(datos_bytes[3],2)))

while True:
	RESPUESTA=s.device_messages('4D1085') #Se ingresa el ID del dispositivo que se quiere recoger la información.
	resp=RESPUESTA[0] # Se revisa el último mensaje.
	if int(resp['time']) != int(ultimaResp['time']):
		print('Base de datos actualizada con el último valor')
	else:
		print('No hay datos nuevos')
	time.sleep(10) 