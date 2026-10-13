# Bibliothèque Python
import json
import os
import sys
from pathlib import Path

from appTricot.models import CouvertureModel, EchantillonModel
from appTricot.services.couverture_service import charger_user_couverture_par_id, charger_user_couvertures, creer_couverture
from appTricot.services.echantillon_service import charger_user_echantillon, charger_user_echantillon_par_id, charger_user_echantillons, creer_echantillon

from appTricot.domaine import echantillon

# Nécessaire pour charger WeasyPrint sous Windows
if sys.platform == "win32":
    os.add_dll_directory("C:/msys64/ucrt64/bin")

# Bibliothèques django
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, Http404
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

# Bibliothèques externes
from weasyprint import HTML, CSS

# Domaine - appTricot
from .domaine.couverture import Couverture
from .domaine.echantillon import Echantillon
from .domaine.maille import TypeMaille

# Services - appTricot

from appTricot.services.documentation_service import charger_markdown

from .services.affichage_service import (
    afficher_grille, 
    construire_grille_pdf, 
    construire_legende, 
    afficher_tuile_texte, 
    preparer_grille_affichage,
)

from .services.session_service import (
    get_couverture_session, 
    get_echantillon_session, 
    save_couverture_session, 
    save_echantillon_session,
)

from .services.couverture_runtime import (
    get_current_couverture, 
    reset_couverture, 
    reset_tuiles_couverture,
)

from .services.motifs_service import charger_motifs, chemin_image_motif, get_motif, preparer_contexte_motif_print, preparer_motif_pour_affichage
from .services.tuile_service import tuile_to_rangs

# Forms - appTricot
from .forms import CouvertureFormulaire, EchantillonFormulaire

def _get_tuile(request, i, j):
    couverture = get_current_couverture(request)

    try:
        return couverture.tuiles[i][j]
    except IndexError:
        raise Http404("Cette tuile n'existe pas")



def sauvegarde_json(obj, fichier):
    response = HttpResponse(
        obj.to_json(),
        content_type="application/json"
    )
    response["Content-Disposition"]=(f'attachment; filename="{ fichier }"')

    return response

def sauvegarde_couverture_json(couverture, echantillon, fichier):
    data = {
        "couverture": couverture.to_dict(),
        "echantillon": echantillon.to_dict(),
    }

    response = HttpResponse(
        json.dumps(data, indent=4, ensure_ascii=False),
        content_type="application/json"
    )
    response["Content-Disposition"] = (
        f'attachment; filename="{fichier}"'
    )

    return response

def index(request):
    if request.user.is_authenticated:
        couvertures = charger_user_couvertures(request.user)

        if couvertures.exists():
            couverture_model = couvertures.last()

            couverture, echantillon = charger_user_couverture_par_id(
                request.user,
                couverture_model.id,
            )

            save_couverture_session(request, couverture)
            save_echantillon_session(request, echantillon)

        else:

            echantillon = charger_user_echantillon(request.user)

            if echantillon is not None:
                save_echantillon_session(request, echantillon)
            
    return render(request, 'appTricot/index.html')

def lexique(request):
    return render(request, 'appTricot/lexique.html', {"types_maille":list(TypeMaille)})

def apropos(request):

    contenu = charger_markdown(Path("appTricot")/"docs"/"textes"/"a_propos.md")

    return render(request, 'appTricot/a_propos.html', {"contenu": contenu} )

def bases_tricot_view(request):

    contenu = charger_markdown(Path("appTricot")/"docs"/"guide"/"base-du-tricot.md")

    return render(request, "appTricot/bases_tricot.html", {"contenu": contenu,  "page_active":"bases_tricot",})

def materiel_view(request):

    contenu = charger_markdown(Path("appTricot")/"docs"/"guide"/"materiel.md")

    return render(request, "appTricot/materiel.html", {"contenu": contenu,  "page_active":"materiel"})

def tutoriel_adappmailles_view(request):

    contenu = charger_markdown(Path("appTricot")/"docs"/"guide"/"tutoriel.md")

    return render(request, "appTricot/tutoriel_adappmailles.html", {"contenu":contenu, "page_active":"tutoriel_adappmailles"})

