# Generated by Django 5.0 on 2024-01-18 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_chef'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef',
            name='slug',
            field=models.SlugField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
