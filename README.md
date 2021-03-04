# Kode

Kode es un bot dedicado y mantenido por la comunidad de [Kodetica](https://discord.com/invite/Q3vcJcwDR5).

## Instalación

Clona este repositorio. Ten en cuenta que debes tener instalado [pipenv](https://pypi.org/project/pipenv/) para el manejo del local enviroment. 

Crea un local enviroment

```sh
pipenv --python 3.9
```

Instala las dependencias

```sh
pipenv install
```

Quita la extensión `example` del archivo **.env** y reemplaza los valores.

Una vez hecho esto, deberás iniciar el bot escribiendo

```sh
pipenv run python run.py
```

## Milestones

### v1.0.0

- [x] Skeleton del proyecto.
    - [x] Comando de ejemplo.
    - [x] Evento de ejemplo.
- [ ] Bienvenidas para nuevos usuarios.
- [ ] Integración de base de datos Mongo.
- [ ] Seguimiento a los canales de lenguajes de programación.
    - [ ] Recuento de mensajes.
    - [ ] Métricas en comando.
- [ ] Retos
    - [ ] Comandos de gestión del ranking.
    - [ ] Enviar retos mediante Kode.
    - [ ] Añadir/quitar puntos mediante Kode.


## Contribución

¡Contribuye a Kode!

Haz **fork** a este repositorio, sube los cambios y haz un pull request.

*Una guía de contribución está siendo redactada. ¡Disculpa las molestias!*

## Licencia

Kode está distribuido bajo la licencia [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/)