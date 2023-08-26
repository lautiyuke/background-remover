import os
from datetime import datetime
from rembg import remove

class RemoverFondo:
    def __init__(self, carpeta_entrada, carpeta_salida):
        self.carpeta_entrada = carpeta_entrada
        self.carpeta_salida = carpeta_salida
    
    def process_images(self):
        today = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        carpeta_procesada = os.path.join(self.carpeta_salida, today)
        os.makedirs(carpeta_procesada, True)
        
        for archivo in os.listdir(self.carpeta_entrada):
            if archivo.endswith(('.png', '.jpg', '.jpeg')):
                direccion_entrada = os.path.join(self.carpeta_entrada, archivo)
                direccion_salida = os.path.join(carpeta_procesada, archivo)
                self._eliminar_fondo(direccion_entrada, direccion_salida)
                self._mover_originales(direccion_entrada, carpeta_procesada)
            
    def _eliminar_fondo(self, d_entrada, d_salida):
        with open(d_entrada, 'rb') as ent, open(d_salida, 'wb') as sal:
            fondo_salida = remove(ent.read())
            sal.write(fondo_salida)
    
    def _mover_originales(self, d_entrada, d_salida):
        carpeta_originales = os.path.join(d_salida, 'originales')
        os.makedirs(carpeta_originales, True)
        
        archivo = os.path.basename(d_entrada)
        nueva_direccion = os.path.join(carpeta_originales, archivo)
        os.rename(d_entrada, nueva_direccion)
        
if __name__ == '__main__':
    carpeta_entrada = "entrada"
    carpeta_salida = "salida"
    
    borrar = RemoverFondo(carpeta_entrada, carpeta_salida)
    borrar.process_images()
        