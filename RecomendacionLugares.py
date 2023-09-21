import redis
import random

class RecomendacionLugares:
    def __init__(self):
        self.hostname = "redis-15333.c283.us-east-1-4.ec2.cloud.redislabs.com"
        self.port = 15333
        self.password = "R6MU6xvnR8ZwmsQuMFvRQ51NTreENeHz"
        self.client = redis.Redis(host=self.hostname, port=self.port, password=self.password)
        self.datos = self.obtener_datos()

    def obtener_datos(self):
        datos = {}
        keys = self.client.keys()
        for key in keys:
            key = key.decode()
            lugares = self.client.lrange(key, 0, -1)
            lugares = [lugar.decode() for lugar in lugares]
            datos[key] = set(lugares)
        return datos

    def similitud_jaccard(self, conjunto1, conjunto2):
        intersection = len(conjunto1.intersection(conjunto2))
        union = len(conjunto1) + len(conjunto2) - intersection
        return intersection / union

    def generar_recomendaciones(self, usuario, num_recomendaciones=5):
        puntuaciones = {}
        for otro_usuario, lugares_visitados in self.datos.items():
            if otro_usuario == usuario:
                continue  # Saltar el propio usuario
            similitud = self.similitud_jaccard(self.datos[usuario], lugares_visitados)
            for lugar in lugares_visitados:
                if lugar not in self.datos[usuario]:
                    puntuaciones.setdefault(lugar, 0)
                    puntuaciones[lugar] += similitud

        # Ordenar lugares por puntuación en orden descendente
        lugares_recomendados = sorted(puntuaciones, key=lambda lugar: puntuaciones[lugar], reverse=True)

        # Obtener una muestra aleatoria de las mejores recomendaciones
        if len(lugares_recomendados) > num_recomendaciones:
            recomendaciones_aleatorias = random.sample(lugares_recomendados, num_recomendaciones)
        else:
            recomendaciones_aleatorias = lugares_recomendados

        return recomendaciones_aleatorias
   
############ estas si 
#    recomendador = RecomendacionLugares()
#    usuario_a_recomendar = 'javier.rodriguez.soto@gmail.com'
#    recomendaciones_usuario = recomendador.generar_recomendaciones(usuario_a_recomendar, num_recomendaciones=5)
#    print(f"Recomendaciones para {usuario_a_recomendar}: {recomendaciones_usuario}")
