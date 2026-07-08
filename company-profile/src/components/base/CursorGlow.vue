<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const x = ref(0)
const y = ref(0)
const visible = ref(false)
let raf = null

const onMove = (e) => {
  if (raf) return
  raf = requestAnimationFrame(() => {
    x.value = e.clientX
    y.value = e.clientY
    visible.value = true
    raf = null
  })
}
const onLeave = () => { visible.value = false }

onMounted(() => {
  if (window.matchMedia('(hover: none)').matches) return
  window.addEventListener('mousemove', onMove, { passive: true })
  document.addEventListener('mouseleave', onLeave)
})
onBeforeUnmount(() => {
  window.removeEventListener('mousemove', onMove)
  document.removeEventListener('mouseleave', onLeave)
})
</script>

<template>
  <div v-if="visible"
       class="pointer-events-none fixed z-[55] mix-blend-multiply hidden md:block"
       :style="`left: ${x}px; top: ${y}px; transform: translate(-50%, -50%);`">
    <div class="w-72 h-72 rounded-full opacity-20 blur-3xl"
         style="background: radial-gradient(circle, rgba(70,173,100,0.6), rgba(34,211,238,0.3) 50%, transparent 70%);"></div>
  </div>
</template>
