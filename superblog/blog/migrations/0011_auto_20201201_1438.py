# Generated by Django 3.1.3 on 2020-12-01 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_commet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commet',
            new_name='Comment',
        ),
    ]
