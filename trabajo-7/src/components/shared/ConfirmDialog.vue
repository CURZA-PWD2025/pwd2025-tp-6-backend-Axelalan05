<template>
    <div v-if="show" class="modal-overlay">
        <div class="modal-content">
            <h4>{{ title }}</h4>
            <p>{{ message }}</p>
            <div class="modal-actions">
                <button @click="$emit('cancel')" class="btn-secondary">Cancelar</button>
                <button @click="$emit('confirm')" class="btn-danger">Confirmar</button>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
defineProps<{
    show: boolean
    title: string
    message: string
}>();

defineEmits<{
    (e: 'confirm'): void
    (e: 'cancel'): void
}>();
</script>

<style scoped>
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 2000;
}

.modal-content {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    width: 90%;
    max-width: 400px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.modal-actions {
    margin-top: 1.5rem;
    display: flex;
    justify-content: flex-end;
    gap: 1rem;
}
</style>