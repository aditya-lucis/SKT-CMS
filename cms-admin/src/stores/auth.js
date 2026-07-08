import { reactive } from 'vue'
import { api } from '@/lib/api'

const state = reactive({
  token: localStorage.getItem('cms_token') || null,
  username: localStorage.getItem('cms_username') || null,
})

export function useAuthStore() {
  const isAuthenticated = () => !!state.token

  async function login(username, password) {
    const { data } = await api.post('/api/auth/login', { username, password })
    state.token = data.access_token
    state.username = username
    localStorage.setItem('cms_token', data.access_token)
    localStorage.setItem('cms_username', username)
  }

  function logout() {
    state.token = null
    state.username = null
    localStorage.removeItem('cms_token')
    localStorage.removeItem('cms_username')
  }

  return { state, isAuthenticated, login, logout }
}
