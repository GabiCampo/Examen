# Generated by Django 4.2.2 on 2023-07-10 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_boleta'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleBoleta',
            fields=[
                ('id_detalle_boleta', models.AutoField(primary_key=True, serialize=False)),
                ('boleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.boleta')),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
            ],
        ),
    ]
