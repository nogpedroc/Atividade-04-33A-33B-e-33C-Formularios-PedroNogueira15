# Generated by Django 3.2.13 on 2023-09-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('trilogy', models.CharField(choices=[('OG', 'Original Trilogy'), ('SQ', 'Sequels Trilogy'), ('PQ', 'Prequels Trilogy')], max_length=2)),
                ('translation_PTBR', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SequelsPros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('irony', models.CharField(choices=[('I', 'Ironic'), ('R', 'For real')], max_length=1)),
                ('category', models.CharField(choices=[('CH', 'Chracters'), ('CA', 'Cast'), ('N', 'Nostalgia'), ('L', 'Lore'), ('P', 'Plot'), ('RD', 'Random')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='TableInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=4)),
                ('newName', models.CharField(max_length=50)),
                ('reason', models.CharField(max_length=250)),
            ],
        ),
    ]
