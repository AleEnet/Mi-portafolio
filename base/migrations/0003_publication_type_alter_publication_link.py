# Generated by Django 4.1.4 on 2022-12-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_remove_publication_type_delete_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="publication",
            name="type",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="publication",
            name="link",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
