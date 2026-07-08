<script setup>
import { Teleport, Transition } from 'vue'
import { AlertTriangle } from 'lucide-vue-next'

defineProps({
  show: { type: Boolean, default: false },
  title: { type: String, default: 'Hapus item ini?' },
  message: { type: String, default: 'Tindakan ini tidak bisa dibatalkan.' },
})
const emit = defineEmits(['confirm', 'cancel'])
</script>

<template>
  <Teleport to="body">
    <Transition name="fade">
      <div v-if="show" class="fixed inset-0 z-50 flex items-center justify-center bg-navy-950/50 backdrop-blur-sm p-4">
        <div class="card w-full max-w-sm p-6">
          <div class="w-11 h-11 rounded-full bg-red-50 flex items-center justify-center mb-4">
            <AlertTriangle :size="20" class="text-red-500" />
          </div>
          <h3 class="font-display font-bold text-navy-900 mb-1.5">{{ title }}</h3>
          <p class="text-sm text-navy-500 mb-6">{{ message }}</p>
          <div class="flex gap-3">
            <button class="btn-secondary flex-1" @click="emit('cancel')">Batal</button>
            <button class="btn-danger flex-1" @click="emit('confirm')">Hapus</button>
          </div>
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
.fade-enter-active, .fade-leave-active { transition: opacity 0.2s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>
