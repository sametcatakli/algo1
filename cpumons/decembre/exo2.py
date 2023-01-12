liste = []


class membre():
    def __init__(self, nom, prenom, faculte, section, inscription, participation, date):
        self.nom = nom
        self.prenom = nom
        self.email = prenom + '.' + nom + '@student.umons.ac.be'
        self.faculte = faculte
        self.section = section
        self.inscription = inscription
        self.participation = participation
        self.date = date


def new(nom, prenom, faculte, section, inscription, participation, date):
    m = membre(nom, prenom, faculte, section, inscription, participation, date)
    liste.append(m)


def search(date):
    for i in liste:
        if date in i.participation:
            print("test")


print(liste)
search("071222")
# new("Catakli", "Samet", "sciences", 'info', "010922", "2", ("081022", "071222"))
# new("Nico", "Samet", "sciences", 'info', "010922", "2", ("081022", "071222"))
