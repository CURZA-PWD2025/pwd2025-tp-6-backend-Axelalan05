<template>
    <form @submit.prevent="handleSubmit" class="form-container">
        <h3>{{ isEditing ? 'Editar' : 'Crear' }} Artículo</h3>

        <div class="form-group">
            <label for="descripcion">Descripción:</label>
            <textarea id="descripcion" v-model="formData.descripcion" required rows="3"></textarea>
        </div>

        <div class="form-group">
            <label for="precio">Precio:</label>
            <input type="number" id="precio" v-model="formData.precio" required step="0.01" min="0">
        </div>

        <div class="form-group">
            <label for="stock">Stock:</label>
            <input type="number" id="stock" v-model="formData.stock" required min="0">
        </div>

        <div class="form-group">
            <label for="marca">Marca:</label>
            <select id="marca" v-model="formData.marca_id" required>
                <option disabled value="">Seleccione una marca</option>
                <option v-for="marca in marcas" :key="marca.id" :value="marca.id">
                    {{ marca.nombre }}
                </option>
            </select>
        </div>

        <div class="form-group">
            <label for="proveedor">Proveedor:</label>
            <select id="proveedor" v-model="formData.proveedor_id" required>
                <option disabled value="">Seleccione un proveedor</option>
                <option v-for="proveedor in proveedores" :key="proveedor.id" :value="proveedor.id">
                    {{ proveedor.nombre }}
                </option>
            </select>
        </div>

        <div class="form-group">
            <label for="categorias">Categorías (Ctrl+Click para seleccionar varias):</label>
            <select id="categorias" v-model="formData.categoria_ids" multiple>
                <option v-for="categoria in categorias" :key="categoria.id" :value="categoria.id">
                    {{ categoria.nombre }}
                </option>
            </select>
        </div>

        <div class="form-actions">
            <button type="button" @click="$emit('cancel')" class="btn-secondary">Cancelar</button>
            <button type="submit" class="btn-primary">{{ isEditing ? 'Actualizar' : 'Crear' }}</button>
        </div>
    </form>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue';
import type { Articulo, Marca, Proveedor, Categoria } from '@/types/models';
import type { ArticuloPayload } from '@/stores/articuloStore';

const props = defineProps<{
    articuloToEdit: Articulo | null,
    marcas: Marca[],
    proveedores: Proveedor[],
    categorias: Categoria[]
}>();

const emit = defineEmits<{
    (e: 'submit', payload: ArticuloPayload): void
    (e: 'cancel'): void
}>();

const initialFormData: ArticuloPayload = {
    descripcion: '',
    precio: 0,
    stock: 0,
    marca_id: 0,
    proveedor_id: 0,
    categoria_ids: []
};

const formData = ref<ArticuloPayload>({ ...initialFormData });

const isEditing = computed(() => !!props.articuloToEdit);

watch(() => props.articuloToEdit, (newVal) => {
    if (newVal) {
        formData.value = {
            descripcion: newVal.descripcion,
            precio: parseFloat(newVal.precio), // Convertimos el string a número
            stock: newVal.stock,
            marca_id: newVal.marca?.id || 0,
            proveedor_id: newVal.proveedor?.id || 0,
            categoria_ids: newVal.categorias?.map(c => c.id) || []
        };
    } else {
        formData.value = { ...initialFormData };
    }
}, { immediate: true });

const handleSubmit = () => {
    // Aseguramos que los IDs sean números y no strings de los selects
    const payload: ArticuloPayload = {
        ...formData.value,
        marca_id: Number(formData.value.marca_id),
        proveedor_id: Number(formData.value.proveedor_id),
    };
    emit('submit', payload);
};
</script>