# Generated by Django 4.0.6 on 2022-07-08 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmmapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorie',
            old_name='CategoriePatient',
            new_name='Categoriepatient',
        ),
        migrations.RenameField(
            model_name='etatcivil',
            old_name='EtatCivil',
            new_name='etatcivil',
        ),
        migrations.RenameField(
            model_name='groupesanguin',
            old_name='Groupesanguin',
            new_name='groupesanguin',
        ),
        migrations.RenameField(
            model_name='sexe',
            old_name='SexePatient',
            new_name='sexepatient',
        ),
    ]
