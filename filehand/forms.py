'''
    http://django-crispy-forms.readthedocs.io/en/latest/form_helper.html
    http://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_formsets.html
            
        #HTML("{% if forloop.first %} <div> {{ 'code' }} </div>{% endif %}"),
        
        #MultiField("Text for the label {{ username }}", does not work
        #    'code',
        #   'name'
        #),
                  
        #Div('code_label', css_class="col-sm-6"), does not work. How reference label
    
'''
import os
import sys
import os.path
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import ModelForm, modelformset_factory, formset_factory
from .models import Articles, Clas, SubClas, DocType, ArticleImages

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset, ButtonHolder, Div, Row, HTML, MultiField
from crispy_forms.bootstrap import AppendedText, PrependedAppendedText, StrictButton, FieldWithButtons, FormActions 
from django.forms.widgets import Widget
import widgets
from django.core.exceptions import ValidationError
'''
    Used to show articles present in the file system but not in the database
'''
class ArticlesCollectForm(forms.Form):
    file_name = forms.CharField(max_length = 100)
    
ArticlesCollectFormSet = formset_factory(ArticlesCollectForm)

class ArticlesCollectFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ArticlesCollectFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_show_labels = False
        self.form_class = 'ArticlesCollectForm'
        self.layout = Layout(
            Div(
                Div('file_name', css_class="col-sm-offset-2 col-sm-10"),
                css_class="row"),
            )
        self.add_input(Submit("submit", "Registrar En La Base De Datos", style="margin: 12px 0 0 0; text-align:center"))
        self.render_required_fields = True
'''
'''
class ArticlesMgrForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['file', 'file_name', 'clas', 'subClas', 'docType', 'author', 'access_by_group', 'access_by_status']
        #widgets = {'author': forms.TextInput,}
    #def __init__(self, *args, **kwargs):
    #    self.author = kwargs.pop('author', None)
    #    super(ArticlesForm, self).__init__(*args, **kwargs)

    def clean(self):
        #x = str(request.user.id)
        #try:
        #    author = Articles.objects.get( author = self.author )
        #    print('\n>>> In ArticlesForm, user name = ' + str(author) )
        #except:
        #    pass
        #print('\n\n\ndoing clean')
        data = self.cleaned_data
        # self.file_name is not filled in in the form for file uploads so fill it in here
        if data.get('file_name') == '':
            #for key, value in data.items():
                #print(str(key), str(value))
            try: # if no file was selected there is no item 'file'
                data['file_name'] = data.get('file').name
            except:
                self.add_error('file_name', 'Sin nombre de archivo a subir')
                raise ValidationError('Sin archivo seleccionado')
                return data
        # if file name already in db raise error
        if data.get('pk') == None:
            #print('\n\n>>> data.file.name = ' + data.file.name)
            raiseError = ''
            try:
                fileName = data.get('file').name
                Articles.objects.get( file_name = fileName )
                #print('\n\n>>> File found: ' + data.get('file').name + '\n>>>\n')
                raiseError = 'Nombre de archivo repetido: ' + fileName
            except Exception as e:
                # will raise error if get found 0 or more than 1 match
                #print('\n\n>>> Exception: ' + str(e) + '\n>>>\n')
                pass
            if raiseError != '':
                self.add_error('file_name', 'Ya existe')
                raise ValidationError('Nombre de archivo ' + fileName)
        
        if data.get('author') == None:
            data['access_by_status'] = 'anonimous'
            data['access_by_group'] = None
        return data