def catalogue_view(request, nom_motif=None):

    motifs = charger_motifs()

    for motif in motifs:
        motif.photo = chemin_image_motif(motif)

    if nom_motif is None:
        nom_motif = "Jersey"

  
    motif_selectionne = next(
        (m for m in motifs if m.nom_motif == nom_motif),
        None
    )

    if motif_selectionne is None:
        return HttpResponseNotFound("Motif introuvable")
        
    data = preparer_motif_pour_affichage(motif_selectionne)

    return render(request, 'appTricot/catalogue.html', {
        "motifs" : motifs,
        "motif_selectionne": motif_selectionne,
        "instructions_formatees":data["instructions"] if data else [],
        "grille_motif": data["grille"] if data else [],
        "legende": data["legende"] if data else [],
        "photo": data["photo"] if data else None,
        "types_maille": data["types_maille"] if data else []

    })

def motif_view(request, nom_motif):

    motif = get_motif(nom_motif)

    if motif is None:
        return HttpResponseNotFound("Motif introuvable")

    return render(request, "appTricot/print/motif.html", 
        preparer_contexte_motif_print(motif)
    )

def motif_pdf_view(request, nom_motif):

    motif = get_motif(nom_motif)

    if motif is None:
        return HttpResponseNotFound("Motif introuvable")

    html_string = render_to_string(
        "appTricot/print/motif_pdf.html",
        preparer_contexte_motif_print(motif)
    )

    pdf = HTML(
        string=html_string,
        base_url=request.build_absolute_uri("/")
    ).write_pdf(
        stylesheets=[
            CSS(filename=str(settings.BASE_DIR / "appTricot/static/appTricot/css/mailles.css")),
            CSS(filename=str(settings.BASE_DIR / "appTricot/static/appTricot/css/impression.css")),
            CSS(filename=str(settings.BASE_DIR / "appTricot/static/appTricot/css/pdf.css")),
        ]
    )

    response = HttpResponse (pdf, content_type="application/pdf")
    response["Content-Disposition"]= (
        f'attachment; filename="{motif.nom_motif}.pdf"'
    )

    return response

def couverture_view(request):  

    echantillon_obj = get_echantillon_session(request)
    couverture_obj= get_current_couverture(request)

    tuile_reference = couverture_obj.tuiles[0][0]
    liste_motifs = tuile_reference.motifs_compatibles

    if request.user.is_authenticated:
        user_echantillons = charger_user_echantillons(request.user)
        user_couvertures = charger_user_couvertures(request.user)
    else:
        user_echantillons = []
        user_couvertures = []

    echantillon_form = construire_echantillon_form(request)
    couverture_form = construire_couverture_form(request)

    if request.method == "POST" and "save_echantillon" in request.POST:

        echantillon_form = construire_echantillon_form(request, request.POST)

        if echantillon_form.is_valid():
            request.session["echantillon"]={
                "largeur_cm":echantillon_form.cleaned_data["largeur_cm"],
                "hauteur_cm":echantillon_form.cleaned_data["hauteur_cm"],
                "nb_mailles":echantillon_form.cleaned_data["nb_mailles"],
                "nb_rangs":echantillon_form.cleaned_data["nb_rangs"],
            }

            reset_tuiles_couverture(request)

            messages.success(
                request,
                "L'échantillon a été modifié.  Une nouvelle couverture sera générée."
            )

            return redirect("couverture")

    if request.method == "POST" and "save_couverture" in request.POST:

        couverture_form = construire_couverture_form(request, request.POST)

        if couverture_form.is_valid():
            request.session["couverture"]={
                "largeur_cm":couverture_form.cleaned_data["largeur_cm"],
                "hauteur_cm":couverture_form.cleaned_data["hauteur_cm"],
            }

            messages.success(
                request,
                "La couverture a été modifiée, elle sera donc générée."
            )

            return redirect("couverture")


      
    return render(request, 'appTricot/couverture.html', {
                                                        "echantillon_obj":echantillon_obj,    
                                                         "couverture_obj": couverture_obj,
                                                         "liste_motifs": liste_motifs,
                                                         "user_echantillons": user_echantillons,
                                                         "user_couvertures": user_couvertures,
                                                         "echantillon_form": echantillon_form,
                                                         "couverture_form": couverture_form,
                                                         })

