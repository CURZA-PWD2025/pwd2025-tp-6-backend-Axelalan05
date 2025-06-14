# TRABAJO N°6

Vamos a desarrollar nuestro `backend` para gestionar una tienda de productos informáticos.
para lo cual crearemos los modulos:

- articulos
- marcas
- categorias
- proveedores
  Los mismo como vimos en clases estarán compuestos por un controladr, un modelo y las rutas hacia los metodos correspondientes del controlador por ejemplo:

- `EntidadController`
- `EntidadModel`
- `EntidadRoutes`

## Definiendo los modelos

El **Articulo** tienen como atributos

| Atributo    |      Tipo      |
| ----------- | :------------: |
| id          |      int       |
| descripcion |      str       |
| precio      |     float      |
| stock       |      int       |
| marca       |   MarcaModel   |
| proveedor   | ProveedorModel |
| categorias | list[CategoriaModel]|

**Categorias** y **Marca**

| Atributo    | Tipo |
| ----------- | :--: |
| id          | int  |
| descripcion | str  |

**Proveedores**:

| Atributo  | Tipo |
| --------- | :--: |
| id        | int  |
| nombre    | str  |
| telefono  | int  |
| direccion | str  |
| email     | str  |

### Las relaciones estan dadas de esta manera:

- Un artículo puede tener varias categorias
- Una categoria puede tener muchos articulos
- Un articulo puede tener solo una marca y solo un proveedor

### Métodos necesarios

vamos a crear los metodos para poder persistir los modelos en nuestra base de datos y manejar los recursos

#### MÉTODOS A CREAR EN LOS MODELS

| metodo       |  Tipo  | parametros | Tipos |   retorno    |
| ------------ | :----: | :--------: | :---: | :----------: |
| get_all      | static |     -      |   -   |  list[dict]  |
| get_one      | static |     id     |  int  |     dict     |
| create       | public |    data    | dict  | boolean/None |
| update       | public |    data    | dict  | boolean/None |
| delete       | public |     id     |  int  | boolean/None |
| serializar   | public |     -      |   -   |     dict     |
| deserializar | static |    data    | dict  |    object    |

#### MÉTODOS A CREAR EN LOS CONTROLLERS

| metodo  |  Tipo  | parametros | Tipos |  retorno   |
| ------- | :----: | :--------: | :---: | :--------: |
| get_all | static |     -      |   -   | list[dict] |
| get_one | static |     id     |  int  |    dict    |
| create  | static |    data    | dict  |    dict    |
| update  | static |    data    | dict  |    dict    |
| delete  | static |     id     |  int  |    dict    |

#### FUNCIONES A CREAR EN LAS RUTAS

| metodo  | parametros | Tipos | retorno |
| ------- | :--------: | :---: | :-----: |
| get_all |     -      |   -   |  dict   |
| get_one |     id     |  int  |  dict   |
| create  |     -      |   -   |  dict   |
| update  |     id     |  int  |  dict   |
| delete  |     id     |  int  |  dict   |

