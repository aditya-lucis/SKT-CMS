<script setup>
import { ArrowRight, ArrowDown, Sparkles, Play, Zap, Activity } from 'lucide-vue-next'
import { useMagneticButton } from '@/composables/useMagneticButton'
import ParticleField from '@/components/base/ParticleField.vue'
import { useSiteContent } from '@/store/siteContent'
import { resolveMediaUrl } from '@/lib/api'

const { magneticRef: ctaRef } = useMagneticButton(0.3)
const { magneticRef: secondaryRef } = useMagneticButton(0.25)

const { state } = useSiteContent()
const hero = state.data.hero

const scrollToNext = () => {
  if (window.__lenis) window.__lenis.scrollTo('#trusted', { offset: -80, duration: 1.4 })
  else document.querySelector('#trusted')?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <section id="home" data-parallax-scope class="relative min-h-screen flex items-center overflow-hidden pt-28 pb-24 md:pb-16">
    <!-- Background image: slow drift + cinematic zoom, scroll-linked -->
    <div class="absolute left-0 will-change-transform" style="top: -10%; height: 122%; width: 100%;"
         data-parallax data-parallax-speed="0.18" data-parallax-scale="1.14">
      <img :src="resolveMediaUrl(hero.background_image)" alt="" class="w-full h-full object-cover"
           style="filter: brightness(0.32) saturate(1.1);" loading="eager" />
    </div>

    <!-- Gradient overlays -->
    <div class="absolute inset-0" style="background: linear-gradient(180deg, rgba(4,37,74,0.6) 0%, rgba(3,26,54,0.85) 60%, rgba(3,26,54,0.95) 100%);"></div>
    <div class="absolute inset-0" style="background: radial-gradient(60% 80% at 70% 30%, rgba(70,173,100,0.25), transparent 60%), radial-gradient(40% 60% at 20% 80%, rgba(34,211,238,0.18), transparent 60%);"></div>

    <!-- Aurora blobs: opposite directions + different speeds for depth -->
    <div class="aurora-blob w-[55vw] h-[55vw] top-[-10%] right-[-15%] animate-float-slow"
         data-parallax data-parallax-speed="0.3" data-parallax-rotate="10"
         style="background: radial-gradient(circle, rgba(70,173,100,0.5), transparent 65%);"></div>
    <div class="aurora-blob w-[40vw] h-[40vw] bottom-[-10%] left-[-10%] animate-float"
         data-parallax data-parallax-speed="-0.22"
         style="background: radial-gradient(circle, rgba(34,211,238,0.35), transparent 65%); animation-delay: -4s;"></div>

    <!-- Particles: subtle drift, slowest layer -->
    <div data-parallax data-parallax-speed="0.06" class="absolute inset-0">
      <ParticleField :count="80" color="255,255,255" :speed="0.35" :link-distance="150" :opacity="0.85" :radius="2.2" />
    </div>

    <!-- Grid overlay -->
    <div class="absolute inset-0 bg-grid-dark opacity-30 pointer-events-none" data-parallax data-parallax-speed="0.1"></div>

    <!-- Content -->
    <div class="container-x relative z-10 w-full">
      <div class="grid lg:grid-cols-12 gap-10 lg:gap-12 items-center">
        <!-- Left: Headline + CTAs + stats -->
        <div class="lg:col-span-7 xl:col-span-8">
          <!-- Badge -->
          <div data-reveal="fade-up" class="inline-flex items-center gap-2 rounded-full glass-dark px-4 py-2 text-xs font-medium text-white/90 mb-6">
            <Sparkles :size="14" class="text-emerald-brand-300" />
            <span>{{ hero.badge }}</span>
            <span class="w-1 h-1 rounded-full bg-emerald-brand-300 animate-pulse"></span>
          </div>

          <!-- Headline -->
          <h1 data-reveal="fade-up" data-reveal-delay="100"
              class="font-display font-bold tracking-tight text-white leading-[1.08] text-balance text-[clamp(2.25rem,6vw,5rem)]">
            {{ hero.headline_1 }}<br />
            {{ hero.headline_2 }} <span class="text-gradient-aurora">{{ hero.headline_highlight }}</span>
          </h1>

          <!-- Subheadline -->
          <p data-reveal="fade-up" data-reveal-delay="200"
             class="mt-6 text-lg md:text-xl text-white/70 leading-relaxed max-w-2xl">
            {{ hero.subheadline }}
          </p>

          <!-- CTAs -->
          <div data-reveal="fade-up" data-reveal-delay="300" class="mt-8 flex flex-wrap items-center gap-4">
            <button ref="ctaRef"
                    @click="scrollToNext"
                    class="magnetic relative inline-flex items-center gap-2 rounded-full px-7 py-4 font-semibold text-white overflow-hidden group shadow-glow-green">
              <span class="absolute inset-0" style="background: linear-gradient(120deg, #46ad64, #22d3ee, #46ad64); background-size: 200% 100%; animation: gradient-x 4s ease infinite;"></span>
              <span class="absolute inset-0 shimmer-bg opacity-0 group-hover:opacity-100 transition-opacity"></span>
              <span class="relative flex items-center gap-2">
                {{ hero.cta_primary_label }}
                <ArrowRight :size="18" class="group-hover:translate-x-1 transition-transform" />
              </span>
            </button>

            <button ref="secondaryRef"
                    @click="$emit('contact')"
                    class="magnetic inline-flex items-center gap-2 rounded-full px-7 py-4 font-semibold text-white glass-dark hover:bg-white/15 transition-colors">
              <Play :size="16" class="text-emerald-brand-300" />
              {{ hero.cta_secondary_label }}
            </button>
          </div>

          <!-- Stats preview -->
          <div data-reveal="fade-up" data-reveal-delay="400" class="mt-10 grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-2xl">
            <div v-for="s in state.data.stats.slice(0, 4)" :key="s.id" class="glass-dark rounded-2xl p-3 md:p-4">
              <div class="font-display font-bold text-xl md:text-2xl text-white">{{ s.value }}{{ s.suffix }}</div>
              <div class="text-[11px] md:text-xs text-white/60 mt-0.5">{{ s.label }}</div>
            </div>
          </div>
        </div>

        <!-- Right: Floating cards column (desktop only) -->
        <div class="hidden lg:flex lg:col-span-5 xl:col-span-4 flex-col gap-4 relative">
          <!-- Main AI Lab card -->
          <div data-reveal="fade-left" data-reveal-delay="200"
               class="glass-dark rounded-3xl p-6 shadow-glow-green animate-float-slow">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 rounded-xl flex items-center justify-center" style="background: linear-gradient(135deg, #46ad64, #22d3ee);">
                <Sparkles :size="18" class="text-white" />
              </div>
              <div>
                <div class="text-white font-semibold text-sm">SKT AI Lab</div>
                <div class="text-white/60 text-xs">Shipping production AI</div>
              </div>
            </div>
            <div class="space-y-2.5">
              <div class="flex justify-between items-center text-xs">
                <span class="text-white/70">Model accuracy</span>
                <span class="text-emerald-brand-300 font-mono font-semibold">98.4%</span>
              </div>
              <div class="h-1.5 rounded-full bg-white/10 overflow-hidden">
                <div class="h-full rounded-full" style="width: 98%; background: linear-gradient(90deg, #46ad64, #22d3ee);"></div>
              </div>
              <div class="flex justify-between items-center text-xs pt-1">
                <span class="text-white/70">Latency P99</span>
                <span class="text-emerald-brand-300 font-mono font-semibold">87ms</span>
              </div>
              <div class="h-1.5 rounded-full bg-white/10 overflow-hidden">
                <div class="h-full rounded-full" style="width: 22%; background: linear-gradient(90deg, #46ad64, #22d3ee);"></div>
              </div>
            </div>
          </div>

          <!-- Two mini cards side by side -->
          <div class="grid grid-cols-2 gap-4">
            <div data-reveal="fade-left" data-reveal-delay="350"
                 class="glass-dark rounded-2xl p-4 animate-float flex flex-col gap-2">
              <div class="w-9 h-9 rounded-lg flex items-center justify-center" style="background: linear-gradient(135deg, #8b5cf6, #ec4899);">
                <Zap :size="16" class="text-white" />
              </div>
              <div>
                <div class="text-white text-xs font-semibold opacity-80">Deploy freq</div>
                <div class="text-emerald-brand-300 font-mono text-base font-bold">142/day</div>
              </div>
            </div>

            <div data-reveal="fade-left" data-reveal-delay="450"
                 class="glass-dark rounded-2xl p-4 animate-float-slow flex flex-col gap-2">
              <div class="w-9 h-9 rounded-lg flex items-center justify-center" style="background: linear-gradient(135deg, #053063, #1c4f96);">
                <Activity :size="16" class="text-white" />
              </div>
              <div>
                <div class="text-white text-xs font-semibold opacity-80">Uptime SLA</div>
                <div class="text-emerald-brand-300 font-mono text-base font-bold">99.99%</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Scroll indicator (centered, below content, no overlap) -->
      <div class="hidden md:flex mt-12 flex-col items-center gap-2 text-white/60">
        <span class="font-mono text-[10px] uppercase tracking-[0.3em]">Scroll</span>
        <span class="relative w-6 h-10 rounded-full border-2 border-white/30 flex items-start justify-center p-1.5">
          <span class="w-1 h-2 rounded-full bg-emerald-brand-300 animate-bounce"></span>
        </span>
        <ArrowDown :size="14" class="animate-bounce" />
      </div>
    </div>
  </section>
</template>
