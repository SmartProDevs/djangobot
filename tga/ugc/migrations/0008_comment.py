# Generated by Django 3.2.4 on 2021-07-08 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0007_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('comment_text', models.TextField()),
                ('username', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Kommentariya',
                'verbose_name_plural': 'Kommentariyalar',
                'db_table': 'comment',
                'managed': False,
            },
        ),
    ]