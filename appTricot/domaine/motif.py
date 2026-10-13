from appTricot.domaine.maille import TypeMaille

from .rang import TypeRang
from .rang_instructions import RangInstructions

class Motif:
    """
    Représente un motif tricoté.

    Un motif est défini par une suite de rangs (instructions).
    Hypothèse : tous les rangs sont supposés contenir le même nombre total de mailles,
    structurées comme :

        mailles_ajoutees + k * mailles_repetees

    Le premier rang est utilisé comme référence pour ces calculs.
    """

    def __init__(self, nom_motif=None, instructions=None, coefficient_horizontal=1, coefficient_vertical = 1, couleur_motif=None):
        """
        Initialise un motif.

        Args:
            nom_motif (str | None): nom du motif.
            instructions: liste de RangInstructions décrivant les rangs du motif.
            coefficient_horizontal: coefficient de densité horizontal (pour les mailles).
            coefficient_vertical: coefficient de densité vertical (pour les rangs).
            couleur_motif: couleur attribuée au motif pour l'affichage de la couverture.

        """
        self.nom_motif = nom_motif
        self.instructions = instructions if instructions is not None else []
        if not isinstance(coefficient_horizontal, (int, float)):
            raise TypeError("Le coefficient horizontal doit être numérique")
        if coefficient_horizontal <= 0:
            raise ValueError("Le coefficient horizontal doit être strictement positif")
        self.coefficient_horizontal = coefficient_horizontal
        if not isinstance(coefficient_vertical, (int, float)):
            raise TypeError("Le coefficient vertical doit être numérique")
        if coefficient_vertical <= 0:
            raise ValueError("Le coefficient vertical doit être strictement positif")        
        self.coefficient_vertical = coefficient_vertical
        self.couleur_motif = couleur_motif

    def __lt__(self, autre):
        return self.nom_motif < autre.nom_motif

    def _instruction_reference(self):
        """Retourne les instructions du premier rang représentatif du motif (référence)"""
        if not self.instructions:
            raise ValueError("Le motif ne contient aucun rang")
        
        for r in self.instructions:
            if not getattr(r, "est_remplissage", False):
                return r
        
        return self.instructions[0]


    @property
    def nb_mailles_repetees(self) -> int:
        """Retourne le nombre de mailles répétées du motif."""
        instruction = self._instruction_reference()
        return sum(n for _, n in instruction.repetees)

    @property
    def nb_mailles_ajoutees(self) -> int:
        """Retourne le nombre de mailles ajoutées au motif."""
        instruction = self._instruction_reference()
        return (
            sum(n for _, n in instruction.avant)
            + sum(n for _, n in instruction.apres)
        )

    @property
    def nb_mailles_minimum(self) -> int:
        """Retourne le nombre minimal de mailles pour ce motif."""
        return self.nb_mailles_ajoutees + self.nb_mailles_repetees

    @property
    def couleur_texte(self):
        """Retourne noir ou blanc selon la luminosité de la couleur du motif."""
        if not self.couleur_motif:
            return "#000000"

        couleur = self.couleur_motif.lstrip("#")

        r = int(couleur[0:2], 16)
        g = int(couleur[2:4], 16)
        b = int(couleur[4:6], 16)

        luminosite = (r * 299 + g * 587 + b * 114) / 1000

        return "#000000" if luminosite > 128 else "#FFFFFF"
    
    @classmethod
    def from_json(cls, data):
        instructions = []

        for r in data["instructions"]:
            rang = RangInstructions(
                type_rang=TypeRang[r["type_rang"]],
                avant=cls._parse_group(r["avant"]),
                repetees=cls._parse_group(r["repetees"]),
                apres=cls._parse_group(r["apres"]),
            )

            rang.est_remplissage = cls._est_rang_remplissage(rang)

            instructions.append(rang)

        return cls(
            nom_motif=data["nom_motif"],
            coefficient_horizontal=data["coefficient_horizontal"],
            coefficient_vertical = data["coefficient_vertical"],
            couleur_motif=data["couleur_motif"],
            instructions=instructions
        )
    
    @staticmethod
    def _est_rang_remplissage(rang):
        """
        Détecte un rang de type :
        - une seule instruction
        - répétée 1 fois
        - sans structure avant/après

        => ex : "K", "P"
        => signifie : remplir toute la largeur
        """
        return (
            not rang.avant
            and not rang.apres
            and rang.est_pattern_simple
        )
    
    @staticmethod
    def _parse_group(group):

        sequence = []

        for item in group:
            n = item.get("n",1)

            if type(n) is not int or n<1:
                raise ValueError( "Le nombre de maille 'n' doit être un entier positif ")

            sequence.append((TypeMaille(item["type"]), n))

        return sequence

    def to_json(self):
        return {
            "nom_motif": self.nom_motif,
            "coefficient_horizontal": self.coefficient_horizontal,
            "coefficient_vertical": self.coefficient_vertical,
            "couleur_motif": self.couleur_motif,
            "instructions":[
                r.to_json() for r in self.instructions
            ]
        }
    
    def types_mailles_utilises(self):
        types = set()

        for instruction in self.instructions:
            for type_maille, _ in instruction.avant:
                types.add(type_maille)

            for type_maille, _ in instruction.repetees:
                types.add(type_maille)

            for type_maille, _ in instruction.apres:
                types.add(type_maille)

        return types

