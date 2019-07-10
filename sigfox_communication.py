import serial

def completeByte(s):
	if len(s)<8:
		num0=8-len(s)
		k="0"*num0
		resp=k+s
		return(resp)

ser = serial.Serial()
port="COM6"
ser.port=port
ser.baudrate = 9600
ser.timeout=5
ser.open()

Temperatura=19
Humedad=33
VelViento=120
Irradiacion=67

TemperaturaBin=str(bin(Temperatura))[2:]
HumedadBin=str(bin(Humedad))[2:]
VelVientoBin=str(bin(VelViento))[2:]
IrradiacionBin=str(bin(Irradiacion))[2:]


TemperaturaByte=completeByte(TemperaturaBin)
HumedadByte=completeByte(HumedadBin)
VelVientoByte=completeByte(VelVientoBin)
IrradiacionByte=completeByte(IrradiacionBin)

msgBin=TemperaturaByte+HumedadByte+VelVientoByte+IrradiacionByte
print(msgBin)
print(TemperaturaByte)
print(HumedadByte)
print(VelVientoByte)
print(IrradiacionByte)



valores=str(11)
valores_enc=valores.encode(encoding='UTF-8',errors='strict')
msg=b"AT$I="+valores_enc+b"\r"
ser.write(msg)
response =  ser.readline()
print(response)
ser.close()


