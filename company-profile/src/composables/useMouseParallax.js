import { onMounted, onBeforeUnmount, ref } from 'vue'

/**
 * Mouse parallax for floating elements.
 * Returns a ref to attach to a parent and a function to register children with depth.
 *
 * Usage:
 *   const { register, containerRef } = useMouseParallax()
 *   <div ref="containerRef">
 *     <img :ref="el => register(el, 0.04)" />
 *   </div>
 */
export function useMouseParallax(maxDepth = 0.15) {
  const containerRef = ref(null)
  const items = []
  let rafId = null
  let targetX = 0, targetY = 0
  let currentX = 0, currentY = 0

  const register = (el, depth = 0.05) => {
    if (el && !items.find((i) => i.el === el)) {
      items.push({ el, depth: Math.min(depth, maxDepth) })
    }
  }

  const onMove = (e) => {
    if (!items.length) return
    const w = window.innerWidth
    const h = window.innerHeight
    targetX = (e.clientX / w - 0.5) * 2
    targetY = (e.clientY / h - 0.5) * 2
    if (!rafId) tick()
  }

  const tick = () => {
    currentX += (targetX - currentX) * 0.08
    currentY += (targetY - currentY) * 0.08
    items.forEach(({ el, depth }) => {
      const tx = currentX * depth * 200
      const ty = currentY * depth * 200
      el.style.transform = `translate3d(${tx}px, ${ty}px, 0)`
    })
    if (Math.abs(targetX - currentX) > 0.001 || Math.abs(targetY - currentY) > 0.001) {
      rafId = requestAnimationFrame(tick)
    } else {
      rafId = null
    }
  }

  onMounted(() => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
    if (window.matchMedia('(hover: none)').matches) return
    window.addEventListener('mousemove', onMove, { passive: true })
  })

  onBeforeUnmount(() => {
    window.removeEventListener('mousemove', onMove)
    if (rafId) cancelAnimationFrame(rafId)
  })

  return { containerRef, register }
}
