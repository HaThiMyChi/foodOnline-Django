Create virtual enviroment

- python -m venv env
- source env/Scripts/activate (activate virtual enviroment)
- deactivate (deactivate virtual enviroment)

=== Mục tiêu tạo ra môi trường là để cài đặt những packages cần sử dụng trong dự án đó

Install django
- pip install django

- django-admin startproject "tencandat" .


Khi tao folder templates, css, images... phải nằm cùng cấp với thư mục gốc của python và import nó trong DIRS CỦA TEMPLATES, trong file settings.py

Run python
- py manage.py runserver

Create Superuser
- python manage.py migrate (dể nó migrate ra database, nếu sử dụng postgresql thì cũng chạy câu này)
- python manage.py createsuperuser 
(dùng để tạo user/password khi đăng nhập vào admin)


======
STATIC_ROOT = BASE_DIR /'static' (là nó nằm cùng cấp với thư mục python) root directory


https://pypi.org/project/python-decouple/ (kham khao cai nay)
- pip install python-decouple


- python manage.py startapp "tencandat" (dùng để tạo models, views, admin file tương tác với sql), nó tạo ra app
    và import "tencandat" này vào chỗ 'INSTALLED_APPS' trong settings.py

- python manage.py makemigrations  (chạy sau khi tạo fields trong models.py)

- python manage.py migrate


    









