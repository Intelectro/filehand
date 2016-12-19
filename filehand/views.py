'''
    filehand

'''
import os
import sys
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404 

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
import inspect
import os.path
import string
import re

from django import forms

from filehand.models import GalleryDocument, Clas, SubClas, DocType, Articles, ArticleImages
from django.contrib.auth.models import Group, User
from filehand.forms import GalleryDocumentForm
from filehand.forms import ClassificationForm, ClassificationFormSet, ClassificationFormSetHelper
from filehand.forms import ClasForm, ArticlesForm, articlesFormSet, ArticlesFormSetHelper, articlesMgrFormSet, ArticlesMgrFormSetHelper
from filehand.forms import ArticleImagesForm, articleImagesFormSet, ArticleImagesFormSetHelper
from filehand.forms import ArticlesCollectForm, ArticlesCollectFormSet, ArticlesCollectFormSetHelper
#from filehand.models import Tiny_MCE
#from filehand.forms import TinyMCEform

from django.conf import settings #or from my_project import settings
from pip._vendor import requests

from django.utils.translation import ugettext as _
from django.views.generic import View
from django.conf import settings

from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

import hashlib
from django.template.defaultfilters import last
from django.contrib.auth.models import User

from django.contrib.auth.decorators import permission_required

from PIL import Image
'''
fileIn is a file name in which spaces have been replaced with character "~" as in
    data-popup-url="/filehand/uploadArticleImages/IN-DJ-DO-Setting~Up~An~Existing~Django~Project~At~Localhost~In~Windows.html"

user is a username as in "admin"

Return the full URL of an existing file whose name in the file system matches fileIn with charecters "~" replaced with spaces
    if file not found then return the last file in database table Articles that was added by user
'''
def landing(request):
    pageName = 'landing-page.html'
    title = 'Landing Page'
    #form = SignUpForm(request.POST or None)
    #queryset = SignUp.objects.all().order_by('-timestamp')
    #context = {"pageName": pageName, "title": title, "form": form, }
    #context = {"pageName": pageName, "title": title, "form": form, 'request': request, 'user': request.user}
    context = {"pageName": pageName, "title": title, 'request': request, 'user': request.user}
    '''
    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        instance.save()
        context = {
            "title": 'Thank you for signing up',
            "pageName": pageName,
        }
   
    if request.user.is_authenticated() and request.user.is_staff:

        try:
            queryset = SignUp.objects.all().order_by('-timestamp')
        except:
            queryset = None
            pass
#         queryset = SignUp.objects.all().order_by('-timestamp').filter(full_name___iexact="Justin")
        context = {
            "queryset": queryset,
            "pageName": pageName,
            "title": title,
        }
    else:
        context = {
            "queryset": 'You Are Not Staff',
            "pageName": pageName,
            "title": title,
        }

        title = "After POST"
        context = {"pageName": pageName, "title": title, "form": form, "queryset": queryset, 'request': request, 'user': request.user}
    '''   
    return render(request, "landing-page.html", context)

def error(request):
    context = {'title': 'Error',
               'message_1': 'Si estas enfermo, ve a ver si tu mama te quiere cuidar.',
               'message_2': 'O cuida tu a tu mamá. O cuidense mutuamente.' }
    return render(request, 'error_page.html', context)

def user_page(request):
    pageName = 'user_page.html'
    title = 'user_name'
    '''
    print('str(request.user.groups): ' + str(request.user.groups) )
    print('str(request.user): ' + str(request.user) )
    print('request.user.is_staff: ' + str(request.user.is_staff) )
    print('request.user.is_authenticated(): ' + str(request.user.is_authenticated()) )
    print('user.get_all_permissions: ' + str(request.user.get_all_permissions()) )
    group = Group.objects.get(name='add_receipt')
    if group in request.user.groups.all():    
    '''
    print('\n\n*** FILE SYSTEM ACCESS TESTS BEGIN ***')
    print('BASE_DIR: ' + settings.BASE_DIR)
    print('STATICFILES_DIRS: ' + str(settings.STATICFILES_DIRS))
    
    print('MEDIA_URL: ' + settings.MEDIA_URL)
    print('MEDIA_ROOT: ' + settings.MEDIA_ROOT)
    
    print('STATIC_URL: ' + settings.STATIC_URL)
    print('STATIC_ROOT: ' + settings.STATIC_ROOT)
    
    print('LOCALE_PATHS: ' + str(settings.LOCALE_PATHS))
    
    print('\nNOW FIND THE RIGHT WAY TO ACCESS FILES')
    '''
    fileToReturn = os.path.join(settings.MEDIA_ROOT + '/articles/', fileToReturn)
    fileToReturn = os.path.abspath(fileToReturn)
    if os.path.isfile( fileToReturn ):
    '''
    fileToTry = Articles.objects.filter(author = 1 ).last()
    try:
        fileToTry = os.path.join(settings.MEDIA_ROOT, fileToTry.file.name)
        print('fileToTry = os.path.join(settings.MEDIA_ROOT, fileToTry.file.name')
        print('trying: ' + fileToTry)
        if os.path.isfile( fileToTry ):
            print('I S F I L E !')
        else:
            print('I S   N O T   F I L E !')
         
        fileToTry = Articles.objects.filter(author = 1 ).last()
        fileToTry = fileToTry.file
        print('fileToTry = fileToTry.file)')
        print('trying: ' + str(fileToTry))
        if os.path.isfile( fileToTry ):
            print('I S F I L E !')
        else:
            print('I S   N O T   F I L E !')
               
        #fileToTry = os.path.join(settings.MEDIA_ROOT, fileToTry.file.name)
        fileToTry = Articles.objects.filter(author = 1 ).last()
        print('fileToTry = Articles.objects.filter(author = 1 ).last()')
        print('trying: ' + str(fileToTry))
        if os.path.isfile( fileToTry ):
            print('I S F I L E !')
        else:
            print('I S   N O T   F I L E !')
    except:
        print('E X C E P T I O N !')
    print('\n*** NEXT TRY ***\n')

    fileToShow = 'MS-GE-RE-El Fascinante Mundo De Los Olores'
    fileToShow += '.html'
    file = os.path.join(settings.MEDIA_ROOT + '/articles/', fileToShow)
    file = os.path.abspath(file)
    print('trying: ' + file)
    if os.path.isfile( file ):
        print('I S F I L E !')
        #f = open(file, encoding='utf8')
        #fContents2 = f.read()
        #f.close()
    else:
        print('I S   N O T   F I L E !')
    print('*** FILE SYSTEM ACCESS TESTS END ***\n')

    clientIp = get_ip(request)
    
    context = {
        "pageName": pageName,
        "title": title,
        "clientIp": clientIp
    }

    return render(request, "user_page.html", context)

'''
get client ip address
'''
def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip

