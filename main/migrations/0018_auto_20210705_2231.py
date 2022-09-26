# Generated by Django 3.2 on 2021-07-05 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0017_alter_cartorder_order_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productreview',
            options={'verbose_name_plural': '10. Reviews'},
        ),
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name_plural': '11. Wishlist'},
        ),
        migrations.CreateModel(
            name='UserAddressBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '12. AddressBook',
            },
        ),
    ]
