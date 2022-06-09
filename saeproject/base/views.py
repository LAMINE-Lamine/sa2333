from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CategorieForm
from .forms import FilmForm
from .forms import Film_ajoutForm
from .forms import CommentairesForm
from .forms import PersonnesForm
from .forms import ActeurForm





from . import  models
# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = CategorieForm(request)
        if form.is_valid():
            categorie = form.save()
            return HttpResponseRedirect("/base/")
        else:
            return render(request,"base/ajout.html",{"form": form})
    else :
        form = CategorieForm()
        return render(request,"base/ajout.html",{"form" : form})

def home(request):
    liste = list(models.Categorie.objects.all())
    return render(request, 'base/home.html', {'liste': liste})



#..................................................................................................
def affiche(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    liste2=list(models.Film.objects.filter(classe_id=id))
    return render(request,"base/affiche.html",{"categorie" : categorie,"liste2":liste2})

def delete(request, id):
    categorie = models.Categorie.objects.get(pk=id)
    categorie.delete()
    return HttpResponseRedirect("/base/")

def update(request, id):
    categorie= models.Categorie.objects.get(pk=id)
    cform = CategorieForm(categorie.dico())
    return render(request, "base/update.html", {"form": cform,"id": id})

def traitementupdate(request, id):
    cform = CategorieForm(request.POST)
    if cform.is_valid():
        categorie = cform.save(commit=False)
        categorie.id = id
        categorie.save()
        return HttpResponseRedirect("/base/")
    else:
        return render(request, "base/update.html", {"form": cform, "id": id})

def traitement(request):
    cform = CategorieForm(request.POST)
    if cform.is_valid():
        categorie = cform.save()
        return HttpResponseRedirect("/base/")
    else:
        return render(request,"base/ajout.html",{"form": cform})

#................................................................................................

def ajout2(request):
    if request.method == "POST":

        form = FilmForm(request)
        if form.is_valid():
            film = form.save()
            return render(request,"base/ajout2.html",{"film" : film})

    else :
        form = FilmForm()
        return render(request,"base/ajout2.html",{"form" : form})

def traitement2(request):
    mform = FilmForm(request.POST)
    if mform.is_valid():
        film = mform.save()
        return render(request,"base/affiche.html",{"film" : film})
    else:
        return render(request,"base/ajout2.html",{"form": mform})


def delete2(request, id):
    film = models.Film.objects.get(pk=id)
    film.delete()
    return HttpResponseRedirect("/base/affiche/" + str(film.categorie_id) + '/')

def update2(request, id):
    film = models.Film.objects.get(pk=id)
    mform = FilmForm(film.dico())
    return render(request, "base/update2.html", {"form": mform,'id':id})

def traitementupdate2(request, id):
    mform = FilmForm(request.POST)
    if mform.is_valid():
        film = mform.save(commit=False)

        film.id = id
        film.save()
        return HttpResponseRedirect("/base/affiche/" + str(film.categorie_id) + '/')
    else:
        return render(request, "base/update2.html", {"form": mform, "id": id})

def ajout3(request, id):
    form = Film_ajoutForm()
    return render(request, "base/ajout3.html", {"form": form, "id": id})



def traitement3(request , id):
    fform = Film_ajoutForm(request.POST)
    categorie= models.Categorie.objects.get(pk=id)
    if fform.is_valid():
        film_ajout = fform.save(commit=False)
        film_ajout.categorie_id = id
        film_ajout.categorie = categorie
        film_ajout.save()
        return HttpResponseRedirect(f"/base/affiche/{id}/")
    else:
        return render(request, "base/ajout3.html", {"form": fform, "id": id})

def traitementupdate3(request, id):
        fform = FilmForm(request.POST)
        if fform.is_valid():
            film = fform.save(commit=False)
            film.id = id
            film.save()
            return HttpResponseRedirect("/base")
        else:
            return render(request, "base/update3.html", {"form": fform, "id": id})

  #;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;





def ajout4(request):
    if request.method == "POST":

        form = ActeurForm(request)
        if form.is_valid():
            acteur = form.save()
            return render(request,"base/ajout4.html",{"acteur" :acteur})

    else :
        form = ActeurForm()
        return render(request,"base/ajout4.html",{"form" : form})

def traitement4(request):
    pform = ActeurForm(request.POST)
    if pform.is_valid():
        acteur = pform.save()
        return render(request,"base/affiche.html",{"acteur" : acteur})
    else:
        return render(request,"base/ajout4.html",{"form": pform})


def delete4(request, id):
    film = models.Acteur.objects.get(pk=id)
    film.delete()
    return HttpResponseRedirect("/base/affiche/" + str(film.acteur_id) + '/')

def update4(request, id):
    acteur = models.Acteur.objects.get(pk=id)
    pform = ActeurForm(acteur.dico())
    return render(request, "base/update4.html", {"form": pform,'id':id})

def traitementupdate4(request, id):
    pform = ActeurForm(request.POST)
    if pform.is_valid():
        acteur = pform.save(commit=False)

        acteur.id = id
        acteur.save()
        return HttpResponseRedirect("/base/affiche/" + str(acteur.categorie_id) + '/')
    else:
        return render(request, "base/update4.html", {"form": pform, "id": id})








    #................................................


def ajout5(request):
    if request.method == "POST":

        form = PersonnesForm(request)
        if form.is_valid():
            personnes = form.save()
            return render(request,"base/ajout5.html",{"personnes" :personnes})

    else :
        form = PersonnesForm()
        return render(request,"base/ajout5.html",{"form" : form})

def traitement5(request):
    rform = PersonnesForm(request.POST)
    if rform.is_valid():
        personnes = rform.save()
        return render(request,"base/affiche.html",{"personnes" : personnes})
    else:
        return render(request,"base/ajout5.html",{"form": rform})


def delete5(request, id):
    film = models.Personnes.objects.get(pk=id)
    film.delete()
    return HttpResponseRedirect("/base/affiche/" + str(personnes.acteur_id) + '/')

def update5(request, id):
    personnes = models.Personnes.objects.get(pk=id)
    rform = PersonnesForm(personnes.dico())
    return render(request, "base/update5.html", {"form": rform,'id':id})

def traitementupdate5(request, id):
    rform = PersonnesForm(request.POST)
    if rform.is_valid():
        personnes = rform.save(commit=False)

        personnes.id = id
        personnes.save()
        return HttpResponseRedirect("/base/affiche/" + str(personnes.categorie_id) + '/')
    else:
        return render(request, "base/update4.html", {"form": rform, "id": id})

