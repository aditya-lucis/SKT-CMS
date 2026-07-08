<script setup>
import { CheckCircle2, XCircle } from 'lucide-vue-next'
import { useToast } from '@/stores/toast'

const { toasts } = useToast()
</script>

<template>
  <div class="fixed bottom-5 right-5 z-[100] flex flex-col gap-2 w-80">
    <TransitionGroup name="toast">
      <div v-for="t in toasts" :key="t.id"
           class="flex items-start gap-2.5 rounded-xl px-4 py-3 shadow-card-lg text-sm font-medium"
           :class="t.type === 'error' ? 'bg-red-600 text-white' : 'bg-navy-800 text-white'">
        <CheckCircle2 v-if="t.type === 'success'" :size="18" class="shrink-0 mt-0.5 text-emerald-brand-300" />
        <XCircle v-else :size="18" class="shrink-0 mt-0.5 text-red-200" />
        <span>{{ t.message }}</span>
      </div>
    </TransitionGroup>
  </div>
</template>

<style scoped>
.toast-enter-active, .toast-leave-active { transition: all 0.3s ease; }
.toast-enter-from { opacity: 0; transform: translateX(20px); }
.toast-leave-to { opacity: 0; transform: translateY(-10px); }
</style>
