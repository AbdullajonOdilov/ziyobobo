# Generated by Django 4.1.4 on 2022-12-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasm', models.FileField(upload_to='')),
                ('sarlavha', models.CharField(max_length=150)),
                ('sarlavha_uz_latn', models.CharField(max_length=150, null=True)),
                ('sarlavha_en', models.CharField(max_length=150, null=True)),
                ('sarlavha_ru', models.CharField(max_length=150, null=True)),
                ('sana', models.DateField()),
                ('matn', models.TextField()),
                ('matn_uz_latn', models.TextField(null=True)),
                ('matn_en', models.TextField(null=True)),
                ('matn_ru', models.TextField(null=True)),
                ('korishlar_soni', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
