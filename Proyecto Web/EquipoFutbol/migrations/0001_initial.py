
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipoFutbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('estadio', models.CharField(max_length=100)),
                ('fechafundacion', models.DateTimeField()),
                ('cantidadtitulos', models.IntegerField()),
                ('coloresequipacion', models.CharField(max_length=100)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ciudad.ciudad')),
            ],
        ),
    ]
