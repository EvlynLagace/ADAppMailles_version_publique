from markdown import markdown

from config import settings

from bs4 import BeautifulSoup
from django.templatetags.static import static

def _resource_images(contenu):
    soup = BeautifulSoup(contenu, "html.parser")

    for image in soup.find_all("img"):
        src = image.get("src")

        if src and src.startswith("images/"):
            image["src"] = static(f"guide/{src}")

    return str(soup)

def charger_markdown(chemin):
    fichier = settings.BASE_DIR/chemin
    texte = fichier.read_text(encoding="utf-8")
    contenu = markdown(
        texte,
        extensions=[
            "extra",
            "attr_list",
            "admonition",
            "toc",
        ],
    )

    contenu = _resource_images(contenu)

    return contenu