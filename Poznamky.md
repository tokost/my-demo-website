pgAdmin4 od Docker-a

http://localhost:8888/

Prihlásenie:

user-name@domain-name.com/strong-password

Do založky General vložíme:
Name: PostgreSQL_Web

Do záložky Connection vložíme:
Hostname/addres: db
Port: 5432
Maitenance dataabse: postgres
Username:user-name
Pssword:strong-password
Save pssword: yes

![]()

Často používané príkazy:


$ rm -rf venv
$ python -m venv venv
$ source venv/Scripts/activate
$ deactivate
$ python --version
$ pip --version
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
$ pip freeze
pip uninstall psycopg2-binary

$ pip show django
$ python manage.py createsuperuser


$ pip uninstall psycopg2-binary
Found existing installation: psycopg2-binary 2.9.9
Uninstalling psycopg2-binary-2.9.9:
  Would remove:
    c:\program files\python\python37\lib\site-packages\psycopg2\*
    c:\program files\python\python37\lib\site-packages\psycopg2_binary-2.9.9.dist-info\*  
Proceed (Y/n)? y
  Successfully uninstalled psycopg2-binary-2.9.9

tomast@DESKTOP-CENTRAL MINGW64 /e/DJANGOGIRLS/my-demo-website-develop (main)
$ pip install psycopg2-binary
Collecting psycopg2-binary
  Downloading psycopg2_binary-2.9.9-cp310-cp310-win_amd64.whl.metadata (4.6 kB)
Downloading psycopg2_binary-2.9.9-cp310-cp310-win_amd64.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 3.4 MB/s eta 0:00:00
Installing collected packages: psycopg2-binary
Successfully installed psycopg2-binary-2.9.9

$ python -m pip show psycopg2-binary
Name: psycopg2-binary
Version: 2.9.9
Summary: psycopg2 - Python-PostgreSQL Database Adapter
Home-page: https://psycopg.org/
Author: Federico Di Gregorio
Author-email: fog@initd.org
License: LGPL with exceptions
Location: c:\users\tomast\appdata\local\programs\python\python310\lib\site-packages       
Requires:
Required-by:

