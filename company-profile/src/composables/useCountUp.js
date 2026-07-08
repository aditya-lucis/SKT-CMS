import { ref, onMounted, onBeforeUnmount } from 'vue'

/**
 * CountUp animation that triggers when the element enters the viewport.
 * Returns (target, ref) — attach ref to the element, target is final number.
 */
export function useCountUp() {
  const refs = []
  let observer = null

  const register = (el, target, opts = {}) => {
    if (!el) return
    refs.push({ el, target, opts, done: false })
    if (!observer) {
      observer = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const rec = refs.find((r) => r.el === entry.target)
            if (rec && !rec.done) {
              rec.done = true
              animate(rec)
            }
          }
        })
      }, { threshold: 0.4 })
    }
    observer.observe(el)
  }

  const animate = ({ el, target, opts }) => {
    const duration = opts.duration || 2200
    const decimals = opts.decimals || 0
    const prefix = opts.prefix || ''
    const suffix = opts.suffix || ''
    const start = performance.now()
    const step = (now) => {
      const p = Math.min((now - start) / duration, 1)
      // easeOutExpo
      const eased = p === 1 ? 1 : 1 - Math.pow(2, -10 * p)
      const val = target * eased
      el.textContent = prefix + val.toLocaleString('en-US', { minimumFractionDigits: decimals, maximumFractionDigits: decimals }) + suffix
      if (p < 1) requestAnimationFrame(step)
    }
    requestAnimationFrame(step)
  }

  onBeforeUnmount(() => {
    if (observer) observer.disconnect()
  })

  return { register }
}
