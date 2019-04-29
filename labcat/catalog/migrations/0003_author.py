from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('first name', models.CharField(max_length=32)),
                ('middle name', models.CharField(max_length=32)),
                ('last name', models.CharField(max_length=32)),
            ],
        )
    ]
