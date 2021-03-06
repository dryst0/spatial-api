# Generated by Django 3.1.2 on 2020-10-03 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminlevel1',
            name='iso_3166_alpha_3',
        ),
        migrations.AddField(
            model_name='adminlevel1',
            name='iso',
            field=models.CharField(default='', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adminlevel0',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='adminlevel1',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='adminlevel2',
            name='iso_3166_alpha_3',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='adminlevel3',
            name='iso_3166_alpha_3',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='adminlevel3',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='adminlevel4',
            name='iso_3166_alpha_3',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='adminlevel4',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='adminlevel5',
            name='iso_3166_alpha_3',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='adminlevel5',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
