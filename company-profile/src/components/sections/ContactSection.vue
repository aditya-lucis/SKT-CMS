<script setup>
import { ref } from 'vue'
import { Mail, Phone, MapPin, Send, Linkedin, Twitter, Github, Instagram, Youtube, Check, Loader2 } from 'lucide-vue-next'
import SectionHeading from '@/components/base/SectionHeading.vue'
import { useSiteContent } from '@/store/siteContent'
import { api } from '@/lib/api'

const iconMap = { Linkedin, Twitter, Github, Instagram, Youtube }

const { state } = useSiteContent()
const company = state.data.site_settings

const form = ref({
  name: '', email: '', company: '', budget: '', message: '',
})
const sending = ref(false)
const sent = ref(false)
const error = ref('')

const submit = async () => {
  error.value = ''
  sending.value = true
  try {
    await api.post('/api/contact', {
      name: form.value.name,
      email: form.value.email,
      phone: '',
      subject: [form.value.company, form.value.budget].filter(Boolean).join(' · '),
      message: form.value.message,
    })
    sent.value = true
    setTimeout(() => {
      sent.value = false
      form.value = { name: '', email: '', company: '', budget: '', message: '' }
    }, 3500)
  } catch (err) {
    error.value = 'Gagal mengirim pesan. Coba lagi sebentar ya.'
  } finally {
    sending.value = false
  }
}

const budgets = ['< $50k', '$50k – $250k', '$250k – $1M', '> $1M', 'Not sure yet']
</script>

