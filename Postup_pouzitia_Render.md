>## Postup ako použiť Render

1. Najprv si urobiť účet na Render ak ešte nemáme
2. Vybrať DB službu a vyplniť položky viď. README.md
3. Doplniť do settings.py
   1. URL DB odkaz napr. 
   ~~~
   # postgres://prettyprinted_django_render_t4ni_user:TGw32m7C1Tq74FaVoGFo3uQgXuOqNI9D@dpg-cp8r0gcf7o1s739n914g-a.frankfurt-postgres.render.com/prettyprinted_django_render_t4ni
   ~~~
   2. Inštalovať dj-database-url ak ešte nemáme. Použijeme príkaz 
   ~~~
    $ pip install dj-database-url
   ~~~
   3. Na začiatok settings.py vložiť import
   ~~~
    $ import dj_database_url 
   ~~~
   4. Pod DATABASES vložiť
   ~~~
    DATABASES["default"] = dj_database_url.parse("postgres://prettyprinted_django_render_t4ni_user:TGw32m7C1Tq74FaVoGFo3uQgXuOqNI9D@dpg-cp8r0gcf7o1s739n914g-a.frankfurt-postgres.render.com/prettyprinted_django_render_t4ni")
   ~~~
   5. Urobiť migráciu 
   ~~~
    $ python manage.py migrate
   ~~~
   a ak tam nebude OK ale chyby resp. niečo bude chýbať ako napr. psycopg2 tak odstrániť a doinštalovať (doinštalované doplniť do)

   Chyba InconsistentMigrationHistorypočas makemigrationsnaznačuje, že história migrácie je nekonzistentná. Tu je postup, ako tento problém vyriešiť krok za krokom:
   1. Odstrániť migračné súbory:

Odstráňte všetky migračné súbory v admin/migrationsa users/migrationsokrem __init__.py.

   2. Vytvoriť makemigrations príkazom:
   ~~~
    $ python manage.py makemigrations
   ~~~
   3. Vytvoriť migráciu príkazom:
    ~~~
    $ python manage.py migrate
    ~~~
    5. Skontrolujte a opravte závislosti
        Uistite sa, že sú správne špecifikované závislosti migrácie.

    6. Skontrolujte závislosti migrácie: 
        Otvorte a 0001_initial.py overte atribút .admin/migrations, users/migrations dependencies

    7. Úprava závislostí: 
        Uistite sa , že admin.0001_initial zoznamy sú správne uvedené users.0001_initial ako závislosť, ak sa na ňu spolieha.

    8. Zobraziť migrácie
    Príkaz použite showmigrationsna vizualizáciu aktuálneho stavu a plánu migrácií.

    Zobraziť migrácie:
    ~~~
    $ python manage.py showmigrations
    ~~~
    Plán migrácie:
    ~~~
    $ python manage.py migrate --plan
    ~~~

Chyba InconsistentMigrationHistorypretrváva v dôsledku nesúladu v poradí aplikácie migrácie. Tu je podrobný postup, ako to vyriešiť:

Krok 1: Identifikujte a opravte problémy s migráciou
Chyba InconsistentMigrationHistoryzvyčajne naznačuje, že určité migrácie boli aplikované mimo poradia. Cieľom je zosúladiť históriu migrácie bez manuálneho vrátenia zmien databázy.

Krok 2: Vymažte nekonzistentné záznamy migrácie
Odstrániť všetky správcovské migrácie : Keďže ste odstránili iba admin.0001_initialzáznam, ale admin.0002_logentry_remove_auto_addzáznam stále existuje, odstráňte všetky záznamy migrácie správcov:

sh

Kopírovať kód
python manage.py dbshell
Vo vnútri databázového shellu:

sql

Kopírovať kód
DELETE FROM django_migrations WHERE app='admin';
DELETE FROM django_migrations WHERE app='users';
Potom ukončite prostredie databázy:

sh

Kopírovať kód
\q
Krok 3: Falošné aplikovanie počiatočných migrácií
Falošná žiadosťusers.0001_initial :

sh

Kopírovať kód
python manage.py migrate users 0001_initial --fake
Falošná žiadosťadmin.0001_initial :

sh

Kopírovať kód
python manage.py migrate admin 0001_initial --fake
Krok 4: Použite všetky migrácie
Teraz použite všetky zostávajúce migrácie:

sh

Kopírovať kód
python manage.py migrate
Krok 5: Overte stav migrácie
Skontrolujte stav migrácie, aby ste sa uistili, že je všetko v poriadku:

sh

Kopírovať kód
python manage.py showmigrations
Zhrnutie príkazov krok za krokom:
Otvorte shell databázy:

sh

Kopírovať kód
python manage.py dbshell
Odstrániť nekonzistentné záznamy migrácie:

sql

Kopírovať kód
DELETE FROM django_migrations WHERE app='admin';
DELETE FROM django_migrations WHERE app='users';
Ukončite prostredie databázy:

