<script setup>
import { ref, watch, nextTick } from 'vue'
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Autoplay, Pagination, Navigation, EffectFade } from 'swiper/modules'
import { Star, Quote, ChevronLeft, ChevronRight } from 'lucide-vue-next'
import SectionHeading from '@/components/base/SectionHeading.vue'
import { useSiteContent } from '@/store/siteContent'
import { resolveMediaUrl } from '@/lib/api'
import 'swiper/css'
import 'swiper/css/pagination'
import 'swiper/css/effect-fade'

const { state } = useSiteContent()
const modules = [Autoplay, Pagination, Navigation, EffectFade]
const swiperRef = ref(null)

const onSwiper = (s) => { swiperRef.value = s }
const prev = () => swiperRef.value?.slidePrev()
const next = () => swiperRef.value?.slideNext()

// Testimonials arrive async; nudge Swiper (loop mode especially) to
// re-measure once the real slides have rendered.
watch(() => state.data.testimonials.length, async () => {
  await nextTick()
  swiperRef.value?.update()
})
</script>

<template>
  <section id="testimonials" class="section relative overflow-hidden section-dark">
    <!-- bg -->
    <div class="absolute inset-0 pointer-events-none">
      <div data-parallax data-parallax-speed="0.22" class="aurora-blob w-[50vw] h-[50vw] top-[-10%] left-[10%] animate-float-slow"
           style="background: radial-gradient(circle, rgba(70,173,100,0.35), transparent 65%);"></div>
      <div data-parallax data-parallax-speed="-0.18" data-parallax-rotate="8" class="aurora-blob w-[40vw] h-[40vw] bottom-[-10%] right-[10%] animate-float"
           style="background: radial-gradient(circle, rgba(139,92,246,0.25), transparent 65%); animation-delay: -5s;"></div>
    </div>
    <div class="absolute inset-0 bg-grid-dark opacity-20 pointer-events-none"></div>

    <div class="container-x relative">
      <SectionHeading
        eyebrow="Testimonials"
        title="What our clients"
        highlight="say about working with us"
        subtitle="We measure our success by the success of the people who trust us with their hardest problems. Here's a sampling."
        dark
      />

      <div class="mt-14 relative" data-reveal="fade-up">
        <Swiper
          :modules="modules"
          :slides-per-view="1"
          :space-between="32"
          :loop="true"
          :autoplay="{ delay: 5500, disableOnInteraction: false }"
          :pagination="{ clickable: true }"
          @swiper="onSwiper"
          class="!pb-14"
        >
          <SwiperSlide v-for="t in state.data.testimonials" :key="t.id">
            <div class="relative glass-dark rounded-3xl p-8 md:p-12 max-w-4xl mx-auto">
              <!-- Quote icon -->
              <div class="absolute -top-4 -left-2 md:left-6 w-14 h-14 rounded-2xl flex items-center justify-center"
                   style="background: linear-gradient(135deg, #46ad64, #22d3ee);">
                <Quote :size="24" class="text-white" />
              </div>

              <!-- Rating -->
              <div class="flex gap-1 mb-5 pt-3">
                <Star v-for="r in t.rating" :key="r" :size="18" class="text-amber-400 fill-amber-400" />
              </div>

              <!-- Quote -->
              <p class="text-lg md:text-2xl text-white leading-relaxed font-medium mb-8">
                "{{ t.quote }}"
              </p>

              <!-- Author -->
              <div class="flex items-center gap-4">
                <img :src="resolveMediaUrl(t.img)" :alt="t.name"
                     class="w-14 h-14 rounded-full object-cover border-2 border-emerald-brand-400" loading="lazy" />
                <div>
                  <div class="font-display font-bold text-white text-lg">{{ t.name }}</div>
                  <div class="text-sm text-emerald-brand-300">{{ t.role }}</div>
                </div>
              </div>
            </div>
          </SwiperSlide>
        </Swiper>

        <!-- Custom nav -->
        <div class="flex justify-center gap-3 mt-6">
          <button @click="prev" aria-label="Previous"
                  class="w-12 h-12 rounded-full glass-dark text-white flex items-center justify-center hover:bg-white/15 transition-colors">
            <ChevronLeft :size="20" />
          </button>
          <button @click="next" aria-label="Next"
                  class="w-12 h-12 rounded-full glass-dark text-white flex items-center justify-center hover:bg-white/15 transition-colors">
            <ChevronRight :size="20" />
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
:deep(.swiper-pagination-bullet) {
  background: white;
  opacity: 0.3;
  width: 10px;
  height: 10px;
  transition: all 0.3s ease;
}
:deep(.swiper-pagination-bullet-active) {
  opacity: 1;
  width: 28px;
  border-radius: 99px;
  background: linear-gradient(90deg, #46ad64, #22d3ee);
}
</style>
