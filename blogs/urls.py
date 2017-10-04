from django.conf.urls import patterns, url


urlpatterns = patterns('blogs.views',
                       url(r'all', 'index', name='get_all_blogs'),
                       url(r'create_blog', 'create_blog', name='create_blog'),
                       url(r'get_blog', 'blog', name='get_blog'),
                       url(r'add_blog_paragraph', 'create_blog_paragraph', name='add_blog_paragraph'),
                       url(r'update_blog_paragraph', 'edit_blog_paragraph', name='update_blog_paragraph'),
                       url(r'add_comment', 'create_comment', name='add_comment'),
                       url(r'update_comment', 'edit_comment', name='update_comment'),
                       url(r'blog_comments', 'blog_comments', name='get_blog_comments'),
                       )
