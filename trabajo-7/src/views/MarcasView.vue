<template>
    <div class="view-container">
        <h1>Gestión de Marcas</h1>
        <div class="controls">
            <button @click="openForm()" class="btn-primary">Crear Nueva Marca</button>
        </div>

        <div v-if="showForm" class="form-overlay">
            <MarcaForm :marcaToEdit="seleccionada" @submit="handleFormSubmit" @cancel="closeForm" />
        </div>

        <ConfirmDialog :show="showDeleteDialog" title="Confirmar Eliminación"
            message="¿Estás seguro de que deseas eliminar esta marca? Esta acción no se puede deshacer."
            @confirm="confirmDelete" @cancel="cancelDelete" />

        <div v-if="store.loading" class="loading">Cargando...</div>
        <div v-else-if="store.error" class="error">{{ store.error }}</div>
        <MarcaList v-else :marcas="store.marcas" @edit="openForm" @delete="prepareDelete" />
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useMarcaStore } from '@/stores/marcaStore';
import type { Marca } from '@/types/models';
import MarcaList from '@/components/marcas/MarcaList.vue';
import MarcaForm from '@/components/marcas/MarcaForm.vue';
import ConfirmDialog from '@/components/shared/ConfirmDialog.vue';

const store = useMarcaStore();
const showForm = ref(false);
const seleccionada = ref<Marca | null>(null);
const showDeleteDialog = ref(false);
const aEliminar = ref<Marca | null>(null);

onMounted(() => {
    store.fetchAll();
});

const openForm = (item: Marca | null = null) => {
    seleccionada.value = item;
    showForm.value = true;
};

const closeForm = () => {
    showForm.value = false;
    seleccionada.value = null;
};

const handleFormSubmit = async (formData: Omit<Marca, 'id'>) => {
    try {
        if (seleccionada.value) {
            await store.update(seleccionada.value.id, formData);
        } else {
            await store.create(formData);
        }
        closeForm();
    } catch (error) {
        alert('Ocurrió un error al guardar la marca.');
    }
};

const prepareDelete = (item: Marca) => {
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