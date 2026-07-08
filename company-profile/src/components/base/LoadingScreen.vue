<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const progress = ref(0)
const done = ref(false)
let raf = null
let start = 0

const tick = (t) => {
  if (!start) start = t
  const elapsed = t - start
  // ease-out over ~2s, never reaching 100 until we say done
  const p = Math.min(1, elapsed / 2000)
  // easeOutExpo
  const eased = p === 1 ? 1 : 1 - Math.pow(2, -10 * p)
  progress.value = Math.min(98, Math.round(eased * 100))
  if (p < 1) {
    raf = requestAnimationFrame(tick)
  } else {
    progress.value = 100
    setTimeout(() => { done.value = true }, 200)
  }
}

onMounted(() => { raf = requestAnimationFrame(tick) })
onBeforeUnmount(() => { if (raf) cancelAnimationFrame(raf) })
</script>

<template>
  <div class="fixed inset-0 z-[100] flex items-center justify-center overflow-hidden bg-white">
    <!-- Aurora blobs -->
    <div class="aurora-blob w-[60vw] h-[60vw] -top-[20%] -left-[10%]" style="background: radial-gradient(circle, rgba(70,173,100,0.55), transparent 65%);"></div>
    <div class="aurora-blob w-[55vw] h-[55vw] -bottom-[20%] -right-[10%]" style="background: radial-gradient(circle, rgba(5,48,99,0.55), transparent 65%);"></div>
    <div class="aurora-blob w-[40vw] h-[40vw] top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2" style="background: radial-gradient(circle, rgba(34,211,238,0.35), transparent 65%);"></div>

    <!-- grid overlay -->
    <div class="absolute inset-0 bg-grid opacity-40 pointer-events-none"></div>

    <div class="relative flex flex-col items-center gap-8 px-6">
      <!-- Logo with morphing glow -->
      <div class="relative">
        <div class="absolute inset-0 -m-8 rounded-full opacity-60 blur-2xl animate-pulse"
             style="background: conic-gradient(from 0deg, #46ad64, #22d3ee, #8b5cf6, #46ad64); animation: spin 4s linear infinite;"></div>
        <img src="@/assets/images/logo.png" alt="Nexus Technology"
             class="relative w-28 h-28 md:w-36 md:h-36 object-contain drop-shadow-2xl"
             :class="{ 'logo-enter': true }" />
      </div>

      <!-- Wordmark -->
      <div class="text-center">
        <h1 class="font-display text-2xl md:text-3xl font-bold tracking-tight text-navy-700">
          NEXUS<span class="text-emerald-brand-400">.</span>
        </h1>
        <p class="font-mono text-[11px] md:text-xs uppercase tracking-[0.4em] text-slate-500 mt-1">
          Technology Group
        </p>
      </div>

      <!-- Progress bar -->
      <div class="w-64 md:w-80">
        <div class="relative h-[3px] rounded-full bg-slate-200/80 overflow-hidden">
          <div class="absolute inset-y-0 left-0 rounded-full transition-[width] duration-200 ease-out"
               :style="`width: ${progress}%; background: linear-gradient(90deg, #053063, #46ad64, #22d3ee);`"></div>
        </div>
        <div class="flex justify-between items-center mt-3">
          <span class="font-mono text-[10px] uppercase tracking-[0.3em] text-slate-400">Loading experience</span>
          <span class="font-mono text-[11px] text-navy-700 tabular-nums">{{ progress }}%</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.logo-enter {
  animation: logoIn 1.2s cubic-bezier(0.16, 1, 0.3, 1) both;
}
@keyframes logoIn {
  from { opacity: 0; transform: scale(0.8) translateY(10px); filter: blur(8px); }
  to { opacity: 1; transform: scale(1) translateY(0); filter: blur(0); }
}
</style>
