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

Ďalšie tipy
Testovacia konfigurácia:

Pred reštartovaním kontajnera nginx môžete otestovať konfiguráciu nginx spustením:

sh

Kopírovať kód
docker run --rm -v $(pwd)/nginx/default.conf:/etc/nginx/conf.d/default.conf:ro nginx:latest nginx -t
Tento príkaz spustí nginx v dočasnom kontajneri a otestuje konfiguráciu na prípadné chyby.

Skontrolujte denníky Nginx:

Ak sa nginx nepodarí spustiť, znova skontrolujte protokoly, aby ste zistili, či nie sú nejaké ďalšie chyby:

sh

Kopírovať kód
docker-compose logs nginx

>##Čo je os.getenv

os.getenvje funkcia v osmodule Python, ktorá sa používa na získanie hodnoty premennej prostredia. Ak premenná prostredia neexistuje, môže vrátiť predvolenú hodnotu, ak je zadaná, alebo Noneak nie je zadaná žiadna predvolená hodnota.

Syntax
pytón

Kopírovať kód
os.getenv(key, default=None)
Parametre
key : Názov premennej prostredia, ktorú chcete načítať.
default : (Voliteľné) Hodnota, ktorá sa má vrátiť, ak sa nenájde premenná prostredia. Ak nie je zadaná, predvolená hodnota je None.
Návraty
Hodnota premennej prostredia, ak existuje.
Predvolená hodnota, ak premenná prostredia neexistuje a je poskytnutá predvolená hodnota.
Noneak premenná prostredia neexistuje a nie je poskytnutá žiadna predvolená hodnota.
Príklad použitia
pytón

Kopírovať kód
import os

# Retrieve the value of the 'HOME' environment variable
home_dir = os.getenv('HOME')
print(f'Home Directory: {home_dir}')

# Retrieve the value of a non-existing environment variable with a default value
debug_mode = os.getenv('DEBUG_MODE', 'False')
print(f'Debug Mode: {debug_mode}')

# Retrieve the value of a non-existing environment variable without a default value
api_key = os.getenv('API_KEY')
print(f'API Key: {api_key}')
Praktický príklad použitia v Django
V projekte Django os.getenvsa bežne používa na správu konfiguračných nastavení, najmä pri nasadzovaní aplikácií. To vám umožňuje uchovávať citlivé informácie, ako sú kľúče API a databázové poverenia, mimo zdrojového kódu.

Tu je príklad toho, ako os.getenvsa dá použiť v súbore nastavení Django:

pytón

Kopírovať kód
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'default_db_name'),
        'USER': os.getenv('POSTGRES_USER', 'default_db_user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'default_db_password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Debug mode
DEBUG = os.getenv('DEBUG', 'False') == 'True'
V tomto príklade:

The SECRET_KEYsa získava z premennej prostredia s názvom DJANGO_SECRET_KEY. Ak neexistuje, použije sa predvolená hodnota.
Nastavenia databázy ako NAME, USER, PASSWORD, HOSTa PORTsa získavajú z príslušných premenných prostredia, pričom každá má predvolenú hodnotu.
Nastavenie DEBUGje určené na základe hodnoty DEBUGpremennej prostredia s predvolenou hodnotou False.
Použitie os.getenvtýmto spôsobom pomáha zvýšiť bezpečnosť a flexibilitu vašej aplikácie, pretože môžete jednoducho meniť konfigurácie bez úpravy zdrojového kódu.

>##Čo je config

V kontexte vývoja softvéru, najmä vo väčších a komplexnejších aplikáciách, "config" (skratka pre konfiguráciu) zvyčajne odkazuje na nastavenia alebo parametre, ktoré určujú, ako program beží. Konfiguračné súbory a nastavenia vám umožňujú spravovať a ovládať rôzne aspekty aplikácie bez zmeny kódu. Tieto konfigurácie môžu zahŕňať databázové pripojenia, kľúče API, nastavenia prostredia, prepínače funkcií, úrovne protokolovania a ďalšie.

Typy konfigurácií
Premenné prostredia : Premenné prostredia sa používajú na konfiguráciu nastavení, ktoré sa môžu meniť v závislosti od prostredia (napr. vývoj, testovanie, výroba).

Príklad: DATABASE_URL, SECRET_KEY.
Konfiguračné súbory : Tieto súbory často obsahujú nastavenia v rôznych formátoch, ako sú JSON, YAML, INI alebo dokonca skripty Python.

Príklady: config.json, settings.py, config.yaml.
Argumenty príkazového riadka : Nastavenia možno pri spustení aplikácie odovzdať aj ako argumenty príkazového riadka.

Príklad: python app.py --debug --port=5000.
Bežné formáty konfiguračných súborov
JSON (JavaScript Object Notation) :

json

Kopírovať kód
{
    "debug": true,
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "password": "secret"
    }
}
YAML (YAML nie je značkovací jazyk) :

yaml

Kopírovať kód
debug: true
database:
  host: localhost
  port: 5432
  user: admin
  password: secret
INI (inicializačný súbor) :

Toto

Kopírovať kód
[default]
debug = true