def whatArticleToProcess(fileIn, user):
    useLastFileInDb = False
    if fileIn == None or fileIn == ' ':
        useLastFileInDb = True
    else:
        fileToReturn = fileIn.replace('~', ' ')
        fileToReturn = os.path.join(settings.MEDIA_ROOT + '/articles/', fileToReturn)
        fileToReturn = os.path.abspath(fileToReturn)
        if os.path.isfile( fileToReturn ):
            #print('\n***\n*** 1.1: PARAMETER RECEIVED ONCE STRIPPED OF ~S IS FILE ! ' + fileToReturn + '\n***\n')
            title = 'Diálogo para subir imágenes referenciadas en un artículo seleccionado'
            useLastFileInDb = False
    if useLastFileInDb:
        print('FILE RECEIVED AS PARAMETER I S   N O T   F I L E ! so grab last file in db' + fileIn + '\n***\n')
        title = 'Diálogo para subir imágenes referenciadas en un artículo recien subido'
        try:
            fileToReturn = Articles.objects.filter(author = user).last()
            fileToReturn = os.path.join(settings.MEDIA_ROOT, fileToReturn.file.name)
            if os.path.isfile( fileToReturn ):
                useLastFileInDb = True
                title = 'Dialogo para subir imagenes referenciadas en un articulo recién subido'
        except:
            title = 'Problema: ningún artículo seleccionado y ningún artículo con el usuario actual como autor'
            fileToReturn = ' '
    return [fileToReturn, title]
'''
In template articlePermissions an article has been selected for uploading image files that it uses
Check what images it uses and which of them are already uploaded and pass this info to a template
    for the user to know what images he needs to upload
Process the form where user selects an image file to upload and assigns privacy permissions to it or
    selects one or more image files to delete 
'''
def uploadArticleImages(request, file = None):
    #print('__________________________________________________________________________________________________________')
    #print('\n***\n*** uploadArticleImages E N T E R E D !, file =  ' + file + '  \n***')
    articleToProcessAndPageTitle = whatArticleToProcess(file, request.user)
    articleToProcess = articleToProcessAndPageTitle[0]
    pageTitle = articleToProcessAndPageTitle[1]
    helper = ArticleImagesFormSetHelper()
                    
    f = open(articleToProcess, encoding='utf8')
    fContents = f.read()
    f.close()
    imagesInArticle = re.findall(r'src="(.*?)"', fContents)
    
    imagesInArticleHtml = []
    for image in imagesInArticle:
        newImage = os.path.split(image)[1]
        if not newImage in imagesInArticleHtml:
            imagesInArticleHtml.append(newImage)

    if request.method == 'GET':
        #print('G E T   G E T   G E T   G E T   G E T   G E T   G E T   G E T   G E T   G E T   G E T   G E T   G E T')
        imagesAlreadyUploaded = ArticleImages.objects.filter(file_name__in = imagesInArticleHtml)
        #print ('imagesAlreadyUploaded: ' + articleToProcess + ' follow')
        #for ex in imagesAlreadyUploaded:
        #    print('imagesAlreadyUploaded ', ex)
        context = {'articleProcessed': os.path.split(articleToProcess)[1], 
                   'title': pageTitle,
                   #'msg': 'It is a GET',
                   'imagesInArticleHtml': imagesInArticleHtml, 
                   'imagesAlreadyUploaded': imagesAlreadyUploaded, 
                   'formset': articleImagesFormSet(queryset = imagesAlreadyUploaded),
                   'helper': helper}

    if request.method == 'POST':
        #print('P O S T   P O S T   P O S T   P O S T   P O S T   P O S T   P O S T   P O S T   P O S T   P O S T   P O S T   ')
        '''
        if data in locals():
            print(' D A T A   I S           I N   L O C A L S')
        else:
            print(' D A T A   I S   N O T   I N   L O C A L S')
        '''
        data = request.POST
        files = request.FILES
        receivedFormset = articleImagesFormSet(data, files)
        #receivedFormset = articleImagesFormSet(data=request.POST, files=request.FILES)
        #for key, value in data.items():
        #    print ('data key = ' + key + ' value = ' + value)
        if receivedFormset.is_valid():
            #print ('\n>>>\n>>> = V A L I D  \n>>>')
            receivedFormset.save(commit=False)
            for form in receivedFormset:
                if form.cleaned_data.get('DELETE'):
                    fileToRemove = os.path.join(settings.MEDIA_ROOT, str(form.cleaned_data.get('file')))
                    fileToRemove = os.path.abspath(fileToRemove)
                    #print('\n>>> file to remove = ' + fileToRemove + '\n')
                    os.remove ( fileToRemove )
                else:
                    #for key, value in form.cleaned_data.items():
                    #    print('>>> file that appears in cleaned_data and is not marked for deletion: key= ' + str(key) + ' value = ' + str(value))
                    pass
            receivedFormset.save()
            imagesAlreadyUploaded = ArticleImages.objects.filter(file_name__in = imagesInArticleHtml)
            #print ('\n>>> imagesAlreadyUploaded: ' + articleToProcess + ' follow')
            #for ex in imagesAlreadyUploaded:
            #    print('imagesAlreadyUploaded ', ex)
            
            pageTitle = 'Check if the form was saved'
            msg = extractFormEditingResults(receivedFormset)
            
            context = {'articleProcessed': os.path.split(articleToProcess)[1], 
                       'title': pageTitle,
                       'msg': msg,
                       'imagesInArticleHtml': imagesInArticleHtml, 
                       'imagesAlreadyUploaded': imagesAlreadyUploaded, 
                       'formset': articleImagesFormSet(queryset = imagesAlreadyUploaded),
                       'helper': helper}
        else:
            print ('\n>>>\n>>> = N O T  V A L I D  \n>>>')
            pageTitle = 'Favor de CORREGIR'
            msg = extractFormEditingResults(receivedFormset)
            imagesAlreadyUploaded = ArticleImages.objects.filter(file_name__in = imagesInArticleHtml)
            context = {'articleProcessed': os.path.split(articleToProcess)[1], 
                       'title': pageTitle,
                       'msg': msg,
                       'imagesInArticleHtml': imagesInArticleHtml, 
                       'imagesAlreadyUploaded': imagesAlreadyUploaded, 
                       'formset': receivedFormset,
                       'helper': helper}
    #print('\n***\n*** uploadArticleImages R E T U R N I N G !, file =  ' + file + '\n***')
    #print('__________________________________________________________________________________________________________\n')
    return render(request, 'filehand/articleImagesUpload.html', context)
'''
Return the contents of an html file to be displayed in a modal window.
Used for example to display to the user information about the application or the webpage he is in.  
'''
def modalinfo(request, fileToShow):
    #print('\n>>>\n>>> In modalinfo, fileToShow = '+ fileToShow +'\n>>>\n')
    fileToShow += '.html'
    file = os.path.join(settings.MEDIA_ROOT + '/info/', fileToShow)
    file = os.path.abspath(file)
    if os.path.isfile( file ):
        #print('\n***\n*** 1.1: RECEIVED AS PARAMETER FILE IS FILE ! ' + file + '\n***\n')
        status = 'success'
        pass
    else:
        #print('RECEIVED AS PARAMETER FILE I S   N O T   F I L E ! ' + file + '\n***\n')
        file = os.path.join(settings.MEDIA_ROOT + '/info/', 'info_not_found.html')
        file = os.path.abspath(file)
        status = 'failure'
    f = open(file, encoding='utf8')
    fContents = f.read()
    f.close()
    return HttpResponse(fContents, status)
