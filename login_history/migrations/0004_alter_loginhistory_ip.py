# Generated by Django 5.0 on 2024-06-12 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_history', '0003_alter_loginhistory_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginhistory',
            name='ip',
            field=models.CharField(blank=True, max_length=39, null=True),
        ),
    ]
