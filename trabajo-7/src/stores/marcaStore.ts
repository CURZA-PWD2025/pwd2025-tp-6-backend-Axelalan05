import { defineStore } from 'pinia';
import ApiService from '../../services/ApiService';
import type { Marca } from '@/types/models';

interface MarcaState {
    marcas: Marca[];
    loading: boolean;
    error: string | null;
}

export const useMarcaStore = defineStore('marca', {
    state: (): MarcaState => ({
        marcas: [],
        loading: false,
        error: null
    }),
    actions: {
        async fetchAll() {
            this.loading = true;
            this.error = null;
            try {
                const response = await ApiService.getAll<Marca[]>('marcas');
                this.marcas = response.data;
            } catch (error) {
                this.error = 'Error al cargar las marcas.';
            } finally {
                this.loading = false;
            }
        },
        async create(data: Omit<Marca, 'id'>) {
            await ApiService.create('marcas', data);
            await this.fetchAll();
        },
        async update(id: number, data: Omit<Marca, 'id'>) {
            await ApiService.update('marcas', id, data);
            await this.fetchAll();
        },
        async remove(id: number) {
            await ApiService.destroy('marcas', id);
            await this.fetchAll();
        }
    }
});