# Generated by Django 4.2.5 on 2023-10-11 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0030_remove_userprofile_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo_barras',
            field=models.CharField(default='da93712a10b740e198d855051dafdb32', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
