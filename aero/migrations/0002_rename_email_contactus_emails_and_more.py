# Generated by Django 4.0.4 on 2022-08-23 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aero', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='email',
            new_name='emails',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='fname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='lname',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='message',
            new_name='messages',
        ),
        migrations.RenameField(
            model_name='contactus',
            old_name='pname',
            new_name='phonename',
        ),
    ]