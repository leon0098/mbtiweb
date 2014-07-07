# 设置django admin静态资源的访问路径
Alias /static/ "d:/myFirstDjango/static/"
<Directory "d:/myFirstDjango/static">
Allow from all
</Directory>
# 设置root，不要使用"^/"
WSGIScriptAlias / "d:/myFirstDjango/apache/django.wsgi"
<Directory "d:/myFirstDjango/apache">
Allow from all
</Directory>