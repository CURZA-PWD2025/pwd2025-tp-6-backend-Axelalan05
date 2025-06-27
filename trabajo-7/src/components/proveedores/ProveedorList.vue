<template>
    <div class="list-container">
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Teléfono</th>
                    <th>Dirección</th>
                    <th>Email</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="proveedor in proveedores" :key="proveedor.id">
                    <td>{{ proveedor.id }}</td>
                    <td>{{ proveedor.nombre }}</td>
                    <td>{{ proveedor.telefono }}</td>
                    <td>{{ proveedor.direccion }}</td>
                    <td>{{ proveedor.email }}</td>
                    <td class="actions">
                        <button @click="$emit('edit', proveedor)" class="btn-edit">Editar</button>
                        <button @click="$emit('delete', proveedor)" class="btn-danger">Eliminar</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import type { Proveedor } from '@/types/models';

defineProps<{
    proveedores: Proveedor[]
}>();
defineEmits<{
    (e: 'edit', value: Proveedor): void
    (e: 'delete', value: Proveedor): void
}>();
</script>

<style scoped>
.actions {
    display: flex;
    gap: 0.5rem;
}
</style>