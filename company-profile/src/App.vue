<script setup>
import { ref, onMounted } from 'vue'
import { useLenis } from '@/composables/useLenis'
import { useReveal, refreshReveal } from '@/composables/useReveal'
import { useParallax, refreshParallax } from '@/composables/useParallax'
import { useSiteContent } from '@/store/siteContent'
import { API_BASE_URL } from '@/lib/api'
import LoadingScreen from '@/components/base/LoadingScreen.vue'

const loading = ref(true)
const fetchFailed = ref(false)
useLenis()
useReveal()
useParallax()

const { fetchContent } = useSiteContent()

onMounted(() => {
  const minTimer = new Promise((resolve) => setTimeout(resolve, 2200))
  const contentReady = fetchContent().catch(() => { fetchFailed.value = true })

  // Loading screen is an overlay; content is always rendered underneath.
  // Hide it once both the minimum splash time AND the content fetch are
  // done, then refresh reveal/parallax so anything that mounted while
  // hidden gets properly animated in.
  Promise.all([minTimer, contentReady]).then(() => {
    loading.value = false
    setTimeout(() => { refreshReveal(); refreshParallax() }, 100)
    setTimeout(() => { refreshReveal(); refreshParallax() }, 1000)
  })
})
</script>

<template>
  <div v-if="fetchFailed" class="fixed top-0 inset-x-0 z-[200] bg-red-600 text-white text-sm text-center py-2 px-4">
    ⚠️ Gagal memuat konten dari <code>{{ API_BASE_URL }}</code> — pastikan backend jalan, dan cek CORS_ORIGINS di <code>cms-backend/.env</code> sudah termasuk origin ini. Detail error ada di browser console (F12).
  </div>
  <RouterView />
  <Transition name="loader-fade">
    <LoadingScreen v-if="loading" />
  </Transition>
</template>

<style>
.loader-fade-leave-active {
  transition: opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1), transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
}
.loader-fade-leave-to {
  opacity: 0;
  transform: translateY(-2%) scale(1.02);
}
</style>