'''
Return articles that a user has permission to edit
'''
def getArticlesUserCanEdit(request):
    '''
    usersQuerySet = User.objects.values()
    print('\n>>>\n>>> Inspecting User.objects in A R T I C L E  P E R M I S S I O N S')
    x = str(request.user.id)
    print('>>> user id = ' + str(x) )
    for item in usersQuerySet:
        for key, value in item.items():
            print('>>> key = ' + str(key) + ' value = ' + str(value) )
    print('\n>>>')
    '''
    if request.user.is_superuser:
        toReturn = Articles.objects.all()
    else:
        user = request.user
        toReturn = Articles.objects.filter(author = user.id)
    return toReturn   
'''
    Find articles (html documents) in /media_root/articles that are not registered (present) in the database
    List them for the user to give the go ahead to register them in the database
    If go ahead register them unless name unacceptable. See regex check
'''
def articles_collect(request):
    helper = ArticlesCollectFormSetHelper()
    unacceptableNames = []
    if request.method == 'GET':
        title = 'Artículos no registrados en la base de datos'
        dirData = os.listdir(os.path.join(settings.MEDIA_ROOT, 'articles'))
        fileNamesInDb = Articles.objects.values_list("file_name", flat=True).order_by("file_name")
        filesNotInDb = []
        for item in dirData:
            if item not in fileNamesInDb[:]:
                filesNotInDb.append(item)
        # https://docs.djangoproject.com/en/1.10/topics/forms/formsets/
        x = str(len(filesNotInDb))
        title += ': ' + str(x)
        filesNotInDbDict = {
            'form-TOTAL_FORMS': x,
            'form-INITIAL_FORMS': x,
            'form-MAX_NUM_FORMS': '',
            }
        for i in range(len(filesNotInDb)):
            s='form-'+str(i)+'-file_name'
            filesNotInDbDict.update({s:filesNotInDb[i]})
        formset = ArticlesCollectFormSet(filesNotInDbDict)
    else:
        formset = ArticlesCollectFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                name = form.cleaned_data.get('file_name')
                #regexHtmlFileName = r"([-_$@,'áéíóúÁÉÍÓÚ \w\d+]+.html)$"
                regexHtmlFileName = r"([-_$@#()^=&,'áéíóúÁÉÍÓÚ \w\d+]+.html)$"
                checkedName = re.search(regexHtmlFileName, name).group()
                if name == checkedName:
                    newInstance = Articles(file = 'articles/' + name, file_name = name, author = User.objects.first(), access_by_status = 'is_superuser', access_by_group = None )
                    newInstance.save()
                else:
                    unacceptableNames.append(name)
            if len(formset) == 0 or len(formset) == len(unacceptableNames):
                title = 'Sin Artíulos Que Agregar A La Base De Datos'
            else:
                title = 'Los Artículos Se Han Registrado'
            formset = []
        else:
            title = 'Error Al Registrar los Artículos'
    return render(request, 'filehand/articles_collect.html', {'title': title, 'formset':formset, 'helper': helper, 'unacceptableNames': unacceptableNames})
'''
def clean_author(self):
    author = self.cleaned_data['author']
    author = 

@permission_required('is_staff')
@permission_required('add_receipt', login_url='/accounts/login')
'''
def old_articlePermissions(request, msg='', images='False'):
    print('\n\n\n ---------------------------------->>>>> images? = ' + images + '\n\n')
    helper = ArticlesFormSetHelper()
    title = _('Sube O Borra Artículos, Asígnales Permisos Para Privacidad, Carga Imágenes Usadas En Ellos ')
    if request.method == 'GET':
        articlesQueryset = Articles.objects.all()
        # make a list of the file names in the MEDIA_ROOT/articles directory ( if articlesQueryset.exists() )
        filesInDb = []
        for instance in articlesQueryset:
            filesInDb.append( os.path.split(instance.file.name)[1] )
            #if instance.file_name == '': this is now taken care of in form.clean()
            #    instance.file_name = os.path.split(instance.file.name)[1]
            #    instance.save()
        # returns a list of info on the files contained in MEDIA_ROOT/articles
        # dirData[i][0]:      absolute path to the files contained in directory
        # dirData[i][1]:      the file names without extension
        # dirData[i][2][1:3]: the clasification codes of the files. Each file name begins with three two-character classification codes, separated by a hyphen between them and between them and the rest of the file name
        # dirData[i][3]:      the article title, which is the file name with no classification codes nor file extension
        dirData = getPathsCatsAndArticles(os.path.join(settings.MEDIA_ROOT, 'articles'))
        # if a file exists in MEDIA_ROOT/articles but not in the database, add it to the database
        filesInDir = []
        for item in dirData:
            filesInDir.append(item[1])
            if  os.path.split(item[0])[1] not in filesInDb[:]:
                newInstance = Articles(file = 'articles/' + os.path.split(item[0])[1], file_name = os.path.split(item[0])[1], author = User.objects.first(), access_by_status = 'is_superuser', access_by_group = Group.objects.first() )
                newInstance.save()        
        for item in articlesQueryset:
            print('item. in queryset ' + item.file_name)
        for item in filesInDir:
            print('item in dirData ' + item)
        # msg will be set to a value only if view has been called from within POST.
        # If view was called from within POST, and a file was added to the file system, it will not yet appear in dirData
        # So in such a case do not delete it from the database for not appearing in dirData, else, do delete it
        #print('1 past msg= empty string msg?, =' + msg + '*')
        if msg == ' ':
            #print('2 past msg= empty string?, msg =' + str(msg) + '*')
            # if a file exists in the database but is not present in the directory, delete it from the database
            x = request.user
            try:
                for item in articlesQueryset:
                    #print('checking for ' + item.file_name + ' in ' + str(filesInDir))
                    if item.file_name not in filesInDir:
                        #print('found an item that s in the database but not in filesystem ' + item.file_name)
                        #input('\n\n***\n*** In GET if item.file_name not in filesInDir:, Suspended until you press enter\n***\n')
                        item.delete()
                    else:
                        if item.author == None:
                            item.author = x
                            item.save() 
            except:
                print('\n\n x = ' + str(x) + ' type = ' + str(type(x)))
                pass
        # if an article was just added, let the template know by setting images parameter to True
        # the view will then offer to upload the image files referenced in the article through a popup
        #if images == "True":
        #newArticlesQueryset = Articles.objects.all()
        newArticlesQueryset = getArticlesUserCanEdit(request)
        formset = articlesFormSet(request.POST or None, queryset = newArticlesQueryset, )
        
        context = {'title':title, 'msg': msg, 'images':images, 'formset':formset, 'helper': helper}
    else:
        #input('\n\n***\n*** 1 articlePermissions P O S T, Suspended until you press enter\n***\n')
        thereAreImagesToUpload = 'False'
        
        formset = articlesFormSet(request.POST, request.FILES)

        if formset.is_valid():
            formset.save(commit=False)
            for form in formset:
                if form.cleaned_data.get('DELETE'):
                    os.remove ( os.path.join(settings.MEDIA_ROOT, 'articles', form.cleaned_data.get('file_name')) )
                else:
                    if form.cleaned_data.get('id') == None and form.cleaned_data.get('file') != None :
                        #form.author = x
                        #print('\n>>>\n>>> form.author = ' + str(form.author))
                        thereAreImagesToUpload = 'True'
                        #print('\n_________________________\nid = ' + str(form.cleaned_data.get('id')))
                        #form.cleaned_data['author'] = 1
                        #for key, value in form.cleaned_data.items():
                            #print(str(key), str(value))
                            #if(key == 'author'):
                                #print('again ' + str(key), str(value))
                #form.save()        
            formset.save() # if a file is marked for deletion, is it deleted here? The file is not, the database record YES
            msg = extractFormEditingResults(formset)
            return redirect(reverse('articlePermissions', args=[msg, thereAreImagesToUpload]), permanent=True)
        else:
            msg = '<span class="has-errors">' + _('1 Por favor, corrige los campos marcados en rojo') + '</span>'
            context = {'title':title, 'msg': msg, 'formset':formset, 'helper': helper}

    return render(request, 'filehand/article_permissions.html', context)