sh

Kopírovať kód
\q
Falošná users.0001_initialmigrácia aplikácie:

sh

Kopírovať kód
python manage.py migrate users 0001_initial --fake
Falošná admin.0001_initialmigrácia aplikácie:

sh

Kopírovať kód
python manage.py migrate admin 0001_initial --fake
Použiť všetky migrácie:

sh

Kopírovať kód
python manage.py migrate
Overte stav migrácie:

sh

Kopírovať kód
python manage.py showmigrations
Dodržiavanie týchto krokov by malo správne zarovnať históriu migrácie a umožniť vám použiť všetky potrebné migrácie bez ďalších nezrovnalostí.

## Konecne riesenie s admin 0001_initial založené na DROP tabuľky

Chyba relation "django_admin_log" already existsnaznačuje, že tabuľka databázy django_admin_loguž existuje. To sa môže stať, ak bola migrácia čiastočne aplikovaná predtým alebo bola tabuľka vytvorená manuálne.

Ak to chcete vyriešiť, môžete:

Zrušte existujúcu django_admin_logtabuľku a znova použite migráciu.
Sfalšujte adminúvodnú migráciu, ak ste si istí, že štruktúra tabuľky zodpovedá očakávanej štruktúre migrácie.
Možnosť 1: Zrušte existujúcu tabuľku a znova použite migráciu
Otvorte shell databázy:

sh

Kopírovať kód
python manage.py dbshell
Zložte django_admin_logstôl:

sql

Kopírovať kód
DROP TABLE django_admin_log;
Ukončite prostredie databázy:

sh

Kopírovať kód
\q
Znova použite pôvodnú adminmigráciu:

sh

Kopírovať kód
python manage.py migrate admin 0001_initial
Možnosť 2: Falošná adminpočiatočná migrácia
Použiť úvodnú adminmigráciu s --fakepríznakom:

sh

Kopírovať kód
python manage.py migrate admin 0001_initial --fake
Použiť všetky zostávajúce migrácie:

sh

Kopírovať kód
python manage.py migrate
Rekapitulácia krokov
Otvorte shell databázy:

sh

Kopírovať kód
python manage.py dbshell
Zrušte existujúcu django_admin_logtabuľku:

sql

Kopírovať kód
DROP TABLE django_admin_log;
Ukončite prostredie databázy:

sh

Kopírovať kód
\q
Znova použite pôvodnú adminmigráciu:

sh

Kopírovať kód
python manage.py migrate admin 0001_initial
Ak sa rozhodnete migráciu predstierať, postupujte takto:

Falošná počiatočná adminmigrácia:

sh

Kopírovať kód
python manage.py migrate admin 0001_initial --fake
Použiť všetky zostávajúce migrácie:

sh

Kopírovať kód
python manage.py migrate
Vyberte si možnosť, ktorá najlepšie vyhovuje vašej situácii. Zrušením tabuľky a opätovným použitím migrácie sa zabezpečí správne použitie schémy tabuľky, zatiaľ čo predstieranie migrácie je rýchlejšie, ale predpokladá sa, že schéma tabuľky je už správna.

### Zhrnutie
* Zálohujte si databázu.
* Skontrolujte migračné súbory a django_migrations tabuľku.
* Použite --fakena opravu poradia migrácie.
* V prípade potreby odstráňte a znova vytvorte migrácie.
* Uistite sa, že sú správne nastavené závislosti migrácie.
* Použite showmigrationsa migrate --plann a ďalšiu kontrolu.

Podľa týchto krokov by ste mali byť schopní vyriešiť problém s nekonzistentnou históriou migrácie a úspešne spustiť svoje migrácie.

9. Ak sú vyriešené problémy s migráciou otvoríme si DBeaver
    aby sme sa pozreli na našu DB v Render-i. Najskôr však musíme nakonfigurovať pripojenie k PostgrSQL na čo použijeme DB URL z Render-a
    ![](./DBeaver_connection.png)

10. Vytvoríme si na Render webovú službu s commitom našej aplikácie ktorý Render použije pre zostavenie služby.

11. V settings.py vytvoríme prepojenie na Render DB pridaním nasledovnych riadkov:
~~~
database_url = os.getenv("DATABASE_URL")
DATABASES["default"] = dj_database_url.parse(database_url)
~~~
a do .env pridáme nasledovnú premennú prostredia
~~~
DATABASE_URL="postgres://prettyprinted_django_render_t4ni_user:TGw32m7C1Tq74FaVoGFo3uQgXuOqNI9D@dpg-cp8r0gcf7o1s739n914g-a.frankfurt-postgres.render.com/prettyprinted_django_render_t4ni"
~~~

12. Zmeny poleme na github príkazmi:
~~~
$ git add .
$ git commit -m "Komentár o tom čo sa urobilo"
$ git push mdw-gh main
~~~
    