'''
'''
articlesMgrFormSet = modelformset_factory(Articles, ArticlesMgrForm, extra=1, min_num=0, validate_min=False, can_delete=True)
'''
'''
class ArticlesMgrFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ArticlesMgrFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_show_labels = False
        #self.form_style = 'inline'
        self.form_class = 'articles-form'
        #self.form_show_errors = False
        self.layout = Layout(
            Div(
                HTML("{% if forloop.first %} \
                    <div class = 'col-xs-1'> <label class='col-xs-18 text-xs-center ttip2' title='1: Cargar imágenes, 2: Editar documento, 3: Ver documento' > Acciones </label> </div> \
                    <label class='col-xs-4 text-xs-center ttip2' title='Hasta 100 caracteres' > Archivo* </label> \
                    <label class='col-xs-2 text-xs-center ttip2' title='Selecciona + para agregar nueva' > Clasificación </label> \
                    <label class='col-xs-2 text-xs-center ttip2' title='Selecciona + para agregar nueva' > Sub Clas </label> \
                    <label class='col-xs-2 text-xs-center ttip2' title='Selecciona + para agregar nuevo' > Tipo de Doc </label> \
                    <label class='col-xs-2 text-xs-center ttip3', title='=Usuario' > Autor </label> \
                    <label class='col-xs-2 text-xs-center ttip5' title='Estatus en el sistema'> Acceso Por Tipo </label> \
                    <label class='col-xs-2 text-xs-center ttip4' title='Permisos por grupo. Si no sabes pregunta' > Acceso Por Grupo </label> \
                    <label class ='col-xs-1 text-xs-center ttip1' title='Selecciona para borrar'><i class='fa fa-trash' aria-hidden='true'></i></label> \
                    {% endif %}"),
                css_class="row font-weight-bold"),
            Div(
                #Div('DELETE', css_class="col-xs-1", style="margin-top: 7px"),
                # <a class="link" href="/filehand/article_display/Text%20To%20Speech%20Pointers.html"> &nbsp; <i class="fa fa-file-o" aria-hidden="true"></i> &nbsp; Text To Speech Pointers </a>
                
                Div(
                    #Field('DELETE', css_class="col-xs-6", style="margin-top: 7px"),
                    
                    #HTML('{% if forloop.revcounter != 1 %}<a class="fa fa-file col-xs-9 text-xs-center" style="padding:5px 0 0 0" data-toggle="modal" href="not_required" \
                    #  data-popup-url=' + "{% url 'uploadArticleImages' 'gato' %}" + ' \
                    #  data-target="#modal" data-popup-title="Subir / Borrar Imágenes de Artículos" title="Imágenes del artículo" tabindex="-1"></a>{% endif %}'),
                    # <a class="nav-link" href="{% url 'about' %}">About <span class="sr-only">(about)</span> </a>
                    #<a class="link" href="{% url 'articleEdit' datum.3 %}"> &nbsp; <i class="fa fa-pencil-square-o" aria-hidden="true"></i> </a>
                    
                    HTML('{% if forloop.revcounter != 1 %} \
                        <a class="fa fa-file-image-o col-xs-6 text-xs-center" data-toggle="modal" href="not_required" \
                        data-popup-url=' + "{% url 'uploadArticleImages' 'perro.html' %}" + ' \
                        data-target="#modal" data-popup-title="Subir / Borrar Imágenes de Artículos" title="Imágenes del artículo" tabindex="-1"></a> \
                        <a class="fa fa-pencil-square-o col-xs-6" href=' + "{% url 'articleEdit' 'pistol.html' 'ArticlesMgr' %}" + '  target="_blank"></a> \
                        <a class="fa fa-file-o col-xs-6" href=' + "{% url 'article_display' 'gato.html' 'ArticlesMgr' %}" + ' target="_blank"></a> \
                        {% endif %}'),
                    
                    #HTML('{% if forloop.revcounter != 1 %}<a class="fa fa-file-image-o col-xs-6 text-xs-center" style="padding:5px 0 0 0" data-toggle="modal" href="not_required" \
                    #  data-popup-url=' + "{% url 'uploadArticleImages' 'perro.html' %}" + ' \
                    #  data-target="#modal" data-popup-title="Subir / Borrar Imágenes de Artículos" title="Imágenes del artículo" tabindex="-1"></a>{% endif %}'),
                    
                    css_class="col-xs-1", style="padding:5px 0 0 0"),
                
                
                Div('file_name', css_class="col-xs-4"),
                Div('clas', css_class="col-xs-2"),
                Div('subClas', css_class="col-xs-2"),
                Div('docType', css_class="col-xs-2"),
                Div('author', css_class="col-xs-2"),
                Div('access_by_status', css_class="col-xs-2"),
                Div('access_by_group', css_class="col-xs-2"),
                Field('DELETE', css_class="col-xs-1", style="margin-top: 7px"),
                #HTML('{% if forloop.revcounter != 1 %}<a class="fa fa-file-image-o col-xs-1 text-xs-center" style="padding:5px 0 0 0" data-toggle="modal" href="not_required" \
                #      data-popup-url=' + "{% url 'uploadArticleImages' 'perro.html' %}" + ' \
                #      data-target="#modal" data-popup-title="Subir / Borrar Imágenes de Artículos" title="Imágenes del artículo" tabindex="-1"></a>{% endif %}'),
                #HTML('<a class="link" style="padding:10px 0 0 0; color:red" href=' + "{% url 'uploadArticleImages' 'perro' %}" + '> <i class="fa fa-check-square" aria-hidden="true"></i> </a>'),
                css_class="row"),
            Div(
                Div(css_class="col-xs-1"),
                Div('file', css_class="col-xs-8"),
                css_class="row"),
            HTML('{% if forloop.revcounter == 1 %} \
                <div class="row"> <div class="col-xs-1"> </div>\
                <div class="form-actions col-xs-8"> <input name="submit" value="Guardar" class="btn btn-primary" id="submit-id-submit" type="submit"> </div> \
                </div> \
                {% endif %}'),
            )
        #self.add_input(Submit("submit", "Guardar", style="margin: 12px 0 0 46px; text-align:center"))    
        self.render_required_fields = True
