from adappmailles.modele.maille import Maille
from adappmailles.modele.rang import TypeRang

class RangInstructions:
    """
    Représente les instructions pour construire un rang.

    Un rang est composé de trois parties :
    avant : des mailles tricotées une seule fois au début
    repetees : des mailles répétées un certain nombre de fois
    après : des mailles tricotées une seule fois à la fin du rang

    Chaque élément de avant/repetees/apres est un tuple (Maille, int)
    où le int représente le nombre d'occurences de la maille.
    """
    def __init__(
            self,
            type_rang=TypeRang.ENDROIT,
            avant: list[tuple[Maille, int]] | None = None,
            repetees: list[tuple[Maille, int]] | None = None,
            apres: list[tuple[Maille, int]] | None = None,
         ):
        """
        Initialise les instructions pour un rang.

        Args:
            type_rang: le type du rang (défaut ENDROIT).
            avant: liste des tuples des mailles tricotées au début.
            repetees: liste des tuples des mailles tricotées au milieu du rang un certain nombre de fois.
            apres: liste des tuples des mailles tricotées à la fin du rang.
        """
        self.type_rang = type_rang
        self.avant = list(avant) if avant else []
        self.repetees = list(repetees) if repetees else []
        self.apres = list(apres) if apres else []

    @property
    def nb_mailles_repetees(self) -> int:
        """Nombre de mailles qui sont répétées"""
        return sum(n for _, n in self.repetees)

    @property
    def nb_mailles_ajoutees(self) -> int:
        """Nombre de mailles qui sont ajoutées au début et à la fin"""
        return (
            sum(n for _, n in self.avant)
            + sum(n for _, n in self.apres)
        )
    
    def to_json(self):
        return {
            "type_rang":self.type_rang.name,
            "avant":self._encode_group(self.avant),
            "repetees":self._encode_group(self.repetees),
            "apres":self._encode_group(self.apres),
        }

    @staticmethod
    def _encode_group(group):
        return [
            {"type": t, "n":n}
            for (t, n) in group
        ]