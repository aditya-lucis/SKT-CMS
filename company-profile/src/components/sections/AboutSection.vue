<script setup>
import { ref, watch, nextTick } from 'vue'
import { Check, ArrowRight, Award } from 'lucide-vue-next'
import { useCountUp } from '@/composables/useCountUp'
import SectionHeading from '@/components/base/SectionHeading.vue'
import { useSiteContent } from '@/store/siteContent'
import { resolveIcon } from '@/lib/icons'
import { resolveMediaUrl } from '@/lib/api'

const { register } = useCountUp()
const { state } = useSiteContent()
const about = state.data.about

const statRefs = ref([])
// Stats arrive asynchronously from the CMS; register the count-up animation
// once they land and the DOM for each stat card has rendered.
watch(() => state.data.stats.length, async () => {
  await nextTick()
  state.data.stats.forEach((s, i) => {
    if (statRefs.value[i]) register(statRefs.value[i], s.value, { suffix: s.suffix, duration: 2400 })
  })
})
</script>

<template>
  <section id="about" class="section relative overflow-hidden">
    <!-- Background accents -->
    <div class="absolute inset-0 bg-dots opacity-50 pointer-events-none"></div>
    <div data-parallax data-parallax-speed="0.22" class="aurora-blob w-[40vw] h-[40vw] top-[10%] -right-[15%] animate-float-slow"
         style="background: radial-gradient(circle, rgba(70,173,100,0.18), transparent 65%);"></div>

    <div class="container-x relative">
      <div class="grid lg:grid-cols-2 gap-12 lg:gap-16 items-center">
        <!-- Left: Images -->
        <div class="relative" data-reveal="fade-right">
          <!-- Main image -->
          <div class="relative rounded-3xl overflow-hidden gradient-border shadow-glass-lg h-[400px] md:h-[440px]">
            <div class="absolute left-0 w-full will-change-transform" style="top: -10%; height: 120%;"
                 data-parallax data-parallax-speed="0.14" data-parallax-scale="1.1">
              <img :src="resolveMediaUrl(about.office_image)" alt="Nexus Technology office" class="w-full h-full object-cover" loading="lazy" />
            </div>
            <div class="absolute inset-0" style="background: linear-gradient(180deg, transparent 50%, rgba(5,48,99,0.4) 100%);"></div>
            <!-- Floating badge -->
            <div class="absolute bottom-4 left-4 glass-dark rounded-2xl px-4 py-3 flex items-center gap-3 max-w-[calc(100%-2rem)]">
              <div class="w-10 h-10 rounded-full flex items-center justify-center shrink-0" style="background: linear-gradient(135deg, #46ad64, #22d3ee);">
                <Award :size="18" class="text-white" />
              </div>
              <div class="min-w-0">
                <div class="text-white font-semibold text-sm">{{ about.badge_text }}</div>
                <div class="text-white/60 text-xs">Clutch · Awwwards · 2024</div>
              </div>
            </div>
          </div>

          <!-- Floating stat card (top-left, within bounds) -->
          <div class="absolute -top-5 left-3 md:left-5 glass rounded-2xl px-4 py-2.5 shadow-glass hidden md:block animate-float-slow z-10">
            <div class="text-xl md:text-2xl font-display font-bold text-navy-700">96%</div>
            <div class="text-xs text-slate-500">Client retention</div>
          </div>
        </div>

        <!-- Right: Text -->
        <div data-reveal="fade-left">
          <SectionHeading
            :eyebrow="about.eyebrow"
            :title="about.title"
            :highlight="about.highlight_word"
            :subtitle="about.subtitle"
            align="left"
          />

          <!-- Highlights -->
          <ul class="mt-7 grid sm:grid-cols-2 gap-3">
            <li v-for="h in about.highlights" :key="h"
                class="flex items-center gap-3 text-sm text-slate-700">
              <span class="w-6 h-6 rounded-full flex items-center justify-center shrink-0"
                    style="background: linear-gradient(135deg, #46ad64, #22d3ee);">
                <Check :size="14" class="text-white" />
              </span>
              {{ h }}
            </li>
          </ul>

          <!-- Mini CTA -->
          <button @click="$emit('contact')"
                  class="mt-8 inline-flex items-center gap-2 text-navy-700 font-semibold group">
            <span class="border-b-2 border-emerald-brand-400 pb-0.5">Start a conversation</span>
            <ArrowRight :size="18" class="group-hover:translate-x-1 transition-transform" />
          </button>
        </div>
      </div>

      <!-- Stats grid -->
      <div class="mt-20 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
        <div v-for="(s, i) in state.data.stats" :key="s.id"
             data-reveal="fade-up"
             :data-reveal-delay="i * 80"
             class="group relative glass rounded-2xl p-6 text-center card-hover overflow-hidden">
          <div class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500"
               style="background: radial-gradient(circle at 50% 0%, rgba(70,173,100,0.12), transparent 70%);"></div>
          <div class="relative">
            <div class="w-12 h-12 mx-auto rounded-xl flex items-center justify-center mb-3 group-hover:scale-110 transition-transform"
                 style="background: linear-gradient(135deg, rgba(5,48,99,0.1), rgba(70,173,100,0.15));">
              <component :is="resolveIcon(s.icon)" :size="22" class="text-navy-700" />
            </div>
            <div :ref="el => statRefs[i] = el"
                 class="font-display font-bold text-3xl md:text-4xl text-navy-700 tabular-nums">0</div>
            <div class="text-sm text-slate-500 mt-1">{{ s.label }}</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
