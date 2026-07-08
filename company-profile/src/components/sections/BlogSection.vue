<script setup>
import { Calendar, Clock, ArrowUpRight } from 'lucide-vue-next'
import SectionHeading from '@/components/base/SectionHeading.vue'
import { useSiteContent } from '@/store/siteContent'
import { resolveMediaUrl } from '@/lib/api'

const { state } = useSiteContent()
</script>

<template>
  <section id="blog" class="section relative overflow-hidden bg-navy-50/40">
    <div class="absolute inset-0 bg-grid opacity-40 pointer-events-none"></div>
    <div data-parallax data-parallax-speed="0.22" class="aurora-blob w-[45vw] h-[45vw] top-[20%] -left-[15%] animate-float-slow"
         style="background: radial-gradient(circle, rgba(5,48,99,0.15), transparent 65%);"></div>

    <div class="container-x relative">
      <SectionHeading
        eyebrow="From the Blog"
        title="Ideas, lessons, and"
        highlight="field notes from the team"
        subtitle="Hard-won knowledge from shipping software at scale. Written by the engineers, designers, and AI researchers doing the work — not the marketing team."
      />

      <div class="mt-16 grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        <article v-for="(post, i) in state.data.blog_posts" :key="post.id"
                 data-reveal="fade-up"
                 :data-reveal-delay="(i % 3) * 100"
                 class="group relative rounded-3xl overflow-hidden glass card-hover flex flex-col">
          <!-- Image -->
          <div class="relative aspect-[16/10] overflow-hidden">
            <div class="absolute left-0 w-full will-change-transform" style="top: -12%; height: 124%;"
                 data-parallax :data-parallax-speed="0.09 + (i % 3) * 0.03">
              <img :src="resolveMediaUrl(post.image)" :alt="post.title"
                   class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
                   loading="lazy" />
            </div>
            <div class="absolute inset-0" style="background: linear-gradient(180deg, transparent 50%, rgba(4,37,74,0.4) 100%);"></div>
            <span class="absolute top-4 left-4 px-3 py-1 rounded-full text-[10px] font-mono uppercase tracking-wider glass-dark text-white">
              {{ post.category }}
            </span>
          </div>

          <!-- Body -->
          <div class="p-6 flex-1 flex flex-col">
            <h3 class="font-display font-bold text-lg text-navy-700 leading-snug mb-2 group-hover:text-emerald-brand-600 transition-colors line-clamp-2">
              {{ post.title }}
            </h3>
            <p class="text-sm text-slate-600 leading-relaxed line-clamp-2 mb-4 flex-1">
              {{ post.excerpt }}
            </p>
            <div class="flex items-center justify-between text-xs text-slate-500 pt-4 border-t border-slate-200">
              <div class="flex items-center gap-3">
                <span class="flex items-center gap-1"><Calendar :size="12" />{{ post.date }}</span>
                <span class="flex items-center gap-1"><Clock :size="12" />{{ post.read_time }}</span>
              </div>
              <span class="font-semibold text-navy-700 group-hover:text-emerald-brand-600 transition-colors">
                by {{ post.author }}
              </span>
            </div>
          </div>

          <!-- Hover arrow -->
          <div class="absolute top-4 right-4 w-10 h-10 rounded-full glass-dark text-white flex items-center justify-center opacity-0 group-hover:opacity-100 transition-all duration-500 -translate-y-2 group-hover:translate-y-0">
            <ArrowUpRight :size="16" />
          </div>
        </article>
      </div>

      <!-- View all -->
      <div class="mt-12 text-center" data-reveal="fade-up">
        <a href="#" @click.prevent
           class="inline-flex items-center gap-2 px-6 py-3 rounded-full glass font-semibold text-navy-700 group hover:scale-105 transition-transform">
          Read all articles
          <ArrowUpRight :size="16" class="group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
        </a>
      </div>
    </div>
  </section>
</template>