'''
'''
def articlePermissions(request, msg='', images='False'):
    helper = ArticlesFormSetHelper()
    title = _('Sube O Borra Artículos, Asígnales Permisos Para Privacidad, Carga Imágenes Usadas En Ellos ')
    if request.method == 'GET':
        newArticlesQueryset = getArticlesUserCanEdit(request)
        formset = articlesFormSet(request.POST or None, queryset = newArticlesQueryset, )        
        context = {'title':title, 'msg': msg, 'images':images, 'formset':formset, 'helper': helper}
    else:
        thereAreImagesToUpload = 'False'
        formset = articlesFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save(commit=False)
            for form in formset:
                if form.cleaned_data.get('DELETE'):
                    os.remove ( os.path.join(settings.MEDIA_ROOT, 'articles', form.cleaned_data.get('file_name')) )
                else:
                    if form.cleaned_data.get('id') == None and form.cleaned_data.get('file') != None :
                        thereAreImagesToUpload = 'True'
            formset.save() # if a file is marked for deletion, is it deleted here? The file is not, the database record YES
            msg = extractFormEditingResults(formset)
            return redirect(reverse('articlePermissions', args=[msg, thereAreImagesToUpload]), permanent=True)
        else:
            msg = '<span class="has-errors">' + _('1 Por favor, corrige los campos marcados en rojo') + '</span>'
            context = {'title':title, 'msg': msg, 'formset':formset, 'helper': helper}
    return render(request, 'filehand/article_permissions.html', context)
'''
'''
def articlesMgr_1(request, msg='', images='False'):
    helper = ArticlesMgrFormSetHelper()
    title = _('Sube O Borra Artículos, Clasifícalos Y Asígnales Permisos De Acceso, Carga Imágenes Usadas En Ellos ')
    if request.method == 'GET':
        newArticlesQueryset = getArticlesUserCanEdit(request)
        formset = articlesMgrFormSet(request.POST or None, queryset = newArticlesQueryset, )        
        context = {'title':title, 'msg': msg, 'images':images, 'formset':formset, 'helper': helper}
    else:
        thereAreImagesToUpload = 'False'
        formset = articlesMgrFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save(commit=False)
            for form in formset:
                if form.cleaned_data.get('DELETE'):
                    # in case the file does not exist like if it was deleted or renamed by hand
                    try:
                        os.remove ( os.path.join(settings.MEDIA_ROOT, 'articles', form.cleaned_data.get('file_name')) )
                    except:
                        pass
                else:
                    if form.cleaned_data.get('id') == None and form.cleaned_data.get('file') != None :
                        thereAreImagesToUpload = 'True'
            formset.save() # if a file is marked for deletion, is it deleted here? The file is not, the database record YES
            msg = extractFormEditingResults(formset)
            return redirect(reverse('articlesMgr_1', args=[msg, thereAreImagesToUpload]), permanent=True)
        else:
            msg = '<span class="has-errors">' + _('1 Por favor, corrige los campos marcados en rojo') + '</span>'
            context = {'title':title, 'msg': msg, 'formset':formset, 'helper': helper}
    return render(request, 'filehand/articles_mgr_1.html', context)
'''
'''
def articlesMgr_2(request, msg='', images='False'):
    helper = ArticlesMgrFormSetHelper()
    title = _('Sube O Borra Artículos, Clasifícalos Y Asígnales Permisos De Acceso, Carga Imágenes Usadas En Ellos ')
    if request.method == 'GET':
        newArticlesQueryset = getArticlesUserCanEdit(request)
        formset = articlesMgrFormSet(request.POST or None, queryset = newArticlesQueryset, )        
        context = {'title':title, 'msg': msg, 'images':images, 'formset':formset, 'helper': helper}
    else:
        thereAreImagesToUpload = 'False'
        formset = articlesMgrFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save(commit=False)
            for form in formset:
                if form.cleaned_data.get('DELETE'):
                    os.remove ( os.path.join(settings.MEDIA_ROOT, 'articles', form.cleaned_data.get('file_name')) )
                else:
                    if form.cleaned_data.get('id') == None and form.cleaned_data.get('file') != None :
                        thereAreImagesToUpload = 'True'
            formset.save() # if a file is marked for deletion, is it deleted here? The file is not, the database record YES
            msg = extractFormEditingResults(formset)
            return redirect(reverse('articlesMgr_2', args=[msg, thereAreImagesToUpload]), permanent=True)
        else:
            msg = '<span class="has-errors">' + _('1 Por favor, corrige los campos marcados en rojo') + '</span>'
            context = {'title':title, 'msg': msg, 'formset':formset, 'helper': helper}
    return render(request, 'filehand/articles_mgr_2.html', context)
'''
'''
def classify_obsolete(request, msg=''):
    helper = ClassificationFormSetHelper()
    title = _('Formato para Capturar, Editar y Borrar Abreviaciones y Nombres de Clasificaciones para Artículos')
    if request.method == 'GET':
        queryset = Clas.objects.all()
        formset = ClassificationFormSet(request.POST or None, queryset = queryset)
        context = {'title':title, 'msg': msg, 'formset':formset, 'helper': helper}
    else:
        formset = ClassificationFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            msg = extractFormEditingResults(formset)
            return redirect(reverse('classify_obsolete', args=[msg]), permanent=True)
        else: # if len(receipt_form.errors)==1 and 'receipt_number' in receipt_form.errors and 'unique' in receipt_form.errors.as_json():
            msg = '<span class="has-errors">' + _('Por favor, corrige los campos marcados en rojo') + '</span>'
            #context = {'title':title, 'formset' :formset, 'helper': helper}
            context = {'title':title, 'msg': msg, 'formset':formset, 'helper': helper}
            
    return render(request, 'filehand/classifications_obsolete.html', context)
