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
- python manage.py migrate
- python manage.py createsuperuser 
(dùng để tạo user/password khi đăng nhập vào admin)







