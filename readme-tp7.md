# Trabajo Práctico N.º 7

## Consumir recursos de nuestra API REST

Para este trabajo vamos a utilizar nuestro **backend** en **Flask**.  
Crearemos nuestro **frontend**, el cual se servirá del mismo para mostrar y persistir los datos en la base de datos.  
Pensemos en un _dashboard_ para el área de administración de la aplicación, en la cual un administrador o usuario trabaje creando, actualizando o eliminando recursos.

Recuerden crear una aplicación de **VUEJS** como lo venimos haciendo. Pueden usar el instalador oficial de **VueJS**, que ya les da como opción de instalación `vue-router` y `pinia`.  
Aparte, no se olviden de instalar el _plugin_ de `axios`:

```bash
npm i axios
```

La idea es tener dos carpetas centrales:

- Una que contenga nuestro **backend**.
- Otra que contenga el **frontend**.

```bash
/app
    |-- /backend
    |   |-- /app
    |   |-- /venv
    |   |-- .gitignore
    |   |-- .env
    |   |-- requirements.txt
    |   |-- run.py
    |   |-- db-init.py
    |   |-- ...
    |-- /frontend
        |-- /src
        |-- package.json
        |-- package-lock.json
        |-- .env
        |-- ...    
```

### Creación del ApiService (servicio genérico) o servicios por módulo

Como estuvimos trabajando en clase, pueden crear un `ApiService` genérico para consumir nuestra API REST. Allí tendremos nuestros métodos para trabajar con el **backend**.  
También pueden crear un servicio por cada módulo. Si eligen esta última opción, ya no reciben un endpoint, sino que lo escriben directamente en el mismo servicio.

Métodos comunes:

- **listar / getAll()** → recibe un endpoint y retorna una respuesta.
- **listarUno / getOne() / getByID** → recibe un endpoint y un identificador para buscar, y retorna un recurso.
- **crear / create()** → recibe un endpoint y datos que persistirá en la base; si es exitosa, retornará un mensaje y/o _status code_.
- **modificar / update()** → recibe un endpoint, un identificador y datos que servirán para modificar un recurso; retorna un mensaje y/o _status code_.
- **eliminar / destroy()** → recibe un endpoint y un identificador que servirá para eliminar un recurso en particular.

> Ejemplo de uno y otro método:

```js
// En ApiService
async getAll(url: string) {
    const response = await axios.get(url);
}

// En MarcaService
async getAllMarcas() {
    const response = await axios.get("marcas/");
}
```

### Creación de los **stores** o **almacenes**

Para cada módulo crearemos su propio `store`, por ejemplo:

- proveedores
- marcas
- categorías
- artículos

Cada uno manejará la información correspondiente, con las funciones necesarias para:

- listar
- mostrar un recurso
- crear
- editar
- eliminar

### Creación de los componentes

Vamos a crear nuestros componentes para cada módulo, los mismos que trabajamos en el **backend**:

- Proveedores
- Marcas
- Categorías
- Artículos

Estos componentes tendrán la lógica para:

- crear
- editar
- eliminar
- mostrar
- listar

Como sugerencia para tener ordenados sus archivos y códigos, trabajen dentro de la carpeta `components`, y por cada módulo creen una subcarpeta para alojar sus archivos.

### Creación de las vistas

Para cada módulo crearemos una vista, donde implementaremos la navegación. Tendrán que crear como mínimo 4 vistas. También piensen cómo mostrar el _dashboard_, creando una vista `Home` que contenga todo.

Vistas sugeridas:

- ArticulosView
- CategoriasView
- MarcasView
- ProveedoresView

### Creación de las rutas

Una vez que tenemos creados todos los componentes necesarios (módulos y vistas), vamos a definir las rutas para acceder a ellos.  
Pueden hacerlo con archivos independientes y agregarlos al enrutador principal, o definirlas directamente en el enrutador principal. Esta última opción, si bien funciona, es más difícil de mantener o actualizar si la aplicación crece.

> **Consideraciones de diseño:**  
Si bien no es parte directa de la materia, usen los conocimientos de **Diseño Gráfico** para que la aplicación tenga una estética acorde. Tengan en cuenta:

- paleta de colores
- tipografías / fuentes
- jerarquía tipográfica
- iconografía
- logotipo (tipografía o imagen)
