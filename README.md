$ python -m venv venv

$ . venv/Scripts/activate

$ pip install -r requirements.txt

# Príklad webového projektu FullStack

![image](https://user-images.githubusercontent.com/23359514/183810177-cfb570bf-2432-4625-a9d3-9a843735bc3d.png)

## Obsah
  - [Description](#description)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Licenses](#license)
  - [Contributing](#contributing)
  - [Tests](#tests)
  - [Deployment](#deployment)
  - [Questions](#questions)

  ## Popis
  Toto je jednoduchá webová stránka, ktorá demonštruje kompletný vývoj webu pomocou Django a Vanilla JavaScript, CSS a HTML a ktorá sa dá replikovať v rôznych kontextoch, ako sú osobné portfólio a iné webové stránky. K dispozícii je sprievodné bezplatné vlákno s výukovým videom pre prístup použitý pri písaní kódu a testovaní jeho fungovania. Dá sa k nemu dostať [tu](https://bit.ly/3HXmdLd).

  ## Inštalácia
  Softvérové komponenty tohto projektu zahŕňajú:
  * **Git**
  * **Docker & Docker Compose**
  * **Python**  python==3.10.11
  * **Django**  django==4.2.11
  * **PostgreSQL**

### . my

  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) - Používa sa na kontrolu verzií pri vývoji tohto projektu.
  - [Docker Desktop Windows](https://docs.docker.com/desktop/windows/install/) - Softvér na spracovanie vývojových operácií [(DevOps)](https://about.gitlab.com/topics/devops/) pomocou grafického používateľského rozhrania (GUI) v systéme Windows. Nainštaluje rozhranie príkazového riadka Docker, Docker Compose atď.
  - [Docker Desktop Linux](https://docs.docker.com/desktop/linux/install/) - Softvér na spracovanie vývojových operácií (DevOps-VývojOperatíva) pomocou grafického používateľského rozhrania (GUI) v systéme Linux.
  - [Postgres](https://hub.docker.com/_/postgres?tab=tags) - Systém správy objektovo relačných databáz používaný na ukladanie a podporu operácií DB v tomto projekte. Konkrétna verzia je uvedená v konfiguráciach[development](docker-compose-dev.yml) a [production](docker-compose-dev.yml).
  - [Python](https://www.python.org/downloads/release/python-3810/) - Základný programovací jazyk použitý pri vývoji tohto projektu. Konkrétna verzia (build) je uvedená v konfigurácich [development](Dockerfile-dev) a [production](Dockerfile).
  - [Django](https://docs.djangoproject.com/en/4.0/topics/install/) - Python webový vývojový rámec, ktorý je hlavným rámcom použitým v tomto projekte.

### Závislosti
Back-end pozostáva z kontajnera Docker s Pythonom a Django. Počiatočné závislosti tohto projektu sú uvedené v [Pipfile](Pipfile) a obsahujú: 
* [__Django__](https://docs.djangoproject.com/) ako základný rámec
* [__django-environ__](https://django-environ.readthedocs.org/) pre správu premenných prostredia
* [__markdown__](http://pythonhosted.org/Markdown/siteindex.html) na popis značiek pomocou markdown v HTML
* [__psycopg__](https://www.psycopg.org/docs/) databázový adaptér na uľahčenie pripojenia k databáze a iných operácií.
* [__psycopg-binary__](https://www.psycopg.org/docs/) databázový adaptér na uľahčenie pripojenia k databáze a iných operácií.
* [__crispy-bootstrap5__](https://github.com/django-crispy-forms/crispy-bootstrap5) Balík šablón Bootstrap5 pre crispy-forms django.
* [__django-allauth__](https://django-allauth.readthedocs.io/en/latest/) opakovane použiteľná aplikácia Django, ktorá umožňuje miestne aj sociálne overenie
* [__django-ckeditor__](https://github.com/django-ckeditor/django-ckeditor) poskytovanie podpory editorov v projekte.
* [__whitenoise__](https://github.com/evansd/whitenoise) na správu statického a používateľského nahrávania pri vývoji a produkcii
* [__pillow__](https://python-pillow.org/) na podporu spracovania image a ich schopností. 
* [__gunicorn__](https://gunicorn.org/) HTTP server na podporu poskytovania tohto projektu cez web
* [__dj-database-url__](https://github.com/jazzband/dj-database-url) podpora premennej prostredia URL databázy
* [__boto3__](https://github.com/boto/boto3) podpora schopností Amazonu S3
* [__django-storages__](https://github.com/jschneier/django-storages) podpora pre backend úložiska Amazon S3. Dá sa použiť s inými backendmi úložiska, napr. Digital Ocean, DropBox, Google Cloud atď. 
* [__djangorestframework__](https://www.django-rest-framework.org) na poskytovanie funkcií WebAPI a REST
* [__black__](https://github.com/psf/black) na linting a automatické formátovanie kódu počas vývoja
* [__pytest__](https://docs.pytest.org/en/latest/) na písanie testov
* [__Django Debug Toolbar__](https://django-debug-toolbar.readthedocs.io/) pomôcť s ladením počas vývoja
* [__Faker__](https://faker.readthedocs.io) na generovanie falošných údajov na použitie/testu v tomto projekte (TODO)
* [__coverage__](https://coverage.readthedocs.io/) na meranie pokrytia kódom
* [__pytest-django__](https://pytest-django.readthedocs.io/) na testovanie špecifických funkcií django počas vývoja (TODO)
* [__django-csp__](https://django-csp.readthedocs.io/) na implementáciu Politiky bezpečnosti obsahu v tomto projekte.

### Nasadenie
Minimálne požiadavky potrebné na nasadenie tohto projektu sú [Docker Engine](). Docker Engine obsahuje docker, [docker compose]() a ak na desktopovom prostredí preferujete grafické užívateľské rozhranie,  môžete využiť [Docker Desktop]().

#### Lokalne použitie
1. Naklonujte úložisko pomocou príkazového riadka spustením `git clone https://github.com/jkariukidev/my-demo-website.git`
2. Vytvorte súbor premenných prostredia z poskytnutého súboru [development sample file](.env_dev.sample). Teraz by ste mali mať súbor `.env` vyžadovaný docker-compose.
3. Podľa toho upravte premenné prostredia. Ktoré obsahujú:
   * ``PROJECT_ENV`` - Stav prostredia projektu. Nastavte to na vývoj v nastavení vášho lokálneho počítača.
   * ``SECRET_KEY`` - Podrobne opísaný kryptografický kľúč Django [here](https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key).
   * ``DEBUG`` - Premenná použitá pri riešení problémov vo vývoji (preto ju iba pri vývoji nastavte na ``True``) a nikdy by nemala byť nastavená na  ``True`` v produkcii. [Reference](https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/#debug)
   * ``ALLOWED_HOSTS`` - Zoznam názvov hostiteľov/domén, ktorým môže slúžiť táto stránka Django.
   * ``ENGINE`` - Databázový backend na použitie. Tento projekt štandardne používa backend PostgreSQL, ale dá sa zmeniť v premenných prostredia.
   * ``DB_NAME`` - Databáza, ktorú má táto aplikácia používať.
   * ``DB_USER`` - Užívateľ/rola databázy, ktorú má táto aplikácia používať.
   * ``DB_PASSWORD`` - Heslo pre užívateľa definovaného v `DB_USER`.
   * ``DB_HOST`` - Hostiteľ databázového servera. Definované service `database` v súbore docker-compose.
   * ``DB_PORT`` - Sieťový port používaný databázou je definovaný aj v súboroch docker-compose.
   * ``EMAIL_BACKEND`` - Tbackend, ktorý sa má použiť na odosielanie e-mailov nastavený na `console` vo vývoji. Podrobnosti sú dobre znázornené [tu](https://docs.djangoproject.com/en/4.1/topics/email/).
   * ``POSTGRES_DB`` - Názov databázy Postgres definovaný v súboroch docker-compose. [postgresql reference](https://www.postgresql.org/docs/14/libpq-envars.html), [docker reference](https://hub.docker.com/_/postgres)
   * ``POSTGRES_USER`` - Voliteľná premenná použitá spolu s ``POSTGRES_PASSWORD`` ktorý nastavuje používateľa a heslo. Tiež definované v súboroch docker-compose.
   * ``POSTGRES_PASSWORD`` - Povinná premenná používaná na nastavenie hesla superužívateľa. Nesmie byť prázdne. Tiež definované v súboroch docker-compose.
   
4. Vytvorte požadované obrázky ukotvenia na vývoj spustením `make build-dev`
5. Spustite dokovacie kontajnery spustením `make runserver-dev`
6. Použite migrácie na synchronizáciu stavu databázy s aktuálnou sadou modelov a pomocou migrácie `make migrate-dev`
7. Načítajte počiatočné údaje, vytvorte testovací používateľský účet, kategóriu blogu a blogové príspevky s využitím [django fixtures](https://docs.djangoproject.com/en/4.1/howto/initial-data/) a odkazujúci na súbor [initial.json](website/fixtures/initial.json).
   `make load-initial-data` vytvára vzorové blogové príspevky, superužívateľa a testovacieho používateľa. Ak chcete vidieť túto zmenu, obnovte svoj prehliadač na stránke článkov. 
8. Vytvorte superužívateľa (voliteľné) spustením `make superuser-dev`
9. Ak sa chcete prihlásiť do administračného panela, použite podrobnosti nižšie:
    * URL: http://localhost:8000/tajiri (miestne prostredie) zmenené na [admin](http://localhost:8000/admin)
    * Username: `webadmin`
    * Password: `IAmTheAdmin123`
10. Skontrolujte protokoly pomocou `make logs-dev` alebo na prezeranie protokolov v interakcii `make logs-interactive-dev`

#### Produkcia
  1. Clone this project using `git clone ` command.
      ```shell
     git clone https://github.com/jkariukidev/my-demo-website.git
     ```
  2. Navigate into the cloned project folder and using a terminal/shell or otherwise, rename the [env_prod.sample](.env_prod.sample) to `.env` in production to be recognized by docker compose.
  3. Edit the environment variables as required and ensure you do not share passwords and secure keys with the public. The additional environment variables for production include:
     * ``PROJECT_ENV`` - The project environment state. Set this to production in your in public server host.
     * ``USE_S3`` - Tells Django whether to use AWS S3 bucket for static file management which brings about additional variables defined [here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html). AWS account is required. Read more about [AWS S3](https://docs.aws.amazon.com/s3/).
     * ``EMAIL_BACKEND`` - This is the backend to use for email. Django supports various  [email backends](https://docs.djangoproject.com/en/4.1/topics/email/#topic-email-backends).
     * ``DEFAULT_FROM_EMAIL`` - The default email to use from this site's manager. 
     * ``EMAIL_HOST`` - This is the host to use for sending email.
     * ``EMAIL_HOST_USER`` - The username for the sending service / SMTP defined in the ``EMAIL_HOST``
     * ``EMAIL_HOST_PASSWORD`` - The password for the user for sending service / SMTP defined in the ``EMAIL_HOST``
     * ``EMAIL_PORT`` - The port to use for the email sending service.
     * ``EMAIL_USE_TLS`` - This tells the project whether to use secure protocol (port 587) when communicating with email sending service.
     
  4. Run the docker services for this project using compose in production environment.
     ```
     make runserver
     ```
  5. Propagate models into your database schema using the [migrate command](https://docs.djangoproject.com/en/4.0/ref/django-admin/#migrate). Note
     that this command is being run inside the docker web container. Refer for more on [exec docker command](https://docs.docker.com/engine/reference/commandline/compose_exec/).
     ```
     make migrate
     ```
  6. Check logs using `make logs` or to view the logs interactively use `make logs-interactive`

For several other commands, view them in the [Makefile](Makefile)


  ## Použitie

  - Vývoj a nasadenie modernej webovej stránky
   - Správa osobných blogových článkov
   - Správa používateľských účtov vrátane rozšírenia autentifikácie a autorizácie.
   - Zabezpečenie odosielania e-mailov a webových formulárov
   - REST API

  ## Licencia
  - [LICENSE](LICENSE)

  ## Prispievanie
  If you want to contribute to a project and make it better, your help is very welcome. Contributing is also a great 
  way to learn more about social coding on GitHub, new technologies and their ecosystems and how to make constructive, 
  helpful bug reports, feature requests and the noblest of all contributions: a good, clean pull request.

### vytvorenie požiadavky na čisté vytiahnutie

Vyhľadajte pokyny na príspevok k projektu. Ak sú stručné, postupujte podľa nich.

- Create a personal fork of the project on GitHub by clicking [here](https://github.com/jkariukidev/my-demo-website/fork).
- Clone the fork on your local machine. Your remote repo on GitHub is called `origin`.
- Add the original repository as a remote called `upstream`.
- If you created your fork a while ago be sure to pull upstream changes into your local repository.
- Create a new branch to work on! Branch from `develop` if it exists, else from `master`.
- Implement/fix your feature, comment your code.
- Follow the code style of the project, including indentation.
- If the project has tests run them!
- Write or adapt tests as needed.
- Add or change the documentation as needed.
- Squash your commits into a single commit with git's [interactive rebase](https://help.github.com/articles/interactive-rebase). 
  Create a new branch if necessary.
- Push your branch to your fork on GitHub, the remote `origin`.
- From your fork open a pull request in the correct branch. Target the project's `develop` branch if there is one, else 
  go for `master`!

- If the maintainer requests further changes just push them to your branch. The PR will be updated automatically.
- Once the pull request is approved and merged you can pull the changes from `upstream` to your local repo and delete
your extra branch(es).

And last but not least: Always write your commit messages in the present tense. Your commit message should describe what 
the commit, when applied, does to the code – not what you did to the code.

## Testy
Following the guidelines on testing Python projects using:
 - Implementation of Django Unittest in this project. Run the tests using:
   * ``make test-project`` - To run all automatic django tests for the entire project.
   * ``make test-website`` - To run all automatic django tests for the website app only.
   * ``make test-users`` - To run all automatic django tests for the users app only.
 - Other testing tools that cab be incorporated here include:
   * [Tox](https://docs.djangoproject.com/en/4.0/internals/contributing/writing-code/unit-tests/#running-tests-using-tox)
   * [Django testing tools](https://docs.djangoproject.com/en/4.0/topics/testing/tools/)
 
 Some of the packages that help in testing include:
   * ``Django-Debug-Toolbar`` which by default appears on the test/development deployment as shown.
   ![image](https://user-images.githubusercontent.com/23359514/222653944-16ca0957-582d-42db-8d20-f4d7de68fedd.png)



## Deployment
Use the [production configuration](docker-compose-prod.yml) in deploying into a public server. Following the guidelines on deployment in tutorial demo:
- [Video Tutorial Demo](https://www.youtube.com/playlist?list=PLIET7uEHqcqif6wye0sL-XZ9o95zgYmaa)

## Questions
If you have any questions you can contact me!

- [My Socials](https://linktr.ee/josephkariuki)
- [My Website](https://josephkariuki.com)

## References
- [Django Documentation](https://docs.djangoproject.com/)
- [Learn Django](https://learndjango.com/)
- [Docker Documentation](https://docs.docker.com/)


## PRENOS ÚDAJOV Z SQLite do PostgreSQL

1. Vytvoríme si zálohu celej databázy dumpdata zariadenia SQLite.
najprv musíte urobiť zálohu celej SQLiteDB do formátu JSON pomocou nižšie uvedeného príkazu
~~~
python manage.py dumpdata > whole.json
~~~

2. Ak nemáme PostgreSQL tok kho nainštalujeme z tejto adresy:

https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

3. Pomocou PostgreSQL Shell-u (psql) ktorý sa nachádza pri inštalácii PostgreSQL vytvoríme DB **my_db** a prístupové údaje:
~~~
Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]:
Password for user postgres:

psql (16.2)
WARNING: Console code page (852) differs from Windows code page (1250)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

postgres=# 
~~~

4. Zadáme údaje pre konektivitu na PostgreSQL DB do setting.py :
V settings.py vytvoríme Postgres DB pomocou používateľa a hesla.
~~~
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my_db',
        'USER' : 'postgres',
        'PASSWORD' : '03091953-Tomo',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}
~~~

5. Nainštaluje konektor PostgreSQL DB pre Python

Psycopg je najpopulárnejší databázový adaptér PostgreSQL pre programovací jazyk Python . Jeho hlavnými vlastnosťami sú úplná implementácia špecifikácie Python DB API 2.0 a bezpečnosť vlákien (viacero vlákien môže zdieľať rovnaké pripojenie). https://docs.yugabyte.com/preview/reference/drivers/python/postgres-psycopg2-reference/ 
~~~
$ pip install psycopg2
~~~
6. Vymažte databázu:
$ rm db.sqlite3

7. Odstráňte všetky súbory migrácie (.py) napr. manualne, pretože nepotrebujeme všetky staré migrácie.
$ rm users/migrations/*

Teraz odstráňte typy obsahu (povinné kroky), inak budete mať krásne miliardy chýb
~~~
$ python manage.py shell

>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> ^Z

7. Namiesto toho vytvoríme jeden súbor migrácie na aplikáciu.
~~~
$ python manage.py makemigrations
$ python manage.py migrate
~~~

8. Importujte prípravok pomocou údajov o zaťažení.
Jedným z hlavných krokov je deaktivácia všetkých signálov v projektoch, inak získate jedinečné obmedzenie alebo už vytvorený objekt.
~~~
$ python manage.py loaddata whole.json
~~~
To je všetko, napriek varovaniu, že adresár so statickými súbormi neexistuje. Toto upozornenie nás len informuje, že zadaný adresár pre statické súbory neexistuje, čo môže, ale nemusí byť relevantné pre našu aktuálnu operáciu.

Údaje z SQLite sa úspešne presunuli do PostgreSQL, čo si môžeme overiť v phAdmin4 alebo nainštalovaním rozšírenia PostgreSQL od Chris Kolkman-a do VS-Code.
