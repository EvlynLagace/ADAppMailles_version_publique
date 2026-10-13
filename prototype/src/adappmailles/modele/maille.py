from enum import Enum

class TypeMaille(Enum):
    """Représente le type d'une maille : endroit ou envers."""
    ENDROIT = "K"
    ENVERS = "P"

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