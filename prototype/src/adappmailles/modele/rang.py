from enum import Enum

class TypeRang(Enum):
    """Représente le type du rang: endroit ou envers."""
    ENDROIT = "endroit"
    ENVERS = "envers"

class Rang:
    """Représente un rang."""
    def __init__(self, type_rang: TypeRang = TypeRang.ENDROIT, mailles: list|None=None):
        """
        Initialise un rang

        Args: 
            type_rang: type du rang (ENDROIT par défaut).
            mailles: liste des objets Maille représentant le rang.
        """
        self.type_rang = type_rang
        self.mailles = list(mailles) if mailles is not None else []

    @property
    def est_endroit(self) -> bool:
        """Indique si un rang est endroit."""
        return self.type_rang == TypeRang.ENDROIT
    
    @property
    def est_envers(self) -> bool:
        """Indique si un rang est envers."""
        return self.type_rang == TypeRang.ENVERS

    def __str__(self):
        return self.type_rang.value
   
    def __iter__(self):
        yield from self.mailles

    def __repr__(self):
        return f"Rang({self.type_rang.name}, {len(self.mailles)} mailles)"
