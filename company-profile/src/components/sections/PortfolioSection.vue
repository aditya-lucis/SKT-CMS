<script setup>
import { ref, computed } from 'vue'
import { ArrowUpRight } from 'lucide-vue-next'
import SectionHeading from '@/components/base/SectionHeading.vue'
import { useSiteContent } from '@/store/siteContent'
import { resolveMediaUrl } from '@/lib/api'

const { state } = useSiteContent()

const categories = computed(() => ['All', ...new Set(state.data.portfolio.map((p) => p.category))])
const active = ref('All')

const filtered = computed(() =>
  active.value === 'All'
    ? state.data.portfolio
    : state.data.portfolio.filter((p) => p.category === active.value)
)
</script>

<template>
  <section id="portfolio" class="section relative overflow-hidden">
    <div class="absolute inset-0 bg-dots opacity-50 pointer-events-none"></div>
    <div data-parallax data-parallax-speed="0.22" class="aurora-blob w-[45vw] h-[45vw] top-[10%] -right-[15%] animate-float-slow"
         style="background: radial-gradient(circle, rgba(70,173,100,0.18), transparent 65%);"></div>

    <div class="container-x relative">
      <SectionHeading
        eyebrow="Portfolio"
        title="Selected work that"
        highlight="moved real metrics"
        subtitle="A glimpse into the platforms, products, and systems we've shipped for clients across fintech, healthcare, retail, and beyond."
      />

      <!-- Filters -->
      <div class="mt-10 flex flex-wrap justify-center gap-2" data-reveal="fade-up">
        <button v-for="cat in categories" :key="cat"
                @click="active = cat"
                class="relative px-5 py-2 rounded-full text-sm font-medium transition-all duration-300 overflow-hidden"
                :class="active === cat
                  ? 'text-white shadow-glow-green'
                  : 'glass text-slate-700 hover:text-navy-700'">
          <span v-if="active === cat" class="absolute inset-0 rounded-full"
                style="background: linear-gradient(120deg, #053063, #46ad64);"></span>
          <span class="relative">{{ cat }}</span>
        </button>
      </div>

      <!-- Masonry grid -->
      <div class="mt-10 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5 auto-rows-[280px] md:auto-rows-[320px]">
        <article v-for="(item, i) in filtered" :key="item.id"
                 data-reveal="fade-up"
                 :data-reveal-delay="(i % 3) * 90"
                 class="group relative rounded-3xl overflow-hidden shadow-glass card-hover cursor-pointer"
                 :class="[
                   item.size === 'tall' ? 'row-span-2' : '',
                   item.size === 'wide' ? 'lg:col-span-2' : '',
                 ]">
          <div class="absolute left-0 w-full will-change-transform" style="top: -12%; height: 124%;"
               data-parallax :data-parallax-speed="0.1 + (i % 3) * 0.04">
            <img :src="resolveMediaUrl(item.image)" :alt="item.title"
                 class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
                 loading="lazy" />
          </div>

          <!-- Overlay -->
          <div class="absolute inset-0 transition-opacity duration-500"
               style="background: linear-gradient(180deg, transparent 30%, rgba(4,37,74,0.7) 70%, rgba(3,26,54,0.92) 100%);"></div>

          <!-- Hover glass overlay -->
          <div class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500"
               style="background: linear-gradient(135deg, rgba(70,173,100,0.18), rgba(34,211,238,0.12)); backdrop-filter: blur(2px);"></div>

          <!-- Content -->
          <div class="absolute inset-0 p-6 flex flex-col justify-end text-white">
            <div class="flex items-center gap-2 mb-3 opacity-90">
              <span class="px-2.5 py-1 rounded-full text-[10px] font-mono uppercase tracking-wider glass-dark">{{ item.category }}</span>
            </div>
            <h3 class="font-display font-bold text-xl md:text-2xl leading-tight mb-2">{{ item.title }}</h3>
            <p class="text-sm text-white/75 leading-relaxed line-clamp-2 opacity-0 group-hover:opacity-100 transition-all duration-500 -translate-y-2 group-hover:translate-y-0">
              {{ item.desc }}
            </p>
            <div class="mt-3 flex items-center justify-between opacity-0 group-hover:opacity-100 transition-all duration-500 translate-y-2 group-hover:translate-y-0">
              <div class="flex flex-wrap gap-1.5">
                <span v-for="t in item.tags" :key="t"
                      class="px-2 py-0.5 rounded-full text-[10px] font-medium bg-white/10 text-white/90">{{ t }}</span>
              </div>
              <span class="w-9 h-9 rounded-full flex items-center justify-center glass-dark group-hover:bg-emerald-brand-400 transition-colors">
                <ArrowUpRight :size="16" />
              </span>
            </div>
          </div>
        </article>
      </div>
    </div>
  </section>
</template>
