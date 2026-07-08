import { onMounted, onBeforeUnmount } from 'vue'
import Lenis from 'lenis'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

let lenisInstance = null
let tickerFn = null

export function useLenis() {
  const init = () => {
    if (lenisInstance) return lenisInstance

    lenisInstance = new Lenis({
      duration: 1.15,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true,
      wheelMultiplier: 1,
      touchMultiplier: 1.5,
      lerp: 0.1,
    })

    // Keep every GSAP ScrollTrigger (incl. all scroll-linked parallax)
    // perfectly in sync with Lenis's smoothed scroll position.
    lenisInstance.on('scroll', ScrollTrigger.update)

    // Drive Lenis off GSAP's ticker instead of a separate rAF loop so both
    // stay on the same frame — this is what removes parallax jitter/lag.
    tickerFn = (time) => lenisInstance.raf(time * 1000)
    gsap.ticker.add(tickerFn)
    gsap.ticker.lagSmoothing(0)

    // expose globally for manual control
    window.__lenis = lenisInstance

    return lenisInstance
  }

  onMounted(() => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
    init()
  })

  onBeforeUnmount(() => {
    if (tickerFn) {
      gsap.ticker.remove(tickerFn)
      tickerFn = null
    }
    if (lenisInstance) {
      lenisInstance.destroy()
      lenisInstance = null
    }
  })

  return {
    get lenis() { return lenisInstance },
    scrollTo: (target, opts = {}) => {
      if (lenisInstance) lenisInstance.scrollTo(target, { offset: -80, duration: 1.2, ...opts })
      else if (typeof target === 'string') {
        const el = document.querySelector(target)
        if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' })
      }
    },
    stop: () => lenisInstance?.stop(),
    start: () => lenisInstance?.start(),
  }
}
