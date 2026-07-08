<script setup>
import { ref, onMounted } from 'vue'
import { Trash2, Mail, MailOpen } from 'lucide-vue-next'
import { api } from '@/lib/api'
import ConfirmDialog from '@/components/ConfirmDialog.vue'
import { useToast } from '@/stores/toast'

const toast = useToast()
const submissions = ref([])
const loading = ref(true)
const deleteTarget = ref(null)

async function load() {
  loading.value = true
  const { data } = await api.get('/api/contact-submissions')
  submissions.value = data
  loading.value = false
}

async function toggleRead(s) {
  await api.patch(`/api/contact-submissions/${s.id}`, { is_read: !s.is_read })
  s.is_read = !s.is_read
}

async function confirmDelete() {
  await api.delete(`/api/contact-submissions/${deleteTarget.value.id}`)
  toast.success('Pesan dihapus')
  deleteTarget.value = null
  await load()
}

onMounted(load)
</script>

<template>
  <div>
    <h1 class="text-xl font-display font-bold text-navy-900 mb-1">Pesan Masuk</h1>
    <p class="text-sm text-navy-500 mb-6">Submission dari form contact di website.</p>

    <div v-if="loading" class="card p-8 text-center text-navy-400">Memuat...</div>
    <div v-else-if="submissions.length === 0" class="card p-8 text-center text-navy-400">Belum ada pesan masuk.</div>

    <div v-else class="space-y-3">
      <div v-for="s in submissions" :key="s.id" class="card p-5" :class="!s.is_read && 'ring-1 ring-emerald-brand-300'">
        <div class="flex items-start justify-between gap-4">
          <div class="flex-1 min-w-0">
            <div class="flex items-center gap-2 flex-wrap">
              <span class="font-semibold text-navy-900">{{ s.name }}</span>
              <span class="text-navy-400 text-sm">{{ s.email }}</span>
              <span v-if="s.phone" class="text-navy-400 text-sm">· {{ s.phone }}</span>
            </div>
            <div v-if="s.subject" class="text-sm font-medium text-navy-600 mt-1">{{ s.subject }}</div>
            <p class="text-sm text-navy-600 mt-2 whitespace-pre-wrap">{{ s.message }}</p>
            <div class="text-xs text-navy-400 mt-2">{{ new Date(s.created_at).toLocaleString('id-ID') }}</div>
          </div>
          <div class="flex gap-1.5 shrink-0">
            <button class="btn-icon" @click="toggleRead(s)" :title="s.is_read ? 'Tandai belum dibaca' : 'Tandai sudah dibaca'">
              <MailOpen v-if="s.is_read" :size="15" />
              <Mail v-else :size="15" />
            </button>
            <button class="btn-icon hover:!bg-red-50 hover:!text-red-600 hover:!border-red-100" @click="deleteTarget = s">
              <Trash2 :size="15" />
            </button>
          </div>
        </div>
      </div>
    </div>

    <ConfirmDialog :show="!!deleteTarget" title="Hapus pesan ini?" @confirm="confirmDelete" @cancel="deleteTarget = null" />
  </div>
</template>
