# Generated by Django 2.0 on 2020-05-04 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(help_text='Область деятельности', max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Наименование', max_length=255)),
                ('code', models.CharField(help_text='Код товара', max_length=10)),
                ('cost', models.IntegerField(help_text='Стоимость')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('login', models.CharField(max_length=75, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(help_text='Имя', max_length=25)),
                ('lastname', models.CharField(help_text='Фамилия', max_length=50)),
                ('age', models.SmallIntegerField(help_text='Возраст')),
                ('email', models.EmailField(blank=True, help_text='e-mail', max_length=254)),
                ('social', models.CharField(blank=True, help_text='Профиль Facebook/Instagram', max_length=100)),
                ('activity', models.ForeignKey(help_text='Выбор деятельности', on_delete=django.db.models.deletion.PROTECT, to='userprofile.Activity')),
            ],
        ),
    ]