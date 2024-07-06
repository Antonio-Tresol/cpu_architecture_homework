# Tarea de Simulación de Caché
### Estudiantes:
- ####  Antonio Badilla Olivas - B80874
- ####  Brandon Mora Umaña - C15179
- ####  Oscar Fernández Jiménez - C12840


Este README describe cómo configurar directorios, compilar el proyecto y limpiar los archivos generados para el proyecto de Simulación de Caché. También tiene una sección que explica conceptos fundamentales de caché.

## 1. Compilando el Proyecto

### 1.0. Estructura de Directorios

Antes de compilar el proyecto, asegúrese de que la estructura de directorios sea la siguiente:

- `src/`: Contiene todos los archivos fuente `.cpp`.
- `build/`: Este directorio contendrá todos los archivos objeto `.o` generados durante la compilación.
- `bin/`: Este directorio contendrá el archivo ejecutable después de la compilación.

El `Makefile` creará automáticamente los directorios `build/` y `bin/` si no existen cuando compiles el proyecto.


Para compilar el proyecto y generar el ejecutable, ejecuta el siguiente comando en la terminal:

```bash
make all
```

Este comando compilará todos los archivos `.cpp` en el directorio [`src/`] en archivos objeto en el directorio `build/` y luego vinculará estos archivos objeto para crear un ejecutable en el directorio `bin/`.

### 1.1. Ejecutando el Proyecto

Después de compilar, puedes ejecutar el proyecto con el siguiente comando:

```bash
make run
```

Este comando ejecutará el archivo binario ubicado en el directorio `bin/`.

### 1.2. Limpieza

Para limpiar el proyecto (es decir, eliminar los directorios `build/` y `bin/` y su contenido), ejecuta el siguiente comando:

```bash
make clean
```

Esto eliminará los directorios `build/` y `bin/`, asegurando un estado limpio para una nueva compilación.

### 1.3. Resumen de Comandos

- Compilar el proyecto: `make all`
- Ejecutar el proyecto: `make run`
- Limpiar archivos generados: `make clean`

Asegúrese de estar en el directorio raíz del proyecto al ejecutar estos comandos.

## 2. Un resumen del funcionamiento de una caché y conceptos clave


#### Basado en:

