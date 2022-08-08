# Generated by Django 4.0.6 on 2022-08-06 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_schoolprofile_address_alter_schoolprofile_alt_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('SCHOOL', 'School'), ('GUARDIAN', 'Guardian')], default='GUARDIAN', max_length=50, null=True),
        ),
    ]
