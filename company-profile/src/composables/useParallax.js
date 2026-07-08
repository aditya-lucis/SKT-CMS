/**
 * useParallax — auto-scanning, scroll-linked parallax driven by data attributes.
 * Mirrors the useReveal() convention: sprinkle attributes in markup, call
 * useParallax() once (e.g. in App.vue), and every matching element gets a
 * buttery-smooth GSAP ScrollTrigger scrub tween. No per-component JS needed.
 *
 * Markup:
 *   <section data-parallax-scope>              <!-- optional explicit scope -->
 *     <div data-parallax
 *          data-parallax-speed="0.2"            <!-- drift amount, +/- for direction -->
 *          data-parallax-scale="1.15"           <!-- optional end scale (zoom) -->
 *          data-parallax-rotate="8">            <!-- optional end rotation (deg) -->
 *       ...
 *     </div>
 *   </section>
 *
 * Scope resolution: closest [data-parallax-scope] ancestor, else parentElement.
 * The scope element defines the scroll range the parallax tween scrubs across
 * (top-of-scope hits bottom-of-viewport -> bottom-of-scope hits top-of-viewport).
 */
import { onMounted, onBeforeUnmount } from 'vue'
import { gsap } from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

const REDUCED_MOTION = typeof window !== 'undefined'
  && window.matchMedia('(prefers-reduced-motion: reduce)').matches

const activeTriggers = new Set()
let loadRefreshBound = false

function buildOne(el) {
  const speed = parseFloat(el.dataset.parallaxSpeed ?? '0.15') || 0.15
  const rotateTo = el.dataset.parallaxRotate ? parseFloat(el.dataset.parallaxRotate) : null
  const scaleTo = el.dataset.parallaxScale ? parseFloat(el.dataset.parallaxScale) : null
  const scopeEl = el.closest('[data-parallax-scope]') || el.parentElement || el

  const fromVars = { yPercent: -speed * 100, ease: 'none' }
  const toVars = { yPercent: speed * 100, ease: 'none' }

  if (rotateTo !== null) {
    fromVars.rotate = -rotateTo
    toVars.rotate = rotateTo
  }
  if (scaleTo !== null) {
    fromVars.scale = 1
    toVars.scale = scaleTo
  }

  toVars.scrollTrigger = {
    trigger: scopeEl,
    start: 'top bottom',
    end: 'bottom top',
    scrub: 0.65,
  }

  const tween = gsap.fromTo(el, fromVars, toVars)
  if (tween.scrollTrigger) activeTriggers.add(tween.scrollTrigger)
}

function scanAndBuild() {
  document.querySelectorAll('[data-parallax]:not([data-parallax-init])').forEach((el) => {
    el.setAttribute('data-parallax-init', '')
    buildOne(el)
  })
}

export function useParallax() {
  onMounted(() => {
    if (REDUCED_MOTION) return
    scanAndBuild()

    if (!loadRefreshBound) {
      loadRefreshBound = true
      window.addEventListener('load', () => ScrollTrigger.refresh())
    }
  })

  onBeforeUnmount(() => {
    // Single-page app: triggers persist intentionally across route/section
    // lifecycles, cleaned up implicitly on full page unload.
  })
}

/**
 * Call after dynamically-added content mounts (e.g. late-loaded images,
 * filtered lists) so newly rendered [data-parallax] elements get wired up.
 */
export function refreshParallax() {
  if (REDUCED_MOTION) return
  scanAndBuild()
  ScrollTrigger.refresh()
}
