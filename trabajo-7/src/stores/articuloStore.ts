import { defineStore } from 'pinia';
import ApiService from '../../services/ApiService';
import type { Articulo } from '@/types/models';

export interface ArticuloPayload {
    descripcion: string;
    precio: number;
    stock: number;
    marca_id: number;
    proveedor_id: number;
    categoria_ids: number[];
}

interface ArticuloState {
    articulos: Articulo[];
    loading: boolean;
    error: string | null;
}

export const useArticuloStore = defineStore('articulo', {
    state: (): ArticuloState => ({
        articulos: [],
        loading: false,
        error: null
    }),
    actions: {
        async fetchAll() {
            this.loading = true;
            this.error = null;
            try {
                const response = await ApiService.getAll<Articulo[]>('articulos');
                this.articulos = response.data;
            } catch (error) {
                this.error = 'Error al cargar los artículos.';
            } finally {
                this.loading = false;
            }
        },
        async create(data: ArticuloPayload) {
            await ApiService.create('articulos', data);
            await this.fetchAll();
        },
        async update(id: number, data: ArticuloPayload) {
            await ApiService.update('articulos', id, data);
            await this.fetchAll();
        },
        async remove(id: number) {
            await ApiService.destroy('articulos', id);
            await this.fetchAll();
        }
    }
});
