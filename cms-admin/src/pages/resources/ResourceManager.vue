<script setup>
import { ref, computed, watch } from 'vue'
import { useRoute } from 'vue-router'
import { Plus, Pencil, Trash2, ArrowUp, ArrowDown, Star, X } from 'lucide-vue-next'
import { api, resolveMediaUrl } from '@/lib/api'
import { resourceConfigs } from '@/config/resourceConfigs'
import DynamicForm from '@/components/DynamicForm.vue'
import ConfirmDialog from '@/components/ConfirmDialog.vue'
import { useToast } from '@/stores/toast'

const route = useRoute()
const toast = useToast()

const resourceKey = computed(() => route.params.resource)
const config = computed(() => resourceConfigs[resourceKey.value])

const items = ref([])
const loading = ref(true)
const showModal = ref(false)
const editingId = ref(null)
const form = ref({})
const saving = ref(false)
const deleteTarget = ref(null)

function emptyForm() {
  const obj = {}
  for (const f of config.value.fields) {
    if (f.type === 'tags') obj[f.key] = []
    else if (f.type === 'socials') obj[f.key] = {}
    else if (f.type === 'boolean') obj[f.key] = true
    else if (f.type === 'number') obj[f.key] = 0
    else obj[f.key] = ''
  }
  return obj
}

async function load() {
  loading.value = true
  try {
    const { data } = await api.get(config.value.endpoint)
    items.value = data
  } catch (err) {
    toast.error('Gagal memuat data')
  } finally {
    loading.value = false
  }
}

watch(resourceKey, load, { immediate: true })

function openCreate() {
  editingId.value = null
  form.value = emptyForm()
  showModal.value = true
}

function openEdit(item) {
  editingId.value = item.id
  form.value = { ...item }
  showModal.value = true
}

async function save() {
  saving.value = true
  try {
    if (editingId.value) {
      await api.put(`${config.value.endpoint}/${editingId.value}`, form.value)
      toast.success('Perubahan disimpan')
    } else {
      await api.post(config.value.endpoint, form.value)
      toast.success('Item baru ditambahkan')
    }
    showModal.value = false
    await load()
  } catch (err) {
    toast.error(err.response?.data?.detail?.[0]?.msg || err.response?.data?.detail || 'Gagal menyimpan')
  } finally {
    saving.value = false
  }
}

async function confirmDelete() {
  try {
    await api.delete(`${config.value.endpoint}/${deleteTarget.value.id}`)
    toast.success('Item dihapus')
    deleteTarget.value = null
    await load()
  } catch (err) {
    toast.error('Gagal menghapus')
  }
}

async function move(index, dir) {
  const target = index + dir
  if (target < 0 || target >= items.value.length) return
  const arr = [...items.value]
  ;[arr[index], arr[target]] = [arr[target], arr[index]]
  items.value = arr
  const payload = arr.map((item, i) => ({ id: item.id, order_index: i }))
  try {
    await api.patch(`${config.value.endpoint}/reorder/bulk`, payload)
  } catch (err) {
    toast.error('Gagal mengubah urutan')
    await load()
  }
}

function displayValue(item, col) {
  const val = item[col]
  if (typeof val === 'boolean') return val ? 'Ya' : 'Tidak'
  if (Array.isArray(val)) return val.join(', ')
  return val
}
</script>

<template>
  <div v-if="config">
    <div class="flex items-start justify-between mb-6">
      <div>
        <h1 class="text-xl font-display font-bold text-navy-900">{{ config.title }}</h1>
        <p class="text-sm text-navy-500 mt-1">{{ config.subtitle }}</p>
      </div>
      <button class="btn-primary" @click="openCreate">
        <Plus :size="16" /> Tambah
      </button>
    </div>

    <div class="card overflow-hidden">
      <table class="w-full text-sm">
        <thead>
          <tr class="border-b border-navy-100 text-left text-xs uppercase tracking-wide text-navy-400">
            <th class="px-5 py-3 w-16">Urutan</th>
            <th v-for="col in config.columns" :key="col" class="px-5 py-3">{{ col }}</th>
            <th class="px-5 py-3 w-28 text-right">Aksi</th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="loading"><td :colspan="config.columns.length + 2" class="px-5 py-8 text-center text-navy-400">Memuat...</td></tr>
          <tr v-else-if="items.length === 0"><td :colspan="config.columns.length + 2" class="px-5 py-8 text-center text-navy-400">Belum ada data.</td></tr>
          <tr v-for="(item, i) in items" :key="item.id" class="border-b border-navy-50 last:border-0 hover:bg-navy-50/50">
            <td class="px-5 py-3">
              <div class="flex flex-col gap-0.5">
                <button class="text-navy-300 hover:text-navy-700 disabled:opacity-20" :disabled="i === 0" @click="move(i, -1)"><ArrowUp :size="14" /></button>
                <button class="text-navy-300 hover:text-navy-700 disabled:opacity-20" :disabled="i === items.length - 1" @click="move(i, 1)"><ArrowDown :size="14" /></button>
              </div>
            </td>
            <td v-for="col in config.columns" :key="col" class="px-5 py-3 max-w-xs truncate text-navy-700">
              {{ displayValue(item, col) }}
            </td>
            <td class="px-5 py-3">
              <div class="flex justify-end gap-1.5">
                <button class="btn-icon" @click="openEdit(item)"><Pencil :size="15" /></button>
                <button class="btn-icon hover:!bg-red-50 hover:!text-red-600 hover:!border-red-100" @click="deleteTarget = item"><Trash2 :size="15" /></button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Create/Edit modal -->
    <Teleport to="body">
      <Transition name="fade">
        <div v-if="showModal" class="fixed inset-0 z-50 flex items-center justify-center bg-navy-950/50 backdrop-blur-sm p-4">
          <div class="card w-full max-w-lg max-h-[85vh] flex flex-col">
            <div class="flex items-center justify-between px-6 py-4 border-b border-navy-100">
              <h3 class="font-display font-bold text-navy-900">{{ editingId ? 'Edit' : 'Tambah' }} {{ config.title }}</h3>
              <button class="btn-icon" @click="showModal = false"><X :size="16" /></button>
            </div>
            <div class="px-6 py-5 overflow-y-auto">
              <DynamicForm :fields="config.fields" v-model="form" />
            </div>
            <div class="px-6 py-4 border-t border-navy-100 flex gap-3">
              <button class="btn-secondary flex-1" @click="showModal = false">Batal</button>
              <button class="btn-primary flex-1" :disabled="saving" @click="save">
                {{ saving ? 'Menyimpan...' : 'Simpan' }}
              </button>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>

    <ConfirmDialog
      :show="!!deleteTarget"
      :title="`Hapus ${deleteTarget ? config.itemLabel(deleteTarget) : ''}?`"
      message="Data yang dihapus tidak bisa dikembalikan."
      @confirm="confirmDelete"
      @cancel="deleteTarget = null"
    />
  </div>
</template>

<style scoped>
.fade-enter-active, .fade-leave-active { transition: opacity 0.2s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>
