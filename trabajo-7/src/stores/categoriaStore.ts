import { defineStore } from 'pinia';
import ApiService from '../../services/ApiService';
import type { Categoria } from '@/types/models';

interface CategoriaState {
    categorias: Categoria[];
    loading: boolean;
    error: string | null;
}

export const useCategoriaStore = defineStore('categoria', {
    state: (): CategoriaState => ({
        categorias: [],
        loading: false,
        error: null
    }),
    actions: {
        async fetchAll() {
            this.loading = true;
            this.error = null;
            try {
                const response = await ApiService.getAll<Categoria[]>('categorias');
                this.categorias = response.data;
            } catch (error) {
                this.error = 'Error al cargar las categorías.';
            } finally {
                this.loading = false;
            }
        },
        async create(data: Omit<Categoria, 'id'>) {
            await ApiService.create('categorias', data);
            await this.fetchAll();
        },
        async update(id: number, data: Omit<Categoria, 'id'>) {
            await ApiService.update('categorias', id, data);
            await this.fetchAll();
        },
        async remove(id: number) {
            await ApiService.destroy('categorias', id);
            await this.fetchAll();
        }
    }
});