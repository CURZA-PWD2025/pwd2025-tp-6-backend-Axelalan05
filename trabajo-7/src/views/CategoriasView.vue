<template>
    <div class="view-container">
        <h1>Gestión de Categorías</h1>
        <div class="controls">
            <button @click="openForm()" class="btn-primary">Crear Nueva Categoría</button>
        </div>

        <div v-if="showForm" class="form-overlay">
            <CategoriaForm :categoriaToEdit="seleccionada" @submit="handleFormSubmit" @cancel="closeForm" />
        </div>

        <ConfirmDialog :show="showDeleteDialog" title="Confirmar Eliminación"
            message="¿Estás seguro de que deseas eliminar esta categoría? Esta acción no se puede deshacer."
            @confirm="confirmDelete" @cancel="cancelDelete" />

        <div v-if="store.loading" class="loading">Cargando...</div>
        <div v-else-if="store.error" class="error">{{ store.error }}</div>
        <CategoriaList v-else :categorias="store.categorias" @edit="openForm" @delete="prepareDelete" />
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useCategoriaStore } from '@/stores/categoriaStore';
import type { Categoria } from '@/types/models';
import CategoriaList from '@/components/categorias/CategoriaList.vue';
import CategoriaForm from '@/components/categorias/CategoriaForm.vue';
import ConfirmDialog from '@/components/shared/ConfirmDialog.vue';

const store = useCategoriaStore();
const showForm = ref(false);
const seleccionada = ref<Categoria | null>(null);
const showDeleteDialog = ref(false);
const aEliminar = ref<Categoria | null>(null);

onMounted(() => {
    store.fetchAll();
});

const openForm = (item: Categoria | null = null) => {
    seleccionada.value = item;
    showForm.value = true;
};

const closeForm = () => {
    showForm.value = false;
    seleccionada.value = null;
};

const handleFormSubmit = async (formData: Omit<Categoria, 'id'>) => {
    try {
        if (seleccionada.value) {
            await store.update(seleccionada.value.id, formData);
        } else {
            await store.create(formData);
        }
        closeForm();
    } catch (error) {
        alert('Ocurrió un error al guardar la categoría.');
    }
};

const prepareDelete = (item: Categoria) => {
    aEliminar.value = item;
    showDeleteDialog.value = true;
};

const confirmDelete = async () => {
    if (aEliminar.value) {
        await store.remove(aEliminar.value.id);
    }
    cancelDelete();
};

const cancelDelete = () => {
    showDeleteDialog.value = false;
    aEliminar.value = null;
};
</script>

<style scoped>
.form-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}
</style>