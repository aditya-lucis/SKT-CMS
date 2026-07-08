import axios from 'axios'
import router from '@/router'

export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export const api = axios.create({
  baseURL: API_BASE_URL,
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('cms_token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  return config
})

api.interceptors.response.use(
  (res) => res,
  (err) => {
    if (err.response?.status === 401) {
      localStorage.removeItem('cms_token')
      if (router.currentRoute.value.name !== 'login') {
        router.push({ name: 'login' })
      }
    }
    return Promise.reject(err)
  }
)

/** Resolves a possibly-relative media URL (e.g. "/uploads/x.jpg") to an absolute one. */
export function resolveMediaUrl(url) {
  if (!url) return ''
  if (url.startsWith('http://') || url.startsWith('https://')) return url
  return `${API_BASE_URL}${url}`
}
