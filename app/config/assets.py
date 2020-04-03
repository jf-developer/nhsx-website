from django_assets import Bundle, register
from webassets.filter import get_filter
from django.conf import settings


LIBSASS = get_filter(
    'libsass'
)

uglify_js = get_filter(
    'uglifyjs',
    extra_args=['--source-map', '-c', '-m']
)


closure_js = get_filter(
    'closure_js'
)

if settings.DEBUG:
    css_filters = [LIBSASS]
    js_filters: list = []
else:
    css_filters = [LIBSASS, 'cssmin']
    js_filters = [closure_js]

core_css_files = [
    '_dev/scss/screen.scss'
]

admin_css_files = [
    '_dev/scss/admin.scss'
]

core_js_files = [
    '_dev/js/lib/cookieconsent.min.js',
    '_dev/js/main.js',
]

admin_js_files = [
    '_dev/js/admin.js'
]

css_core_bundle = Bundle(
    *core_css_files,
    depends="_dev/scss/**/*.scss",
    filters=css_filters,
    output='dist/dist/css/main.min.css'
)
register('css_core', css_core_bundle)


css_admin_bundle = Bundle(
    *admin_css_files,
    depends="_dev/scss/**/*.scss",
    filters=css_filters,
    output='dist/css/admin_extra.min.css'
)

js_core_bundle = Bundle(
    *core_js_files,
    filters=[closure_js],
    output='dist/js/main.min.js'
)

js_admin_bundle = Bundle(
    *admin_js_files,
    filters=[closure_js],
    output='dist/js/admin_extra.min.js'
)


register('css_core', css_core_bundle)
register('css_admin', css_admin_bundle)

register('js_core', js_core_bundle)
register('js_admin', js_admin_bundle)