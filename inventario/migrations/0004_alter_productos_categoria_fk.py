# Generated by Django 4.2.5 on 2023-10-04 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_categorias_productos_categoria_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='categoria_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.categorias'),
        ),
    ]
