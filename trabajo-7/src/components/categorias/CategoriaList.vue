<template>
    <div class="list-container">
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="categoria in categorias" :key="categoria.id">
                    <td>{{ categoria.id }}</td>
                    <td>{{ categoria.nombre }}</td>
                    <td class="actions">
                        <button @click="$emit('edit', categoria)" class="btn-edit">Editar</button>
                        <button @click="$emit('delete', categoria)" class="btn-danger">Eliminar</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import type { Categoria } from '@/types/models';

defineProps<{
    categorias: Categoria[]
}>();

defineEmits<{
    (e: 'edit', value: Categoria): void
    (e: 'delete', value: Categoria): void
}>();
</script>

<style scoped>
.actions {
    display: flex;
    gap: 0.5rem;
}
</style>