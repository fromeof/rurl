# Generated by Django 4.2.6 on 2023-11-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rurlapp', '0002_remove_url_url_originale_remove_url_url_raccourcie_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='idd',
            field=models.CharField(default=10, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='url',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='url',
            name='lien',
            field=models.CharField(max_length=255),
        ),
    ]
