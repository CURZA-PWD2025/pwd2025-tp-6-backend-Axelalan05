import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/marcas',
            name: 'marcas',
            component: () => import('../views/MarcasView.vue')
        },
        {
            path: '/categorias',
            name: 'categorias',
            component: () => import('../views/CategoriasView.vue')
        },
        {
            path: '/proveedores',
            name: 'proveedores',
            component: () => import('../views/ProveedoresView.vue')
        },
        {
            path: '/articulos',
            name: 'articulos',
            component: () => import('../views/ArticulosView.vue')
        }
    ]
})

export default router