def parametres_view(request):

    if request.method == "POST":

        if "save_echantillon" in request.POST :

            echantillon_form = construire_echantillon_form(request, request.POST)
            couverture_form = construire_couverture_form(request)

            if echantillon_form.is_valid():
                request.session["echantillon"]={
                    "largeur_cm":echantillon_form.cleaned_data["largeur_cm"],
                    "hauteur_cm":echantillon_form.cleaned_data["hauteur_cm"],
                    "nb_mailles":echantillon_form.cleaned_data["nb_mailles"],
                    "nb_rangs":echantillon_form.cleaned_data["nb_rangs"],
                }

                reset_couverture(request)

                messages.success(request, "L'échantillon a été mis à jour. Une nouvelle couverture sera générée.")
                return redirect("voir_parametres")
            
        elif "save_couverture" in request.POST:

            couverture_form = construire_couverture_form(request, request.POST)
            echantillon_form = construire_echantillon_form(request)

            if couverture_form.is_valid():
                request.session["couverture"] = {
                    "largeur_cm":couverture_form.cleaned_data["largeur_cm"],
                    "hauteur_cm":couverture_form.cleaned_data["hauteur_cm"]
                }

                messages.success(request, "La couverture a été mise à jour.")
                return redirect("voir_parametres")
    else:
        echantillon_form=construire_echantillon_form(request)
        couverture_form = construire_couverture_form(request)

    return render(request, 'appTricot/parametres.html', {"echantillon_form": echantillon_form, "couverture_form":couverture_form} )

def construire_echantillon_form(request, post_data=None):
    
    initial = get_echantillon_session(request).to_dict()

    if post_data is not None:
        return EchantillonFormulaire(
            post_data,
            initial=initial
        )
    return EchantillonFormulaire(initial=initial)

def construire_couverture_form(request, post_data=None):
    
    initial = get_couverture_session(request).to_dict()

    if post_data is not None:
        return CouvertureFormulaire(
            post_data,
            initial=initial
        )
    return CouvertureFormulaire(initial=initial)

def sauvegarder_couverture_json_view(request):
    couverture_obj = get_current_couverture(request)
    echantillon_obj = get_echantillon_session(request)

    return sauvegarde_couverture_json(couverture_obj, echantillon_obj, "ma_couverture.json")

def sauvegarder_echantillon_json_view(request):
    echantillon_obj = get_echantillon_session(request)

    return sauvegarde_json(echantillon_obj, "mon_echantillon.json")

def charger_echantillon_json_view(request):
    if request.method == "POST":

        fichier = request.FILES.get("fichier_echantillon")

        if fichier is None:
            messages.error(request, "Aucun fichier sélectionné.")
            return redirect("couverture")

        try:
            data = json.load(fichier)

            echantillon = Echantillon.from_dict(data)

        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as e:
            messages.error(
                request, 
                "Impossible de charger cet échantillon. "
                "Le fichier sélectionné n'est pas un échantillon valide"
            )

            return redirect("couverture")

        save_echantillon_session(
            request,
            echantillon
        )

        return redirect("couverture")

@login_required
def sauvegarder_echantillon_compte_view(request):
    echantillon = get_echantillon_session(request)
    nom_echantillon = request.POST["nom_echantillon"]

    creer_echantillon(request.user, echantillon, nom_echantillon)

    messages.success(
        request,
        "L'échantillon a été sauvegardé dans votre compte."
    )

    return JsonResponse({"success": True})

@login_required
def sauvegarder_couverture_compte_view(request):
    couverture = get_couverture_session(request)
    echantillon = get_echantillon_session(request)
    nom_couverture = request.POST["nom_couverture"]

    creer_couverture(request.user, couverture, echantillon, nom_couverture)

    messages.success(
        request,
        "La couverture a été sauvegardée dans votre compte."
    )

    return JsonResponse({"success": True})

@login_required
def recuperer_couverture_compte_view(request):
    couverture_id = request.POST["couverture_id"]

    resultat = charger_user_couverture_par_id(
        request.user,
        couverture_id,
    )

    if resultat is not None:
        couverture, echantillon = resultat

        save_couverture_session(request, couverture)
        save_echantillon_session(request, echantillon)

    return redirect("couverture")

@login_required
def user_couvertures_view(request):
    user_couvertures = charger_user_couvertures(request.user)

    return render(
        request,
        "appTricot/user_couvertures.html",
        {
            "user_couvertures":user_couvertures,
        },
    )

