<script setup>
import { computed } from 'vue'

const props = defineProps({
  variant: { type: String, default: 'light' }, // 'light' | 'dark' | 'transparent'
  hover: { type: Boolean, default: true },
  glow: { type: Boolean, default: false },
  padded: { type: Boolean, default: true },
})

const classes = computed(() => {
  const base = 'relative rounded-2xl overflow-hidden transition-all duration-500'
  const v = {
    light: 'glass',
    dark: 'glass-dark text-white',
    transparent: 'bg-transparent border border-white/10',
  }[props.variant]
  const h = props.hover ? 'hover:-translate-y-1.5 hover:shadow-glass-lg' : ''
  const p = props.padded ? 'p-6 md:p-7' : ''
  return [base, v, h, p].join(' ')
})
</script>

<template>
  <div :class="classes">
    <!-- Gradient border -->
    <div v-if="glow"
         class="pointer-events-none absolute inset-0 rounded-2xl opacity-0 transition-opacity duration-500"
         style="padding: 1px; background: linear-gradient(120deg, rgba(70,173,100,0.6), rgba(34,211,238,0.4), rgba(139,92,246,0.3)); -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0); -webkit-mask-composite: xor; mask-composite: exclude;">
    </div>
    <slot />
  </div>
</template>
