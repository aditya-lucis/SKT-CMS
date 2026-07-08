<script setup>
import { RouterView, RouterLink, useRouter, useRoute } from 'vue-router'
import {
  LayoutDashboard, FileText, Users2, Layers, Image as ImageIcon, LogOut,
  Sparkles, Building2, Settings, Briefcase, GitBranch, Milestone as MilestoneIcon,
  MessagesSquare, Newspaper, HelpCircle, Award, Mail,
} from 'lucide-vue-next'
import { useAuthStore } from '@/stores/auth'
import { singletonConfigs } from '@/config/resourceConfigs'

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

function isActiveResource(key) {
  return route.name === 'resource' && route.params.resource === key
}
function isActiveSection(key) {
  return route.name === 'content' && route.params.section === key
}
</script>

<template>
  <div class="min-h-screen flex">
    <!-- Sidebar -->
    <aside class="w-64 shrink-0 bg-navy-900 text-white flex flex-col">
      <div class="px-5 py-5 flex items-center gap-2.5 border-b border-white/10">
        <div class="w-8 h-8 rounded-lg flex items-center justify-center font-display font-bold text-sm"
             style="background: linear-gradient(135deg, #46ad64, #22d3ee);">N</div>
        <div class="leading-none">
          <div class="font-display font-bold text-sm">Nexus CMS</div>
          <div class="text-[10px] text-white/40 uppercase tracking-wide mt-0.5">Admin Panel</div>
        </div>
      </div>

      <nav class="flex-1 overflow-y-auto px-3 py-4 space-y-6">
        <div>
          <RouterLink :to="{ name: 'dashboard' }"
                      class="flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors"
                      :class="route.name === 'dashboard' ? 'bg-white/10 text-white' : 'text-white/60 hover:text-white hover:bg-white/5'">
            <LayoutDashboard :size="16" /> Dashboard
          </RouterLink>
        </div>

        <div>
          <div class="px-3 text-[10px] font-bold uppercase tracking-wider text-white/30 mb-1.5">Page Content</div>
          <RouterLink v-for="item in contentNav" :key="item.key"
                      :to="{ name: 'content', params: { section: item.key } }"
                      class="flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors"
                      :class="isActiveSection(item.key) ? 'bg-white/10 text-white' : 'text-white/60 hover:text-white hover:bg-white/5'">
            <component :is="item.icon" :size="16" /> {{ item.label }}
          </RouterLink>
        </div>

        <div>
          <div class="px-3 text-[10px] font-bold uppercase tracking-wider text-white/30 mb-1.5">Content Lists</div>
          <RouterLink v-for="item in resourceNav" :key="item.key"
                      :to="{ name: 'resource', params: { resource: item.key } }"
                      class="flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors"
                      :class="isActiveResource(item.key) ? 'bg-white/10 text-white' : 'text-white/60 hover:text-white hover:bg-white/5'">
            <component :is="item.icon" :size="16" /> {{ item.label }}
          </RouterLink>
        </div>

        <div>
          <div class="px-3 text-[10px] font-bold uppercase tracking-wider text-white/30 mb-1.5">Lainnya</div>
          <RouterLink :to="{ name: 'contact-submissions' }"
                      class="flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors"
                      :class="route.name === 'contact-submissions' ? 'bg-white/10 text-white' : 'text-white/60 hover:text-white hover:bg-white/5'">
            <Mail :size="16" /> Pesan Masuk
          </RouterLink>
        </div>
      </nav>

      <div class="px-3 py-4 border-t border-white/10">
        <div class="px-3 text-xs text-white/40 mb-2">Masuk sebagai <b class="text-white/70">{{ auth.state.username }}</b></div>
        <button @click="logout" class="flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm font-medium text-white/60 hover:text-white hover:bg-white/5 w-full transition-colors">
          <LogOut :size="16" /> Keluar
        </button>
      </div>
    </aside>

    <!-- Main content -->
    <main class="flex-1 overflow-y-auto">
      <div class="max-w-5xl mx-auto px-8 py-8">
        <RouterView />
      </div>
    </main>
  </div>
</template>
