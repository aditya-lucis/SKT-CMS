<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink } from 'vue-router'
import { Mail, ArrowRight } from 'lucide-vue-next'
import { api } from '@/lib/api'
import { resourceConfigs } from '@/config/resourceConfigs'

const counts = ref({})
const submissions = ref([])
const loading = ref(true)

onMounted(async () => {
  const entries = Object.entries(resourceConfigs)
  const results = await Promise.allSettled(entries.map(([, cfg]) => api.get(cfg.endpoint)))
  results.forEach((r, i) => {
    const [key] = entries[i]
    counts.value[key] = r.status === 'fulfilled' ? r.value.data.length : 0
  })

  try {
    const { data } = await api.get('/api/contact-submissions')
    submissions.value = data.slice(0, 5)
  } catch { /* ignore */ }

  loading.value = false
})

const unreadCount = () => submissions.value.filter((s) => !s.is_read).length
</script>

<template>
  <div>
    <h1 class="text-xl font-display font-bold text-navy-900 mb-1">Dashboard</h1>
    <p class="text-sm text-navy-500 mb-6">Ringkasan konten website SKT CMS.</p>

    <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
      <RouterLink v-for="(cfg, key) in resourceConfigs" :key="key"
                  :to="{ name: 'resource', params: { resource: key } }"
                  class="card p-5 hover:shadow-card-lg transition-shadow">
        <div class="text-2xl font-display font-bold text-navy-900">{{ loading ? '–' : (counts[key] ?? 0) }}</div>
        <div class="text-xs text-navy-500 mt-1">{{ cfg.title }}</div>
      </RouterLink>
    </div>

    <div class="card">
      <div class="flex items-center justify-between px-6 py-4 border-b border-navy-100">
        <h2 class="font-display font-bold text-navy-900 flex items-center gap-2">
          <Mail :size="18" /> Pesan Masuk Terbaru
          <span v-if="unreadCount()" class="bg-emerald-brand-500 text-white text-xs font-bold rounded-full px-2 py-0.5">{{ unreadCount() }} baru</span>
        </h2>
        <RouterLink :to="{ name: 'contact-submissions' }" class="text-sm text-emerald-brand-600 font-semibold flex items-center gap-1 hover:gap-2 transition-all">
          Lihat semua <ArrowRight :size="14" />
        </RouterLink>
      </div>
      <div v-if="submissions.length === 0" class="px-6 py-8 text-center text-navy-400 text-sm">Belum ada pesan masuk.</div>
      <div v-for="s in submissions" :key="s.id" class="px-6 py-4 border-b border-navy-50 last:border-0 flex items-start justify-between">
        <div>
          <div class="font-semibold text-navy-800 text-sm">{{ s.name }} <span class="font-normal text-navy-400">— {{ s.email }}</span></div>
          <p class="text-sm text-navy-500 mt-0.5 line-clamp-1">{{ s.message }}</p>
        </div>
        <span v-if="!s.is_read" class="w-2 h-2 rounded-full bg-emerald-brand-500 mt-1.5 shrink-0"></span>
      </div>
    </div>
  </div>
</template>