'''
'''
def classify_new(request, msg=''):
    helper = ClassificationFormSetHelper()
    title = _('Captura, Edita y Borra Clasificaciones De Artículos')
    if request.method == 'GET':
        queryset = Clas.objects.all()
        formset = ClassificationFormSet(request.POST or None, queryset = queryset)
        context = {'title':title, 'msg': msg, 'formset':formset, 'helper': helper}
    else:
        formset = ClassificationFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            msg = extractFormEditingResults(formset)
            return redirect(reverse('classify_new', args=[msg]), permanent=True)
        else: # if len(receipt_form.errors)==1 and 'receipt_number' in receipt_form.errors and 'unique' in receipt_form.errors.as_json():
            msg = '<span class="has-errors">' + _('Por favor, corrige los campos marcados en rojo') + '</span>'
            #context = {'title':title, 'formset' :formset, 'helper': helper}
            context = {'title':title, 'msg': msg, 'formset':formset, 'helper': helper}
            
    return render(request, 'filehand/classifications_new.html', context)
'''
'''
def addClas(request):
    if request.method == 'GET':
        title = 'Capturar'
        queryset = Clas.objects.all()
        form = ClasForm(request.POST or None, prefix = 'clasifications')
        context = {'title':title, 'form':form, 'queryset': queryset }
    else:
        form = ClasForm(request.POST, request.FILES, prefix = 'clasifications')
        if form.is_valid():
            form.save()
            title = 'Agregado'
            queryset = Clas.objects.all()
            form = ClasForm(request.POST or None, prefix = 'clasifications')
            context = {'title':title, 'form':form, 'queryset': queryset }
        else:
            title = 'CORREGIR'
            context = {'title':title, 'form': form, 'queryset': queryset }
    return render(request, 'filehand/addClas.html', context)
'''
    Compose a message containing the info about edit operations performed on a formset
    Use this function after successfully saving the formset to obtain the message as text    
'''
def extractFormEditingResults( aFormset ):
    msg = _('Cambios hechos:') + '<br>'
    try:
        nChanged = len(aFormset.changed_objects)
        nDeleted = len(aFormset.deleted_objects)
        nAdded   = len(aFormset.new_objects)
        if (nChanged or nDeleted or nAdded):
            sep = ''
            if(nChanged):
                msg += _('Líneas modificadas: ') + str(nChanged)
                sep = ', '
            if(nDeleted):
                msg += sep + _('Líneas borradas: ') + str(nDeleted)
                sep = ','
            if(nAdded):
                msg += sep + _('Líneas agregadas: ') + str(nAdded) 
        else:
            msg += _(' ninguno')
    except:
        msg += _('ninguno (Sin atributo changed_objects)')
    return msg
    
    #nDeleted = aFormset.deleted_objects
    #nAdded   = aFormset.new_objects
'''
'''
def gallery(request):
    if request.method == 'POST':
        form = GalleryDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = GalleryDocument(docfile = request.FILES['docfile'])
            newdoc.save()
            return HttpResponseRedirect(reverse('gallery'))
    else:
        form = GalleryDocumentForm() # An empty, unbound form        
        try:
            listDirectory('/temp', 'txt, jpg, png')
            listDirectory(os.path.join(settings.MEDIA_ROOT, 'articles'), 'txt, jpg, png')
        except:
            pass
    try:
        documents = GalleryDocument.objects.all()
    except:
        pass
    return render(request, 'filehand/gallery.html', {'documents': documents, 'form': form})
'''
    Present an image from the image gallery by itself at it's full size unless it's full size exceeds the container element's size in which case display it to fit the container
    The database field that contains the image is not an ImageField but a FileField. An image field would have the image's size directly available. Here I receive the file name
    from gallery.html which means the image is already in the database for sure. I still get the FileField object from the database, actually just for kicks. It's practice.
    example:
        imgFileName: /media/documents/2016/11/26/12355397-squareiconslogo.jpg
        GalleryDocument model docfile field name = documents/2016/11/26/12355397-squareiconslogo.jpg
'''
def gallery_lg(request, imgFileName = ''):
    docfileName = imgFileName.replace('/media/', '')
    try:
        galleryDocumentObject = GalleryDocument.objects.filter(docfile = docfileName).first()
        #print('\n***\n***\n GOT galleryDocumentObject: ' + str(galleryDocumentObject) + ' .docfile = ' + str(galleryDocumentObject.docfile) + ' .docfile.name = ' + galleryDocumentObject.docfile.name + '\n***\n***')
        pathToImg = os.path.abspath(os.path.join(settings.MEDIA_ROOT, galleryDocumentObject.docfile.name ))
        #print('\n***\n***\n pathToImg = ' + pathToImg + '\n***\n***')
        if os.path.isfile( pathToImg ):
            #get image size with os
            #info = os.popen( "file " + pathToImg ).read()
            #print('\n***\n***\n with os file info = ' + info + '\n***\n***')
            #get image size with Pillow/PIL
            img = Image.open(pathToImg) # file is closed automatically?! see https://bytes.com/topic/python/answers/24308-pil-do-i-need-close
            imgWidth = img.size[0]
            imgHeight = img.size[1]
            #print('\n***\n***\n with PIL str(img.size) = ' + str(img.size) + ' str(img.size[0]) = ' + str(img.size[0]) + ' str(img.size[1]) = ' + str(img.size[1]) + ' type = ' + str(type(img.size[0])) + ' \n***\n***')
    except:
        #print('\n***\n***\n FAILED DOING IMAGE OPERATIONS\n***\n***')
        pass
    return render(request, 'filehand/gallery_lg.html', { 'galleryDocumentObject': galleryDocumentObject, 'file': imgFileName, 'imgWidth': imgWidth, 'imgHeight': imgHeight  })
