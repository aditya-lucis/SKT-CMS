import * as Icons from 'lucide-vue-next'

/**
 * Resolves an icon name string (e.g. "Code2", stored by the CMS) to its
 * lucide-vue-next component. Falls back to a neutral icon if the name
 * doesn't exist, so a typo in the CMS never breaks the page.
 */
export function resolveIcon(name, fallback = 'Circle') {
  return Icons[name] || Icons[fallback] || Icons.Circle
}
