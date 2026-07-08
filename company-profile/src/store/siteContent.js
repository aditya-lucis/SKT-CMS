import { reactive } from 'vue'
import { api } from '@/lib/api'

const state = reactive({
  loaded: false,
  error: null,
  data: {
    site_settings: {},
    hero: {},
    about: {},
    stats: [],
    vision_mission: [],
    services: [],
    milestones: [],
    portfolio: [],
    process_steps: [],
    team: [],
    testimonials: [],
    blog_posts: [],
    faqs: [],
    trusted_by: [],
  },
})

let inflight = null

export function useSiteContent() {
  async function fetchContent() {
    if (state.loaded) return state.data
    if (inflight) return inflight

    inflight = api.get('/api/public/content')
      .then(({ data }) => {
        // Mutate existing nested objects/arrays in place (rather than
        // replacing them) so any component that destructured e.g.
        // `const hero = state.data.hero` at setup time keeps observing
        // the same reactive reference once this resolves.
        for (const key of Object.keys(state.data)) {
          const incoming = data[key]
          if (Array.isArray(state.data[key])) {
            state.data[key].splice(0, state.data[key].length, ...(incoming || []))
          } else {
            Object.assign(state.data[key], incoming || {})
          }
        }
        state.loaded = true
        return state.data
      })
      .catch((err) => {
        state.error = err
        console.error(
          '[siteContent] Gagal fetch /api/public/content dari',
          api.defaults.baseURL,
          '\nCek: backend jalan? VITE_API_BASE_URL benar? CORS_ORIGINS di backend .env sudah termasuk origin ini?',
          err
        )
        throw err
      })
      .finally(() => {
        inflight = null
      })

    return inflight
  }

  return { state, fetchContent }
}
