<template>
    <div class="view-container">
        <h1>Gestión de Artículos</h1>
        <div class="controls">
            <button @click="openForm()" class="btn-primary">Crear Nuevo Artículo</button>
        </div>

        <div v-if="showForm" class="form-overlay">
            <ArticuloForm :articuloToEdit="seleccionado" :marcas="marcaStore.marcas"
                :proveedores="proveedorStore.proveedores" :categorias="categoriaStore.categorias"
                @submit="handleFormSubmit" @cancel="closeForm" />
        </div>

        <ConfirmDialog :show="showDeleteDialog" title="Confirmar Eliminación"
            message="¿Estás seguro de que deseas eliminar este artículo? Esta acción no se puede deshacer."
            @confirm="confirmDelete" @cancel="cancelDelete" />

        <div v-if="articuloStore.loading" class="loading">Cargando artículos...</div>
        <div v-else-if="articuloStore.error" class="error">{{ articuloStore.error }}</div>
        <ArticuloList v-else :articulos="articuloStore.articulos" @edit="openForm" @delete="prepareDelete" />
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useArticuloStore, type ArticuloPayload } from '@/stores/articuloStore';
import { useMarcaStore } from '@/stores/marcaStore';
import { useProveedorStore } from '@/stores/proveedorStore';
import { useCategoriaStore } from '@/stores/categoriaStore';
import type { Articulo } from '@/types/models';

import ArticuloList from '@/components/articulos/ArticuloList.vue';
import ArticuloForm from '@/components/articulos/ArticuloForm.vue';
import ConfirmDialog from '@/components/shared/ConfirmDialog.vue';

const articuloStore = useArticuloStore();
const marcaStore = useMarcaStore();
const proveedorStore = useProveedorStore();
const categoriaStore = useCategoriaStore();

const showForm = ref(false);
const seleccionado = ref<Articulo | null>(null);
const showDeleteDialog = ref(false);
const aEliminar = ref<Articulo | null>(null);

onMounted(() => {
    articuloStore.fetchAll();
    marcaStore.fetchAll();
    proveedorStore.fetchAll();
    categoriaStore.fetchAll();
});

const openForm = (item: Articulo | null = null) => {
    seleccionado.value = item;
    showForm.value = true;
};

const closeForm = () => {
    showForm.value = false;
    seleccionado.value = null;
};

const handleFormSubmit = async (formData: ArticuloPayload) => {
    try {
        if (seleccionado.value) {
            await articuloStore.update(seleccionado.value.id, formData);
        } else {
            await articuloStore.create(formData);
        }
        closeForm();
    } catch (error) {
        alert('Ocurrió un error al guardar el artículo.');
    }
};

const prepareDelete = (item: Articulo) => {
    aEliminar.value = item;
    showDeleteDialog.value = true;
};

const confirmDelete = async () => {
    if (aEliminar.value) {
        await articuloStore.remove(aEliminar.value.id);
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