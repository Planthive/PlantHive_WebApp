# Generated by Django 3.2.5 on 2021-08-13 09:55

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actuators', djongo.models.fields.JSONField()),
                ('sensors', djongo.models.fields.JSONField()),
                ('metadata', djongo.models.fields.JSONField()),
                ('system', djongo.models.fields.JSONField()),
            ],
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
    ]
