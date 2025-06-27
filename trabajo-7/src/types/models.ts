export interface Marca {
    id: number;
    nombre: string;
}

export interface Categoria {
    id: number;
    nombre: string;
}

export interface Proveedor {
    id: number;
    nombre: string;
    telefono: string;
    direccion: string;
    email: string;
}

export interface Articulo {
    id: number;
    descripcion: string;
    precio: string;
    stock: number;
    marca: Marca;
    proveedor: Proveedor;
    categorias: Categoria[];
}