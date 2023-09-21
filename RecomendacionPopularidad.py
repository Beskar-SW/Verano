import random

class RecomendacionPopularidad:
    def __init__(self):
        self.elementos_populares = {
    "Museo De La Filatelia MUFI": 4.8,
    "Museum of Cultures of Oaxaca, Santo Domingo": 4.7,
    "MUSEO DE SITIO MONTE ALBAN": 4.7,
    "MUSEO BELBER": 4.3,
    "Museum of Oaxacan Painters": 4.5,
    "Museo de Sitio Casa Juarez": 4.2,
    "Museo de Arte Prehispanico de Mexico": 4.6,
    "SALA DE INMERSION": 5,
    "MUSEO SAN MARTIN": 5,
    "Museo Textil de Oaxaca": 4.5,
    "Museo Infantil de Oaxaca": 4.6,
    "Patio del Huaje": 4.5,
    "Earthquake Arts/Studio Sismo": 4,
    "MUSEO DEL FRONTISPICIO": 5,
    "Museum of the Basilica of La Soledad": 4.3,
    "Museo de Arte de Santa Maria Coyotepec": 4,
    "Museo Regional de la Palma": 5,
    "Zona Arqueologica de Monte Alban": 4.8,
    "Zona Arqueologica de Atzompa": 4.6,
    "El Cerrito": 4.9,
    "Lambityeco": 4.4,
    "Plataforma Sur": 4.9,
    "Yagul": 4.6,
    "Dainzu": 4.5,
    "Plataforma Norte": 4.8,
    "El Palacio": 4.6,
    "Astronomical Observatories (Building J)": 4.9,
    "Tumba 105": 4.8,
    "Plaza Central": 4.8,
    "Tumba 104": 5,
    "Patio Hundido": 4.8,
    "Ay Guey! Oaxaca": 5,
    "STOP OAXACA": 5,
    "Supplementstore oaxaca": 5,
    "IMPERIO Store": 5,
    "General Store Luna": 5,
    "Cafe Cafe Autentico como tu": 4.1,
    "Cafe Mava": 4.5,
    "CAFE CRIOLLO": 4.1,
    "Cafebre": 4.4,
    "Amor del Cafe": 4.9,
    "Cafe Nuevo Mundo": 4.3,
    "Cafe la Antigua": 4.3,
    "Candiani Cafe": 4.3,
    "Cafe Cafe": 4.4,
    "Cafe Cafe de Oaxaca": 4,
    "Cafe SL28": 4.5,
    "Cafe Boca del Monte": 4.4,
    "Cafe Rustiko": 4.7,
    "Cafe Finca El Olivo": 4.8,
    "Mondo Cafe": 4.6,
    "Cafe Brujula Belisario Dominguez | Cafe de Especialidad de Oaxaca, Mexico": 4.3,
    "Muss Cafe": 4.4,
    "Cafe Brujula Porfirio Diaz | Cafe de Especialidad de Oaxaca, Mexico": 4.3,
    "Cafe Lupita": 4.8,
    "Cafe La Leyenda": 4.8,
    "Palenque Jose Santiago": 4.1,
    "Restaurant -Bar El rinconcito": 4.5,
    "La escondida bar": 5,
    "Wombat Oaxaca": 4.8,
    "Mistereo": 4.9,
    "SweetBar": 4,
    "El Manis": 4.4,
    "Restaurante bar Camino Real": 4,
    "Cebada Bar": 5,
    "Yesterday Micheladeria": 4.5,
    "Renessi's truck": 4.2,
    "La Tenera Cantina": 5,
    "El Catron Bar": 4.3,
    "Punto Cinco": 5,
    "Mi Ranchito": 4.7,
    "SAINT FOOD": 4.2,
    "Fast food": 5,
    "Al Patio Food": 5,
    "Pig & fish Food Truck": 4.2,
    "Fish Food!": 5,
    "Food Center": 4.5,
    "Restaurante Dubai": 4.7,
    "Burguers street food": 4.3,
    "Litho's Fast Food and Drinks": 5,
    "Hooligans Food & Drynk": 4.5,
    "Barbajon Tacos & Food": 4.8,
    "JK Fast Food": 5,
    "Drinks & food capital": 4,
    "Restaurant Tierra del Sol": 4.4,
    "Red Indian Chilli Express": 4.4,
    "Okasa lovely food": 4.5,
    "Red Dot Art Gallery/ Galeria ESPACIO DIEZ": 4.9,
    "Galeria Shadai": 5,
    "Yaguar Zoo Xoo": 4.7,
    "Divertigranja": 5,
    "La Casa del Jaguar": 5,
    "Centro de Rehabilitacion La vina": 5,
    "Super zoo": 4.9,
    "La Chiche de Maria Sanchez": 5,
    "Fernando lara": 4.3,
    "El Santuario del Jaguar": 4.6,
    "Zoologico Magico": 4.6,
    "El Llano": 4.5,
    "ESTADIO TECNOLOGICO DE OAXACA": 4.4,
    }

    def recomendacion_popularidad(self, num_recomendaciones=5):
        elementos_ordenados = sorted(self.elementos_populares.items(), key=lambda x: x[1], reverse=True)
        recomendaciones = [elemento[0] for elemento in elementos_ordenados[:num_recomendaciones]]
        return recomendaciones

    def recomendacion_popularidad_aleatoria(self, num_recomendaciones=5):
        elementos_populares_lista = list(self.elementos_populares.keys())
        random.shuffle(elementos_populares_lista)
        recomendaciones = elementos_populares_lista[:num_recomendaciones]
        return recomendaciones

# Ejemplo de uso
# recomendador = RecomendacionPopularidad()
# num_recomendaciones = 5
# recomendaciones = recomendador.recomendacion_popularidad(num_recomendaciones)
# recomendaciones = recomendador.recomendacion_popularidad_aleatoria(num_recomendaciones)
# print(f"Recomendaciones basadas en popularidad: {recomendaciones}")
