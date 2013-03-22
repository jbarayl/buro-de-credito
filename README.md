buro-de-credito
===============

Para migraciondes de modelos ver:
	http://south.aeracode.org/


	To start using south...

	Make sure your django tables match your current database tables exactly - if you planned to add or remove columns, comment those out.
	
	manage.py schemamigration creditos --initial
	manage.py migrate creditos --fake
	
	Make changes to your django model
	
	manage.py schemamigration creditos --auto
	manage.py migrate creditos

	Solo para migrar nuevos cambios

	manage.py schemamigration creditos --auto
	manage.py migrate creditos


En caso de que no se pueda subir datos de ciudades a base de datos poner: 
  manage.py cities_light --force-import-all


Tutorial básico de django south
Posted: octubre 24th, 2012 | Author: fpuga | Filed under: Sin categoría | Tags: desarrollo sofware, django, south, tutorial, web | No Comments »
South es una app de django que permite modificar la estructura de la base de datos de una aplicación django cuando cambiamos el modelo (models.py).

El comando syncdb sólo crea nuevas tablas, pero no modifica tablas existentes, así que si en el modelo de una aplicación renombramos un campo de una tabla existente syncdb no realizará ese cambio en la base de datos. A este tipo de cambios en la base de datos se les denomina “migración del esquema” y es de lo que se encarga South.

Instalación

SOLO: pip install -r requirements.txt

pip install south
Agregar “south” a INSTALLED_APPS
Ejecutar syncdb antes de crear nuestros propios modelos. Está será la última (y única) vez, que necesitamos ejecutar este comando
manage.py syncdb
Usar south en un una app nueva
 Crear la aplicación, y empezar a rellenar el models.py
Crear el script de migración inicial
python manage.py schemamigration app_name –initial
Hacer los cambios en la bbdd
python manage.py migrate app_name
Usar south en una app ya creada
python manage.py convert_to_south app_name

En el caso de que haya otros desarrolladores en el equipo y cada cual esté usando su propia instancia de la base de datos, el resto de desarrolladores ejecutará:
python manage.py migrate app_name –fake

Migración de modelos
Modificamos el models.py de nuestra aplicación
Crear un nuevo script de migración
python manage.py schemamigration app_name –auto
Aplicar la migración a la bbdd
python manage.py migrate app_name
Como funciona
Se puede decir que South funciona en varios niveles de abstracción disintos.

Añade una tabla en la base de datos que mantiene el estado actual de la base de datos. Es decir, guarda que migraciones se han aplicado.
Crea un directorio en la applicación, donde guarda para cada migración un fichero (script) con la información necesaria para realizarla
Añade varios comandos al manage.py
Los ficheros de migración generados en deben subirse al repositorio para que el resto de los desarrolladores pueda también realizar la migración.

PARA VER ESTRUCTURA DE LAS TABLAS DE LA BASE DE DATOS:
	python manage.py sql polls