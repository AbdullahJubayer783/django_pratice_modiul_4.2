# Generated by Django 4.2.7 on 2023-12-21 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('release_date', models.DateField(auto_now_add=True)),
                ('Rating', models.CharField(choices=[('1', ' 1 star'), ('2', ' 2 star'), ('3', ' 3 star'), ('4', ' 4 star'), ('5', ' 5 star')], max_length=10)),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musicians')),
            ],
        ),
    ]