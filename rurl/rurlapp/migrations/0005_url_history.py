# Generated by Django 4.2.6 on 2024-01-15 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rurlapp', '0004_link_delete_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='url_history',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('original_url', models.URLField()),
                ('short_url', models.URLField()),
            ],
        ),
    ]
