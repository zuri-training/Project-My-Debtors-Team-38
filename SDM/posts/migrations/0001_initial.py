# Generated by Django 4.0.6 on 2022-08-07 16:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0007_remove_student_debt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt_incured', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(verbose_name=datetime.datetime.now)),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.school')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
        ),
        migrations.CreateModel(
            name='Contend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('made_payment', models.BooleanField(default=False)),
                ('receipt', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('debt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.debt')),
                ('guardian_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.guardian')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(verbose_name=datetime.datetime.now)),
                ('updated_at', models.DateTimeField(verbose_name=datetime.datetime.now)),
                ('debt_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.debt')),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.school')),
            ],
        ),
    ]