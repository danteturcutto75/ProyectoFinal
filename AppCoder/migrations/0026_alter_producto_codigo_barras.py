# Generated by Django 4.2.5 on 2023-10-09 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0025_alter_producto_codigo_barras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo_barras',
            field=models.CharField(default='01d972ffb9fc46b0a55ec5d73425d176', max_length=50),
        ),
    ]
