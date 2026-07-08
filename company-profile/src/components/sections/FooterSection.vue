<script setup>
import { ref, computed } from 'vue'
import { ArrowRight, Linkedin, Twitter, Github, Instagram, Youtube, Mail, MapPin, Phone, Check } from 'lucide-vue-next'
import { useSiteContent } from '@/store/siteContent'

const iconMap = { Linkedin, Twitter, Github, Instagram, Youtube }

const { state } = useSiteContent()
const company = state.data.site_settings
const services = computed(() => state.data.services.map((s) => s.title))

const email = ref('')
const subscribed = ref(false)
const subscribe = () => {
  if (!email.value) return
  subscribed.value = true
  setTimeout(() => { subscribed.value = false; email.value = '' }, 3500)
}

const quickLinks = [
  { label: 'About', href: '#about' },
  { label: 'Services', href: '#services' },
  { label: 'Portfolio', href: '#portfolio' },
  { label: 'Process', href: '#process' },
]
const moreLinks = [
  { label: 'Team', href: '#team' },
  { label: 'Testimonials', href: '#testimonials' },
  { label: 'Blog', href: '#blog' },
  { label: 'FAQ', href: '#faq' },
  { label: 'Contact', href: '#contact' },
]

const go = (href) => {
  if (window.__lenis) window.__lenis.scrollTo(href, { offset: -80, duration: 1.3 })
  else document.querySelector(href)?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <footer class="relative overflow-hidden bg-navy-950 text-white pt-20 pb-8">
    <!-- bg -->
    <div class="absolute inset-0 pointer-events-none">
      <div data-parallax data-parallax-speed="0.22" class="aurora-blob w-[60vw] h-[60vw] -top-[20%] left-[20%] animate-float-slow"
           style="background: radial-gradient(circle, rgba(70,173,100,0.25), transparent 65%);"></div>
      <div data-parallax data-parallax-speed="-0.18" data-parallax-rotate="8" class="aurora-blob w-[40vw] h-[40vw] -bottom-[10%] -left-[10%] animate-float"
           style="background: radial-gradient(circle, rgba(34,211,238,0.18), transparent 65%); animation-delay: -4s;"></div>
    </div>
    <div class="absolute inset-0 bg-grid-dark opacity-15 pointer-events-none"></div>

    <div class="container-x relative">
      <!-- Top CTA strip -->
      <div class="relative rounded-3xl overflow-hidden p-8 md:p-12 mb-16"
           data-reveal="fade-up">
        <div class="absolute inset-0" style="background: linear-gradient(120deg, rgba(5,48,99,0.95), rgba(28,79,150,0.9) 40%, rgba(70,173,100,0.85));"></div>
        <div class="absolute inset-0 bg-grid-dark opacity-30"></div>
        <div class="relative flex flex-col md:flex-row items-center justify-between gap-6 text-center md:text-left">
          <div>
            <h3 class="font-display font-bold text-2xl md:text-3xl text-white leading-tight">Ready to build your next big thing?</h3>
            <p class="text-white/80 mt-2">Schedule a 30-minute discovery call with our team. No pressure, no jargon — just a real conversation about your goals.</p>
          </div>
          <button @click="go('#contact')"
                  class="magnetic shrink-0 inline-flex items-center gap-2 rounded-full bg-white px-7 py-4 font-semibold text-navy-700 shadow-glow-green hover:scale-105 transition-transform group">
            Start your project
            <ArrowRight :size="18" class="group-hover:translate-x-1 transition-transform" />
          </button>
        </div>
      </div>

      <!-- Footer grid -->
      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-8 mb-12">
        <!-- Brand -->
        <div class="col-span-2 lg:col-span-2">
          <a href="#home" @click.prevent="go('#home')" class="flex items-center gap-2.5 mb-5">
            <img src="@/assets/images/logo.png" alt="SKT" class="w-10 h-10 object-contain" />
            <div class="leading-none">
              <div class="font-display font-bold text-lg text-white">SKT<span class="text-emerald-brand-400">.</span></div>
              <div class="font-mono text-[9px] uppercase tracking-[0.25em] text-white/50">CMS</div>
            </div>
          </a>
          <p class="text-sm text-white/60 leading-relaxed max-w-sm mb-5">
            {{ company.tagline }}. We are a senior engineering studio crafting software, ERP, cloud, and AI solutions for category-defining companies.
          </p>

          <!-- Newsletter -->
          <div>
            <p class="text-xs font-semibold uppercase tracking-wider text-white/50 mb-2">Subscribe to our newsletter</p>
            <form @submit.prevent="subscribe" class="flex gap-2">
              <input v-model="email" type="email" required placeholder="you@company.com"
                     class="flex-1 min-w-0 rounded-xl bg-white/10 border border-white/15 px-3 py-2.5 text-sm text-white placeholder-white/40 focus:outline-none focus:border-emerald-brand-400 transition-colors" />
              <button type="submit" :disabled="subscribed"
                      class="shrink-0 w-10 h-10 rounded-xl flex items-center justify-center text-white shadow-glow-green hover:scale-105 transition-transform"
                      style="background: linear-gradient(135deg, #46ad64, #22d3ee);">
                <Check v-if="subscribed" :size="16" />
                <ArrowRight v-else :size="16" />
              </button>
            </form>
          </div>
        </div>

        <!-- Quick links -->
        <div>
          <h4 class="font-display font-semibold text-sm text-white mb-4">Company</h4>
          <ul class="space-y-2.5">
            <li v-for="l in quickLinks" :key="l.label">
              <a :href="l.href" @click.prevent="go(l.href)"
                 class="text-sm text-white/60 hover:text-emerald-brand-300 transition-colors">{{ l.label }}</a>
            </li>
          </ul>
        </div>

        <div>
          <h4 class="font-display font-semibold text-sm text-white mb-4">More</h4>
          <ul class="space-y-2.5">
            <li v-for="l in moreLinks" :key="l.label">
              <a :href="l.href" @click.prevent="go(l.href)"
                 class="text-sm text-white/60 hover:text-emerald-brand-300 transition-colors">{{ l.label }}</a>
            </li>
          </ul>
        </div>

        <!-- Services -->
        <div class="col-span-2 lg:col-span-2">
          <h4 class="font-display font-semibold text-sm text-white mb-4">Services</h4>
          <ul class="grid grid-cols-2 gap-x-3 gap-y-2.5">
            <li v-for="s in services" :key="s">
              <a href="#services" @click.prevent="go('#services')"
                 class="text-sm text-white/60 hover:text-emerald-brand-300 transition-colors">{{ s }}</a>
            </li>
          </ul>
        </div>
      </div>

      <!-- Contact row -->
      <div class="grid sm:grid-cols-3 gap-4 py-8 border-y border-white/10">
        <a :href="`mailto:${company.email}`" class="flex items-center gap-3 text-sm text-white/70 hover:text-white transition-colors">
          <Mail :size="16" class="text-emerald-brand-400" />
          {{ company.email }}
        </a>
        <a :href="`tel:${company.phone}`" class="flex items-center gap-3 text-sm text-white/70 hover:text-white transition-colors">
          <Phone :size="16" class="text-emerald-brand-400" />
          {{ company.phone }}
        </a>
        <div class="flex items-center gap-3 text-sm text-white/70">
          <MapPin :size="16" class="text-emerald-brand-400" />
          {{ company.address }}
        </div>
      </div>

      <!-- Bottom -->
      <div class="pt-8 flex flex-col md:flex-row items-center justify-between gap-4">
        <p class="text-xs text-white/40 order-2 md:order-1">
          © {{ new Date().getFullYear() }} {{ company.company_name }}. All rights reserved. · SOC 2 Type II · ISO 27001 · HIPAA
        </p>
        <div class="flex items-center gap-2 order-1 md:order-2">
          <a v-for="s in company.social" :key="s.name" :href="s.href" :aria-label="s.name" @click.prevent
             class="w-9 h-9 rounded-lg glass-dark flex items-center justify-center text-white/70 hover:text-white hover:bg-emerald-brand-400 transition-all">
            <component :is="iconMap[s.icon]" :size="15" />
          </a>
        </div>
      </div>
    </div>
  </footer>
</template>
