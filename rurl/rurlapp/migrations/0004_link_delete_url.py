# Generated by Django 4.2.6 on 2023-11-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rurlapp', '0003_url_idd_alter_url_id_alter_url_lien'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lien', models.CharField(max_length=10000)),
                ('idd', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='url',
        ),
    ]
