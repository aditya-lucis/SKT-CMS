import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import('@/pages/Login.vue'),
  },
  {
    path: '/',
    component: () => import('@/layouts/AdminLayout.vue'),
    meta: { requiresAuth: true },
    children: [
      { path: '', name: 'dashboard', component: () => import('@/pages/Dashboard.vue') },
      { path: 'content/:section', name: 'content', component: () => import('@/pages/content/SingletonEditor.vue') },
      { path: 'resources/:resource', name: 'resource', component: () => import('@/pages/resources/ResourceManager.vue') },
      { path: 'contact-submissions', name: 'contact-submissions', component: () => import('@/pages/ContactSubmissions.vue') },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to) => {
  const auth = useAuthStore()
  if (to.meta.requiresAuth && !auth.isAuthenticated()) {
    return { name: 'login' }
  }
  if (to.name === 'login' && auth.isAuthenticated()) {
    return { name: 'dashboard' }
  }
})

export default router