'''
'''
class GalleryDocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
    def clean(self):
        acceptedExtensions = [".jpg",".png",".gif"]
        data = self.cleaned_data
        fileName = data.get("docfile").name
        print('fileName = ' + fileName)
        extension = os.path.splitext(fileName)[1]
        print('extension = ' + extension)
        if extension not in acceptedExtensions[:]:
            self.add_error("docfile", "Extensiones aceptadas: .jpg, .png, .gif")
            raise ValidationError("Extensión Inválida.")
            return data
        return data

'''
    This form along with ClassificationFormSet and ClassificationFormSetHelper is used to handle the entering, editing and deleting of entries for the Clas model.
    - Look at classifications.html to see how little template code is required to carry out all the work of handling the user interface.
    - Look at how little code goes into the classify view too.
    With this I came to realize the value of working with helpers and crispy forms. They do help a lot in achieving the Don't Repeat Yourself vision.  
'''
class ClassificationForm(forms.ModelForm):
    class Meta:
        model = Clas
        fields = ['code', 'name']
    def clean_code(self):
        return self.cleaned_data['code'].upper()
    def clean_name(self):
        return self.cleaned_data['name'].capitalize()

ClassificationFormSet = modelformset_factory(Clas, ClassificationForm, extra=1, min_num=1, validate_min=False, can_delete=True)

'''
'''
class ClassificationFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ClassificationFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_show_labels = False
        #self.form_show_errors = False
        self.layout = Layout(
            Div(
                HTML("{% if forloop.first %} \
                    <div class='text-xs-center'> \
                    <label class='col-md-1 ttip1' title='Records a borrar'><i class='fa fa-trash' style='' aria-hidden='true'></i></label> \
                    <label class='col-md-5 ttip2' title='2 caracteres'> Código* </label> \
                    <label class='col-md-12 ttip3' title='Hasta 24 caracteres' > Clasificación* </label> \
                    </div> \
                    {% endif %}"),
                css_class="row", style="font-weight:bold"),
            Div(
                Div('DELETE', css_class="col-sm-1", style="margin-top: 6px"),
                Div('code', css_class="col-md-5 text-xs-center"),
                Div('name', css_class="col-md-12"),
                css_class="row"),
            Div(css_class="col-sm-1")
            )
        self.add_input(Submit("submit", "Guardar", style="margin: 12px 0 0 0; text-align:center"))    
        self.render_required_fields = True

class ClasForm(forms.ModelForm):
    class Meta:
        model = Clas
        fields = ['code', 'name']
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_show_labels = False
        self.helper.form_id = 'add-clas'
        self.helper.layout = Layout(
        Div(
            Div('code', css_class="col-sm-1"),
            Div('name', css_class="col-sm-3"),
            css_class="row", style="line-height: 24px"),
        HTML('<div class="row"><div class="btn-group" style="margin: 12px 0 0 46px"> \
              <input id="submit-id-submit" class="btn btn-primary" type="submit" value="Guardar" name="Guardar"></input></div></div>')
        )
        super(ClasForm, self).__init__(*args, **kwargs)
