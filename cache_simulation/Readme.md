# Tarea de Simulación de Caché

Este README describe cómo configurar directorios, compilar el proyecto y limpiar los archivos generados para el proyecto de Simulación de Caché.

## Estructura de Directorios

Antes de compilar el proyecto, asegúrese de que la estructura de directorios sea la siguiente:

- `src/`: Contiene todos los archivos fuente `.cpp`.
- `build/`: Este directorio contendrá todos los archivos objeto `.o` generados durante la compilación.
- `bin/`: Este directorio contendrá el archivo ejecutable después de la compilación.

El `Makefile` creará automáticamente los directorios `build/` y `bin/` si no existen cuando compiles el proyecto.

## Compilando el Proyecto

Para compilar el proyecto y generar el ejecutable, ejecuta el siguiente comando en la terminal:

```bash
make all
```

Este comando compilará todos los archivos `.cpp` en el directorio [`src/`] en archivos objeto en el directorio `build/` y luego vinculará estos archivos objeto para crear un ejecutable en el directorio `bin/`.

## Ejecutando el Proyecto

Después de compilar, puedes ejecutar el proyecto con el siguiente comando:

```bash
make run
```

Este comando ejecutará el archivo binario ubicado en el directorio `bin/`.

## Limpieza

Para limpiar el proyecto (es decir, eliminar los directorios `build/` y `bin/` y su contenido), ejecuta el siguiente comando:

```bash
make clean
```

Esto eliminará los directorios `build/` y `bin/`, asegurando un estado limpio para una nueva compilación.

## Resumen de Comandos

- Compilar el proyecto: `make all`
- Ejecutar el proyecto: `make run`
- Limpiar archivos generados: `make clean`

Asegúrese de estar en el directorio raíz del proyecto al ejecutar estos comandos.