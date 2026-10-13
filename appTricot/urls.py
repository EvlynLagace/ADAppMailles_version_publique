from django.urls import path
from . import views

urlpatterns = [
    
    #pour les pages
    path('',views.index, name='indexTricot'),
    path('lexique/', views.lexique, name='lexique'),
    path('apropos/', views.apropos, name='a_propos'),
    path('bases_tricot/', views.bases_tricot_view, name='bases_tricot'),
    path('materiel/', views.materiel_view, name='materiel'),
    path('tutoriel_adappmailles/', views.tutoriel_adappmailles_view, name='tutoriel_adappmailles'),

    path('couverture/', views.couverture_view, name='couverture'),
    path('sauvegarder_couverture/', views.sauvegarder_couverture_json_view, name='sauvegarder_couverture'), 
    path('charger_couverture/', views.charger_couverture_json_view, name='charger_couverture'),
    path('sauvegarder_couverture_compte/', views.sauvegarder_couverture_compte_view, name='sauvegarder_couverture_compte'),
    path('recuperer_couverture_compte/', views.recuperer_couverture_compte_view, name='recuperer_couverture_compte'),
    path('user_couvertures/', views.user_couvertures_view, name='user_couvertures'),
    path('supprimer_couverture_compte/', views.supprimer_couverture_compte_view, name='supprimer_couverture_compte'),

    path('sauvegarder_echantillon/', views.sauvegarder_echantillon_json_view, name='sauvegarder_echantillon'),
    path('charger_echantillon/', views.charger_echantillon_json_view, name='charger_echantillon'),
    path('sauvegarder_echantillon_compte/', views.sauvegarder_echantillon_compte_view, name='sauvegarder_echantillon_compte'),
    path('recuperer_echantillon_compte/', views.recuperer_echantillon_compte_view, name="recuperer_echantillon_compte"),
    path('user_echantillons/', views.user_echantillons_view, name='user_echantillons'),
    path('supprimer_echantillon_compte/', views.supprimer_echantillon_compte_view, name='supprimer_echantillon_compte'),
    
    path('catalogue/', views.catalogue_view, name='catalogue'),
    path('motifs/<str:nom_motif>/', views.catalogue_view, name="motif_detail"),
    path('parametres/', views.parametres_view, name='voir_parametres'),
    path('tuile/<int:i>/<int:j>/', views.tuile_view, name='tuile_detail'),
    path('nouvelle-couverture/', views.nouvelle_couverture_view, name='nouvelle_couverture'),
    path('print/motif/<str:nom_motif>/', views.motif_view, name='motif'),
    path('print/motif_pdf/<str:nom_motif>/pdf/', views.motif_pdf_view, name='motif_pdf'),
    path('print/tuile/<int:i>/<int:j>/', views.tuile_view_print, name='tuile_detail_print'),
    path('print/tuile_pdf/<int:i>/<int:j>/', views.tuile_pdf_view, name='tuile_detail_pdf'),


    #pour React
    path('api/couverture/', views.couverture_api, name='couverture_api'),
    path('api/tuile/<int:i>/<int:j>/motif/',views.tuile_motif_api, name='tuile_motif_api'),
    path('api/echantillons/', views.echantillons_api, name='echantillons_api'),
    path('api/couvertures/', views.couvertures_api, name='couvertures_api')
]