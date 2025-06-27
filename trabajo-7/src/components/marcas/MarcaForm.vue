<template>
    <form @submit.prevent="handleSubmit" class="form-container">
        <h3>{{ isEditing ? 'Editar' : 'Crear' }} Marca</h3>
        <div class="form-group">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" v-model="formData.nombre" required>
        </div>
        <div class="form-actions">
            <button type="button" @click="$emit('cancel')" class="btn-secondary">Cancelar</button>
            <button type="submit" class="btn-primary">{{ isEditing ? 'Actualizar' : 'Crear' }}</button>
        </div>
    </form>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue';
import type { Marca } from '@/types/models';

const props = defineProps<{
    marcaToEdit: Marca | null
}>();

const emit = defineEmits<{
    (e: 'submit', payload: Omit<Marca, 'id'>): void
    (e: 'cancel'): void
}>();

const formData = ref({
    nombre: ''
});

const isEditing = computed(() => !!props.marcaToEdit);

watch(() => props.marcaToEdit, (newVal) => {
    formData.value.nombre = newVal?.nombre || '';
}, { immediate: true });


const handleSubmit = () => {
    emit('submit', { nombre: formData.value.nombre });
};
</script>