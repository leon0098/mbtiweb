# ����django admin��̬��Դ�ķ���·��
Alias /static/ "d:/myFirstDjango/static/"
<Directory "d:/myFirstDjango/static">
Allow from all
</Directory>
# ����root����Ҫʹ��"^/"
WSGIScriptAlias / "d:/myFirstDjango/apache/django.wsgi"
<Directory "d:/myFirstDjango/apache">
Allow from all
</Directory>