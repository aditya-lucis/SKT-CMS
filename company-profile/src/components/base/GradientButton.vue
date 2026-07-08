<script setup>
import { useMagneticButton } from '@/composables/useMagneticButton'

const props = defineProps({
  variant: { type: String, default: 'primary' }, // 'primary' | 'outline' | 'ghost' | 'white'
  size: { type: String, default: 'md' }, // 'sm' | 'md' | 'lg'
  href: { type: String, default: null },
  magnetic: { type: Boolean, default: true },
})

const { magneticRef } = useMagneticButton(0.25)

const sizes = {
  sm: 'px-4 py-2 text-sm',
  md: 'px-6 py-3 text-sm',
  lg: 'px-8 py-4 text-base',
}

const variants = {
  primary: 'text-white shadow-glow-green',
  outline: 'text-navy-700 border border-navy-200 hover:border-emerald-brand-400',
  ghost: 'text-navy-700 hover:bg-navy-50',
  white: 'bg-white text-navy-700 shadow-glass',
}
</script>

<template>
  <component
    :is="href ? 'a' : 'button'"
    :href="href"
    @click="href && $emit('click', $event)"
    :ref="magnetic ? magneticRef : null"
    :class="[
      'magnetic relative inline-flex items-center justify-center gap-2 rounded-full font-semibold overflow-hidden group transition-colors',
      sizes[size],
      variants[variant],
    ]"
  >
    <!-- Primary gradient bg -->
    <span v-if="variant === 'primary'" class="absolute inset-0"
          style="background: linear-gradient(120deg, #053063, #1c4f96 40%, #46ad64);"></span>
    <span v-if="variant === 'primary'" class="absolute inset-0 shimmer-bg opacity-0 group-hover:opacity-100 transition-opacity"></span>
    <span class="relative flex items-center gap-2">
      <slot />
    </span>
  </component>
</template>
