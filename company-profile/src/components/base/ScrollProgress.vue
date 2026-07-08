<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const progress = ref(0)
const onScroll = () => {
  const h = document.documentElement.scrollHeight - window.innerHeight
  progress.value = h > 0 ? (window.scrollY / h) * 100 : 0
}
onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  onScroll()
})
onBeforeUnmount(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <div class="fixed top-0 left-0 right-0 z-[60] h-[3px] pointer-events-none">
    <div class="h-full origin-left transition-[width] duration-100 ease-out"
         :style="`width: ${progress}%; background: linear-gradient(90deg, #053063, #46ad64, #22d3ee);`"></div>
  </div>
</template>
