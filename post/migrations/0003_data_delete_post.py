# Generated by Django 4.1.7 on 2023-03-11 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_remove_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('area', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
