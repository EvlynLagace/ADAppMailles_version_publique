from django import forms

class EchantillonFormulaire(forms.Form):

    largeur_cm = forms.IntegerField(
        label="Largeur en cm",
        min_value=1,
        widget=forms.NumberInput(
            attrs={"class": "form-control input-small"}
        ),
        error_messages={
            "invalid": "La largeur de l'échantillon doit être un nombre entier.",
            "min_value": "La largeur de l'échantillon doit être strictement positive."
        }
    )

    hauteur_cm = forms.IntegerField(
        label="Hauteur en cm",
        min_value=1,
        widget=forms.NumberInput(
            attrs={"class": "form-control input-small"}
        ),
        error_messages={
            "invalid": "La hauteur de l'échantillon doit être un nombre entier.",
            "min_value": "La hauteur de l'échantillon doit être strictement positive."
        }
    )

    nb_mailles = forms.IntegerField(
        label="Nombre de mailles",
        min_value=1,
        widget=forms.NumberInput(
            attrs={"class": "form-control input-small"}
        ),
        error_messages={
            "invalid": "Le nombre de mailles de l'échantillon doit être un entier.",
            "min_value":"Le nombre de mailles de l'échantillon doit être strictement positif."
        }
    )

    nb_rangs = forms.IntegerField(
        label="Nombre de rangs",
        min_value=1,
        widget=forms.NumberInput(
            attrs={"class": "form-control input-small"}
        ),
        error_messages={
            "invalid": "Le nombre de rangs de l'échantillon doit être un entier.",
            "min_value":"Le nombre de rangs de l'échantillon doit être strictement positif."
        }
    )

class CouvertureFormulaire(forms.Form):

    largeur_cm=forms.IntegerField(
        label="Largeur en cm",
        min_value=1,
        widget=forms.NumberInput(
            attrs={"class":"form-control input-small"}
        ),
        error_messages={
            "invalid":"La largeur de la couverture doit être un nombre entier.",
            "min_value":"La largeur de la couverture doit être strictement positive."
        }
    )

    hauteur_cm = forms.IntegerField(
        label="Hauteur en cm",
        min_value=1,
        widget=forms.NumberInput(
            attrs={"class": "form-control input-small"}
        ),
        error_messages={
            "invalid": "La hauteur de la couverture doit être un nombre entier.",
            "min_value": "La hauteur de la couverture doit être strictement positive."
        }
    )