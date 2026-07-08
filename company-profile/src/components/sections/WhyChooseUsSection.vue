<script setup>
import { ref, onMounted, onBeforeUnmount, watch, nextTick } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import SectionHeading from '@/components/base/SectionHeading.vue'
import { useSiteContent } from '@/store/siteContent'

gsap.registerPlugin(ScrollTrigger)

const { state } = useSiteContent()
const timelineRef = ref(null)
const lineFillRef = ref(null)
let ctx

onMounted(() => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
  ctx = gsap.context(() => {
    gsap.fromTo(lineFillRef.value,
      { scaleY: 0 },
      {
        scaleY: 1,
        ease: 'none',
        scrollTrigger: {
          trigger: timelineRef.value,
          start: 'top 75%',
          end: 'bottom 60%',
          scrub: 0.6,
        },
      })
  })
})

// Milestones load asynchronously from the CMS, which changes the timeline's
// height after mount — refresh ScrollTrigger once they're rendered so the
// fill animation's start/end range matches the real timeline height.
watch(() => state.data.milestones.length, async () => {
  await nextTick()
  ScrollTrigger.refresh()
})

onBeforeUnmount(() => ctx && ctx.revert())
</script>

<template>
  <section id="why-choose" class="section relative overflow-hidden bg-navy-50/40">
    <div class="absolute inset-0 bg-dots opacity-50 pointer-events-none"></div>
    <div class="container-x relative">
      <SectionHeading
        eyebrow="Why Choose Us"
        title="A track record built on"
        highlight="twelve years of craft"
        subtitle="We've been quietly shipping the software that runs some of the world's most demanding businesses. Here's the story — in milestones."
      />

      <div ref="timelineRef" class="mt-16 relative">
        <!-- Vertical line (static track) -->
        <div class="absolute left-4 md:left-1/2 top-0 bottom-0 w-px -translate-x-1/2 bg-navy-700/10"></div>
        <!-- Vertical line (scroll-filled progress, grows as you scroll) -->
        <div ref="lineFillRef" class="absolute left-4 md:left-1/2 top-0 bottom-0 w-px -translate-x-1/2 origin-top shadow-glow-green"
             style="background: linear-gradient(180deg, #053063, #46ad64 60%, #22d3ee); transform: scaleY(0);"></div>

        <div class="space-y-12 md:space-y-0">
          <div v-for="(item, i) in state.data.milestones" :key="item.id"
               class="relative md:grid md:grid-cols-2 md:gap-12 md:items-center md:py-8">

            <!-- Marker -->
            <div class="absolute left-4 md:left-1/2 -translate-x-1/2 z-10 top-2 md:top-1/2 md:-translate-y-1/2">
              <div class="relative w-4 h-4 rounded-full bg-white border-2 border-emerald-brand-400 shadow-glow-green">
                <span class="absolute inset-0 rounded-full animate-pulse-ring"></span>
              </div>
            </div>

            <!-- Card alternating sides -->
            <div :class="i % 2 === 0 ? 'md:col-start-1 md:pr-12' : 'md:col-start-2 md:pl-12'"
                 class="pl-12 md:pl-0">
              <div data-reveal="fade-up"
                   class="glass rounded-2xl p-6 card-hover">
                <div class="font-display font-bold text-3xl md:text-4xl text-gradient mb-2">{{ item.year }}</div>
                <h3 class="font-display font-bold text-lg text-navy-700 mb-2">{{ item.title }}</h3>
                <p class="text-sm text-slate-600 leading-relaxed">{{ item.desc }}</p>
              </div>
            </div>

            <!-- Spacer for grid -->
            <div :class="i % 2 === 0 ? 'md:col-start-2' : 'md:col-start-1'" class="hidden md:block"></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
