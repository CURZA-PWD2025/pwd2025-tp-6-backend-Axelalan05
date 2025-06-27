<template>
    <form @submit.prevent="handleSubmit" class="form-container">
        <h3>{{ isEditing ? 'Editar' : 'Crear' }} Proveedor</h3>
        <div class="form-group">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" v-model="formData.nombre" required>
        </div>
        <div class="form-group">
            <label for="telefono">Teléfono:</label>
            <input type="text" id="telefono" v-model="formData.telefono" required>
        </div>
        <div class="form-group">
            <label for="direccion">Dirección:</label>
            <input type="text" id="direccion" v-model="formData.direccion" required>
        </div>
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="formData.email" required>
        </div>
        <div class="form-actions">
            <button type="button" @click="$emit('cancel')" class="btn-secondary">Cancelar</button>
            <button type="submit" class="btn-primary">{{ isEditing ? 'Actualizar' : 'Crear' }}</button>
        </div>
    </form>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue';
import type { Proveedor } from '@/types/models';

const props = defineProps<{
    proveedorToEdit: Proveedor | null
}>();

const emit = defineEmits<{
    (e: 'submit', payload: Omit<Proveedor, 'id'>): void
    (e: 'cancel'): void
}>();

const initialFormData = { nombre: '', telefono: '', direccion: '', email: '' };
const formData = ref({ ...initialFormData });
const isEditing = computed(() => !!props.proveedorToEdit);

watch(() => props.proveedorToEdit, (newVal) => {
    formData.value = newVal ? { ...newVal } : { ...initialFormData };
}, { immediate: true });

const handleSubmit = () => {
    const { id, ...payload } = formData.value;
    emit('submit', payload);
};
</script>