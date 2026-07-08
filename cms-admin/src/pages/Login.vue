<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { LogIn, Loader2 } from 'lucide-vue-next'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const auth = useAuthStore()

const username = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')

async function onSubmit() {
  error.value = ''
  loading.value = true
  try {
    await auth.login(username.value, password.value)
    router.push({ name: 'dashboard' })
  } catch (err) {
    error.value = err.response?.data?.detail || 'Login gagal'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-navy-900 via-navy-800 to-navy-950 p-4">
    <div class="w-full max-w-sm">
      <div class="text-center mb-8">
        <div class="w-14 h-14 rounded-2xl mx-auto mb-4 flex items-center justify-center font-display font-bold text-white text-xl"
             style="background: linear-gradient(135deg, #053063, #46ad64);">S</div>
        <h1 class="font-display font-bold text-white text-xl">SKT CMS</h1>
        <p class="text-navy-300 text-sm mt-1">Masuk untuk kelola konten website</p>
      </div>

      <form @submit.prevent="onSubmit" class="card p-6 space-y-4">
        <div>
          <label class="label">Username</label>
          <input v-model="username" type="text" class="input" placeholder="admin" required autofocus />
        </div>
        <div>
          <label class="label">Password</label>
          <input v-model="password" type="password" class="input" placeholder="••••••••" required />
        </div>

        <p v-if="error" class="text-sm text-red-600 bg-red-50 rounded-lg px-3 py-2">{{ error }}</p>

        <button type="submit" class="btn-primary w-full" :disabled="loading">
          <Loader2 v-if="loading" :size="16" class="animate-spin" />
          <LogIn v-else :size="16" />
          {{ loading ? 'Memproses...' : 'Masuk' }}
        </button>
      </form>
    </div>
  </div>
</template>
