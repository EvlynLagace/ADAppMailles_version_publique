from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("appTricot", "0004_echantillonmodel_nom_echantillon_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CouvertureModel",
        ),
    ]