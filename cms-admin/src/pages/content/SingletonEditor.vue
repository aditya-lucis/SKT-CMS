<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { Save } from 'lucide-vue-next'
import { api } from '@/lib/api'
import { singletonConfigs } from '@/config/resourceConfigs'
import DynamicForm from '@/components/DynamicForm.vue'
import { useToast } from '@/stores/toast'

const route = useRoute()
const toast = useToast()

const sectionKey = computed(() => route.params.section)
const config = computed(() => singletonConfigs[sectionKey.value])

const form = ref({})
const loading = ref(true)
const saving = ref(false)

async function load() {
  loading.value = true
  try {
    const { data } = await api.get(`/api/content/${config.value.section}`)
    const defaults = {}
    for (const f of config.value.fields) {
      defaults[f.key] = f.type === 'tags' ? [] : ''
    }
    form.value = { ...defaults, ...data.data }
  } finally {
    loading.value = false
  }
}

watch(sectionKey, load, { immediate: true })

async function save() {
  saving.value = true
  try {
    await api.put(`/api/content/${config.value.section}`, { data: form.value })
    toast.success('Perubahan disimpan')
  } catch {
    toast.error('Gagal menyimpan')
  } finally {
    saving.value = false
  }
}
</script>

<template>
  <div v-if="config" class="max-w-2xl">
    <div class="flex items-start justify-between mb-6">
      <div>
        <h1 class="text-xl font-display font-bold text-navy-900">{{ config.title }}</h1>
        <p class="text-sm text-navy-500 mt-1">{{ config.subtitle }}</p>
      </div>
      <button class="btn-primary" :disabled="saving || loading" @click="save">
        <Save :size="16" /> {{ saving ? 'Menyimpan...' : 'Simpan' }}
      </button>
    </div>

    <div v-if="loading" class="card p-8 text-center text-navy-400">Memuat...</div>
    <div v-else class="card p-6">
      <DynamicForm :fields="config.fields" v-model="form" />
    </div>
  </div>
</template>
