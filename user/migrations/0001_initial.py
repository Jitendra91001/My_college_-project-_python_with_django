# Generated by Django 3.2.4 on 2021-09-30 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=38)),
                ('cpic', models.ImageField(default='', upload_to='static/pcategory/')),
                ('cdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200)),
                ('cpic', models.ImageField(default='', upload_to='static/course')),
                ('cdate', models.DateField()),
                ('cadmission', models.CharField(max_length=100)),
                ('cduration', models.CharField(max_length=100)),
                ('chead', models.CharField(max_length=100)),
                ('cseat', models.CharField(max_length=100)),
                ('cdescription', models.CharField(max_length=100)),
                ('ctotal', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdes', models.CharField(max_length=200)),
                ('gpic', models.ImageField(default='', upload_to='static/gallery/')),
                ('gdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='recruiterss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rpic', models.ImageField(default='', upload_to='static/recruiters/')),
                ('rdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='placements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=80)),
                ('cmpname', models.CharField(max_length=80)),
                ('cmplogo', models.ImageField(default='', upload_to='static/placement/')),
                ('city', models.CharField(max_length=100)),
                ('pyear', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('stupic', models.ImageField(default='', upload_to='static/studentpic/')),
                ('pdate', models.DateField()),
                ('pcourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.courses')),
            ],
        ),
    ]
