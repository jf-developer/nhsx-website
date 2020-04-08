# Generated by Django 3.0.4 on 2020-04-02 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('home', '0005_auto_20200402_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='fb_og_description',
            field=models.CharField(blank=True, help_text='Facebook OG description - max 300 chars', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='fb_og_image',
            field=models.ForeignKey(blank=True, help_text='Facebook OG image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.NHSXImage'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='fb_og_title',
            field=models.CharField(blank=True, help_text='Facebook OG title - max 40 chars', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='twitter_card_alt_text',
            field=models.CharField(blank=True, help_text='Twitter card image alt text - max 100 chars', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='twitter_card_description',
            field=models.CharField(blank=True, help_text='Twitter card description - max 200 chars', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='twitter_card_image',
            field=models.ForeignKey(blank=True, help_text='Twitter card image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.NHSXImage'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='twitter_card_title',
            field=models.CharField(blank=True, help_text='Twitter card title - max 40 chars', max_length=40, null=True),
        ),
    ]
