class Ninja:
    def __init__(self, tipo_personaje, nombre, aldea, equipo_especial,
                 resistencia, poder_habilidades, oficio,
                 poder_equipo, tipo_arma, dano_arma, nivel_arma):

        self.tipo_personaje = tipo_personaje
        self.nombre = nombre
        self.aldea = aldea
        self.equipo_especial = equipo_especial
        self.vidas = 3
        self.resistencia = resistencia
        self.poder_habilidades = poder_habilidades
        self.oficio = oficio
        self.poder_equipo = max(poder_equipo, 500)
        self.tipo_arma = tipo_arma
        self.dano_arma = dano_arma
        self.nivel_arma = nivel_arma

    def presentarse(self):
        print(f"Soy {self.nombre}, un {self.tipo_personaje} de la aldea {self.aldea}. Oficio: {self.oficio}.")
        print(f"Tengo 3 vidas y {self.resistencia} pts de resistencia.")

    def usar_habilidad(self):
        print(f"{self.nombre} usa una técnica ninja con {self.poder_habilidades} pts de poder.")

    def usar_equipo(self):
        print(f"{self.nombre} activa su equipo especial '{self.equipo_especial}' con {self.poder_equipo} pts.")

    def atacar(self):
        print(f"{self.nombre} ataca con su arma '{self.tipo_arma}', causando {self.dano_arma} pts de daño. Nivel: {self.nivel_arma}.")

    def descansar(self):
        print(f"{self.nombre} está recuperando chakra y resistencia.")


ninja1 = Ninja(
    tipo_personaje="Shinobi",
    nombre="Naruto Uzumaki",
    aldea="Konoha",
    equipo_especial="Modo Sabio",
    resistencia=6000,
    poder_habilidades=5000,
    oficio="Hokage",
    poder_equipo=1200,
    tipo_arma="Kunai",
    dano_arma=2000,
    nivel_arma="Divino"
)

ninja1.presentarse()
ninja1.usar_habilidad()
ninja1.usar_equipo()
ninja1.atacar()
ninja1.descansar()
