# Generated by Django 4.2.5 on 2023-10-09 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0021_alter_producto_codigo_barras_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo_barras',
            field=models.CharField(default='16b00156ed3046f2ba9119f41079a117', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='media/default_avatar.png', null=True, upload_to='media/'),
        ),
    ]
