# Generated by Django 4.2 on 2023-05-03 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_alter_pelicula_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('resumen', models.TextField(max_length=400)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.director')),
            ],
        ),
        migrations.DeleteModel(
            name='Directores',
        ),
        migrations.DeleteModel(
            name='Pelicula',
        ),
    ]
