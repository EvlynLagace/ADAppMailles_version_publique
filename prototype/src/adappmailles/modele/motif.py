from adappmailles.modele.rang import TypeRang
from adappmailles.modele.rang_instructions import RangInstructions


class Motif:
    """
    Représente un motif tricoté.

    Un motif est défini par une suite de rangs (instructions).
    Hypothèse : tous les rangs sont supposés contenir le même nombre total de mailles,
    structurées comme :

        mailles_ajoutees + k * mailles_repetees

    Le premier rang est utilisé comme référence pour ces calculs.
    """

    def __init__(self, nom_motif=None, instructions=None, coefficient=1, couleur_motif=None):
        """
        Initialise un motif.

        Args:
            nom_motif (str | None): nom du motif.
            instructions: liste de RangInstructions décrivant les rangs du motif.
            coefficient: coefficient de densité horizontal (pour les mailles).
            couleur_motif: couleur attribuée au motif pour l'affichage de la couverture.

        """
        self.nom_motif = nom_motif
        self.instructions = instructions if instructions is not None else []
        self.coefficient = coefficient
        self.couleur_motif = couleur_motif

    def _instruction_reference(self):
        """Retourne les instructions du premier rang (référence)"""
        if not self.instructions:
            raise ValueError("Le motif ne contient aucun rang")
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
            instructions.append(rang)

        return cls(
            nom_motif=data["nom_motif"],
            coefficient=data["coefficient"],
            couleur_motif=data["couleur_motif"],
            instructions=instructions
        )
    
    @staticmethod
    def _parse_group(group):
        return [
        (item["type"], item.get("n", 1))
        for item in group
    ]

    def to_json(self):
        return {
            "nom_motif": self.nom_motif,
            "coefficient": self.coefficient,
            "instructions":[
                r.to_json() for r in self.instructions
            ]
        }