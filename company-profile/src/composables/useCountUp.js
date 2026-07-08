import { ref, onBeforeUnmount } from 'vue'

/**
 * CountUp animation that triggers when the element enters the viewport.
 * Returns { register }: call register(el, target, opts) -> a reactive ref
 * that the template binds to (e.g. `{{ display }}`). Driving the displayed
 * number through Vue state (instead of writing el.textContent directly)
 * means the animation survives any re-render Vue does for unrelated
 * reactive changes elsewhere in the component.
 */
export function useCountUp() {
  let observer = null
  const records = new Map() // el -> record

  const register = (el, target, opts = {}) => {
    const display = ref(0)
    if (!el) return display

    if (!observer) {
      observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          const rec = records.get(entry.target)
          if (rec && entry.isIntersecting && !rec.done) {
            rec.done = true
            animate(rec)
            observer.unobserve(entry.target)
          }
        })
      }, { threshold: 0.3 })
    }

    records.set(el, { target, opts, display, done: false })
    observer.observe(el)
    return display
  }

  const animate = ({ target, opts, display }) => {
    const duration = opts.duration || 2200
    const decimals = opts.decimals || 0
    const start = performance.now()
    const step = (now) => {
      const p = Math.min((now - start) / duration, 1)
      // easeOutExpo
      const eased = p === 1 ? 1 : 1 - Math.pow(2, -10 * p)
      const val = target * eased
      display.value = decimals ? Number(val.toFixed(decimals)) : Math.round(val)
      if (p < 1) requestAnimationFrame(step)
    }
    requestAnimationFrame(step)
  }

  onBeforeUnmount(() => {
    if (observer) observer.disconnect()
  })

  return { register }
}