1. Hennessy, J. L., & Patterson, D. A. (2017). *Computer Architecture: A Quantitative Approach*. Morgan Kaufmann.
2. Intermation. (2020a, November 14). EP 073: Introduction to Cache Memory [Video]. YouTube. [https://www.youtube.com/watch?v=Bz49xnKBH_0](https://www.youtube.com/watch?v=Bz49xnKBH_0)
3. Intermation. (2020b, November 15). EP 074: Fully associative caches and replacement algorithms [Video]. YouTube. [https://www.youtube.com/watch?v=A0vR-ks3hsQ](https://www.youtube.com/watch?v=A0vR-ks3hsQ)
4. Intermation. (2020c, November 16). EP 075: Direct Mapped Caches [Video]. YouTube. [https://www.youtube.com/watch?v=zocwH0g-qQM](https://www.youtube.com/watch?v=zocwH0g-qQM)
5. Intermation. (2020d, November 16). EP 076: Set-Associative caches [Video]. YouTube. [https://www.youtube.com/watch?v=gr5M9CULUZw](https://www.youtube.com/watch?v=gr5M9CULUZw)
6. Prof. Dr. Ben H. Juurlink. (2018a, October 22). 1 5 1 caches and the principle of locality [Video]. YouTube. [https://www.youtube.com/watch?v=KmairurdiaY](https://www.youtube.com/watch?v=KmairurdiaY)
7. Prof. Dr. Ben H. Juurlink. (2018b, October 22). 1 5 2 Direct mapped Cache Organization [Video]. YouTube. [https://www.youtube.com/watch?v=l0f39oid9DM](https://www.youtube.com/watch?v=l0f39oid9DM)
8. Prof. Dr. Ben H. Juurlink. (2018c, October 22). 1 5 3 hit or miss example [Video]. YouTube. [https://www.youtube.com/watch?v=6M2FcQTWWSA](https://www.youtube.com/watch?v=6M2FcQTWWSA)
9. Prof. Dr. Ben H. Juurlink. (2018d, October 22). 1 5 4 basic cache optimizations to reduce miss rate [Video]. YouTube. [https://www.youtube.com/watch?v=fOiIdLupl_Y](https://www.youtube.com/watch?v=fOiIdLupl_Y)
10. Prof. Dr. Ben H. Juurlink. (2018e, October 22). 1 5 5 cache equations for set associative caches [Video]. YouTube. [https://www.youtube.com/watch?v=QPmYclDPkJ0](https://www.youtube.com/watch?v=QPmYclDPkJ0)

### 2.0. Ecuaciones y conceptos generales
Una memoria caché es un memoria de acceso rápido cercana al procesador. Su utilidad yace en que reduce el tiempo de acceso a memoria por parte del procesador.
La ecuación que resume el acceso tiempo de acceso a memoria dada una jerarquía de memoria con una memoria ram y una caché de nivel uno esta dada por:

$
AMAT = HitRate \cdot CacheAccessTime + MissRate \cdot MemoryAccessTime
$

Donde HitRate se define como

$
HitRate = \frac{SuccesfulCacheAccess}{TotalNumberOfMemoryAccesses}
$

El MissRate se define como

$
MissRate = 1 - HitRate
$

Con esto definido es claro ver como tener una caché ayuda a hacer más rápido el acceso a memoria. Por ejemplo, si el HitRate de la caché es alto, esencialmente el tiempo de accesso promedio a memoria disminuye.

Diagramaticamente una caché es un conjunto de líneas de caché. Las líneas albergan bloques de memoria. Un bloque de memoria esta conformado por $n$ palabras el tamaños de las palabras esta definido por la arquitectura.
La idea central de utilizar bloques de memoria es aprovecharse de la localidad espacial de los programas, esto es que los programas tienden a usar durante un mismo periodo valores aledaños a las direcciones que piden. Traer un bloque a cache en vez de un solo dato permite aprovecharse de eso, pues los aledaños estaran cargados cuando se quiera pedir un dato cercano y no se tendrá que ir hasta memoria principal o hasta el siguiente nivel de la jerarquía de memoria.

Para ilustrar como se puede ver una cache, se puede ver la siguiente tabla:

| Tag | Memory Block | Valid | Dirty| Lock |
|:---:|:---:|:---:|:---:|:---:|
| $tag_0$ |  [$a_{01}$, $a_{02}$, ..., $a_{0n}$]  | 1 | 0 | 0 |
| . | . | . | . | . |
| . | . | . | . | . |
| . | . | . | . | . |
| $tag_m$ |  [$a_{m1}$, $a_{m2}$, ..., $a_{mn}$]  | 1 | 1 | 1 |

La columna **Tag** representa el identificador del bloque de memoria, el **Memory Block** es donde esta el bloque de memoria con $n$ elementos, la columna de **Valid** indica si el valor de esta línea es válido, la columna **Dirty** indica si esa línea de la cache ha sido modificada con respecto a cuando se cargo por primera vez y **Lock** indica si la línea de cache esta bloqueado en lugar, esto quiere decir que no puede ser desalojada. Este último tiene sentido para código crítico, el cual necesitamos que este en caché todo el tiempo esencialmente.

### 2.1. Mapeo 


La cache necesita una manera de mapear una dirección de memoria a una línea de cache. Para ello usa algoritmos de mapeo. Para explicar estos se hacen las siguientes suposiciones sobre el la cache, tamaño del bloque y el tamaños de las direcciones.
- Tamaño del bloque es 4, es decir un bloque esta conformado por 4 palabras
- La cache tiene 8 líneas
- El tamaño de las direcciones es de 12 bits
Los algoritmos de mapeo de cache son los siguientes:

#### 2.1.1 Mapeo directo (Direct-Mapping)
En el mapeo directo cada bloque de memoria esta asignado una línea de cache. La dirección de memoria se divide de la siguiente manera, los 2 bits menos significativos de la dirección son utilizados como **word id** este identifica especifícamente la posición dentro del bloque de memoria. Los bits restantes de la dirección son el **block address**, de los cuales los 3 bits menos significativos son el **line id** es decir identifican en que línea de la cache va ese bloque.

**Ejemplo:**

Consideremos una dirección de memoria de 12 bits: `1010 0111 0011`.

* **Word ID:** Los últimos 2 bits (`11`) indican que se desea acceder a la tercera palabra dentro del bloque de memoria.
* **Block Address:** Los 10 bits restantes (`1010 0111 00`) representan la dirección del bloque de memoria.
* **Line ID:** Los últimos 3 bits del Block Address (`100`) indican que este bloque de memoria debe ser almacenado en la línea 4 de la caché (ya que 100 en binario es 4 en decimal).

Esencialmente los bits restantes de la dirección se usan como tag en la cache.

**Diagrama:**

```
Dirección de Memoria (12 bits):  1010011   100    11
                                |-------|  |--|   |-|
                                 Tag     Line ID  Word ID
```

En este ejemplo, si la línea 4 de la caché contiene el bloque de memoria con el tag `1010 0111`, entonces se produce un hit de caché y la palabra deseada se puede recuperar directamente de la caché usando el word id. Si la línea 4 contiene un bloque diferente o está vacía, se produce un miss de caché y el bloque debe ser cargado desde la memoria principal.

**Ventajas y Desventajas:**

* **Ventajas:** Simple de implementar y rápido.
* **Desventajas:** Puede haber conflictos si múltiples bloques de memoria se mapean a la misma línea de caché, esto puede llevar a trashing, que se refiere a cuando dos bloques de memoria estan tratando de entrar a la misma linea constantemente.

#### 2.1.2 Mapeo Completamente Asociativo (Fully-Associative)

En el mapeo completamente asociativo un bloque de memoria puede ir a cualquier linea de la cache. En este esquema la dirección se divide solo en el **Word Id**, que para los supuesto dados serían los 2 bits menos significativos y los bits restantes son el **Block Address** que se usaran como tag para el bloque en el primer espacio disponible dentro de la cache, si no hay espacios disponible una política de remplazo debe ser utilizada para desalojar una línea.

**Ejemplo**
Consideremos la misma dirección de memoria de 12 bits: `1010 0111 0011`.

* **Word ID:** Los últimos 2 bits (`11`) indican que se desea acceder a la tercera palabra dentro del bloque de memoria.
* **Block Address:** Los 10 bits restantes (`1010 0111 00`) representan la dirección del bloque de memoria, que se utilizará como tag.

En este caso, el bloque de memoria con el tag `1010 0111 00` puede ser colocado en cualquier línea de la caché que esté disponible. Para determinar si el bloque está en la caché, se debe comparar el tag de la dirección con los tags de todas las líneas de la caché, en caso de que no este, se debe cargar de memoria.

**Diagrama:**

```
Dirección de Memoria (12 bits):  1010011100   11
                                |----------|  |-|
                                     Tag      Word ID
```

**Ventajas y Desventajas:**

* **Ventajas:** Flexibilidad para almacenar cualquier bloque en cualquier línea, lo que reduce la posibilidad de conflictos.
* **Desventajas:** Más complejo de implementar y más lento que el mapeo directo, ya que requiere comparar el tag con todas las líneas de la caché.

#### 2.1.3. Mapeo Asociativo por Conjuntos (Set-Associative)

Este mapeo es un punto medio entre el mapeo directo y el completamente asociativo. La caché se divide en conjuntos (sets) de líneas. Un bloque de memoria se puede almacenar en cualquier línea de un conjunto específico, pero no en cualquier línea de la caché. La dirección de memoria se divide en tres partes:

* **Word ID:** Los bits menos significativos, que identifican la palabra dentro del bloque.
* **Set ID:** los bits menos significativos del **Block Address**, que identifican el conjunto al que pertenece el bloque.
* **Tag:** Bits más significativos del **Block Address**, que se utilizan para identificar el bloque dentro del conjunto.

**Ejemplo:**

Consideremos una caché de 8 líneas, organizada en 4 conjuntos de 2 líneas cada uno.
Ahora con la misma dirección de memoria de 12 bits: `1010 0111 0011` tendríamos:

```
Dirección de Memoria (12 bits):  1010011    100        11
                                |-------|   |-|        |-|
                                 Tag       Set ID     Word ID
```

En este caso, el bloque de memoria con el tag `1010011` se puede almacenar en cualquier línea del conjunto 4. En caso de que este lleno, se debe usar alguna política de remplazo.
Para saber si un bloque se encuentra en cache basta con comparar los el tag de la dirección con los tags de las dos líneas en el conjunto al que esta dirección esta mapeada.

**Ventajas y Desventajas:**

* **Ventajas:** Ofrece un equilibrio entre la simplicidad del mapeo directo y la flexibilidad del mapeo completamente asociativo.
* **Desventajas:** Un poco más complejo que el mapeo directo, pero más simple que el completamente asociativo.

### 2.2. Políticas de Reemplazo

Cuando la caché está llena y se necesita cargar un nuevo bloque, se debe elegir un bloque existente para ser reemplazado. Algunas políticas de reemplazo comunes incluyen:

* **LRU (Least Recently Used):** Reemplaza el bloque que ha estado sin utilizarse durante más tiempo.
* **FIFO (First In First Out):** Reemplaza el bloque que se cargó primero en la caché.
* **Random:** Reemplaza un bloque aleatoriamente.

### 2.3. Políticas de Escritura

Cuando se escribe en la caché, hay dos enfoques principales:

* **Write-through:** Los datos se escriben tanto en la caché como en la memoria principal al mismo tiempo.
* **Write-back:** Los datos se escriben solo en la caché y se marcan como "sucios" (dirty). El bloque sucio se escribe en la memoria principal solo cuando es desalojado de la cache.

