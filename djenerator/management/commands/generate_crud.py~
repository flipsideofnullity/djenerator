import os
from collections import deque

from django.conf import settings
from django.db.models import get_app, get_models
from django.template.loader import render_to_string as r2s
from django.core.management.base import BaseCommand, CommandError

APP_LEVEL_FILES = ["forms.py", "utils.py", "urls.py", "admin.py"]
TEMPLATE_SUFFICES = ["_form.html", "_list.html", "_detail.html", "_delete_confirm.html"]

model_class_raw = lambda m, as_is=False: "".join(
        [i.capitalize() if as_is else i for i in m._meta.verbose_name.split()])

def create_form_view(
        model_list, 
        path, 
        importlist=["from django import forms\n", "from .models import *",], 
        filename="forms.py",
        template_name="djenerator/forms.html"):
    os.chdir(path)
    contents, view_file = deque(), file(filename, "w")
    view_file.write("\n".join(importlist) + "\n\n")
    for model in model_list:
        model_class_name = model_class_raw(model, as_is=True)
        file_str = r2s(template_name, dict(model=model_class_name))
        contents.append(file_str)
    else:
        for idx in range(len(contents)):
            view_file.write(contents.pop())
            view_file.write("\n")
        else:
            view_file.close()
            

def create_admin_view(model_list, path):
    filename, template_name = "admin.py", "djenerator/admin.html"
    importlist = [
        "from django.contrib import admin\n",
        "from .models import *",
        "from .forms import *",        
    ]
    create_form_view(model_list, path, importlist, filename, template_name)
    
def create_classbased_view(model_list, path):
    filename, template_name = "views.py", "djenerator/views.html"
    importlist = [
        "from django.views.generic import *",
        "from django.db.models import Q",
        "from django.contrib import messages",        
        "from django.utils.translation import ugettext_lazy as _",        
        "from django.core.urlresolvers import reverse_lazy\n",        
        "from djenerator.views import *",
        "from .models import *",
        "from .forms import *",
    ]
    create_form_view(model_list, path, importlist, filename, template_name)    

def create_urls_view(model_list, path):
    filename, template_name = "urls.py", "djenerator/urls.html"
    
    importlist = [
        "from django.conf.urls import patterns, include, url\n",
        "from .views import *",
    ]
    
    os.chdir(path)
    contents, view_file = [], file(filename, "w")
    view_file.write("\n".join(importlist) + "\n\n")
    contents.append("    url(r'^$', TemplateView.as_view(template_name='{0}/{0}_base.html'), name='{0}-base'),".format(model_list[0]._meta.app_label, model_list[0]._meta.app_label.replace("_", "")))
    for model in model_list:
        model_class = model_class_raw(model, as_is=True)
        contents.append(
            "{0}url(r'^{1}/$', {2}ListView.as_view(), name='{1}-list'),".format(
                " "*4, model_class.lower(), model_class,))
        for partial in ["create", "update", "detail", "delete",]:
            line = "{0}url(r'^{1}/{2}/{3}', {4}{5}View.as_view(), name='{1}-{2}'),"
            url_line = line.format(
                " "*4, model_class.lower(), partial,
                "$" if partial in ["create", "list"] else "(?P<pk>[0-9]+)/$",
                model_class, partial.capitalize(),)
            contents.append(url_line)
        #contents.append("    ###")
    else:
        lines = r2s(template_name, dict(urlconf="\n".join(contents))) + "\n"
        view_file.write(lines)
        view_file.close() 

################ TEMPLATE STUFF
def get_fields(model):
    return list(
        set([
            i.name for i in model._meta.fields]
        ).difference(
            set(
                [
                    "created_at", 
                    "modified_at", 
                    "created_by", 
                    "modified_by", 
                    "is_deleted", 
                    "is_active", 
                    "version",
                    "id",
                ]
            )
        )
    )

def app_base_tpl(tpl_path, model_list):
    base_file = file(tpl_path, "w")
    base_file_content = r2s("djenerator/app_base.html", dict(model_list=[(model_class_raw(i), i._meta.verbose_name_plural) for i in model_list]))
    base_file.write(base_file_content)
    base_file.close()
    
def list_tpl(tpl_path, app_name, model_name, attrs):
    _file = file(tpl_path, "w")
    _file_content = r2s("djenerator/app_list.html", dict(app_name=app_name, model_name=model_name, attr_list=attrs))
    _file.write(_file_content)
    _file.close()

def form_tpl(tpl_path, app_name, model_name):
    _file = file(tpl_path, "w")
    _file_content = r2s("djenerator/app_form.html", dict(app_name=app_name, model_name=model_name))
    _file.write(_file_content)
    _file.close()

def delete_tpl(tpl_path, app_name, model_name):
    _file = file(tpl_path, "w")
    _file_content = r2s("djenerator/app_delete.html", dict(app_name=app_name, model_name=model_name))
    _file.write(_file_content)
    _file.close()

def detail_tpl(tpl_path, app_name, model_name, attrs):
    _file = file(tpl_path, "w")
    _file_content = r2s("djenerator/app_detail.html", dict(app_name=app_name, model_name=model_name, attr_list=attrs))
    _file.write(_file_content)
    _file.close()

###############################
def create_skeleton(app, module):
    app_dir = module.__path__[0]
    os.chdir(app_dir)
    module_name = module.__name__
    model_list = get_models(app)
    try:
        os.mkdir("templates")
        os.mkdir("templates/{}".format(module_name))
    except OSError: pass
    app_base_tpl("templates/{0}/{0}_base.html".format(module_name), model_list)
    for f in APP_LEVEL_FILES:
        pyf = file(f, "w")
        pyf.close()

    for model in model_list:
        model_name = model_class_raw(model)
        form_tpl("templates/{}/{}_form.html".format(module_name, model_name), module_name, model_name)
        delete_tpl(
            "templates/{}/{}_confirm_delete.html".format(
                module_name, model_name), module_name, model_name)
        list_tpl(
            "templates/{}/{}_list.html".format(
                module_name, model_name), module_name, model_name, get_fields(model))
        detail_tpl(
            "templates/{}/{}_detail.html".format(
                module_name, model_name), module_name, model_name, get_fields(model))                 
        #print "Templates created successfully"
    else:
        # NO EXCEPTIONS, THEREFORE WE CAN PROCEED
        create_form_view(model_list, app_dir)
        create_admin_view(model_list, app_dir)
        create_classbased_view(model_list, app_dir)
        create_urls_view(model_list, app_dir) 
        print "All models have their skeletons now"

class Command(BaseCommand):
    args = '<module_name>'
    help = 'Enter a module name and find information about that module'

    def handle(self, *args, **options):
        module_name = args[0]
        if len(args) != 1:
            raise CommandError('Please enter a single module name')

        try:
            app, module = get_app(module_name), __import__(module_name)
        except AssertionError:
            raise CommandError('App not found')
        #except Exception:
        #    raise CommandError('An unknown error occured')
        create_skeleton(app, module)
