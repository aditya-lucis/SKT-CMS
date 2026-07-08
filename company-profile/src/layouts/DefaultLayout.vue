<script setup>
import Navbar from '@/components/base/Navbar.vue'
import FooterSection from '@/components/sections/FooterSection.vue'
import ScrollProgress from '@/components/base/ScrollProgress.vue'
import CursorGlow from '@/components/base/CursorGlow.vue'
import BackToTop from '@/components/base/BackToTop.vue'
</script>

<template>
  <div class="relative min-h-screen bg-white text-slate-900 overflow-clip">
    <ScrollProgress />
    <CursorGlow />
    <Navbar />
    <main>
      <RouterView />
    </main>
    <FooterSection />
    <BackToTop />
  </div>
</template>
