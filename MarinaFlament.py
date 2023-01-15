# FLAMENT Marina
# APP

class ArbreBinaire:

    def __init__(self, data):
        self.data = data
        self.child_right = None
        self.child_left = None
        self.parent = None


    def __repr__(self):
        return str(self.data)

    def insert_noeud(self, data: int) -> None:
        if data > self.data:
            if self.child_right == None:
                self.child_right = ArbreBinaire(data)
                self.child_right.parent = self
            else:
                self.child_right.insert_noeud(data)
        if data < self.data:
            if self.child_left == None:
                self.child_left = ArbreBinaire(data)
                self.child_left.parent = self
            else:
                self.child_left.insert_noeud(data)


    def parcours_infixe(self) -> None:
        if self == None:
            return "Arbre vide"
        if self.child_left != None:
            # print("Gauche : " + str(self.child_left))
            self.child_left.parcours_infixe()
        print(self)
        if self.child_right != None:
            # print("Droite : " + str(self.child_right))
            self.child_right.parcours_infixe()

    def recherche(self, valeur: int) -> str:
        if self == None:
            return "Arbre vide"
        else:
            if valeur == self.data:
                return "Valeur trouvée"
            else:
                if valeur > self.data:
                    if self.child_right != None:
                        return self.child_right.recherche(valeur)
                    else : return "Valeur non trouvée"
                elif valeur < self.data:
                    if self.child_left != None:
                        return self.child_left.recherche(valeur)
                    else: return "Valeur non trouvée"
        return "Valeur non trouvée"

if __name__ == "__main__":
    a = ArbreBinaire(20)
    a.insert_noeud(15)
    a.insert_noeud(25)
    print(a)
    print(a.child_left)
    print(a.child_right)
    a.insert_noeud(5)
    a.insert_noeud(10)
    a.insert_noeud(17)
    print(a.child_left.child_left)
    print(a.child_left.child_right)
    print()
    print("Parcours infixe")
    a.parcours_infixe()
    print()
    print("Recherche")
    print(a.recherche(28))
    print(a.recherche(25))
