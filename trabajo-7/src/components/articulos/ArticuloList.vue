<template>
    <div class="list-container">
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Descripción</th>
                    <th>Precio</th>
                    <th>Stock</th>
                    <th>Marca</th>
                    <th>Proveedor</th>
                    <th>Categorías</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="articulo in articulos" :key="articulo.id">
                    <td>{{ articulo.id }}</td>
                    <td>{{ articulo.descripcion }}</td>
                    <td>${{ articulo.precio }}</td>
                    <td>{{ articulo.stock }}</td>
                    <td>{{ articulo.marca?.nombre || 'N/A' }}</td>
                    <td>{{ articulo.proveedor?.nombre || 'N/A' }}</td>
                    <td>{{ formatCategorias(articulo.categorias) }}</td>
                    <td class="actions">
                        <button @click="$emit('edit', articulo)" class="btn-edit">Editar</button>
                        <button @click="$emit('delete', articulo)" class="btn-danger">Eliminar</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import type { Articulo, Categoria } from '@/types/models';

defineProps<{
    articulos: Articulo[]
}>();

defineEmits<{
    (e: 'edit', value: Articulo): void
    (e: 'delete', value: Articulo): void
}>();

const formatCategorias = (categorias: Categoria[]): string => {
    if (!categorias || categorias.length === 0) return 'N/A';
    return categorias.map(c => c.nombre).join(', ');
};
</script>

<style scoped>
.actions {
    display: flex;
    gap: 0.5rem;
}

td:nth-child(2) {
    max-width: 250px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>