@login_required
def recuperer_echantillon_compte_view(request):
    echantillon_id = request.POST["echantillon_id"]

    echantillon = charger_user_echantillon_par_id(
        request.user,
        echantillon_id,
    )

    if echantillon is not None:
        save_echantillon_session(request, echantillon)

    return redirect("couverture")


@login_required
def user_echantillons_view(request):
    user_echantillons = charger_user_echantillons(request.user)

    return render(
        request,
        "appTricot/user_echantillons.html",
        {
            "user_echantillons":user_echantillons,
        },
    )

@login_required
def supprimer_echantillon_compte_view(request):
    echantillon_id = request.POST["echantillon_id"]

    echantillon = (
        EchantillonModel.objects
        .filter(
            id=echantillon_id,
            user=request.user,
        )
        .first()
    )

    if echantillon is not None:
        echantillon.delete()

    return redirect("couverture")

@login_required
def supprimer_couverture_compte_view(request):
    couverture_id = request.POST["couverture_id"]

    couverture = (
        CouvertureModel.objects
        .filter(
            id=couverture_id,
            user=request.user,
        )
        .first()
    )

    if couverture is not None:
        couverture.delete()

    return redirect("couverture")

def charger_couverture_json_view(request):
    if request.method == "POST":

        fichier = request.FILES.get("fichier_couverture")

        if fichier is None:
            messages.error(request, "Aucun fichier sélectionné.")
            return redirect("couverture")

        try:
            data = json.load(fichier)

            catalogue = charger_motifs()

            couverture = Couverture.from_dict(
                data["couverture"],
                catalogue
            )

            echantillon = Echantillon.from_dict(data["echantillon"])


        except (json.JSONDecodeError, KeyError, TypeError, ValueError, IndexError):
            messages.error(
                request, 
                "Impossible de charger cette couverture. "
                "Le fichier sélectionné n'est pas une couverture valide"
            )

            return redirect("couverture")
        
        save_couverture_session(
            request,
            couverture
        )

        save_echantillon_session(
            request,
            echantillon
        )

        return redirect("couverture")

def couverture_api(request):
    couverture = get_current_couverture(request)

    data= {
        "hauteur_cm": couverture.hauteur_cm,
        "largeur_cm": couverture.largeur_cm,
        "tuiles":[
            [
                {
                    "motif":{
                        "nom_motif": tuile.motif.nom_motif,
                        "couleur_motif": tuile.motif.couleur_motif,
                        "photo": chemin_image_motif(tuile.motif),
                    }
                }
                for tuile in ligne
            ]
            for ligne in couverture.tuiles
        ]
    }

    return JsonResponse(data)

def nouvelle_couverture_view(request):
    reset_tuiles_couverture(request)
    return redirect("couverture")

def tuile_view(request, i, j):
    tuile = _get_tuile(request, i, j)

    instructions_formatees = afficher_tuile_texte(tuile.motif, tuile.nb_rangs_effectif, tuile.nb_mailles_effectif, tuile.motif_structure["nb_repetitions"], tuile.motif_structure["reste"])

    rangs = tuile_to_rangs(tuile.motif, tuile.nb_rangs_effectif, tuile.motif_structure["nb_repetitions"], tuile.motif_structure["max_mailles"], tuile.motif_structure["reste"])
    tuile_grille = afficher_grille(rangs)

    nb_mailles=tuile.nb_mailles_effectif
    nb_rangs=tuile.nb_rangs_effectif

    numeros_mailles = list(range(nb_mailles, 0, -1))
    numeros_rangs = list(range(nb_rangs, 0, -1))

    legende = construire_legende (tuile.motif)

    return render (request, "appTricot/tuile.html", {
        "tuile": tuile,
        "i": i,
        "j":j,
        "tuile_grille":tuile_grille,
        "instructions_formatees":instructions_formatees,
        "numeros_mailles":numeros_mailles,
        "numeros_rangs":numeros_rangs,
        "legende": legende
    })

