# Generated by Django 4.2.4 on 2023-09-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_evento_usuario_alter_evento_data_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='local',
            field=models.Field(blank=True, max_length=100, null=True),
        ),
    ]
