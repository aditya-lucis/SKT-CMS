<script setup>
import { ref } from 'vue'
import { ImagePlus, X, Loader2 } from 'lucide-vue-next'
import { api, resolveMediaUrl } from '@/lib/api'
import { useToast } from '@/stores/toast'

const props = defineProps({ modelValue: { type: String, default: '' } })
const emit = defineEmits(['update:modelValue'])

const toast = useToast()
const fileInput = ref(null)
const uploading = ref(false)

function pickFile() {
  fileInput.value?.click()
}

async function onFileChange(e) {
  const file = e.target.files?.[0]
  if (!file) return
  uploading.value = true
  try {
    const form = new FormData()
    form.append('file', file)
    const { data } = await api.post('/api/media/upload', form, {
      headers: { 'Content-Type': 'multipart/form-data' },
    })
    emit('update:modelValue', data.url)
    toast.success('Gambar berhasil diupload')
  } catch (err) {
    toast.error(err.response?.data?.detail || 'Upload gagal')
  } finally {
    uploading.value = false
    e.target.value = ''
  }
}

function clear() {
  emit('update:modelValue', '')
}
</script>

<template>
  <div>
    <input ref="fileInput" type="file" accept="image/*" class="hidden" @change="onFileChange" />

    <div v-if="modelValue" class="relative group w-full h-40 rounded-lg overflow-hidden border border-navy-100">
      <img :src="resolveMediaUrl(modelValue)" alt="" class="w-full h-full object-cover" />
      <div class="absolute inset-0 bg-navy-900/0 group-hover:bg-navy-900/50 transition-colors flex items-center justify-center gap-2 opacity-0 group-hover:opacity-100">
        <button type="button" @click="pickFile" class="btn-secondary !py-1.5 !px-3 text-xs">Ganti</button>
        <button type="button" @click="clear" class="btn-danger !py-1.5 !px-3 text-xs">
          <X :size="14" />
        </button>
      </div>
    </div>

    <button v-else type="button" @click="pickFile" :disabled="uploading"
            class="w-full h-40 rounded-lg border-2 border-dashed border-navy-200 flex flex-col items-center justify-center gap-2 text-navy-400 hover:border-emerald-brand-400 hover:text-emerald-brand-500 transition-colors">
      <Loader2 v-if="uploading" :size="22" class="animate-spin" />
      <ImagePlus v-else :size="22" />
      <span class="text-xs font-medium">{{ uploading ? 'Mengupload...' : 'Klik untuk upload gambar' }}</span>
    </button>

    <!-- Also allow pasting a direct URL -->
    <input :value="modelValue" @input="emit('update:modelValue', $event.target.value)"
           type="text" placeholder="atau paste URL gambar langsung"
           class="input mt-2 !text-xs" />
  </div>
</template>
