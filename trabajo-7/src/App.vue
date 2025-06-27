<template>
  <header>
    <nav class="navbar">
      <div class="logo">
        <RouterLink to="/">Admin Dashboard</RouterLink>
      </div>
      <div class="nav-links">
        <RouterLink to="/articulos">Artículos</RouterLink>
        <RouterLink to="/marcas">Marcas</RouterLink>
        <RouterLink to="/categorias">Categorías</RouterLink>
        <RouterLink to="/proveedores">Proveedores</RouterLink>
      </div>
    </nav>
  </header>
  <main>
    <RouterView />
  </main>
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<style>
@import '@/assets/base.css';

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: #2c3e50;
  color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.logo a {
  font-weight: bold;
  font-size: 1.5rem;
  color: white;
  text-decoration: none;
}

.nav-links {
  display: flex;
  gap: 1.5rem;
}

.nav-links a {
  color: #bdc3c7;
  text-decoration: none;
  font-size: 1rem;
  transition: color 0.3s;
}

.nav-links a:hover,
.nav-links a.router-link-exact-active {
  color: #42b983;
}

main {
  padding: 2rem;
}
</style>