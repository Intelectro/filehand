'''
app: filehandarticles_mgr
'''
from django.conf.urls import patterns, url

urlpatterns = patterns('filehand.views',
    url(r'^$', 'index', name='index'),
    
    url(r'^newArticle/$', 'newArticle', name='newArticle'),
    
    url(r'^articlesMgr_1/(.*)/(.*)$', 'articlesMgr_1', name='articlesMgr_1'),
    url(r'^articlesMgr_2/(.*)/(.*)$', 'articlesMgr_2', name='articlesMgr_2'),
    
    url(r'^classify_new/(.+)$', 'classify_new', name='classify_new'),
    url(r'^classify_obsolete/(.+)$', 'classify_obsolete', name='classify_obsolete'),
    
    url(r'^articlesUserCanEdit_1/$', 'articlesUserCanEdit_1', name='articlesUserCanEdit_1'),
    url(r'^articlesUserCanEdit_2/$', 'articlesUserCanEdit_2', name='articlesUserCanEdit_2'),
    
    url(r'^articlesWithPermissionList/$', 'articlesWithPermissionList', name='articlesWithPermissionList'),
    
    #url(r'^article_display/(.+)/([\w]+)$', 'article_display', name='article_display'),
    url(r'^article_display/(.+.html)/([\w]+)$', 'article_display', name='article_display'),
    #url(r'^articleEdit/(.+)$', 'articleEdit', name='articleEdit'),
    #url(r'^articleEdit/([\w. ]*)$', 'articleEdit', name='articleEdit'),
    url(r'^articleEdit/(.+.html)/([\w]+)$', 'articleEdit', name='articleEdit'),
    #url(r'^articleEdit/(.*)$', 'articleEdit', name='articleEdit'),
    
    url(r'^addClas', 'addClas', name='addClas'),
    url(r'^articlePermissions/(.*)/(.*)$', 'articlePermissions', name='articlePermissions'),
    url(r'^uploadArticleImages/(.*)$', 'uploadArticleImages', name='uploadArticleImages'),
    url(r'^modalinfo/(.*)$', 'modalinfo', name='modalinfo'),

    url(r'^add_clas_get_options/([\w\ ]+)$', 'add_clas_get_options', name='add_clas_get_options'),
    url(r'^add_subClas_get_options/([\w\ ]+)$', 'add_subClas_get_options', name='add_subClas_get_options'),
    url(r'^add_docType_get_options/([\w\ ]+)$', 'add_docType_get_options', name='add_docType_get_options'),
    
    url(r'^gallery$', 'gallery', name='gallery'),
    
    url(r'^gallery_lg/(.*)$', 'gallery_lg', name='gallery_lg'),
    
    url(r'^articles_collect', 'articles_collect', name='articles_collect'),
)
