# Generated by Django 2.0.2 on 2019-03-07 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uphase',
            name='signal',
            field=models.BinaryField(verbose_name='Collected Signal vector'),
        ),
        migrations.AlterField(
            model_name='vphase',
            name='signal',
            field=models.BinaryField(verbose_name='Collected Signal vector'),
        ),
        migrations.AlterField(
            model_name='wphase',
            name='signal',
            field=models.BinaryField(verbose_name='Collected Signal vector'),
        ),
    ]