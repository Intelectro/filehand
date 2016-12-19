'''

    this file project/templatetags/custom.py is a tag or filter library
    
    use in template
    
        {% if request.user|has_group:"add_receipt" %}
        
        {% if string_containing_filename|isImageFile %}

    Ref.
        http://www.abidibo.net/blog/2014/05/22/check-if-user-belongs-group-django-templates/
        http://www.abidibo.net/blog/2014/05/22/check-if-user-belongs-group-django-templates/#sthash.WNnyxoFq.dpuf
        https://docs.djangoproject.com/en/1.10/howto/custom-template-tags/
        
'''
from django import template
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
#from cronosales.models import Employee

register = template.Library()



@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        group = Group.objects.get(name=group_name)
    except:
        group = None
    return True if group in user.groups.all() else False

@register.filter(name='isImageFile')
def isImageFile(file_name):
    return True if file_name.lower().endswith(('.png', '.jpg', '.jpeg')) else False

@register.filter(name='fileContents')
def fileContents(file_obj):
    try:
        f = file_obj.read()
        file_obj.close()
        return f
    except IOError:
        return '- file not found -'
    
@register.filter(name='fileRead')
def fileRead(file_name):
    #print('\n\n>>>\n>>> fileRead, file_name = ' + file_name + '\n>>>\n\n')
    file = open(file_name)
    file_contents = file.read()
    file.close()
    return file_contents
'''
@register.filter(name='employee_first_name')
def employee_first_name(user):
    userData = get_object_or_404(Employee, user_name=user)
    return userData.first_name

@register.filter(name='employee_full_name')
def employee_full_name(user):
    userData = get_object_or_404(Employee, user_name=user)
    return userData.full_name   # full_name is a property of Employee model defined in the model

@register.filter(name='employee_data')
def employee_data(user, whatData):
    #userData = get_object_or_404(Employee, user_name=user)
    try:
        userData = Employee.objects.get(user_name=user)
        if whatData == 'full_name':
            return userData.full_name
        elif whatData == 'first_name':
            return userData.first_name
        elif whatData == 'email':
            return userData.email
        else:
            return 'nothing'
    except:
        return 'No Name'
'''        
        


'''
this would have to be done through a model manager class MUST TRY IT
@register.filter(name='employee_full_name')
def employee_full_name(user):
    #userData = get_object_or_404(Employee, user_name=user)
    #toReturn = userData.first_name + userData.middle_name + userData.last_name + userData.mothers_last
    #toReturn = '%s %s %s %s' % (userData.first_name, userData.middle_name, userData.last_name, userData.mothers_last)
    #toReturn = userData.full_name
    return Employee(user)
'''