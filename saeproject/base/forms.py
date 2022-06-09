from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models


class CategorieForm(ModelForm):
    class Meta:
        model = models.Categorie
        fields = ('ID1','nom','description')
        labels = {
            'ID1': _('ID1'),
            'nom': _('Nom'),
            'description': _('Description'),
        }
class FilmForm(ModelForm):

    class Meta:
        model = models.Film
        fields = ('ID1','titre','annee_de_sortie','affiche','realisateur','categorie')
        labels = {
            'ID1': _("ID1"),
            'titre': _('Titre'),
            'annee_de_sortie': _("Annee_de_sortie"),
            'affiche':  _("Affiche"),
            'realisateur': _("Realisateur"),


        }


class Film_ajoutForm(ModelForm):
    class Meta:
        model = models.Film
        fields = ('ID1','titre','annee_de_sortie','affiche','realisateur','categorie')
        labels = {
            'ID1': _("ID1"),
            'titre': _('Titre'),
            'annee_de_sortie': _("Annee_de_sortie"),
            'affiche':  _("Affiche"),
            'realisateur': _("Realisateur"),
        }



class PersonnesForm(ModelForm):

    class Meta:
        model = models.Personnes
        fields = ('pseudo','nom_prenom','mail','mot_de_passe','ID1','categorie','type')
        labels = {
            'pseudo': _("Pseudo"),
            'nom_prenom': _('Nom_prenom'),
            'mail': _("mail"),
            'mot_de_passe': _("mot_de_passe"),
            'ID1':  _("ID1"),
            'realisateur': _("Realisateur"),


        }



class CommentairesForm(ModelForm):

    class Meta:
        model = models.Commentaires
        fields = ('film','personnes','note','commentaires','date','categorie')
        labels = {
            'film': _("Film"),
            'personnes': _('Personnes'),
            'note': _("Note"),
            'commentaires':  _("Commentaires"),
            'date': _("Date"),


        }



class ActeurForm(ModelForm):

    class Meta:
        model = models.Acteur
        fields = ('ID1','nom','prenom','photos','age')
        labels = {
            'ID1': _("ID1"),
            'nom': _('Nom'),
            'prenom': _("Prenom"),
            'photos':  _("Photos"),
            'age': _("Age"),


        }