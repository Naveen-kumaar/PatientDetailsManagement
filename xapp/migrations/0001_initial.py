# Generated by Django 5.0.7 on 2025-01-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patientdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
                ('Address', models.TextField()),
                ('Contactno', models.IntegerField()),
                ('History', models.CharField(max_length=100)),
                ('Pain', models.CharField(max_length=100)),
                ('Duration', models.TimeField()),
            ],
        ),
    ]