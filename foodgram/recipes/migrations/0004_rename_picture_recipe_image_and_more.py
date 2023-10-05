# Generated by Django 4.2.5 on 2023-09-23 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_remove_recipe_tags_recipetag_recipe_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='picture',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='is_favorited',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='is_in_shopping_cart',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='recipetag',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipetag_recipe', to='recipes.recipe'),
        ),
    ]