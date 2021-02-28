# Generated by Django 3.1.5 on 2021-02-27 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_article_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='publications',
            field=models.ManyToManyField(to='recipes.Publication'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]