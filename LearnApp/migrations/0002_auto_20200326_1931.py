# Generated by Django 2.2 on 2020-03-26 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LearnApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Declaration_Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('question1', models.CharField(max_length=5)),
                ('question2', models.CharField(max_length=5)),
                ('question3', models.CharField(max_length=5)),
                ('question4', models.CharField(max_length=5)),
                ('question5', models.CharField(max_length=5)),
                ('question6', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gov_Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('question1', models.CharField(max_length=5)),
                ('question2', models.CharField(max_length=5)),
                ('question3', models.CharField(max_length=5)),
                ('question4', models.CharField(max_length=5)),
                ('question5', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='White_House_Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('question1', models.CharField(max_length=5)),
                ('question2', models.CharField(max_length=5)),
                ('question3', models.CharField(max_length=5)),
                ('question4', models.CharField(max_length=5)),
                ('question5', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='birthdate',
        ),
    ]