def tuile_view_print(request, i, j):
    tuile = _get_tuile(request, i, j)

    instructions_formatees = afficher_tuile_texte(tuile.motif, tuile.nb_rangs_effectif, tuile.nb_mailles_effectif, tuile.motif_structure["nb_repetitions"], tuile.motif_structure["reste"])

    rangs = tuile_to_rangs(tuile.motif, tuile.nb_rangs_effectif, tuile.motif_structure["nb_repetitions"], tuile.motif_structure["max_mailles"], tuile.motif_structure["reste"])
    tuile_grille = afficher_grille(rangs)

    legende = construire_legende (tuile.motif)

    return render (request, "appTricot/print/tuile.html", {
        "tuile": tuile,
        "i": i,
        "j":j,
        "tuile_grille":tuile_grille,
        "instructions_formatees":instructions_formatees,
        "legende": legende
    })

def tuile_pdf_view(request, i, j):
    tuile = _get_tuile(request, i, j)

    instructions_formatees = afficher_tuile_texte(tuile.motif, tuile.nb_rangs_effectif, tuile.nb_mailles_effectif, tuile.motif_structure["nb_repetitions"], tuile.motif_structure["reste"])
    
    tuile_grille_pdf = construire_grille_pdf(tuile)
    tuile_grille_pdf = preparer_grille_affichage(tuile_grille_pdf)

    legende = construire_legende (tuile.motif)

    contexte = {
        "tuile": tuile,
        "i": i,
        "j":j,
        "tuile_grille_pdf":tuile_grille_pdf,
        "instructions_formatees":instructions_formatees,
        "legende": legende
    }

    html_string = render_to_string("appTricot/print/tuile_pdf.html",contexte)

    pdf = HTML(
        string=html_string,
        base_url=request.build_absolute_uri("/")
    ).write_pdf(
        stylesheets=[
            CSS(filename=str(settings.BASE_DIR / "appTricot/static/appTricot/css/style.css")),
            CSS(filename=str(settings.BASE_DIR / "appTricot/static/appTricot/css/impression.css")),
            CSS(filename=str(settings.BASE_DIR / "appTricot/static/appTricot/css/pdf.css")),
        ]
    )

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = (
        f'attachment; filename="tuile_{i+1}_{j+1}.pdf"'
    )

    return response

def tuile_motif_api(request, i, j):
    couverture = get_current_couverture(request)
    tuile = couverture.tuiles[i][j]

    if request.method == "GET":
        data = [
            {
                "nom_motif":m.nom_motif,
                "couleur_motif": m.couleur_motif
            }
            for m in tuile.motifs_compatibles
        ]
        return JsonResponse({"motifs":data})
    
    if request.method == "POST":
        motif_nom = request.POST.get("nom_motif")

        liste_motifs = tuile.motifs_compatibles

        motif = next(
            (m for m in liste_motifs if m.nom_motif == motif_nom),
            None
        )

        if not motif:
            return JsonResponse({"ok": False, "error":"motif not found"}, status=404)
        
        tuile.motif = motif

        tuile.nb_mailles_effectif =(
            tuile.calculer_nb_mailles_effectif(tuile.motif)
        )

        tuile.nb_rangs_effectif = tuile.calculer_nb_rangs_effectif(tuile.motif)

        tuile.calculer_structure_motif()

        save_couverture_session(request, couverture)

        return JsonResponse({
            "ok": True,
            "motif": {
                "nom_motif":motif.nom_motif,
                "couleur_motif":motif.couleur_motif
            }
        })
    return JsonResponse({"error": "method not allowed"}, status=405)

@login_required
def echantillons_api(request):
    echantillons = charger_user_echantillons(request.user)

    return JsonResponse({
        "echantillons":[
            {
                "id":echantillon.id,
                "nom":echantillon.nom_echantillon,
                "largeur_cm": echantillon.largeur_cm,
                "hauteur_cm": echantillon.hauteur_cm,
                "nb_mailles": echantillon.nb_mailles,
                "nb_rangs": echantillon.nb_rangs,
            }
            for echantillon in echantillons
        ]
    })

@login_required
def couvertures_api(request):
    couvertures = charger_user_couvertures(request.user)

    return JsonResponse({
        "couvertures":[
            {
                "id":couverture.id,
                "nom":couverture.nom_couverture,
                "largeur_cm": couverture.largeur_cm,
                "hauteur_cm": couverture.hauteur_cm,
            }
            for couverture in couvertures
        ]
    })