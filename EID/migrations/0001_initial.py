# Generated by Django 3.2.3 on 2021-08-28 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adhardocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=264)),
                ('phoneno', models.CharField(max_length=264, unique=True)),
                ('adhaarno', models.CharField(max_length=264, unique=True)),
                ('adhaar', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='buspassdocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=264)),
                ('phoneno', models.CharField(max_length=264, unique=True)),
                ('buspassno', models.CharField(max_length=264, unique=True)),
                ('buspass', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='dldocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=264)),
                ('phoneno', models.CharField(max_length=264, unique=True)),
                ('dlno', models.CharField(max_length=264, unique=True)),
                ('dl', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Docstatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vstat', models.CharField(max_length=264)),
                ('phoneno', models.CharField(max_length=264)),
                ('addharstatus', models.CharField(max_length=264)),
                ('passportstatus', models.CharField(max_length=264)),
                ('dlstatus', models.CharField(max_length=264)),
                ('pancardstatus', models.CharField(max_length=264)),
                ('voteridstatus', models.CharField(max_length=264)),
                ('rationcardstatus', models.CharField(max_length=264)),
                ('buspassstatus', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='pancarddocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=264)),
                ('phoneno', models.CharField(max_length=264, unique=True)),
                ('pancardno', models.CharField(max_length=264, unique=True)),
                ('pancard', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='passportdocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=264)),
                ('phoneno', models.CharField(max_length=264, unique=True)),
                ('passportno', models.CharField(max_length=264, unique=True)),
                ('passport', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='rationcarddocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=264)),
                ('phoneno', models.CharField(max_length=264, unique=True)),
                ('rationcardno', models.CharField(max_length=264, unique=True)),
                ('rationcard', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=264)),
                ('password', models.CharField(max_length=264)),
                ('phoneno', models.CharField(max_length=264)),
                ('gmailid', models.CharField(max_length=264)),
                ('dob', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='voteriddocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=264)),
                ('phoneno', models.CharField(max_length=264, unique=True)),
                ('voteridno', models.CharField(max_length=264, unique=True)),
                ('voterid', models.ImageField(upload_to='images')),
            ],
        ),
    ]
