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
                <tr v-for="marca in marcas" :key="marca.id">
                    <td>{{ marca.id }}</td>
                    <td>{{ marca.nombre }}</td>
                    <td class="actions">
                        <button @click="$emit('edit', marca)" class="btn-edit">Editar</button>
                        <button @click="$emit('delete', marca)" class="btn-danger">Eliminar</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import type { Marca } from '@/types/models';

defineProps<{
    marcas: Marca[]
}>();

defineEmits<{
    (e: 'edit', value: Marca): void
    (e: 'delete', value: Marca): void
}>();
</script>

<style scoped>
.actions {
    display: flex;
    gap: 0.5rem;
}
</style>