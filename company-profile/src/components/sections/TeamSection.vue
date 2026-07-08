<script setup>
import { Linkedin, Twitter, Github, Mail, ArrowUpRight } from 'lucide-vue-next'
import SectionHeading from '@/components/base/SectionHeading.vue'
import { useSiteContent } from '@/store/siteContent'
import { resolveMediaUrl } from '@/lib/api'

const { state } = useSiteContent()
const socialIcons = { linkedin: Linkedin, twitter: Twitter, github: Github, email: Mail }
</script>

<template>
  <section id="team" class="section relative overflow-hidden">
    <div class="absolute inset-0 bg-dots opacity-50 pointer-events-none"></div>
    <div data-parallax data-parallax-speed="0.22" class="aurora-blob w-[45vw] h-[45vw] top-[10%] -right-[15%] animate-float-slow"
         style="background: radial-gradient(circle, rgba(70,173,100,0.18), transparent 65%);"></div>

    <div class="container-x relative">
      <SectionHeading
        eyebrow="Our Team"
        title="Senior people who have"
        highlight="shipped at scale"
        subtitle="Our leaders have built and scaled platforms at Stripe, Apple, Datadog, Framer, and Cloudflare. Now they build for you."
      />

      <div class="mt-16 grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-5">
        <article v-for="(member, i) in state.data.team" :key="member.id"
                 data-reveal="fade-up"
                 :data-reveal-delay="(i % 4) * 90"
                 class="group relative rounded-3xl overflow-hidden card-hover">
          <!-- Image -->
          <div class="relative aspect-[3/4] overflow-hidden">
            <div class="absolute left-0 w-full will-change-transform" style="top: -12%; height: 124%;"
                 data-parallax :data-parallax-speed="0.08 + (i % 3) * 0.03">
              <img :src="resolveMediaUrl(member.img)" :alt="member.name"
                   class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
                   loading="lazy" />
            </div>
            <!-- Overlay -->
            <div class="absolute inset-0 transition-opacity duration-500"
                 style="background: linear-gradient(180deg, transparent 40%, rgba(4,37,74,0.6) 75%, rgba(3,26,54,0.95) 100%);"></div>
            <!-- Hover green tint -->
            <div class="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500"
                 style="background: linear-gradient(135deg, rgba(70,173,100,0.25), transparent 60%);"></div>

            <!-- Social icons appear on hover -->
            <div class="absolute top-3 right-3 flex flex-col gap-2 opacity-0 group-hover:opacity-100 translate-x-3 group-hover:translate-x-0 transition-all duration-500">
              <a v-for="(href, key) in member.socials" :key="key" v-show="href"
                 :href="key === 'email' ? `mailto:${href}` : href" target="_blank" rel="noopener"
                 class="w-8 h-8 rounded-full glass-dark flex items-center justify-center text-white hover:scale-110 transition-transform">
                <component :is="socialIcons[key]" :size="14" />
              </a>
            </div>
          </div>

          <!-- Info -->
          <div class="absolute inset-x-0 bottom-0 p-5 text-white">
            <h3 class="font-display font-bold text-lg leading-tight">{{ member.name }}</h3>
            <p class="text-sm text-emerald-brand-300 font-medium mt-0.5">{{ member.role }}</p>
            <p class="text-xs text-white/65 mt-2 leading-relaxed opacity-0 group-hover:opacity-100 transition-all duration-500 max-h-0 group-hover:max-h-20 overflow-hidden">
              {{ member.bio }}
            </p>
          </div>
        </article>
      </div>

      <!-- Bottom CTA -->
      <div class="mt-14 text-center" data-reveal="fade-up">
        <p class="text-slate-600 mb-4">We're always looking for exceptional engineers, designers, and AI researchers.</p>
        <a href="#" @click.prevent="$emit('contact')"
           class="inline-flex items-center gap-2 font-semibold text-navy-700 group">
          <span class="border-b-2 border-emerald-brand-400 pb-0.5">Join the team</span>
          <ArrowUpRight :size="18" class="group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
        </a>
      </div>
    </div>
  </section>
</template>
