from .animal import Animal

class Chien(Animal):
    def parler(self):
        return f"{self.nom} aboie : Woof !"
