from adappmailles.services.conversion_motif import pattern_to_rang
class GenerateurPatron:
    def generer(self, motif):
        return [pattern_to_rang(p) for p in motif.instructions]