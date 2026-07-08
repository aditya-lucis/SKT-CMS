<script setup>
defineProps({
  eyebrow: { type: String, default: '' },
  title: { type: String, default: '' },
  highlight: { type: String, default: '' },
  subtitle: { type: String, default: '' },
  align: { type: String, default: 'center' }, // 'center' | 'left'
  dark: { type: Boolean, default: false },
})
</script>

<template>
  <div class="flex flex-col gap-4"
       :class="align === 'center' ? 'items-center text-center' : 'items-start text-left'">
    <div v-if="eyebrow"
         data-reveal="fade-up"
         class="inline-flex items-center gap-2 rounded-full px-4 py-1.5 text-xs font-semibold uppercase tracking-[0.2em]"
         :class="dark ? 'glass-dark text-white' : 'glass text-navy-700'">
      <span class="w-1.5 h-1.5 rounded-full bg-emerald-brand-400 animate-pulse"></span>
      {{ eyebrow }}
    </div>

    <h2 v-if="title || highlight"
        data-reveal="fade-up"
        data-reveal-delay="80"
        class="font-display font-bold tracking-tight leading-[1.05] text-balance"
        :class="[
          dark ? 'text-white' : 'text-navy-700',
          align === 'center' ? 'text-4xl md:text-5xl lg:text-6xl' : 'text-4xl md:text-5xl'
        ]">
      {{ title }}
      <span v-if="highlight" class="text-gradient">{{ highlight }}</span>
    </h2>

    <p v-if="subtitle"
       data-reveal="fade-up"
       data-reveal-delay="160"
       class="text-base md:text-lg leading-relaxed max-w-2xl"
       :class="dark ? 'text-white/70' : 'text-slate-600'"
       :style="align === 'center' ? 'margin-inline: auto;' : ''">
      {{ subtitle }}
    </p>

    <slot />
  </div>
</template>
