<script setup>
import HeroSection from '@/components/sections/HeroSection.vue'
import TrustedBySection from '@/components/sections/TrustedBySection.vue'
import AboutSection from '@/components/sections/AboutSection.vue'
import VisionMissionSection from '@/components/sections/VisionMissionSection.vue'
import ServicesSection from '@/components/sections/ServicesSection.vue'
import WhyChooseUsSection from '@/components/sections/WhyChooseUsSection.vue'
import PortfolioSection from '@/components/sections/PortfolioSection.vue'
import ProcessSection from '@/components/sections/ProcessSection.vue'
import TeamSection from '@/components/sections/TeamSection.vue'
import TestimonialsSection from '@/components/sections/TestimonialsSection.vue'
import BlogSection from '@/components/sections/BlogSection.vue'
import FAQSection from '@/components/sections/FAQSection.vue'
import ContactSection from '@/components/sections/ContactSection.vue'

const goContact = () => {
  if (window.__lenis) window.__lenis.scrollTo('#contact', { offset: -80, duration: 1.4 })
  else document.querySelector('#contact')?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <HeroSection @contact="goContact" />
  <TrustedBySection />
  <AboutSection @contact="goContact" />
  <VisionMissionSection />
  <ServicesSection />
  <WhyChooseUsSection />
  <PortfolioSection />
  <ProcessSection />
  <TeamSection @contact="goContact" />
  <TestimonialsSection />
  <BlogSection />
  <FAQSection />
  <ContactSection />
</template>
