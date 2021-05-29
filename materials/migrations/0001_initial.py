# Generated by Django 3.1.7 on 2021-05-23 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(default='Desconhecido', max_length=30, unique=True)),
                ('material_description', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
