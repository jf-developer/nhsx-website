# Generated by Django 3.0.4 on 2020-04-01 15:42

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailnhsukfrontend.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionpage',
            name='headline',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='sectionpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hero_image', to='images.NHSXImage'),
        ),
        migrations.AddField(
            model_name='sectionpage',
            name='sub_head',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock(group=' Content')), ('block_quote', wagtail.core.blocks.BlockQuoteBlock(group=' Content')), ('embed', wagtail.embeds.blocks.EmbedBlock(group=' Content')), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))], group=' NHS Components')), ('panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group=' NHS Components')), ('promo', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('heading', wagtail.core.blocks.CharBlock(required=True)), ('description', wagtail.core.blocks.CharBlock(required=False)), ('content_image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small')], required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2))], group=' NHS Components')), ('expander', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))], group=' NHS Components')), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group=' NHS Components')), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))], group=' NHS Components')), ('panel_list', wagtail.core.blocks.StructBlock([('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('left_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('right_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))]))])))], group=' NHS Components')), ('promo_group', wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.ChoiceBlock(choices=[('one-half', 'One-half'), ('one-third', 'One-third')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small')], required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('promos', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.BasePromoBlock))], group=' NHS Components')), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group=' NHS Components'))], blank=True, verbose_name='Body blocks'),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock(group=' Content')), ('block_quote', wagtail.core.blocks.BlockQuoteBlock(group=' Content')), ('embed', wagtail.embeds.blocks.EmbedBlock(group=' Content')), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))], group=' NHS Components')), ('panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group=' NHS Components')), ('promo', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('heading', wagtail.core.blocks.CharBlock(required=True)), ('description', wagtail.core.blocks.CharBlock(required=False)), ('content_image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small')], required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2))], group=' NHS Components')), ('expander', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))], group=' NHS Components')), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group=' NHS Components')), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))], group=' NHS Components')), ('panel_list', wagtail.core.blocks.StructBlock([('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('left_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('right_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))]))])))], group=' NHS Components')), ('promo_group', wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.ChoiceBlock(choices=[('one-half', 'One-half'), ('one-third', 'One-third')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small')], required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('promos', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.BasePromoBlock))], group=' NHS Components')), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group=' NHS Components'))], blank=True, verbose_name='Body blocks'),
        ),
    ]
