from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def include_css(file_name, media="screen,projection"):
    static_url = settings.STATIC_URL
    return """
    <link rel="stylesheet" type="text/css" href="{}base/stylesheets/{}" media="{}" />
    """.format(static_url, file_name, media)

@register.simple_tag
def include_js(file_name):
    static_url = settings.STATIC_URL
    return """
    <script src="{}base/javascripts/{}" type="text/javascript"></script>
    """.format(static_url, file_name)

@register.simple_tag
def include_image(image_name):
    static_url = settings.STATIC_URL
    return """
        <img src="{}base/images/{}" />
    """.format(static_url, image_name)

@register.simple_tag
def include_leaflet(version="0.4.4", cdn=False):
    static_url = settings.STATIC_URL+"base/"
    return """\
    <link rel="stylesheet" href="frameworks/{0}leaflet-{1}/leaflet.css" />
    <!--[if lte IE 8]>
        <link rel="stylesheet" href="frameworks/{0}leaflet-{1}/leaflet.ie.css" />
    <![endif]-->
    <script src="frameworks/{0}leaflet-{1}/leaflet.js"></script>
    <script src="frameworks/{0}leaflet-{1}/leafclusterer.js"></script>
    <script type="text/javascript" src="http://maps.stamen.com/js/tile.stamen.js?v1.1.3"></script>   
    """.format("http://cdn.leafletjs.com/" if cdn else static_url, version)