'''
'''
class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['file', 'file_name', 'author', 'access_by_group', 'access_by_status']
        #widgets = {'author': forms.TextInput,}
    #def __init__(self, *args, **kwargs):
    #    self.author = kwargs.pop('author', None)
    #    super(ArticlesForm, self).__init__(*args, **kwargs)

    def clean(self):
        #x = str(request.user.id)
        #try:
        #    author = Articles.objects.get( author = self.author )
        #    print('\n>>> In ArticlesForm, user name = ' + str(author) )
        #except:
        #    pass
        print('\n\n\ndoing clean')
        data = self.cleaned_data
        # self.file_name is not filled in in the form for file uploads so fill it in here
        if data.get('file_name') == '':
            #for key, value in data.items():
                #print(str(key), str(value))
            try: # if no file was selected there is no item 'file'
                data['file_name'] = data.get('file').name
            except:
                self.add_error('file_name', 'Sin nombre de archivo a subir')
                raise ValidationError('Sin archivo seleccionado')
                return data
        # if file name already in db raise error
        if data.get('pk') == None:
            #print('\n\n>>> data.file.name = ' + data.file.name)
            raiseError = ''
            try:
                fileName = data.get('file').name
                Articles.objects.get( file_name = fileName )
                #print('\n\n>>> File found: ' + data.get('file').name + '\n>>>\n')
                raiseError = 'Nombre de archivo repetido: ' + fileName
            except Exception as e:
                # will raise error if get found 0 or more than 1 match
                #print('\n\n>>> Exception: ' + str(e) + '\n>>>\n')
                pass
            if raiseError != '':
                self.add_error('file_name', 'Ya existe')
                raise ValidationError('Nombre de archivo ' + fileName)
        
        if data.get('author') == None:
            data['access_by_status'] = 'anonimous'
            data['access_by_group'] = None
        return data
        
articlesFormSet = modelformset_factory(Articles, ArticlesForm, extra=1, min_num=0, validate_min=False, can_delete=True)
    
'''
DEFFINITION FOR 18 COLUMNS
'''
class ArticlesFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ArticlesFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_show_labels = False
        #self.form_style = 'inline'
        self.form_class = 'articles-form'
        #self.form_show_errors = False
        self.layout = Layout(
            Div(
                HTML("{% if forloop.first %} \
                    <div class='row'> \
                    <label class ='col-sm-1 text-xs-center ttip1' title='Selecciona artículos a borrar'><i class='fa fa-trash' style='padding-left:8px' aria-hidden='true'></i></label> \
                    <label class='col-sm-8 text-xs-center ttip2' title='Hasta 100 caracteres' > Archivo* </label> \
                    <label class='col-sm-2 text-xs-center ttip3', title='Autoasignado' > Autor </label> \
                    <label class='col-sm-3 text-xs-center ttip5' title='Estatus en el sistema'> Acceso Por Tipo </label> \
                    <label class='col-sm-3 text-xs-center ttip4' title='Permisos por grupo. Si no sabes pregunta' > Acceso Por Grupo </label> \
                    <label class='col-sm-1  text-xs-center ttip6', title='Imágenes referenciadas en el artículo'> Img </label> \
                    </div> \
                    {% endif %}"),
                css_class="row font-weight-bold"),
            Div(
                Field('DELETE', css_class="col-sm-1", style="margin-top: 12px"),
                Div('file_name', css_class="col-sm-8"),
                Div('author', css_class="col-sm-2"),
                Div('access_by_status', css_class="col-sm-3"),
                Div('access_by_group', css_class="col-sm-3"),
                HTML('<a class="fa fa-picture-o col-sm-1 text-xs-center" style="padding:10px 0 0 0" data-toggle="modal" href="not_required" \
                      data-popup-url=' + "{% url 'uploadArticleImages' 'perro' %}" + ' \
                      data-target="#modal" data-popup-title="Subir / Borrar Imágenes de Artículos" title="Imágenes del artículo" tabindex="-1"></a>'),
                #HTML('<a class="link" style="padding:10px 0 0 0; color:red" href=' + "{% url 'uploadArticleImages' 'perro' %}" + '> <i class="fa fa-check-square" aria-hidden="true"></i> </a>'),
                css_class="row"),
            Div(
                Div(css_class="col-sm-1"),
                Div('file', css_class="col-sm-8"),
                css_class="row"),
            HTML('{% if forloop.revcounter == 1 %} \
                <div class="row"> <div class="col-sm-1"> </div>\
                <div class="form-actions col-sm-8"> <input name="submit" value="Guardar" class="btn btn-primary" id="submit-id-submit" type="submit"> </div> \
                </div> \
                {% endif %}'),
            )
        #self.add_input(Submit("submit", "Guardar", style="margin: 12px 0 0 46px; text-align:center"))    
        self.render_required_fields = True

