<script setup>
import { RouterView, RouterLink, useRouter, useRoute } from 'vue-router'
import {
  LayoutDashboard, FileText, Users2, Layers, Image as ImageIcon, LogOut,
  Sparkles, Building2, Settings, Briefcase, GitBranch, Milestone as MilestoneIcon,
  MessagesSquare, Newspaper, HelpCircle, Award, Mail,
} from 'lucide-vue-next'
import { useAuthStore } from '@/stores/auth'
import { singletonConfigs } from '@/config/resourceConfigs'

import { ref, onMounted, onBeforeUnmount } from 'vue'

const router = useRouter()
const route = useRoute()
const auth = useAuthStore()

function logout() {
  auth.logout()
  router.push({ name: 'login' })
}

const contentNav = [
  { key: 'hero', label: 'Hero', icon: Sparkles },
  { key: 'about', label: 'About', icon: Building2 },
  { key: 'site_settings', label: 'Site Settings', icon: Settings },
]

const resourceNav = [
  { key: 'stats', label: 'Stats', icon: Award },
  { key: 'visionMission', label: 'Vision & Mission', icon: GitBranch },
  { key: 'services', label: 'Services', icon: Layers },
  { key: 'milestones', label: 'Milestones', icon: MilestoneIcon },
  { key: 'portfolio', label: 'Portfolio', icon: Briefcase },
  { key: 'processSteps', label: 'Process Steps', icon: GitBranch },
  { key: 'team', label: 'Team', icon: Users2 },
  { key: 'testimonials', label: 'Testimonials', icon: MessagesSquare },
  { key: 'blog', label: 'Blog', icon: Newspaper },
  { key: 'faqs', label: 'FAQ', icon: HelpCircle },
  { key: 'trustedBy', label: 'Trusted By', icon: ImageIcon },
]

const mobileOpen = ref(false)
const openDropdown = ref(null)

function toggleMobile() {
  mobileOpen.value = !mobileOpen.value
}

function toggleDropdown(name) {
  openDropdown.value = openDropdown.value === name ? null : name
}

function handleDocClick(e) {
  if (!e.target.closest('[data-dropdown-wrapper]')) {
    openDropdown.value = null
  }
}

onMounted(() => document.addEventListener('click', handleDocClick))
onBeforeUnmount(() => document.removeEventListener('click', handleDocClick))

function isActiveResource(key) {
  return route.name === 'resource' && route.params.resource === key
}
function isActiveSection(key) {
  return route.name === 'content' && route.params.section === key
}
</script>

<template>
  <div class="min-h-screen flex flex-col bg-slate-50">
    <!-- Top Navbar -->
    <header class="fixed inset-x-0 top-0 z-40 bg-white border-b shadow-sm">
      <div class="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <img src="/logo.png" alt="SKT" class="w-10 h-10 rounded-lg object-contain" />
          <div>
            <div class="font-display font-bold text-lg text-navy-900">SKT CMS</div>
            <div class="text-xs text-navy-500">Admin Panel</div>
          </div>
        </div>

        <nav class="hidden md:flex items-center gap-4">
          <RouterLink :to="{ name: 'dashboard' }"
                      class="px-3 py-2 text-sm font-medium text-navy-700 transition-colors"
                      :class="{ 'text-emerald-600 border-b-2 border-emerald-300': route.name === 'dashboard' }">Dashboard</RouterLink>

          <div class="relative" data-dropdown-wrapper="content">
            <button @click="toggleDropdown('content')"
                    class="px-3 py-2 text-sm font-medium transition-colors"
                    :class="{ 'text-emerald-600 border-b-2 border-emerald-300': route.name === 'content' || openDropdown === 'content' }">
              Page Content
            </button>
            <div v-show="openDropdown === 'content'" class="absolute left-0 mt-2 w-48 bg-white border rounded shadow-md p-2 z-50" data-dropdown-wrapper="content">
              <RouterLink v-for="item in contentNav" :key="item.key"
                          :to="{ name: 'content', params: { section: item.key } }"
                          class="flex items-center gap-2 px-2 py-2 text-sm text-navy-700 hover:bg-slate-50 rounded">
                <component :is="item.icon" :size="14" /> {{ item.label }}
              </RouterLink>
            </div>
          </div>

          <div class="relative" data-dropdown-wrapper="lists">
            <button @click="toggleDropdown('lists')"
                    class="px-3 py-2 text-sm font-medium transition-colors"
                    :class="{ 'text-emerald-600 border-b-2 border-emerald-300': route.name === 'resource' || openDropdown === 'lists' }">
              Content Lists
            </button>
            <div v-show="openDropdown === 'lists'" class="absolute left-0 mt-2 w-56 bg-white border rounded shadow-md p-2 z-50" data-dropdown-wrapper="lists">
              <RouterLink v-for="item in resourceNav" :key="item.key"
                          :to="{ name: 'resource', params: { resource: item.key } }"
                          class="flex items-center gap-2 px-2 py-2 text-sm text-navy-700 hover:bg-slate-50 rounded">
                <component :is="item.icon" :size="14" /> {{ item.label }}
              </RouterLink>
            </div>
          </div>
        </nav>

        <div class="flex items-center gap-3">
          <div class="hidden md:block text-sm text-navy-700">Masuk sebagai <b class="ml-2">{{ auth.state.username }}</b></div>
          <button @click="logout" class="px-3 py-2 rounded text-sm text-emerald-600 border border-emerald-100 hidden md:inline-flex items-center gap-2">Keluar</button>

          <!-- Mobile toggle -->
          <button @click="toggleMobile" class="md:hidden w-10 h-10 rounded-lg flex items-center justify-center bg-slate-100">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-navy-700" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
          </button>
        </div>
      </div>

      <!-- Mobile menu -->
      <div v-if="mobileOpen" class="md:hidden border-t bg-white">
        <div class="px-4 py-3 space-y-2">
          <RouterLink :to="{ name: 'dashboard' }" class="block px-3 py-2 rounded text-navy-700">Dashboard</RouterLink>
          <div>
            <div class="text-xs text-navy-500 uppercase font-semibold mb-1">Page Content</div>
            <RouterLink v-for="item in contentNav" :key="item.key"
                        :to="{ name: 'content', params: { section: item.key } }"
                        class="block px-3 py-2 text-navy-700 rounded">{{ item.label }}</RouterLink>
          </div>
          <div>
            <div class="text-xs text-navy-500 uppercase font-semibold mb-1 mt-2">Content Lists</div>
            <RouterLink v-for="item in resourceNav" :key="item.key"
                        :to="{ name: 'resource', params: { resource: item.key } }"
                        class="block px-3 py-2 text-navy-700 rounded">{{ item.label }}</RouterLink>
          </div>
          <RouterLink :to="{ name: 'contact-submissions' }" class="block px-3 py-2 text-navy-700 rounded">Pesan Masuk</RouterLink>
          <button @click="logout" class="w-full text-left px-3 py-2 rounded text-navy-700">Keluar</button>
        </div>
      </div>
    </header>

    <!-- Main content -->
    <main class="flex-1 overflow-y-auto pt-22">
      <div class="max-w-6xl mx-auto px-6 py-8">
        <RouterView />
      </div>
    </main>
  </div>
</template>
