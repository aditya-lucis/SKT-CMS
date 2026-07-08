import { onMounted, onBeforeUnmount } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

/**
 * Register a batch of scroll-triggered reveal animations.
 * Pass a config object describing the targets and their animation.
 *
 * Usage in setup():
 *   useScrollReveal((scope) => {
 *     scope('.reveal-up', { y: 40, duration: 0.9, stagger: 0.08 })
 *   })
 */
export function useScrollReveal(setup) {
  let ctx
  onMounted(() => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      // Just clear reveal states
      document.querySelectorAll('.reveal, .reveal-up, .reveal-scale, .reveal-blur')
        .forEach((el) => {
          el.style.opacity = '1'
          el.style.transform = 'none'
          el.style.filter = 'none'
        })
      return
    }

    ctx = gsap.context((self) => {
      const scope = (selector, vars = {}, options = {}) => {
        const els = self.selector ? self.selector(selector) : document.querySelectorAll(selector)
        if (!els || !els.length) return
        const { y = 40, x = 0, scale = 1, opacity = 1, duration = 0.9, delay = 0, stagger = 0.08, blur = 0, start = 'top 85%', toggleActions = 'play none none none' } = { ...vars, ...options }
        const tweenVars = { opacity, duration, delay, stagger, ease: 'expo.out', scrollTrigger: { trigger: els[0], start, toggleActions } }
        if (y) tweenVars.y = y
        if (x) tweenVars.x = x
        if (scale !== 1) tweenVars.scale = scale
        if (blur) tweenVars.filter = `blur(${blur}px)`
        // Set initial state then animate to final
        gsap.set(els, { opacity: 0, y: y || 0, x: x || 0, scale, filter: blur ? `blur(${blur}px)` : 'none' })
        gsap.to(els, tweenVars)
      }
      setup(scope, self)
    })
  })

  onBeforeUnmount(() => {
    if (ctx) ctx.revert()
  })

  return { gsap, ScrollTrigger }
}