<template>
  <section id="contact" class="section relative overflow-hidden section-dark">
    <!-- bg -->
    <div class="absolute inset-0 pointer-events-none">
      <div data-parallax data-parallax-speed="0.22" class="aurora-blob w-[50vw] h-[50vw] top-[-10%] right-[-10%] animate-float-slow"
           style="background: radial-gradient(circle, rgba(70,173,100,0.4), transparent 65%);"></div>
      <div data-parallax data-parallax-speed="-0.18" data-parallax-rotate="8" class="aurora-blob w-[40vw] h-[40vw] bottom-[-10%] left-[-10%] animate-float"
           style="background: radial-gradient(circle, rgba(34,211,238,0.3), transparent 65%); animation-delay: -5s;"></div>
    </div>
    <div class="absolute inset-0 bg-grid-dark opacity-20 pointer-events-none"></div>

    <div class="container-x relative">
      <SectionHeading
        eyebrow="Contact"
        title="Let's build something"
        highlight="extraordinary together"
        subtitle="Tell us about your project. We'll get back to you within one business day with a thoughtful response — not a sales pitch."
        dark
      />

      <div class="mt-16 grid lg:grid-cols-5 gap-8">
        <!-- Left: Info + Map -->
        <div class="lg:col-span-2 space-y-5" data-reveal="fade-right">
          <!-- Map placeholder -->
          <div class="relative rounded-3xl overflow-hidden glass-dark h-64">
            <iframe
              title="Nexus Technology HQ"
              src="https://www.openstreetmap.org/export/embed.html?bbox=-122.4017%2C37.7900%2C-122.3917%2C37.8000&layer=mapnik&marker=37.7950%2C-122.3967"
              class="w-full h-full grayscale opacity-80"
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade"
              style="filter: grayscale(1) invert(0.92) hue-rotate(180deg) brightness(0.95) contrast(0.9);"></iframe>
            <div class="absolute inset-0 pointer-events-none" style="background: linear-gradient(135deg, rgba(70,173,100,0.18), transparent 50%, rgba(34,211,238,0.12));"></div>
            <div class="absolute bottom-3 left-3 glass-dark rounded-xl px-3 py-2 text-xs text-white flex items-center gap-2">
              <MapPin :size="14" class="text-emerald-brand-300" />
              One Market St, San Francisco
            </div>
          </div>

          <!-- Contact info -->
          <div class="space-y-3">
            <a :href="`mailto:${company.email}`"
               class="flex items-center gap-4 glass-dark rounded-2xl p-4 text-white hover:bg-white/15 transition-colors group">
              <span class="w-11 h-11 rounded-xl flex items-center justify-center" style="background: linear-gradient(135deg, #46ad64, #22d3ee);">
                <Mail :size="18" />
              </span>
              <div>
                <div class="text-xs text-white/60">Email us</div>
                <div class="font-semibold group-hover:text-emerald-brand-300 transition-colors">{{ company.email }}</div>
              </div>
            </a>
            <a :href="`tel:${company.phone}`"
               class="flex items-center gap-4 glass-dark rounded-2xl p-4 text-white hover:bg-white/15 transition-colors group">
              <span class="w-11 h-11 rounded-xl flex items-center justify-center" style="background: linear-gradient(135deg, #053063, #1c4f96);">
                <Phone :size="18" />
              </span>
              <div>
                <div class="text-xs text-white/60">Call us</div>
                <div class="font-semibold group-hover:text-emerald-brand-300 transition-colors">{{ company.phone }}</div>
              </div>
            </a>
            <div class="flex items-center gap-4 glass-dark rounded-2xl p-4 text-white">
              <span class="w-11 h-11 rounded-xl flex items-center justify-center" style="background: linear-gradient(135deg, #8b5cf6, #ec4899);">
                <MapPin :size="18" />
              </span>
              <div>
                <div class="text-xs text-white/60">Visit us</div>
                <div class="font-semibold">{{ company.address }}</div>
              </div>
            </div>
          </div>

          <!-- Socials -->
          <div class="flex gap-2.5">
            <a v-for="s in company.social" :key="s.name" :href="s.href" :aria-label="s.name"
               @click.prevent
               class="w-11 h-11 rounded-xl glass-dark text-white flex items-center justify-center hover:bg-emerald-brand-400 hover:scale-110 transition-all">
              <component :is="iconMap[s.icon]" :size="18" />
            </a>
          </div>
        </div>

        <!-- Right: Form -->
        <div class="lg:col-span-3" data-reveal="fade-left">
          <form @submit.prevent="submit" class="glass-dark rounded-3xl p-6 md:p-8 space-y-5">
            <div class="grid sm:grid-cols-2 gap-4">
              <div>
                <label class="text-xs font-semibold uppercase tracking-wider text-white/60 mb-2 block">Full name</label>
                <input v-model="form.name" type="text" required
                       placeholder="Jane Doe"
                       class="w-full rounded-xl bg-white/10 border border-white/15 px-4 py-3 text-white placeholder-white/40 focus:outline-none focus:border-emerald-brand-400 focus:bg-white/15 transition-colors" />
              </div>
              <div>
                <label class="text-xs font-semibold uppercase tracking-wider text-white/60 mb-2 block">Work email</label>
                <input v-model="form.email" type="email" required
                       placeholder="jane@company.com"
                       class="w-full rounded-xl bg-white/10 border border-white/15 px-4 py-3 text-white placeholder-white/40 focus:outline-none focus:border-emerald-brand-400 focus:bg-white/15 transition-colors" />
              </div>
            </div>

            <div class="grid sm:grid-cols-2 gap-4">
              <div>
                <label class="text-xs font-semibold uppercase tracking-wider text-white/60 mb-2 block">Company</label>
                <input v-model="form.company" type="text"
                       placeholder="Acme Inc."
                       class="w-full rounded-xl bg-white/10 border border-white/15 px-4 py-3 text-white placeholder-white/40 focus:outline-none focus:border-emerald-brand-400 focus:bg-white/15 transition-colors" />
              </div>
              <div>
                <label class="text-xs font-semibold uppercase tracking-wider text-white/60 mb-2 block">Budget</label>
                <select v-model="form.budget"
                        class="w-full rounded-xl bg-white/10 border border-white/15 px-4 py-3 text-white focus:outline-none focus:border-emerald-brand-400 focus:bg-white/15 transition-colors">
                  <option value="" class="bg-navy-800">Select a range</option>
                  <option v-for="b in budgets" :key="b" :value="b" class="bg-navy-800">{{ b }}</option>
                </select>
              </div>
            </div>

            <div>
              <label class="text-xs font-semibold uppercase tracking-wider text-white/60 mb-2 block">Tell us about your project</label>
              <textarea v-model="form.message" required rows="5"
                        placeholder="What are you trying to build? What does success look like?"
                        class="w-full rounded-xl bg-white/10 border border-white/15 px-4 py-3 text-white placeholder-white/40 focus:outline-none focus:border-emerald-brand-400 focus:bg-white/15 transition-colors resize-none"></textarea>
            </div>

            <button type="submit"
                    :disabled="sent || sending"
                    class="w-full relative overflow-hidden rounded-xl px-6 py-4 font-semibold text-white shadow-glow-green transition-all hover:scale-[1.01] disabled:opacity-70">
              <span class="absolute inset-0" style="background: linear-gradient(120deg, #053063, #1c4f96 40%, #46ad64);"></span>
              <span class="absolute inset-0 shimmer-bg opacity-0 hover:opacity-100 transition-opacity"></span>
              <span class="relative flex items-center justify-center gap-2">
                <template v-if="sent">
                  <Check :size="18" /> Message sent — we'll be in touch!
                </template>
                <template v-else-if="sending">
                  <Loader2 :size="18" class="animate-spin" /> Sending...
                </template>
                <template v-else>
                  <Send :size="18" /> Send message
                </template>
              </span>
            </button>

            <p v-if="error" class="text-sm text-red-300 text-center">{{ error }}</p>
            <p class="text-xs text-white/50 text-center">
              By submitting, you agree to our privacy policy. We never share your information.
            </p>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>