'''
'''
#"get list of file info objects for files of particular extensions" 
def listDirectory(directory, fileExtList): #Ref. http://www.diveintopython.net/file_handling/os_module.html    
    '''
    print('\n>\n> getting executing function name with inspect.stack()[0][3]: ' + inspect.stack()[0][3])
    for x in fileExtList:
        print('> fileExtList = ' + x)
    print('>\n')
    '''
    fileList1 = [os.path.normcase(f) for f in os.listdir(directory)] # the list of files in a directory, case normalized according to operating system defaults
    # os.listdir(directory) returns a list of all the files and folders in directory 
    '''
    print('> List of files and folders in directory: ' + directory + '\n> '  + str(fileList1))
    for x in fileList1:
        print('> fileList1              = ' + x)
        print('> os.path.splitext(x)[1] = ' + os.path.splitext(x)[1])   # the file extension
        print('> os.path.splitext(x)[0] = ' + os.path.splitext(x)[0])   # the file name without extension
    print('>\n')
    print('\n>>>>>>>>>>>>>>>>')
    '''
    regexCats=r"(?<=)\w+(?=-)"
    regexArts=r"([a-zA-Z0-9]+)[^-]*$"
    for x in fileList1:
        cats = re.finditer(regexCats, x)
        art = re.search(regexArts, x)
        for catNum, cat in enumerate(cats):
            catNum = catNum + 1
            #print('# = ' + str(catNum) + ' cat = ' + str(cat))
        #print('art = ' + str(art))
    #print('>>>>>>>>>>>>>>>>\n')

    fileList2 = [os.path.join(directory, f) for f in fileList1 if os.path.splitext(f)[1] in fileExtList] #doesn't work'
    '''
    print('> str(fileList2) = ' + str(fileList2))
    for x in fileList2:
        print('> filelist2 = ' + x)
    print('>\n')
    '''
    fileList3 = [os.path.join(directory, f) for f in fileList1]
    '''
    print('> The complete paths to the files in the list is')
    for x in fileList3:
        print('> ' + x)
    print('>\n')
    '''
    return fileList3
'''
    
'''
def index(request):
    print('In filehand/index view')
    return render_to_response('filehand/index.html', {'message': 'MESSAGE RECEIVED'})
'''
if account inactive user can't log in
http://stackoverflow.com/questions/739776/django-filters-or
from django.db.models import Q
Item.objects.filter(Q(creator=owner) | Q(moderated=False))
'''
def getArticlesUserCanView(request):
    #print('\n in getArticlesUserCanView, request.user.is_authenticated = ' + str(request.user.is_authenticated))
    if request.user.is_superuser:
        toReturn = Articles.objects.all()
    elif not request.user.is_authenticated(): # Don't let status be anonimous and group be set. An anonimous user can't have a group
        #print('\n\n USER IS NOT AUTHENTICATED 1')
        toReturn = Articles.objects.filter(access_by_status = 'anonimous')
        #print('\n\n USER IS NOT AUTHENTICATED 2, toReturn = ' + str(toReturn))
    elif request.user.is_staff:
        queryset_1 = Articles.objects.filter(
            access_by_status = 'is_staff'
        ).filter(
            access_by_group__in = request.user.groups.values_list('name',flat=True) # what if group is not set. There would have to be a group = all
        )
        queryset_2 = Articles.objects.filter(access_by_status = 'anonimous')
        queryset_3 = queryset_1 | queryset_2
        queryset_4 = Articles.objects.filter(
            access_by_status = 'is_authenticated'
        ).filter(
            access_by_group__in = request.user.groups.values_list('name',flat=True) # what if group is not set. There would have to be a group = all
        )
        queryset_5 = Articles.objects.filter(access_by_status = 'anonimous')
        queryset_6 = queryset_4 | queryset_5
        queryset_7 = queryset_3 | queryset_6
        queryset_8 = Articles.objects.filter(author = request.user.id)
        toReturn = queryset_7 | queryset_8
    elif request.user.is_authenticated:
        queryset_1 = Articles.objects.filter(
            access_by_status = 'is_authenticated'
        ).filter(
            access_by_group__in = request.user.groups.values_list('name',flat=True)
        )
        queryset_2 = Articles.objects.filter(access_by_status = 'anonimous')
        queryset_3 = Articles.objects.filter(author = request.user.id) 
        toReturn = queryset_1 | queryset_2 | queryset_3
    else:
        toReturn = None
    
    return toReturn
'''
'''
def articlesUserCanEdit_1(request):
    queryset = getArticlesUserCanView(request)
    templateData = []
    if queryset:
        for rec in queryset:
            fileName = os.path.split(rec.file_name)[1]
            fileNameNoExt = os.path.splitext(fileName)[0]
            title = fileNameNoExt
            clas1 = rec.clas
            clas2 = rec.subClas
            clas3 = rec.docType
            templateData.append( [ clas1, clas2, clas3, fileName, title ] )
    else:
        templateData.append( [ 'None', 'None', 'None', 'sin_articulos.html', 'nada' ] )
    return render(request, 'filehand/articles_user_can_edit_1.html', {'data': templateData, 'title':'Artículos'}) 
'''
'''
def articlesUserCanEdit_2(request):
    queryset = getArticlesUserCanView(request)
    templateData = []
    if queryset:
        for rec in queryset:
            fileName = os.path.split(rec.file.name)[1]
            fileNameNoExt = os.path.splitext(fileName)[0]
            title = fileNameNoExt
            clas1 = rec.clas
            clas2 = rec.subClas
            clas3 = rec.docType
            templateData.append( [ clas1, clas2, clas3, fileName, title ] )
    else:
        templateData.append( [ 'None', 'None', 'None', 'sin_articulos.html', 'nada' ] )
    return render(request, 'filehand/articles_user_can_edit_2.html', {'data': templateData, 'title':'Artículos'})
'''
    articlesList = listDirectory(os.path.join(settings.MEDIA_ROOT, 'articles'), ['txt', 'jpg', 'png', 'html'])
    return render_to_response('filehand/article_list.html', {'message': 'MESSAGE RECEIVED', 'articles': articlesList })
    return render(request, 'filehand/article_list.html', {'message': 'MESSAGE RECEIVED', 'articles': articlesList })

def articles(request): #Ref. https://automatetheboringstuff.com/chapter8/
    #print('In filehand/articles view')
    dirData = getPathsCatsAndArticles(os.path.join(settings.MEDIA_ROOT, 'articles'))
    num = len(dirData)
    templateData = []
    for i in range(num):
        clas1 = Clas.objects.filter(code = dirData[i][2][0]).first()
        clas2 = Clas.objects.filter(code = dirData[i][2][1]).first()
        clas3 = Clas.objects.filter(code = dirData[i][2][2]).first()
        #print('\n---- found clas1 = ' + str(clas1))
        dirData[i][0] = dirData[i][0].replace("/home", "home")
                            #  clas1    2      3      file name        title
        templateData.append( [ clas1, clas2, clas3, dirData[i][1], dirData[i][3] ] )
    return render(request, 'filehand/article_list.html', {'title':'Artículos', 'data': templateData,})
'''
'''
'''
def articlesWithPermissionList(request):
    queryset = getArticlesUserCanView(request)
    templateData = []
    if queryset:
        regexCats = r"(?<=)\w+(?=-)"
        regexArts=r"([a-zA-Z0-9]+)[^-]*$"
        #num = len(queryset)
        clas = []
        for rec in queryset:
            fileName = os.path.split(rec.file.name)[1]
            #fileNameNoExt = os.path.splitext(rec.file.name)[0]
            fileNameNoExt = os.path.splitext(fileName)[0]
            title = re.search(regexArts, fileNameNoExt).group()
            clas = re.findall(regexCats, fileNameNoExt)
            #print('\n\n clas = ' + str(clas) + ' len(clas) = ' + str(len(clas)))
            if len(clas) == 3:
                clas1 = Clas.objects.filter(code = clas[0]).first()
                clas2 = Clas.objects.filter(code = clas[1]).first()
                clas3 = Clas.objects.filter(code = clas[2]).first()
            else:
                clas1 = 'XX'
                clas2 = 'XX'
                clas3 = 'XX'
            templateData.append( [ clas1, clas2, clas3, fileName, title ] )
    else:
        templateData.append( [ 'None', 'None', 'None', 'sin_articulos.html', 'nada' ] )
    return render(request, 'filehand/article_list.html', {'data': templateData, 'title':'Artículos'})            

