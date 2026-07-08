<script setup>
defineProps({
  variant: { type: String, default: 'light' }, // 'light' | 'dark'
})
</script>

<template>
  <div class="absolute inset-0 overflow-hidden pointer-events-none" aria-hidden="true">
    <!-- Aurora blobs -->
    <div data-parallax data-parallax-speed="0.22" class="aurora-blob w-[50vw] h-[50vw] -top-[15%] -left-[10%] animate-float-slow"
         :style="`background: radial-gradient(circle, ${variant === 'dark' ? 'rgba(70,173,100,0.4)' : 'rgba(70,173,100,0.25)'}, transparent 65%);`"></div>
    <div data-parallax data-parallax-speed="-0.18" data-parallax-rotate="8" class="aurora-blob w-[45vw] h-[45vw] top-[20%] -right-[15%] animate-float"
         :style="`background: radial-gradient(circle, ${variant === 'dark' ? 'rgba(34,211,238,0.35)' : 'rgba(34,211,238,0.22)'}, transparent 65%); animation-delay: -3s;`"></div>
    <div data-parallax data-parallax-speed="0.28" class="aurora-blob w-[40vw] h-[40vw] bottom-[-10%] left-[30%] animate-float-slow"
         :style="`background: radial-gradient(circle, ${variant === 'dark' ? 'rgba(139,92,246,0.3)' : 'rgba(139,92,246,0.18)'}, transparent 65%); animation-delay: -6s;`"></div>
    <slot />
  </div>
</template>
