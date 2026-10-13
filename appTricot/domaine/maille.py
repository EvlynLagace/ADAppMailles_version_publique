from enum import Enum

class TypeMaille(Enum):
    """Représente le type d'une maille dans les isntructions """
    ENDROIT = "K"
    ENVERS = "P"
    WYIF = "WYIF"
    WYIB  = "WYIB"

    @property
    def abreviation(self):
        return {
            TypeMaille.ENDROIT:"end.",
            TypeMaille.ENVERS:"env.",
            TypeMaille.WYIF: "FDev gl.",
            TypeMaille.WYIB: "FDerr gl."
        }[self]
    
    @property
    def definition(self):
        return {
            TypeMaille.ENDROIT:" signifie une maille endroit",
            TypeMaille.ENVERS:" signifie une maille envers",
            TypeMaille.WYIF: " signifie une maille glissée avec le fil devant l'ouvrage",
            TypeMaille.WYIB: "  signifie une maille glissée avec le fil derrière l'ouvrage"
        }[self]

    @property
    def lien_video(self):
        return {
            TypeMaille.ENDROIT:"https://www.youtube.com/watch?v=9yFNAHUNttM",
            TypeMaille.ENVERS:"https://www.youtube.com/watch?v=I-m4Cb9RdBs",
            TypeMaille.WYIF: "https://youtu.be/watch?v=69Xt7R4vONQ",
            TypeMaille.WYIB: "https://youtu.be/watch?v=hjX1hXHPnyc"
        }[self]              

class Maille:
    """Représente une maille."""
    def __init__(self, type_maille: TypeMaille = TypeMaille.ENDROIT):
        """
        Initialise une maille

        Args :
            type_maille : Type de la maille (ENDROIT par défaut)
        """
        self._type_maille = type_maille

    @property
    def type_maille(self) -> TypeMaille:
        """Retourne le type de la maille."""
        return self._type_maille

    def __str__(self):
        """Retourne 'K' (endroit) ou 'P' (envers)."""
        return self.type_maille.value

    def __repr__(self):
        return f"Maille({self.type_maille.name})"
    
    def __eq__(self, other): #pour les tests
        if not isinstance(other, Maille):
            return NotImplemented
        return self.type_maille == other.type_maille
    
    @property
    def est_endroit(self) -> bool:
        """Indique si la maille est à l'endroit.""" 
        return self.type_maille == TypeMaille.ENDROIT 
    
    @property
    def est_envers(self) -> bool:
        """Indique si la maille est à l'envers."""
        return self.type_maille == TypeMaille.ENVERS