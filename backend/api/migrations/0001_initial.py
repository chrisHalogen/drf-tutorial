# Generated by Django 5.0 on 2023-12-22 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('major', models.CharField(max_length=45)),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('is_active', models.BooleanField(default=True)),
                ('graduation_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
