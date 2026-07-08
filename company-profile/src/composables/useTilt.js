import { onMounted, onBeforeUnmount } from 'vue'

/**
 * Tilt effect on hover — element rotates slightly toward cursor in 3D.
 */
export function useTilt(max = 8) {
  let el = null

  const bind = (node) => {
    el = node
    if (!el) return
    if (window.matchMedia('(hover: none)').matches) return
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
    el.style.transition = 'transform 0.4s cubic-bezier(0.16,1,0.3,1)'
    el.style.transformStyle = 'preserve-3d'
    el.addEventListener('mousemove', onMove)
    el.addEventListener('mouseleave', onLeave)
  }

  const onMove = (e) => {
    const rect = el.getBoundingClientRect()
    const px = (e.clientX - rect.left) / rect.width - 0.5
    const py = (e.clientY - rect.top) / rect.height - 0.5
    el.style.transform = `perspective(900px) rotateY(${px * max * 2}deg) rotateX(${-py * max * 2}deg) translateZ(8px)`
  }
  const onLeave = () => {
    el.style.transform = 'perspective(900px) rotateY(0) rotateX(0) translateZ(0)'
  }

  onBeforeUnmount(() => {
    if (el) {
      el.removeEventListener('mousemove', onMove)
      el.removeEventListener('mouseleave', onLeave)
    }
  })

  return { bind }
}
