# Generated by Django 4.2.6 on 2024-02-01 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0002_alter_book_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(),
        ),
    ]
