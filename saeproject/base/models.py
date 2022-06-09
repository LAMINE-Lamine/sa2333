from django.db import models

class Categorie(models.Model):
    ID1 = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"{self.nom} "
        return chaine

    def dico(self):
        return{"ID1": self.ID1,"nom": self.nom,"description":self.description}
#..............................................................;;



class Film(models.Model):

    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=None, null=True)
    titre = models.CharField(max_length=100)
    ID1 = models.CharField(max_length=100)
    realisateur = models.CharField(max_length=100)
    annee_de_sortie = models.DateField(blank=True, null=True)
    affiche = models.URLField(null=True)



    def __str__(self):
        chaine = f"{self.titre} {self.realisateur} {self. annee_de_sortie}"
        return chaine

    def dico(self):
        return{"titre": self.titre, "realisateur": self.realisateur," annee_de_sortie": self. annee_de_sortie, "ID1": self.ID1,"categorie":self.categorie,"affiche": self.affiche}

#........................................................;

class Personnes(models.Model):

    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=None, null=True)
    pseudo = models.CharField(max_length=100)

    nom_prenom = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    mot_de_passe=models.IntegerField(blank=False)
    ID1 = models.CharField(max_length=100)
    type=models.CharField(max_length=100)



    def __str__(self):
        chaine = f"{self.pseudo} {self.nom_prenom} {self.type}"
        return chaine

    def dico(self):
        return{"pseudo": self.pseudo," nom_prenom": self.nom_prenom, "mail": self.mail,"mot_de_passe":self.mot_de_passe,"ID1": self.ID1,"type": self.type,"categorie": self.categorie}


#...............................................;

class Commentaires(models.Model):

    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=None, null=True)
    film = models.CharField(max_length=100)
    personnes = models.CharField(max_length=100,primary_key=True)
    note = models.CharField(max_length=100)
    commentaires = models.TextField(null = True, blank = True)
    date = models.DateField(blank=True, null=True)



    def __str__(self):
        chaine = f"{self.film} {self.personnes} {self. commentaires}"
        return chaine

    def dhico(self):
        return{"film": self.film, "personnes": self.personnes,"note": self. note, "commentaires": self.commentaires,"date":self.date,"categorie": self.categorie}

class Acteur(models.Model):

    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, default=None, null=True)
    ID1 = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.DateField(blank=True, null=True)
    photos = models.URLField(null=True)



    def __str__(self):
        chaine = f"{self.nom} {self.prenom} {self.age}"
        return chaine

    def dhico(self):
        return{"ID1": self.ID1, "nom": self.nom,"prenom": self. prenom, "age": self.age,"photos":self.photos,"categorie": self.categorie}
