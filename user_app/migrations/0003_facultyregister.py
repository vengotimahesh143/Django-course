# Generated by Django 3.2.5 on 2021-07-18 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_auto_20210718_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=40, null=True)),
                ('phone', models.CharField(max_length=10)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
                ('dob', models.DateField(null=True)),
            ],
        ),
    ]
