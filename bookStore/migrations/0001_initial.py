
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('wikipedia', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, max_length=100)),
                ('summary', models.CharField(blank=True, max_length=100)),
                ('category', models.CharField(choices=[('AVENTURE', 'Aventure'), ('THRILLER', 'Thriller'), ('FANTASTIQUE', 'Fantastique'), ('ROMANCE', 'Romance'), ('HORREUR', 'Horreur'), ('SCIENCEFICTION', 'cience-fiction')], max_length=30)),
                ('stock', models.IntegerField(blank=True, default=0)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='GestionLivre.author')),
            ],
        ),
    ]