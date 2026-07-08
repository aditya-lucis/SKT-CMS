<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { Menu, X } from 'lucide-vue-next'
import { useMagneticButton } from '@/composables/useMagneticButton'

const scrolled = ref(false)
const mobileOpen = ref(false)

const links = [
  { label: 'Home', href: '#home' },
  { label: 'About', href: '#about' },
  { label: 'Services', href: '#services' },
  { label: 'Portfolio', href: '#portfolio' },
  { label: 'Process', href: '#process' },
  { label: 'Team', href: '#team' },
  { label: 'Testimonials', href: '#testimonials' },
  { label: 'Blog', href: '#blog' },
  { label: 'FAQ', href: '#faq' },
  { label: 'Contact', href: '#contact' },
]

const { magneticRef } = useMagneticButton(0.25)

const onScroll = () => { scrolled.value = window.scrollY > 40 }
const go = (href) => {
  mobileOpen.value = false
  if (window.__lenis) window.__lenis.scrollTo(href, { offset: -80, duration: 1.3 })
  else {
    const el = document.querySelector(href)
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }
}

onMounted(() => { window.addEventListener('scroll', onScroll, { passive: true }); onScroll() })
onBeforeUnmount(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <header class="fixed top-0 left-0 right-0 z-50 transition-all duration-500"
          :class="scrolled ? 'py-3' : 'py-5'">
    <div class="container-x">
      <nav class="flex items-center justify-between rounded-2xl transition-all duration-500 px-4 md:px-6 py-3"
           :class="scrolled ? 'glass shadow-glass' : 'bg-transparent'">
        <!-- Logo -->
        <a href="#home" @click.prevent="go('#home')" class="flex items-center gap-2.5 group">
          <div class="relative">
            <div class="absolute inset-0 rounded-xl blur-md opacity-50 group-hover:opacity-80 transition-opacity"
                 style="background: linear-gradient(120deg, #053063, #46ad64);"></div>
            <img src="@/assets/images/logo.png" alt="SKT"
                 class="relative w-9 h-9 object-contain" />
          </div>
          <div class="leading-none">
            <div class="font-display font-bold text-base text-navy-700">SKT<span class="text-emerald-brand-400">.</span></div>
            <div class="font-mono text-[9px] uppercase tracking-[0.25em] text-slate-500">CMS</div>
          </div>
        </a>

        <!-- Desktop menu -->
        <div class="hidden xl:flex items-center gap-1">
          <button v-for="link in links" :key="link.href"
                  @click="go(link.href)"
                  class="relative px-3 py-2 text-sm font-medium text-slate-700 hover:text-navy-700 transition-colors group">
            {{ link.label }}
            <span class="absolute bottom-1 left-3 right-3 h-[2px] rounded-full origin-left scale-x-0 group-hover:scale-x-100 transition-transform duration-300"
                  style="background: linear-gradient(90deg, #053063, #46ad64);"></span>
          </button>
        </div>

        <!-- CTA + mobile toggle -->
        <div class="flex items-center gap-3">
          <button ref="magneticRef"
                  @click="go('#contact')"
                  class="hidden md:inline-flex magnetic relative overflow-hidden rounded-full px-5 py-2.5 text-sm font-semibold text-white shadow-glow-green group">
            <span class="absolute inset-0" style="background: linear-gradient(120deg, #053063, #1c4f96 40%, #46ad64);"></span>
            <span class="absolute inset-0 shimmer-bg opacity-0 group-hover:opacity-100 transition-opacity"></span>
            <span class="relative flex items-center gap-2">
              Let's Talk
              <span class="w-1.5 h-1.5 rounded-full bg-white/90 animate-pulse"></span>
            </span>
          </button>

          <button @click="mobileOpen = !mobileOpen"
                  class="xl:hidden w-10 h-10 rounded-xl glass flex items-center justify-center text-navy-700"
                  aria-label="Toggle menu">
            <component :is="mobileOpen ? X : Menu" :size="20" />
          </button>
        </div>
      </nav>
    </div>

    <!-- Mobile menu -->
    <Transition name="mobile-menu">
      <div v-if="mobileOpen" class="xl:hidden container-x mt-2">
        <div class="glass rounded-2xl p-4 shadow-glass-lg">
          <div class="grid grid-cols-2 gap-1">
            <button v-for="link in links" :key="link.href"
                    @click="go(link.href)"
                    class="px-3 py-3 rounded-xl text-sm font-medium text-slate-700 hover:bg-navy-50 hover:text-navy-700 text-left transition-colors">
              {{ link.label }}
            </button>
          </div>
          <button @click="go('#contact')"
                  class="mt-3 w-full rounded-xl px-5 py-3 text-sm font-semibold text-white"
                  style="background: linear-gradient(120deg, #053063, #46ad64);">
            Let's Talk →
          </button>
        </div>
      </div>
    </Transition>
  </header>
</template>

<style scoped>
.mobile-menu-enter-active, .mobile-menu-leave-active { transition: all 0.4s cubic-bezier(0.16,1,0.3,1); }
.mobile-menu-enter-from, .mobile-menu-leave-to { opacity: 0; transform: translateY(-12px); }
</style>
