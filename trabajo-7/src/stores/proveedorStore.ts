import { defineStore } from 'pinia';
import ApiService from '../../services/ApiService';
import type { Proveedor } from '@/types/models';

interface ProveedorState {
    proveedores: Proveedor[];
    loading: boolean;
    error: string | null;
}

export const useProveedorStore = defineStore('proveedor', {
    state: (): ProveedorState => ({
        proveedores: [],
        loading: false,
        error: null
    }),
    actions: {
        async fetchAll() {
            this.loading = true;
            this.error = null;
            try {
                const response = await ApiService.getAll<Proveedor[]>('proveedores');
                this.proveedores = response.data;
            } catch (error) {
                this.error = 'Error al cargar los proveedores.';
            } finally {
                this.loading = false;
            }
        },
        async create(data: Omit<Proveedor, 'id'>) {
            await ApiService.create('proveedores', data);
            await this.fetchAll();
        },
        async update(id: number, data: Omit<Proveedor, 'id'>) {
            await ApiService.update('proveedores', id, data);
            await this.fetchAll();
        },
        async remove(id: number) {
            await ApiService.destroy('proveedores', id);
            await this.fetchAll();
        }
    }
});