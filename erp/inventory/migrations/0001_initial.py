# Generated by Django 3.2.13 on 2023-07-24 23:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('distributor', '0001_initial'),
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot', models.CharField(max_length=20)),
                ('expiry', models.DateField(default='4637-11-25')),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributor.item')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.batch')),
            ],
        ),
        migrations.CreateModel(
            name='InventoryIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.batch')),
                ('request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='request.requestitem')),
            ],
        ),
    ]
