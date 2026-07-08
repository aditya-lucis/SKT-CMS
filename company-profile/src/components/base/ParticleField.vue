<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const canvas = ref(null)
let ctx, animId, particles = [], observer

  const props = defineProps({
  count: { type: Number, default: 60 },
  color: { type: String, default: '70, 173, 100' }, // RGB
  speed: { type: Number, default: 0.25 },
  linkDistance: { type: Number, default: 130 },
  opacity: { type: Number, default: 0.7 },
  radius: { type: Number, default: 2.2 },
})

const init = () => {
  const c = canvas.value
  if (!c) return
  ctx = c.getContext('2d')
  resize()
  particles = []
  for (let i = 0; i < props.count; i++) {
    particles.push({
      x: Math.random() * c.width,
      y: Math.random() * c.height,
      vx: (Math.random() - 0.5) * props.speed,
      vy: (Math.random() - 0.5) * props.speed,
      r: Math.random() * props.radius + 0.8,
      o: Math.random() * 0.5 + props.opacity * 0.5,
    })
  }
  if (!observer) {
    observer = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) animate()
        else if (animId) { cancelAnimationFrame(animId); animId = null }
      })
    }, { threshold: 0.05 })
    observer.observe(c)
  }
}

const resize = () => {
  const c = canvas.value
  if (!c) return
  const rect = c.parentElement.getBoundingClientRect()
  c.width = rect.width
  c.height = rect.height
}

const animate = () => {
  const c = canvas.value
  if (!c || !ctx) return
  ctx.clearRect(0, 0, c.width, c.height)
  particles.forEach((p, i) => {
    p.x += p.vx; p.y += p.vy
    if (p.x < 0 || p.x > c.width) p.vx *= -1
    if (p.y < 0 || p.y > c.height) p.vy *= -1
    ctx.beginPath()
    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2)
    ctx.fillStyle = `rgba(${props.color}, ${p.o})`
    ctx.fill()
    // Links
    for (let j = i + 1; j < particles.length; j++) {
      const q = particles[j]
      const dx = p.x - q.x, dy = p.y - q.y
      const d = Math.hypot(dx, dy)
      if (d < props.linkDistance) {
        ctx.beginPath()
        ctx.moveTo(p.x, p.y)
        ctx.lineTo(q.x, q.y)
        ctx.strokeStyle = `rgba(${props.color}, ${(1 - d / props.linkDistance) * 0.15})`
        ctx.lineWidth = 0.6
        ctx.stroke()
      }
    }
  })
  animId = requestAnimationFrame(animate)
}

const onResize = () => { resize(); init() }

onMounted(() => {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
  init()
  window.addEventListener('resize', onResize)
})
onBeforeUnmount(() => {
  window.removeEventListener('resize', onResize)
  if (animId) cancelAnimationFrame(animId)
  if (observer) observer.disconnect()
})
</script>

<template>
  <canvas ref="canvas" class="absolute inset-0 w-full h-full pointer-events-none" aria-hidden="true"></canvas>
</template>
