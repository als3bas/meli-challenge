# Prueba técnica nuevo ingreso
* <s>[Documento con el challenge solicitado](./files/prueba.pdf)</s> (Borrado por privacidad)

# Como empezar

## Requerimientos
* Python > 3.10 & pip
* Docker (Para levantar bd en postgresql)
* Docker-compose > 2.0
* Este repositorio.

## Pasos
### Levantar Base de datos
Debes estar  en la raíz del proyecto.
1. Ejecutar `docker-compose up -d` o `make start`
2. Puedes verificar el estado con `make logs`

### Aplicación
En la raíz del proyecto
1. Ejecutar `pip install -r requirements.txt`
2. Verificar `.env` con los siguientes datos.
```
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
```
3. Ejectuar seeders con `make seeder`
4. Puedes probar la aplicación con:
    * `python ./src/main.py <1>` donde `1` es el mes que quieres ejecutar
    * `make run month=1`, similar al anterior

El archivo `.csv` será almacenado en `./files/reporte_[month].csv`
