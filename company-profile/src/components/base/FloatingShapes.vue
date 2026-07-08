<script setup>
defineProps({
  count: { type: Number, default: 5 },
  dark: { type: Boolean, default: false },
})
</script>

<template>
  <div class="absolute inset-0 overflow-hidden pointer-events-none" aria-hidden="true">
    <div v-for="i in count" :key="i"
         class="absolute rounded-2xl animate-float"
         :class="dark ? 'border border-white/10 bg-white/5' : 'glass-light border border-white/60'"
         :style="`
           width: ${30 + (i * 13) % 60}px;
           height: ${30 + (i * 17) % 60}px;
           top: ${(i * 27) % 90}%;
           left: ${(i * 41) % 90}%;
           animation-delay: -${i * 1.3}s;
           animation-duration: ${6 + (i % 4)}s;
         `">
    </div>
  </div>
</template>
