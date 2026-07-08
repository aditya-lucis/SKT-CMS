<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { ArrowUp } from 'lucide-vue-next'

const show = ref(false)
const onScroll = () => { show.value = window.scrollY > 800 }
const scrollTop = () => {
  if (window.__lenis) window.__lenis.scrollTo(0, { duration: 1.4 })
  else window.scrollTo({ top: 0, behavior: 'smooth' })
}
onMounted(() => { window.addEventListener('scroll', onScroll, { passive: true }); onScroll() })
onBeforeUnmount(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <Transition name="scale-fade">
    <button v-if="show" @click="scrollTop" aria-label="Back to top"
            class="fixed bottom-6 right-6 z-50 w-12 h-12 rounded-full glass-dark text-white flex items-center justify-center shadow-glow-green hover:scale-110 transition-transform">
      <ArrowUp :size="20" />
    </button>
  </Transition>
</template>

<style scoped>
.scale-fade-enter-active, .scale-fade-leave-active { transition: all 0.4s cubic-bezier(0.16,1,0.3,1); }
.scale-fade-enter-from, .scale-fade-leave-to { opacity: 0; transform: scale(0.6); }
</style>
