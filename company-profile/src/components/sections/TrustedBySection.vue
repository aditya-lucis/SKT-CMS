<script setup>
import { computed } from 'vue'
import { useSiteContent } from '@/store/siteContent'

const { state } = useSiteContent()
// Duplicate for seamless marquee
const doubled = computed(() => [...state.data.trusted_by, ...state.data.trusted_by])
</script>

<template>
  <section id="trusted" class="relative py-16 md:py-20 overflow-hidden border-y border-navy-100/50 bg-navy-50/40">
    <div class="container-x">
      <p data-reveal="fade-up" class="text-center font-mono text-xs uppercase tracking-[0.3em] text-slate-500 mb-8">
        Trusted by category-defining teams worldwide
      </p>
    </div>

    <div class="marquee-mask relative">
      <div class="marquee-track gap-12 items-center">
        <div v-for="(item, i) in doubled" :key="i"
             class="flex items-center gap-2 shrink-0">
          <span class="w-2 h-2 rounded-full bg-gradient-to-br from-navy-500 to-emerald-brand-400"></span>
          <span class="font-display font-bold text-2xl md:text-3xl text-slate-400 hover:text-navy-700 transition-colors whitespace-nowrap">
            {{ item.name }}
          </span>
        </div>
      </div>
    </div>
  </section>
</template>
