<script setup>
import SectionHeading from '@/components/base/SectionHeading.vue'
import { useSiteContent } from '@/store/siteContent'
import { resolveIcon } from '@/lib/icons'

const { state } = useSiteContent()
</script>

<template>
  <section id="process" class="section relative overflow-hidden bg-navy-50/40">
    <div class="absolute inset-0 bg-grid opacity-40 pointer-events-none"></div>
    <div data-parallax data-parallax-speed="0.22" class="aurora-blob w-[40vw] h-[40vw] top-[20%] -left-[15%] animate-float-slow"
         style="background: radial-gradient(circle, rgba(5,48,99,0.15), transparent 65%);"></div>

    <div class="container-x relative">
      <SectionHeading
        eyebrow="Development Process"
        title="A delivery process"
        highlight="refined over 320 projects"
        subtitle="From the first conversation to the day after launch and beyond — here's how we turn your goals into software that ships on time, every time."
      />

      <div class="mt-16 relative">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-x-6 gap-y-14">
          <div v-for="(step, i) in state.data.process_steps" :key="step.id"
               data-reveal="fade-up"
               :data-reveal-delay="(i % 4) * 100"
               class="group relative">

            <!-- Card -->
            <div class="relative glass rounded-2xl p-5 pt-9 text-center h-full card-hover">
              <!-- Step number badge, overlaps top edge of the card -->
              <div class="absolute -top-6 left-1/2 -translate-x-1/2 z-10 w-12 h-12 rounded-2xl flex items-center justify-center shadow-glass transition-all duration-500 group-hover:scale-110 group-hover:-rotate-6"
                   :style="`background: linear-gradient(135deg, ${i % 2 === 0 ? '#053063, #1c4f96' : '#46ad64, #22d3ee'});`">
                <span class="font-display font-bold text-white text-base">{{ step.num }}</span>
                <span class="absolute inset-0 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity"
                      style="box-shadow: 0 0 30px rgba(70,173,100,0.5);"></span>
              </div>

              <div class="w-10 h-10 mx-auto rounded-xl flex items-center justify-center mb-3"
                   style="background: linear-gradient(135deg, rgba(5,48,99,0.1), rgba(70,173,100,0.15));">
                <component :is="resolveIcon(step.icon)" :size="18" class="text-navy-700" />
              </div>
              <h3 class="font-display font-bold text-navy-700 mb-1.5">{{ step.title }}</h3>
              <p class="text-xs text-slate-600 leading-relaxed line-clamp-4 min-h-[4.5em]">{{ step.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
