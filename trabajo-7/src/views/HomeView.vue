<template>
    <div class="home-container">
        <h1>Bienvenido al Dashboard de Administración</h1>
        <p>Selecciona una sección en la barra de navegación para empezar a gestionar los recursos.</p>
        <div class="card-container">
            <RouterLink to="/articulos" class="card">
                <h2>Artículos</h2>
                <p>Gestionar productos, stock y precios.</p>
            </RouterLink>
            <RouterLink to="/marcas" class="card">
                <h2>Marcas</h2>
                <p>Administrar las marcas de los productos.</p>
            </RouterLink>
            <RouterLink to="/categorias" class="card">
                <h2>Categorías</h2>
                <p>Organizar los productos en categorías.</p>
            </RouterLink>
            <RouterLink to="/proveedores" class="card">
                <h2>Proveedores</h2>
                <p>Gestionar los proveedores de artículos.</p>
            </RouterLink>
        </div>
    </div>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router';
</script>

<style scoped>
.home-container {
    text-align: center;
}

.card-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
}

.card {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    text-decoration: none;
    color: inherit;
    transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.15);
}

.card h2 {
    color: var(--primary-color);
}
</style>