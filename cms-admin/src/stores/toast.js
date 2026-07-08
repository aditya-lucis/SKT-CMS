import { reactive } from 'vue'

const toasts = reactive([])
let idCounter = 0

export function useToast() {
  function push(message, type = 'success') {
    const id = ++idCounter
    toasts.push({ id, message, type })
    setTimeout(() => {
      const idx = toasts.findIndex((t) => t.id === id)
      if (idx !== -1) toasts.splice(idx, 1)
    }, 3500)
  }

  return {
    toasts,
    success: (msg) => push(msg, 'success'),
    error: (msg) => push(msg, 'error'),
  }
}
