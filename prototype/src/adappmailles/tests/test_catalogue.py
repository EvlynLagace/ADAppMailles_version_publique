from adappmailles.modele.catalogue import Catalogue
from adappmailles.modele.motif import Motif

def test_catalogue_initialisation_par_defaut():
    catalogue = Catalogue()
    
    assert catalogue.motifs == []

def test_catalogue_initialisation_avec_motifs():
    m1 = Motif("Motif 1")
    m2 = Motif("Motif 2")

    catalogue = Catalogue([m1, m2])

    assert m1 in catalogue.motifs
    assert m2 in catalogue.motifs
    assert len(catalogue.motifs) == 2