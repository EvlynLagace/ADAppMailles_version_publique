from django.test import TestCase

from appTricot.domaine.couverture import Couverture
from appTricot.services.session_service import (
    get_couverture_session,
    save_couverture_session,
)


class SessionServiceTest(TestCase):

    def test_ancienne_session_couverture_est_reinitialisee(self):
        self.client.session["couverture"] = {
            "largeur_cm": 100,
            "hauteur_cm": 60,
            "tuiles": [
                [
                    {
                        "motif": "Moss Stitch",
                        "nb_mailles": 10,
                        "nb_rangs": 10,
                    }
                ]
            ],
        }
        self.client.session.save()

        couverture = get_couverture_session(self.client.request().wsgi_request)

        self.assertEqual(couverture.largeur_cm, 100)
        self.assertEqual(couverture.hauteur_cm, 60)
        self.assertEqual(couverture.tuiles, [])

        session = self.client.session
        self.assertNotIn("couverture", session)

    def test_nouvelle_session_couverture_est_versionnee(self):  
        request = self.client.request().wsgi_request

        couverture = Couverture(
            largeur_cm=120,
            hauteur_cm=80,
        )

        save_couverture_session(request, couverture)

        self.assertIn("couverture", request.session)
        self.assertEqual(
            request.session["couverture_version"],
            2,
        )