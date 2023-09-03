import pynmea2
import matplotlib.pyplot as plt

class NMEA:
  """
  Objeto NMEA 
  """

  def __init__(self, data):
    try:
      if data:
        self.data = data
        self.nmeaObj = pynmea2.parse(data)
    except pynmea2.ParseError as e:
      print(f"ParseError: {e}")    

  def __str__(self):
    """
    Imprime todos los atributos del objeto NMEA y del string recibido
    """
    print("\n************************************************************ \n") 
    if self.data:
      print(f"Recibido: {self.data} \n", end="")

    if self.nmeaObj:
     for i in range(len(self.nmeaObj.fields)):
        if i < len(self.nmeaObj.fields) and i < len(self.nmeaObj.data):
          print("\t" + self.nmeaObj.fields[i][0] + " : " + self.nmeaObj.data[i])
    return ""

def server(data):
  """
    Manejo del string NMEA recibido

    :param data: String mensaje NMEA
    :return: El resultado de la operación.
  """
  
  msgNmea = NMEA(data)
  if "$GPGGA" in data:
    lat = float(msgNmea.nmeaObj.data[1])
    lon = float(msgNmea.nmeaObj.data[3])  
    return lat, lon  
  
  return -1, -1


    