'''    getArticlesUserCanView(request)
    Function to extract form a directory containing specially named files, data on these files
        The files are named X1-X2-X3-article title.html, where Xn are two-character classification codes for an article which is the html formatted contents of an article  
    
    Return dirData, a list of data related to the files contained in a directory
    
    directory: an absolute path to a directory, as in settings.MEDIA_ROOT, 'articles'
    
    dirData[i][0]:      absolute path to the files contained in directory
    dirData[i][1]:      the file names without extension
    dirData[i][2][1:3]: the clasification codes of the files. Each file name begins with three two-character classification codes, separated by a hyphen between them and between them and the rest of the file name
    dirData[i][3]:      the article title, which is the file name with no classification coes nor file extension
'''
def getPathsCatsAndArticles(directory):
    absPathToFiles = [os.path.join(directory, f) for f in os.listdir(directory)]
    nOfFiles=len(absPathToFiles)
    dirData = [['' for j in range(4)] for i in range(nOfFiles)]     # declares and initializes a list dirData[0:n][0:3]
    fileNamesNoExt = [os.path.splitext(f)[0] for f in os.listdir(directory)]
    '''
    for item in absPathToFiles:
        print('the paths in absPathToFiles are ' + item)
    for f in fileNamesNoExt:
        print('\n*> the fileNamesNoExt are: ' + f)
    for f in absPathToFiles:
        print('\n*> the absPathToFiles are: ' + f)    
    '''
    regexCats=r"(?<=)\w+(?=-)"
    regexArts=r"([a-zA-Z0-9]+)[^-]*$"
    cats = [['' for j in range(4)] for i in range(nOfFiles)]
    arts = ['' for i in range(nOfFiles)]

    for i in range (nOfFiles):
        cats[i] = re.findall(regexCats, fileNamesNoExt[i])
        if len(cats[i]) < 2:
            cats[i] = ['XX', 'XX', 'XX']
        print('\n*** cats['+str(i)+'] = ' + str(cats[i]) + ' type(cats[i]) = ' + str(type(cats[i])))

        try:
            arts[i] = re.search(regexArts, fileNamesNoExt[i]).group()
        except AttributeError:
            arts[i]=''
        #print('cat = ' + str(cats[i]))
        #print('art = ' + arts[i])
    
    print('\n================================ BEGIN IN getPathsCatsAndArticles: dirData[i][3] = arts[i] = ')
    for i in range(nOfFiles):
        dirData[i][0] = absPathToFiles[i]
        print('i = ' + str(i) + ' dirData[i][0] paths = ' + dirData[i][0])
        dirData[i][1] = fileNamesNoExt[i] + '.html'
        print('i = ' + str(i) + ' dirData[i][1] names = ' + dirData[i][1])
        dirData[i][2] = cats[i]
        #print('i = ' + str(i) + ' dirData[i][2] cats  = ' + str(dirData[i][2]))
        dirData[i][3] = arts[i]
        #print('i = ' + str(i) + ' dirData[i][3] arts  = ' + dirData[i][3])
    print('\n================================ END IN getPathsCatsAndArticles: dirData[i][3] = arts[i] = ')
        
    return dirData

'''
http://www.diveintopython.net/file_handling/os_module.html
http://www.diveintopython.net/file_handling/file_objects.html#d0e14800
https://techtavern.wordpress.com/2009/04/06/regex-that-matches-path-filename-and-extension/
https://regex101.com/r/gV2xB7/1

Displays an HTML document
fileName: name of the file to open
caller:   identifies what function or link invoked this view. Is passed to the template so it behaves differently depending on where the call comes from.
'''
def article_display(request, fileName, caller=''):
    #print('\n***\n***\n*** article_display, fileName = ' + fileName + ' caller = ' + caller + '\n')
    if request.method == "GET":
        file = os.path.join(settings.MEDIA_ROOT + '/articles/', fileName)
        #path = os.path.abspath(file)
        try:
            f = open(file, encoding='utf8')
            fContents = f.read()
            f.close()
        except:
            fContents = "<div style='color:red;'><br><h2>El documento no existe o contiene caracteres no codificados como UTF-8.</h2><br></div>"
        return render_to_response( 'filehand/article_display.html', {'article_contents': fContents, 'file': fileName, 'caller': caller } )
'''
'''
def articleEdit(request, fileName = '', caller = '' ):
    print('\n***\n***\n*** articleEdit, fileName = ' + fileName + ' caller = ' + caller + '\n')
    from filehand.forms import DummyForm
    if request.method == "GET":
        file = os.path.join(settings.MEDIA_ROOT + '/articles/', fileName)
        #path = os.path.abspath(file)
        try:
            f = open(file, encoding='utf8')
            fContents = f.read()
            f.close()
        except:
            fContents = "<div style='color:red;'><br><h2>El documento no existe o contiene caracteres no codificados como UTF-8.</h2><br></div>"
        form = DummyForm(request.POST or None)
        context = { 'title': 'Editar el archivo', 'article_contents': fContents, 'file': fileName, 'form': form, 'caller': caller }
    else:
        form = DummyForm(request.POST or None)
        if form.is_valid():
            theFileName = form.cleaned_data.get('fileName')
            print('\n Validation cleared, fileName gotten from cleaned data = ' + theFileName)
            file = os.path.join(settings.MEDIA_ROOT + '/articles/', theFileName)
            try:
                f = open(file, encoding='utf8')
                fContents = f.read()
                f.close()
                if fContents == form.cleaned_data.get('dummyField'):
                    print("File contents unchanged. DO NOT SAVE")
                    title = 'No hubo modificaciones. Edita o navega a otro lugar.'
                else:
                    f = open(file, 'w', encoding='utf8' )
                    print("File contents changed. DO SAVE")
                    f.write(form.cleaned_data.get("dummyField"))
                    f.close()
                    print('after close')
                    fContents = form.cleaned_data.get("dummyField")
                    #print('\nfContents after write\n ' + fContents)
                    title = 'Modificaciones guardadas. Continúa editando o navega a otro lugar.'
            except:
                title = 'No se guardó. No fué posible abrir, leer o escribir el documento.'
                fContents = "<div style='color:red;'><br><h2>El documento no existe o contiene caracteres no codificados como UTF-8.</h2><br></div>"
            form = DummyForm(request.POST or None)
        else:
            print('\n\nN O T  V A L I D  N O T')
            title = "El contenido es inválido. No continúes editando. Algo esta mal con el archivo."
            fContents = "<div style='color:red;'><br><h2>"
            for key, value in form.errors.items():
                fContents += str(value) + "<br>"
            fContents += "</h2><br></div>"
        context = { 'title': title, 'article_contents': fContents, 'file': fileName, 'form': form, 'caller': caller }
        
    return render( request, 'filehand/article_edit.html', context )

