import { onMounted, onBeforeUnmount, ref } from 'vue'

/**
 * Magnetic button effect — element translates toward cursor when cursor is near.
 * Usage:
 *   const { magneticRef } = useMagneticButton(0.35)
 *   <button :ref="magneticRef">...</button>
 */
export function useMagneticButton(strength = 0.3) {
  const magneticRef = ref(null)
  let el = null
  let rafId = null

  const onMove = (e) => {
    if (!el) return
    const rect = el.getBoundingClientRect()
    const cx = rect.left + rect.width / 2
    const cy = rect.top + rect.height / 2
    const dx = e.clientX - cx
    const dy = e.clientY - cy
    const dist = Math.hypot(dx, dy)
    const range = Math.max(rect.width, rect.height) * 1.4
    if (dist > range) {
      el.style.transform = 'translate3d(0,0,0)'
      return
    }
    const tx = dx * strength
    const ty = dy * strength
    el.style.transform = `translate3d(${tx}px, ${ty}px, 0)`
  }

  const onLeave = () => {
    if (!el) return
    el.style.transform = 'translate3d(0,0,0)'
  }

  onMounted(() => {
    el = magneticRef.value
    if (!el) return
    if (window.matchMedia('(hover: none)').matches) return
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
    el.style.transition = 'transform 0.45s cubic-bezier(0.16, 1, 0.3, 1)'
    el.style.willChange = 'transform'
    window.addEventListener('mousemove', onMove, { passive: true })
    el.addEventListener('mouseleave', onLeave)
  })

  onBeforeUnmount(() => {
    window.removeEventListener('mousemove', onMove)
    if (el) el.removeEventListener('mouseleave', onLeave)
    if (rafId) cancelAnimationFrame(rafId)
  })

  return { magneticRef }
}
