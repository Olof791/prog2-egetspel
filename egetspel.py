class Fordon:
    def __init__(self, märke, typ, effekt, ägare):
        self.märke = märke
        self.typ = typ
        self.effekt = effekt
        self.ägare = ägare

    def varva(self):
        print("Fordonet varvar!")

    

class ägare:
    def __init__(self, förnamn, efternamn, personnummer):
        self.förnamn = förnamn
        self.efternamn = efternamn
        self.__personnummer = personnummer

    def get_personnummer(self):
        return self.__personnummer
   
    def set_personnummer(self, ny_personnummer):
        self.__personnummer = ny_personnummer

    
        

class motorcykel(Fordon):
    def __init__(self, märke, typ, effekt, ägare):
        super().__init__(märke, typ, effekt, ägare)

    def varva(self):
        print("Mc låter Vroom vroom!")
        

    
class Bil(Fordon):
    def __init__(self, märke, typ, effekt, ägare):
        super().__init__(märke, typ, effekt, ägare)

    def varva(self):
        print("Bilen låter Brum brum!")


ägare1 = ägare("Get", "Getsson", 1999-12-22-2223)
ägare2 = ägare("Åsna", "Åsnesson", 2000-11-11-1112)

bil1 = Bil("Bmw", "Coupe", 170, ägare1)
mc1 = motorcykel("Yamaha", "Sport", 200, ägare2)
bil1.varva()
mc1.varva()



        





