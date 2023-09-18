# Generated by Django 3.2.11 on 2023-05-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycomics', '0005_typo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='own_default',
            field=models.BooleanField(default=None, null=True, verbose_name='default ownership status when adding items to this collection'),
        ),
        migrations.AlterField(
            model_name='collectionitem',
            name='own',
            field=models.BooleanField(default=None, null=True, verbose_name='ownership'),
        ),
        migrations.AlterField(
            model_name='collectionitem',
            name='was_read',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
