# Generated by Django 3.2.20 on 2025-02-24 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20250224_1152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'managed': False, 'ordering': ['-created_at']},
        ),
    ]
