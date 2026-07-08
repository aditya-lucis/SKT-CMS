/**
 * useReveal — lightweight, dependency-free scroll reveal using IntersectionObserver.
 * Replaces AOS for max reliability across browsers and network conditions.
 *
 * Usage in setup():
 *   useReveal()  // auto-converts all [data-reveal] elements on mount
 *
 * Markup (any element):
 *   <div data-reveal>...</div>
 *   <div data-reveal="fade-up">...</div>
 *   <div data-reveal="fade-up" data-reveal-delay="100">...</div>
 *
 * Supported variants: fade, fade-up, fade-down, fade-left, fade-right, scale, blur
 */
import { onMounted, onBeforeUnmount } from 'vue'

const VARIANT_OFFSETS = {
  fade:        { y: 0,   x: 0,   scale: 1,    blur: 0  },
  'fade-up':   { y: 40,  x: 0,   scale: 1,    blur: 0  },
  'fade-down': { y: -40, x: 0,   scale: 1,    blur: 0  },
  'fade-left': { y: 0,   x: 40,  scale: 1,    blur: 0  },
  'fade-right':{ y: 0,   x: -40, scale: 1,    blur: 0  },
  scale:       { y: 0,   x: 0,   scale: 0.92, blur: 0  },
  blur:        { y: 0,   x: 0,   scale: 1,    blur: 14 },
}

const REDUCED_MOTION = typeof window !== 'undefined'
  && window.matchMedia('(prefers-reduced-motion: reduce)').matches

let observer = null
const watched = new Set()

function ensureObserver() {
  if (observer) return observer
  observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const el = entry.target
        const delay = parseInt(el.dataset.revealDelay || '0', 10)
        // Stagger children with data-reveal-stagger
        setTimeout(() => el.classList.add('reveal-in'), delay)
        observer.unobserve(el)
        watched.delete(el)
      }
    })
  }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' })
  return observer
}

function applyInitial(el) {
  const variant = el.dataset.reveal || 'fade-up'
  const cfg = VARIANT_OFFSETS[variant] || VARIANT_OFFSETS['fade-up']
  el.style.setProperty('--reveal-y', cfg.y + 'px')
  el.style.setProperty('--reveal-x', cfg.x + 'px')
  el.style.setProperty('--reveal-scale', cfg.scale)
  el.style.setProperty('--reveal-blur', cfg.blur + 'px')
  el.classList.add('reveal-init')
}

export function useReveal() {
  onMounted(() => {
    if (REDUCED_MOTION) {
      // No animation: force everything visible
      document.querySelectorAll('[data-reveal]').forEach((el) => {
        el.style.opacity = '1'
        el.style.transform = 'none'
        el.style.filter = 'none'
      })
      return
    }
    const obs = ensureObserver()
    document.querySelectorAll('[data-reveal]:not(.reveal-init)').forEach((el) => {
      applyInitial(el)
      obs.observe(el)
      watched.add(el)
    })

    // Safety net: force-reveal anything that's still hidden after 6s
    // (handles edge cases like elements above the fold in some browsers)
    setTimeout(() => {
      document.querySelectorAll('[data-reveal]:not(.reveal-in)').forEach((el) => {
        el.classList.add('reveal-in')
      })
    }, 6000)
  })

  onBeforeUnmount(() => {
    if (observer) {
      watched.forEach((el) => observer.unobserve(el))
      watched.clear()
    }
  })
}

/**
 * Refresh — call after dynamic content is added (e.g. after async data loads).
 */
export function refreshReveal() {
  if (REDUCED_MOTION) return
  const obs = ensureObserver()
  document.querySelectorAll('[data-reveal]:not(.reveal-init)').forEach((el) => {
    applyInitial(el)
    obs.observe(el)
    watched.add(el)
  })
  // Also reveal anything already in viewport that the observer might miss
  document.querySelectorAll('[data-reveal].reveal-init:not(.reveal-in)').forEach((el) => {
    const r = el.getBoundingClientRect()
    if (r.top < window.innerHeight && r.bottom > 0) {
      el.classList.add('reveal-in')
      if (observer) observer.unobserve(el)
    }
  })
}