class ArticleImagesForm(forms.ModelForm):
    class Meta:
        model = ArticleImages
        fields = ['file', 'file_name']
    # STILL HAVE TO CHECK/VALIDATE IF FILE EXISTS
    def clean(self):
        data = self.cleaned_data
        # if file name already in db raise error
        if data.get('pk') == None:
            raiseError = ''
            try:
                ArticleImages.objects.get( file_name = data.get('file').name )
                print('\n\n>>> File found: ' + data.get('file').name + '\n>>>\n')
                raiseError = 'Nombre de archivo repetido'
            except Exception as e:
                # will raise error if get found 0 or more than 1 match
                #print('\n\n>>> Exception: ' + str(e) + '\n>>>\n')
                pass
            if raiseError != '':
                self.add_error('file_name', '*Ya existe')
                raise ValidationError('Nombre de archivo repetido')
        return data
    
articleImagesFormSet = modelformset_factory(ArticleImages, ArticleImagesForm, extra=1, min_num=0, validate_min=False, can_delete=True)

class ArticleImagesFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ArticleImagesFormSetHelper, self).__init__(*args, **kwargs)
        self.form_method = 'post'
        self.form_show_labels = False
        self.form_class = 'images-form'
        self.form_id = 'ajax_form_modal_result'
        self.layout = Layout(
            Div(
                HTML("{% if forloop.first %} \
                    <div class='row' style='margin-bottom:6px'> \
                    <label class ='col-xs-1 text-xs-right ttip1' style='margin-left:-2px;' title='Selecciona imágenes a borrar'><i class='fa fa-trash' aria-hidden='true'></i></label> \
                    <label class='col-md-12 text-xs-center ttip2' title='1..n-1 son imágenes ya subidas, n es para subir otra.' > Imágenes </label> \
                    <label class='col-md-5 text-xs-center ttip3', title='Selecciona imágen a subir' > Subir </label> \
                    </div> \
                    {% endif %}"),
                css_class="row font-weight-bold"),
            Div(
                #Field('DELETE', style="margin-top: 15px"),
                Div('DELETE', css_class="col-xs-1 text-xs-center", style="margin-top:6px"),
                Div('file_name', css_class="col-md-12", style="text-align:left"),
                Div('file', css_class="col-md-5", style="text-align:left; margin:4px 0 0 0"),
                css_class="row", style="padding: 0 0 0 0px; margin:0 0 0 0;"),
            HTML('{% if forloop.revcounter == 1 %} \
                <div class="row" style="padding: 0 0 0 0px;"><div class="col-sm-1"></div><div class="btn-group col-sm-4" style="margin:16px 0 -12px 0"> \
                <input id="modal-form-submit" class="btn btn-primary" \
                data-popup-url=' + "{% url 'uploadArticleImages' ' ' %}" + ' \
                type="" value="Guardar" name="Guardar"></input></div></div> \
                {% endif %}'),
            )
        
        #self.add_input(Submit("submit", "Guardar", style="margin: 12px 0 0 40px; text-align:center"))

        self.render_required_fields = True

'''
from .models import Tiny_MCE
class TinyMCEform(forms.ModelForm):
    class Meta:
        model = Tiny_MCE
        fields = ['content'] 
'''
'''
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
class FlatPageForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = FlatPage
        fields = ['content']
'''
class DummyForm(forms.Form):
    dummyField = forms.CharField(initial="dummy HTML")
    fileName = forms.CharField(initial="dummy HTML fileName")
'''
'''
HORMA_CHOICES = (
    ('articulo', 'Artículo'),
    ('nota', 'Nota'),
    ('recordatorio', 'Recordatorio'),
    ('vacio', 'Vacío')
)
class NewDocumentForm(forms.Form):
    fileName = forms.CharField(
        max_length = 100)
    horma = forms.ChoiceField(
        choices = HORMA_CHOICES
        )
    
    def clean(self):
        data = self.cleaned_data
        fileName = data.get("fileName")
        extension = os.path.splitext(fileName)[1]
        if extension == "":
            fileName = fileName.title() + ".html"
        elif extension == ".html":
            fileName = os.path.splitext(fileName)[1].title() + ".html"
        else:
            self.add_error("fileName", "No uses puntos en el nombre del archivo, excepto el punto de la extensión '.html'. Si no incluyes la extensión, se asume '.html'.")
            raise ValidationError("Extensión Inválida.")
            return data 
        import re
        #pattern = re.compile("^[a-zA-Z][\w -]*.html")
        pattern = re.compile("([-_$@#()^=&,'áéíóúÁÉÍÓÚ \w\d+]+.html)$")
        if pattern.match(fileName):
            pass
        else:
            self.add_error("fileName", "Carácteres prohibidos: < > : \ / | ? * doble comilla y . excpto en .html")
            raise ValidationError("Nombre Inválido.")
            return data
        data["fileName"] = fileName
        return data