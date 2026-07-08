<script setup>
import SectionHeading from '@/components/base/SectionHeading.vue'
import { useSiteContent } from '@/store/siteContent'
import { resolveIcon } from '@/lib/icons'

const { state } = useSiteContent()
const colorMap = {
  navy: 'from-navy-700 to-navy-500',
  emerald: 'from-emerald-brand-600 to-emerald-brand-400',
  cyan: 'from-aurora-cyan to-aurora-blue',
}
</script>

<template>
  <section class="section section-dark relative overflow-hidden">
    <!-- Aurora bg -->
    <div class="absolute inset-0 pointer-events-none">
      <div data-parallax data-parallax-speed="0.22" class="aurora-blob w-[50vw] h-[50vw] top-[-10%] left-[-10%] animate-float-slow"
           style="background: radial-gradient(circle, rgba(70,173,100,0.4), transparent 65%);"></div>
      <div data-parallax data-parallax-speed="-0.18" data-parallax-rotate="8" class="aurora-blob w-[40vw] h-[40vw] bottom-[-10%] right-[-10%] animate-float"
           style="background: radial-gradient(circle, rgba(34,211,238,0.3), transparent 65%); animation-delay: -5s;"></div>
    </div>
    <div class="absolute inset-0 bg-grid-dark opacity-20 pointer-events-none"></div>

    <div class="container-x relative">
      <SectionHeading
        eyebrow="Vision · Mission · Values"
        title="The principles that guide"
        highlight="every decision we make"
        subtitle="We are not just a vendor. We are your long-term engineering partner — and these are the commitments we hold ourselves to."
        dark
      />

      <div class="mt-16 grid md:grid-cols-3 gap-6">
        <div v-for="(item, i) in state.data.vision_mission" :key="item.id"
             data-reveal="fade-up"
             :data-reveal-delay="i * 120"
             class="group relative rounded-3xl p-7 transition-all duration-500 hover:-translate-y-2">
          <!-- gradient border on hover -->
          <div class="absolute inset-0 rounded-3xl opacity-30 group-hover:opacity-100 transition-opacity duration-500"
               :style="`padding: 1.5px; background: linear-gradient(135deg, ${item.color === 'navy' ? '#1c4f96, #053063' : item.color === 'emerald' ? '#46ad64, #2e9a4e' : '#22d3ee, #3b82f6'}); -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0); -webkit-mask-composite: xor; mask-composite: exclude;`"></div>

          <div class="relative glass-dark rounded-3xl p-7 h-full">
            <div class="w-14 h-14 rounded-2xl flex items-center justify-center mb-5 group-hover:scale-110 transition-transform"
                 :class="`bg-gradient-to-br ${colorMap[item.color]}`">
              <component :is="resolveIcon(item.icon)" :size="26" class="text-white" />
            </div>

            <div class="font-mono text-xs uppercase tracking-[0.3em] text-emerald-brand-300 mb-2">{{ item.type }}</div>
            <h3 class="font-display font-bold text-xl text-white leading-snug mb-3">{{ item.title }}</h3>
            <p class="text-white/70 leading-relaxed">{{ item.body }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
