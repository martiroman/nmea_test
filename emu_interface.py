# Crea una interfaz emulada del puerto serie
# Escuha en el puerto definido una conexion serial

import os
import pty
import tty
import select
from server import server
import matplotlib.pyplot as plt

master, slave = pty.openpty()
pty_device = '/dev/ttyS50'
os.symlink(os.ttyname(slave), pty_device)

print(f"Emulacion puerto serie: {pty_device}")

latitudes = []
longitudes = []
# Monitorear la entrada en el dispositivo emulado
try:
    while True:
        rlist, _, _ = select.select([master], [], [])
        if master in rlist:
            data = os.read(master, 1024)
            data_decode = data.decode()

            lat, lon = server(data_decode)
            if lat > -1:
              latitudes.append(lat)
              longitudes.append(lon)

except KeyboardInterrupt:
    print(f"\nFinalizando emulacion puerto serie: {pty_device}")
except Exception as e:
    print(f"\nError: {e}")
finally:
    os.unlink(pty_device)  
    plt.plot(longitudes, latitudes)
    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.title('Trayectoria GPS')
    plt.show()
    plt.savefig('grafico.png')