'''
handle call from articlesMgr view to add a row to Clas table and return updated contents of the table formatted as select field options list
'''
def add_clas_get_options(request, clas_name = None):
    #print('\n\nadd_clas_get_options ' + clas_name + '\n')
    if clas_name:
        newRow = Clas(name = clas_name)
        newRow.save()
        qset = Clas.objects.all()
        html = '<option value="" selected="selected">---------</option>\n'
        for row in qset:
            html = html + '<option value="' + str(row.pk) + '">' + row.name + '</option>\n'
    else:
        html = '<option value="1">NOT FOUND</option>\n'
    return HttpResponse(html)
'''
'''
def add_subClas_get_options(request, clas_name = None):
    #print('\n\nadd_clas_get_options ' + clas_name + '\n')
    if clas_name:
        newRow = SubClas(name = clas_name)
        newRow.save()
        qset = SubClas.objects.all()
        html = '<option value="" selected="selected">---------</option>\n'
        for row in qset:
            html = html + '<option value="' + str(row.pk) + '">' + row.name + '</option>\n'
    else:
        html = '<option value="1">NOT FOUND</option>\n'
    return HttpResponse(html)
'''
'''
def add_docType_get_options(request, clas_name = None):
    #print('\n\nadd_clas_get_options ' + clas_name + '\n')
    if clas_name:
        newRow = DocType(name = clas_name)
        newRow.save()
        qset = DocType.objects.all()
        html = '<option value="" selected="selected">---------</option>\n'
        for row in qset:
            html = html + '<option value="' + str(row.pk) + '">' + row.name + '</option>\n'
    else:
        html = '<option value="1">NOT FOUND</option>\n'
    return HttpResponse(html)
'''
newArticle calls this function to add sample content to an html document just created.
The sample contents corresponds to the horma selected in the modal form that comes up
When you select Documentos>Nuevo in the top menu
'''
def strings(type=""):
    if type == "nota":
        toReturn = '<div class="newspaper_1" style="width:60%; min-width:560px; margin:24px auto 12px auto; padding: 24px; border: 1px solid silver; overflow:auto;">' \
        '<h2 class="text-md-center">Document Title</h2><hr><p>Paragraph</p><p>Paragraph</p> ' \
        '<p>link <a href="http://http://nite-lite.net/">nite-lite.net</a></p><p>Paragraph</p>' \
        '<div style="color:darkgreen"><p>Say what you do. Do what you say.</p></div><hr class="prettyline"></div>'
    elif type == "articulo":
        toReturn = '<div class="page-header"><h2>T&iacute;tulo Del Documento</h2></div><div class="newspaper_3">'\
        '<div class="pull-left item-image" style="margin: 0 6px 0 0;"><img src="../../media/img/articles/El Fascinante Mundo De Los Olores 1.jpg" alt="what 1?" width="133" height="113" />'\
        '</div><p>P&aacute;rrafo con im&aacute;gen de introducci&oacute;n. P&aacute;rrafo con im&aacute;gen de introducci&oacute;n. P&aacute;rrafo con im&aacute;gen de introducci&oacute;n.' \
        'P&aacute;rrafo con im&aacute;gen de introducci&oacute;n.</p><p><strong>Encabezado de p&aacute;rrafo o secci&oacute;n</strong> <br /> Primer p&aacute;rrafo de secci&oacute;n. '\
        'Primer p&aacute;rrafo de secci&oacute;n. Primer p&aacute;rrafo de secci&oacute;n. Primer p&aacute;rrafo de secci&oacute;n. Primer p&aacute;rrafo de secci&oacute;n.'\
        'Primer p&aacute;rrafo de secci&oacute;n.</p><p>Segundo p&aacute;rrafo de secci&oacute;n. Segundo p&aacute;rrafo de secci&oacute;n. Segundo p&aacute;rrafo de secci&oacute;n.' \
        'Segundo p&aacute;rrafo de secci&oacute;n. Segundo p&aacute;rrafo de secci&oacute;n. Segundo p&aacute;rrafo de secci&oacute;n. Segundo p&aacute;rrafo de secci&oacute;n.'\
        '</p></div><hr class="prettyline" />'
    elif type == "reminder":
        toRetun = "<div> recordatorio </div>"
    else:
        toReturn = ""
        
    return toReturn
'''
In article_edit.html, errors, if any, are displayed as html in a div.
Here, assemble the html containing error message(s)
'''
def makeErrorMsg(msgHtml):
    toReturn = "<div class='col-md-3'></div><div class='col-md-12'><div style='color:red;'><br>"
    toReturn += msgHtml + "<br></div></div>"
    return toReturn
'''
In top menu Documentos > Nuevo a popup opens for the user to enter a filename and select a document template.
These data are POSTED to here upon modal submit.
The purpose is to create a new file named filename containing an html template for the new file.
This view creates the file and sends the new file to article_edit.html for the user to add content and save.
'''
def newArticle(request):
    from filehand.forms import NewDocumentForm
    from filehand.forms import DummyForm
    try:
        user = request.user
        form = NewDocumentForm(request.POST or None)
        if form.is_valid():
            fileName = form.cleaned_data.get('fileName')
            horma = form.cleaned_data.get('horma')
            #print("\n________________________________\nfileName = " + fileName + " horma = " + horma)
            newFile = os.path.join(settings.MEDIA_ROOT + '/articles/', fileName)
            newFileAbsolutePath = os.path.abspath(newFile)
            if os.path.isfile( newFileAbsolutePath ):
                fContents = makeErrorMsg("Ya existe un documento con el nombre " + fileName)
                context = { "title": "Problema con el nombre del archivo.", "article_contents": fContents }
            else: # file does not yet exist
                newInstance = Articles(file = "articles/" + fileName, file_name = fileName, author = user, access_by_status = None, access_by_group = None )
                newInstance.save()   
                print("New file created")
                html = strings(horma)
                f = open(newFile, 'w', encoding='utf8' )
                f.write(html)
                f.close()
                context = { 'title': 'Editar el archivo', 'article_contents': html, 'file': fileName, 'form': DummyForm(request.POST or None) }
        else: # form not valid
            #print("\n errors = " + str(form.errors.as_json()) ) 
            errorList = []
            for key, value in form.errors.items():
                errorList.append(value)
            tempStr = ''
            for value in errorList:
                tempStr += str(value)
            fContents = makeErrorMsg(tempStr)
            context = { "title": "Problema con el nombre del archivo.", "article_contents": fContents}
    except: # user not signed in
        fContents = makeErrorMsg("Con la novedad: necesitas estar registrado para crear un archivo.")
        context = { "title": "Cómo llegaste aquí?", "article_contents": fContents }
    return render( request, "filehand/article_edit.html", context )
    