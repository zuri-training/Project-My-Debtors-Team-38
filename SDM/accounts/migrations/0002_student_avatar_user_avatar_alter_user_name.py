# Generated by Django 4.0.6 on 2022-08-06 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default='Ellipse 1.svg', max_length=255, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='Ellipse 1.svg', max_length=255, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
    ]
