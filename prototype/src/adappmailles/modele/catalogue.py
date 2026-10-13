import json

from adappmailles.data.motifs_test_listes import get_motifs_test_listes
from adappmailles.modele.motif import Motif

class Catalogue:
    """Représente le catalogue des motifs."""
    def __init__(self, motifs=None):
        """
        Initialise un catalogue.

        Args:
            motifs(list[Motif] | None): liste des motifs disponibles.
        """
        self.motifs = list(motifs) if motifs is not None else []
    
    @classmethod
    def avec_motifs_test_listes(cls):
        return cls(get_motifs_test_listes())
    
    @classmethod
    def from_json_file(cls, path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        motifs = [
            Motif.from_json(m)
            for m in data["motifs"]
        ]

        return cls(motifs)
    
    