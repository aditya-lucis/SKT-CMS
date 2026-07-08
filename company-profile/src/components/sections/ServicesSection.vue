<script setup>
import { ArrowUpRight } from 'lucide-vue-next'
import SectionHeading from '@/components/base/SectionHeading.vue'
import { useSiteContent } from '@/store/siteContent'
import { resolveIcon } from '@/lib/icons'

const { state } = useSiteContent()
</script>

<template>
  <section id="services" class="section relative overflow-hidden">
    <div class="absolute inset-0 bg-grid opacity-40 pointer-events-none"></div>
    <div data-parallax data-parallax-speed="0.22" class="aurora-blob w-[45vw] h-[45vw] top-[20%] -left-[15%] animate-float-slow"
         style="background: radial-gradient(circle, rgba(5,48,99,0.15), transparent 65%);"></div>
    <div data-parallax data-parallax-speed="-0.18" data-parallax-rotate="8" class="aurora-blob w-[40vw] h-[40vw] bottom-[10%] -right-[15%] animate-float"
         style="background: radial-gradient(circle, rgba(70,173,100,0.15), transparent 65%); animation-delay: -4s;"></div>

    <div class="container-x relative">
      <SectionHeading
        eyebrow="Our Services"
        title="Full-stack capabilities for"
        highlight="ambitious organizations"
        subtitle="From strategy to launch to long-term operation — we cover the full spectrum of modern software engineering, so you don't have to coordinate five vendors."
      />

      <div class="mt-16 grid sm:grid-cols-2 lg:grid-cols-4 gap-5">
        <article v-for="(svc, i) in state.data.services" :key="svc.id"
                 data-reveal="fade-up"
                 :data-reveal-delay="(i % 4) * 90"
                 class="group relative rounded-3xl p-7 glass card-hover overflow-hidden h-full flex flex-col">
          <!-- Hover glow -->
          <div class="absolute -inset-px rounded-3xl opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"
               :style="`padding: 1px; background: linear-gradient(135deg, ${svc.gradient.includes('emerald') ? '#46ad64, #22d3ee' : svc.gradient.includes('violet') ? '#8b5cf6, #ec4899' : '#053063, #46ad64'}); -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0); -webkit-mask-composite: xor; mask-composite: exclude;`"></div>

          <!-- Bg gradient on hover -->
          <div class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"
               :class="`bg-gradient-to-br ${svc.gradient}`"
               style="opacity: 0; mix-blend-mode: multiply;"></div>

          <div class="relative flex-1">
            <div class="w-14 h-14 rounded-2xl flex items-center justify-center mb-5 group-hover:scale-110 group-hover:-rotate-6 transition-all duration-500"
                 :class="`bg-gradient-to-br ${svc.gradient}`">
              <component :is="resolveIcon(svc.icon)" :size="26" class="text-white" />
            </div>

            <h3 class="font-display font-bold text-lg text-navy-700 mb-2 group-hover:text-white transition-colors duration-500">
              {{ svc.title }}
            </h3>
            <p class="text-sm text-slate-600 group-hover:text-white/85 transition-colors duration-500 leading-relaxed">
              {{ svc.desc }}
            </p>

            <ul class="mt-4 space-y-1.5">
              <li v-for="p in svc.points" :key="p"
                  class="text-xs font-medium text-slate-500 group-hover:text-white/75 transition-colors duration-500 flex items-center gap-1.5">
                  <span class="w-1 h-1 rounded-full bg-emerald-brand-400"></span>
                  {{ p }}
              </li>
            </ul>
          </div>

          <div class="relative mt-6 flex items-center gap-1.5 text-sm font-semibold text-navy-700 group-hover:text-white transition-colors duration-500">
            Learn more
            <ArrowUpRight :size="16" class="group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
          </div>
        </article>
      </div>
    </div>
  </section>
</template>
