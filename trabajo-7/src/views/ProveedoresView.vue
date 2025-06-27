<template>
    <div class="view-container">
        <h1>Gestión de Proveedores</h1>
        <div class="controls">
            <button @click="openForm()" class="btn-primary">Crear Nuevo Proveedor</button>
        </div>

        <div v-if="showForm" class="form-overlay">
            <ProveedorForm :proveedorToEdit="seleccionado" @submit="handleFormSubmit" @cancel="closeForm" />
        </div>

        <ConfirmDialog :show="showDeleteDialog" title="Confirmar Eliminación"
            message="¿Estás seguro de que deseas eliminar este proveedor? Esta acción no se puede deshacer."
            @confirm="confirmDelete" @cancel="cancelDelete" />

        <div v-if="store.loading" class="loading">Cargando...</div>
        <div v-else-if="store.error" class="error">{{ store.error }}</div>
        <ProveedorList v-else :proveedores="store.proveedores" @edit="openForm" @delete="prepareDelete" />
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useProveedorStore } from '@/stores/proveedorStore';
import type { Proveedor } from '@/types/models';
import ProveedorList from '@/components/proveedores/ProveedorList.vue';
import ProveedorForm from '@/components/proveedores/ProveedorForm.vue';
import ConfirmDialog from '@/components/shared/ConfirmDialog.vue';

const store = useProveedorStore();
const showForm = ref(false);
const seleccionado = ref<Proveedor | null>(null);
const showDeleteDialog = ref(false);
const aEliminar = ref<Proveedor | null>(null);

onMounted(() => {
    store.fetchAll();
});

const openForm = (item: Proveedor | null = null) => {
    seleccionado.value = item;
    showForm.value = true;
};

const closeForm = () => {
    showForm.value = false;
    seleccionado.value = null;
};

const handleFormSubmit = async (formData: Omit<Proveedor, 'id'>) => {
    try {
        if (seleccionado.value) {
            await store.update(seleccionado.value.id, formData);
        } else {
            await store.create(formData);
        }
        closeForm();
    } catch (error) {
        alert('Ocurrió un error al guardar el proveedor.');
    }
};

const prepareDelete = (item: Proveedor) => {
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
