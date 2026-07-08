<script setup>
import { ref } from 'vue'
import { Plus, Minus, HelpCircle } from 'lucide-vue-next'
import SectionHeading from '@/components/base/SectionHeading.vue'
import { useSiteContent } from '@/store/siteContent'

const { state } = useSiteContent()
const open = ref(0)
const toggle = (i) => { open.value = open.value === i ? -1 : i }
</script>

<template>
  <section id="faq" class="section relative overflow-hidden">
    <div class="absolute inset-0 bg-dots opacity-50 pointer-events-none"></div>
    <div data-parallax data-parallax-speed="0.22" class="aurora-blob w-[40vw] h-[40vw] top-[10%] -right-[15%] animate-float-slow"
         style="background: radial-gradient(circle, rgba(70,173,100,0.18), transparent 65%);"></div>

    <div class="container-x relative">
      <SectionHeading
        eyebrow="FAQ"
        title="Answers to the"
        highlight="questions we hear most"
        subtitle="Don't see your question here? Reach out — we'll usually reply within one business day."
      />

      <div class="mt-14 max-w-3xl mx-auto space-y-3">
        <div v-for="(item, i) in state.data.faqs" :key="item.id"
             data-reveal="fade-up"
             :data-reveal-delay="i * 60"
             class="group glass rounded-2xl overflow-hidden transition-all duration-300"
             :class="open === i ? 'shadow-glass-lg' : ''">
          <button @click="toggle(i)"
                  class="w-full flex items-center justify-between gap-4 p-5 md:p-6 text-left"
                  :aria-expanded="open === i">
            <div class="flex items-center gap-3">
              <span class="w-9 h-9 rounded-xl flex items-center justify-center shrink-0 transition-colors"
                    :class="open === i ? 'text-white' : 'text-navy-700'"
                    :style="open === i ? 'background: linear-gradient(135deg, #053063, #46ad64);' : 'background: linear-gradient(135deg, rgba(5,48,99,0.08), rgba(70,173,100,0.12));'">
                <HelpCircle :size="16" />
              </span>
              <span class="font-display font-semibold text-navy-700 text-base md:text-lg">{{ item.q }}</span>
            </div>
            <span class="w-8 h-8 rounded-full flex items-center justify-center shrink-0 transition-all"
                  :class="open === i ? 'bg-emerald-brand-400 text-white rotate-180' : 'bg-navy-50 text-navy-700'">
              <component :is="open === i ? Minus : Plus" :size="16" />
            </span>
          </button>

          <Transition name="faq">
            <div v-show="open === i" class="px-5 md:px-6 pb-5 md:pb-6 pl-[3.85rem] md:pl-[4.35rem]">
              <p class="text-slate-600 leading-relaxed">{{ item.a }}</p>
            </div>
          </Transition>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.faq-enter-active, .faq-leave-active {
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  overflow: hidden;
}
.faq-enter-from, .faq-leave-to {
  opacity: 0;
  max-height: 0;
  padding-top: 0;
  padding-bottom: 0;
}
.faq-enter-to, .faq-leave-from {
  opacity: 1;
  max-height: 400px;
}
</style>
