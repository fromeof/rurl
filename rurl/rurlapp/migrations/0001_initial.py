# Generated by Django 4.2.6 on 2023-11-27 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_originale', models.URLField()),
                ('url_raccourcie', models.URLField()),
            ],
        ),
    ]