[database]
host = localhost
port = 5432
user = admin
password = secret
Modul Python :

pytón

Kopírovať kód
DEBUG = True
DATABASE = {
    'HOST': 'localhost',
    'PORT': 5432,
    'USER': 'admin',
    'PASSWORD': 'secret',
}
Príklad použitia konfigurácie v projekte Django
Projekty Django zvyčajne používajú settings.pysúbor na konfiguráciu. Tu je jednoduchý príklad:

pytón

Kopírovať kód
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'default_db_name'),
        'USER': os.getenv('POSTGRES_USER', 'default_db_user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'default_db_password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
V tomto príklade sú konfiguračné nastavenia dynamicky načítané z premenných prostredia. Ak premenná prostredia nie je nastavená, použije sa predvolená hodnota. Tento prístup zvyšuje bezpečnosť a flexibilitu a umožňuje rôzne konfigurácie pre vývojové, testovacie a produkčné prostredia bez zmeny kódovej základne.

Výhody používania konfiguračných súborov
* Oddelenie obáv : Oddelenie konfigurácie od kódu umožňuje jednoduchšiu údržbu a lepšiu organizáciu.
* Flexibilita : Môžete zmeniť správanie vašej aplikácie bez úpravy kódu, čo je užitočné najmä pre rôzne prostredia (vývoj, testovanie, výroba).
* Bezpečnosť : Citlivé informácie, ako sú kľúče API a heslá databázy, je možné spravovať bezpečnejšie prostredníctvom premenných prostredia alebo samostatných konfiguračných súborov.
* Škálovateľnosť : Ako vaša aplikácia rastie, správa nastavení prostredníctvom konfiguračných súborov pomáha pri škálovaní a nasadzovaní aplikácie v rôznych prostrediach a platformách.

>##Je lepšie použiť os.getenv alebo config

Rozhodnutie medzi použitím os.getenv a prístupom vyhradenej správy konfigurácie ( config) závisí od špecifických požiadaviek a zložitosti vášho projektu. Tu je podrobné porovnanie, ktoré vám pomôže rozhodnúť sa:

## Použitie os.getenv

### Výhody:
1. jednoduchosť :
  * Jednoduché použitie bez potreby ďalších knižníc alebo konfiguračných súborov.
2. Konfigurácia špecifická pre prostredie :
  * Ideálne pre nastavenia, ktoré sa líšia medzi vývojovým, pracovným a produkčným prostredím.
3. Bezpečnosť :
  * Dobré na ukladanie citlivých informácií, ako sú kľúče API a heslá mimo kódovej základne.

### Nevýhody:
1. Obmedzená štruktúra :
  * Nie je vhodné na správu zložitých alebo vnorených konfigurácií.
2. Závislosť na životnom prostredí :
  * Plne sa spolieha na prostredie, ktoré môže byť menej flexibilné na správu konfigurácií v rôznych kontextoch.

### Príklad:
~~~
import os

SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
DATABASE = {
    'NAME': os.getenv('DB_NAME', 'default_db'),
    'USER': os.getenv('DB_USER', 'default_user'),
    'PASSWORD': os.getenv('DB_PASSWORD', 'default_password'),
    'HOST': os.getenv('DB_HOST', 'localhost'),
    'PORT': os.getenv('DB_PORT', '5432'),
}
~~~

## Použitie konfiguračného súboru ( config)

### Výhody:
1. Štruktúrovaná konfigurácia :
  * Vhodné na správu zložitých a vnorených nastavení.
2. Rozdelenie obáv :
  * Udržuje konfiguráciu oddelenú od kódu, čím zlepšuje udržiavateľnosť kódu.
3. Flexibilita :
  * Umožňuje komplexnejšie konfigurácie a môže kombinovať viacero zdrojov (premenné prostredia, súbory, predvolené nastavenia).

### Nevýhody:
1. Zložitosť :
  * Vyžaduje ďalšiu manipuláciu na analýzu a správu konfiguračných súborov.
2. Bezpečnosť :
  * S citlivými informáciami sa musí zaobchádzať opatrne, aby sa predišlo expozícii.

### Príklad použitia konfiguračného súboru Pythonu:

1. config.py :
~~~
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    DEBUG = os.getenv('DEBUG', 'False') == 'True'
    DATABASE = {
        'NAME': os.getenv('DB_NAME', 'default_db'),
        'USER': os.getenv('DB_USER', 'default_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'default_password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
~~~

2. Použitie konfigurácie vo vašej aplikácii :
~~~
from config import Config

SECRET_KEY = Config.SECRET_KEY
DEBUG = Config.DEBUG
DATABASE = Config.DATABASE
~~~

## Kombinácia oboch prístupov

Pri väčších projektoch môže byť efektívna kombinácia oboch prístupov. Použite premenné prostredia pre citlivé nastavenia a nastavenia špecifické pre prostredie a konfiguračné súbory pre štruktúrované a predvolené nastavenia.

## Osvedčené postupy

1. Premenné prostredia pre citlivé údaje :
  * Uchovávajte citlivé informácie, ako sú heslá a kľúče API, v premenných prostredia.
2. Konfiguračné súbory pre štruktúrované dáta :
  * Použite konfiguračné súbory pre nastavenia, ktoré využívajú štruktúru a predvolené hodnoty.
3. Použiť konfiguračné knižnice :
  * Knižnice ako python-decouple, dynaconf alebo dotenv môžu pomôcť efektívne spravovať konfigurácie z rôznych zdrojov.
4. Kontrola verzií :
  * Uchovávajte necitlivé konfiguračné súbory pod kontrolou verzií (git a github) na sledovanie zmien a spoluprácu.

## Záver

* **Malé, jednoduché projekty** : Použitie os.getenv môže byť dostatočné pre jeho jednoduchosť.
* **Komplexné projekty** : Vyhradený prístup správy konfigurácie ( config) je lepší na zvládnutie zložitých a štruktúrovaných nastavení.

Po zvážení zložitosti, bezpečnostných potrieb a udržiavateľnosti vášho projektu si môžete vybrať najvhodnejšiu stratégiu riadenia konfigurácie.

>##Čo je pipfile a pipfile.lock

Pipfile a Pipfile.lock sú súbory používané týmto nástrojom **pipenv**, čo je systém správy závislostí pre projekty Python. Slúžia na podobný účel ako requirements.txt ale ponúkajú viac funkcií a výhod.

## Pipfile

Pipfile je súbor s obyčajným textom, ktorý špecifikuje balíky potrebné pre projekt Python. Používa sa na definovanie závislostí projektu v štruktúrovanom a ľudsky čitateľnom formáte.

### Kľúčové vlastnosti:

1. Sekcie :
  * [[source]] :
  * [packages] : Uvádza hlavné závislosti požadované pre projekt.
  * [dev-packages] : Uvádza závislosti potrebné na vývojové účely, ako sú testovacie a liningové nástroje.
  * [requires] : Požiadavky

2. Špecifikácia verzie :
  * Umožňuje špecifikovať obmedzenia verzie pre každý balík.

3. Verzia Pythonu :
  * Môže určiť požadovanú verziu Pythonu pre projekt.

#### Príklad:
~~~
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[packages]
requests = "*"
flask = "==1.1.2"

[dev-packages]
pytest = "*"
black = "*"

[requires]
python_version = "3.8"
~~~

### Pipfile.lock

Súbor Pipfile.lock sa automaticky generuje pri inštalácii pipenv alebo aktualizácii balíkov. Zaznamenáva presné verzie závislostí a ich podzávislostí, čím zaisťuje, že sa dá prostredie presne replikovať.

### Kľúčové vlastnosti:

1. Rozlíšenie závislosti :
  * Obsahuje vyriešené verzie všetkých závislostí, čím zabezpečuje konzistenciu v rôznych prostrediach.
2. hash :
  * Zahŕňa kryptografické hash pre každý balík na zaistenie integrity a bezpečnosti.
3. Kompatibilita platformy :
  * Môže špecifikovať informácie o kompatibilite pre rôzne operačné systémy.

### Príklad (zjednodušený):
json súbor
~~~
{
    "_meta": {
        "hash": {
            "sha256": "..."
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.8"
        }
    },
    "default": {
        "flask": {
            "version": "==1.1.2",
            "hashes": [
                "sha256:..."
            ]
        },
        "requests": {
            "version": "==2.24.0",
            "hashes": [
                "sha256:..."
            ]
        }
    },
    "develop": {
        "pytest": {
            "version": "==6.0.1",
            "hashes": [
                "sha256:..."
            ]
        },
        "black": {
            "version": "==20.8b1",
            "hashes": [
                "sha256:..."
            ]
        }
    }
}
~~~

## Výhody používania Pipfile a Pipfile.lock

1. Vylepšená správa závislostí :
  * V porovnaní s requirements.txt.
  * Oddeľuje vývojové a výrobné závislosti.
2. Reprodukovateľnosť prostredia :
  * Zabezpečuje, že všetky inštalácie projektu používajú presne rovnaké verzie závislostí.
3. Bezpečnosť :
  * Hash Pipfile.lock overuje integritu nainštalovaných balíkov.
4. Kontrola verzií :
  * Jednoduchšia údržba a pochopenie zmien závislostí v systémoch správy verzií.

## Použitie s Pipenv
Na prácu s Pipfile a Pipfile.lock použite nástroj pipenv príkazového riadka.

Inštalácia Pipenv:
~~~
pip install pipenv
~~~
Vytvorenie nového projektu:
~~~
pipenv --python 3.8
~~~
Pridanie závislosti:
~~~
pipenv install requests
~~~
Pridanie závislosti od vývoja:
~~~
pipenv install --dev pytest
~~~
Závislosti uzamknutia:
~~~
pipenv lock
~~~
Inštalácia z Pipfile.lock:
~~~
pipenv install
~~~

## Záver

Pipfile a Pipfile.lock poskytujú moderný a efektívny spôsob správy závislostí projektu Python. Používaním pipenv spolu s týmito súbormi môžete zabezpečiť konzistentné, bezpečné a spravovateľné prostredia pre svoje projekty Python.