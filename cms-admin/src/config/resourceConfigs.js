/**
 * One config object per repeatable resource. The generic ResourceManager page
 * + DynamicForm/DataTable components read this to render list columns and
 * create/edit forms without any resource-specific Vue code.
 *
 * Field types: text | textarea | number | select | image | tags | socials
 */
export const resourceConfigs = {
  stats: {
    title: 'Stats',
    subtitle: 'Angka pencapaian di section About (Projects Delivered, Global Clients, dst).',
    endpoint: '/api/stats',
    itemLabel: (item) => item.label,
    columns: ['label', 'value', 'suffix', 'icon'],
    fields: [
      { key: 'label', label: 'Label', type: 'text', required: true, placeholder: 'Projects Delivered' },
      { key: 'value', label: 'Value', type: 'number', required: true },
      { key: 'suffix', label: 'Suffix', type: 'text', placeholder: '+ / % / (kosongin kalau tidak ada)' },
      { key: 'icon', label: 'Icon (nama Lucide icon)', type: 'text', placeholder: 'Briefcase' },
    ],
  },

  visionMission: {
    title: 'Vision, Mission & Values',
    subtitle: 'Tiga kartu di section Vision & Mission.',
    endpoint: '/api/vision-mission',
    itemLabel: (item) => `${item.type} — ${item.title}`,
    columns: ['type', 'title'],
    fields: [
      { key: 'type', label: 'Type', type: 'select', options: ['Vision', 'Mission', 'Values'], required: true },
      { key: 'icon', label: 'Icon (nama Lucide icon)', type: 'text', placeholder: 'Eye' },
      { key: 'color', label: 'Warna tema', type: 'select', options: ['navy', 'emerald', 'cyan'] },
      { key: 'title', label: 'Title', type: 'text', required: true },
      { key: 'body', label: 'Body', type: 'textarea', rows: 4, required: true },
    ],
  },

  services: {
    title: 'Services',
    subtitle: '8 kartu layanan di section Services.',
    endpoint: '/api/services',
    itemLabel: (item) => item.title,
    columns: ['title', 'icon'],
    fields: [
      { key: 'icon', label: 'Icon (nama Lucide icon)', type: 'text', placeholder: 'Code2', required: true },
      { key: 'title', label: 'Title', type: 'text', required: true },
      { key: 'desc', label: 'Deskripsi', type: 'textarea', rows: 3, required: true },
      { key: 'points', label: 'Bullet points', type: 'tags', placeholder: 'Pisahkan dengan koma' },
      { key: 'gradient', label: 'Gradient class (Tailwind)', type: 'text', placeholder: 'from-navy-700 to-navy-500' },
    ],
  },

  milestones: {
    title: 'Milestones (Why Choose Us)',
    subtitle: 'Timeline pencapaian perusahaan dari tahun ke tahun.',
    endpoint: '/api/milestones',
    itemLabel: (item) => `${item.year} — ${item.title}`,
    columns: ['year', 'title'],
    fields: [
      { key: 'year', label: 'Tahun', type: 'text', required: true, placeholder: '2013' },
      { key: 'title', label: 'Title', type: 'text', required: true },
      { key: 'desc', label: 'Deskripsi', type: 'textarea', rows: 3, required: true },
    ],
  },

  portfolio: {
    title: 'Portfolio',
    subtitle: 'Project showcase di section Portfolio.',
    endpoint: '/api/portfolio',
    itemLabel: (item) => item.title,
    columns: ['title', 'category', 'size'],
    fields: [
      { key: 'title', label: 'Title', type: 'text', required: true },
      { key: 'category', label: 'Kategori', type: 'text', required: true, placeholder: 'FinTech' },
      { key: 'desc', label: 'Deskripsi', type: 'textarea', rows: 3, required: true },
      { key: 'image', label: 'Gambar', type: 'image', required: true },
      { key: 'tags', label: 'Tags', type: 'tags', placeholder: 'Vue, Go, Kubernetes' },
      { key: 'size', label: 'Ukuran kartu grid', type: 'select', options: ['normal', 'wide', 'tall'] },
    ],
  },

  processSteps: {
    title: 'Process Steps',
    subtitle: '7 langkah kerja di section Process.',
    endpoint: '/api/process-steps',
    itemLabel: (item) => `${item.num} — ${item.title}`,
    columns: ['num', 'title', 'icon'],
    fields: [
      { key: 'num', label: 'Nomor', type: 'text', required: true, placeholder: '01' },
      { key: 'title', label: 'Title', type: 'text', required: true },
      { key: 'icon', label: 'Icon (nama Lucide icon)', type: 'text', placeholder: 'Search' },
      { key: 'desc', label: 'Deskripsi', type: 'textarea', rows: 3, required: true },
    ],
  },

  team: {
    title: 'Team',
    subtitle: 'Anggota tim di section Team.',
    endpoint: '/api/team',
    itemLabel: (item) => item.name,
    columns: ['name', 'role'],
    fields: [
      { key: 'name', label: 'Nama', type: 'text', required: true },
      { key: 'role', label: 'Jabatan', type: 'text', required: true },
      { key: 'img', label: 'Foto', type: 'image', required: true },
      { key: 'bio', label: 'Bio singkat', type: 'textarea', rows: 2 },
      { key: 'socials', label: 'Social links', type: 'socials' },
    ],
  },

  testimonials: {
    title: 'Testimonials',
    subtitle: 'Testimoni klien di section Testimonials.',
    endpoint: '/api/testimonials',
    itemLabel: (item) => item.name,
    columns: ['name', 'role', 'rating'],
    fields: [
      { key: 'quote', label: 'Quote', type: 'textarea', rows: 4, required: true },
      { key: 'name', label: 'Nama', type: 'text', required: true },
      { key: 'role', label: 'Jabatan / Perusahaan', type: 'text', required: true },
      { key: 'img', label: 'Foto', type: 'image', required: true },
      { key: 'rating', label: 'Rating (1-5)', type: 'number' },
    ],
  },

  blog: {
    title: 'Blog Posts',
    subtitle: 'Artikel di section Blog.',
    endpoint: '/api/blog',
    itemLabel: (item) => item.title,
    columns: ['title', 'category', 'published'],
    fields: [
      { key: 'title', label: 'Judul', type: 'text', required: true },
      { key: 'slug', label: 'Slug (URL)', type: 'text', required: true, placeholder: 'judul-artikel' },
      { key: 'category', label: 'Kategori', type: 'text', required: true },
      { key: 'excerpt', label: 'Ringkasan', type: 'textarea', rows: 3, required: true },
      { key: 'content', label: 'Isi artikel (opsional)', type: 'textarea', rows: 8 },
      { key: 'image', label: 'Gambar cover', type: 'image', required: true },
      { key: 'author', label: 'Penulis', type: 'text' },
      { key: 'date', label: 'Tanggal (teks bebas)', type: 'text', placeholder: 'May 12, 2025' },
      { key: 'read_time', label: 'Estimasi baca', type: 'text', placeholder: '12 min' },
      { key: 'published', label: 'Tayangkan?', type: 'boolean' },
    ],
  },

  faqs: {
    title: 'FAQ',
    subtitle: 'Pertanyaan yang sering diajukan.',
    endpoint: '/api/faqs',
    itemLabel: (item) => item.q,
    columns: ['q'],
    fields: [
      { key: 'q', label: 'Pertanyaan', type: 'textarea', rows: 2, required: true },
      { key: 'a', label: 'Jawaban', type: 'textarea', rows: 4, required: true },
    ],
  },

  trustedBy: {
    title: 'Trusted By (Logos)',
    subtitle: 'Logo klien di marquee "Trusted By".',
    endpoint: '/api/trusted-by',
    itemLabel: (item) => item.name,
    columns: ['name'],
    fields: [
      { key: 'name', label: 'Nama perusahaan', type: 'text', required: true },
      { key: 'logo_url', label: 'Logo (opsional, kosongin buat text-only)', type: 'image' },
    ],
  },
}

export const singletonConfigs = {
  hero: {
    title: 'Hero Section',
    subtitle: 'Konten utama di paling atas halaman.',
    section: 'hero',
    fields: [
      { key: 'badge', label: 'Badge text', type: 'text', placeholder: 'Trusted by 180+ global clients' },
      { key: 'headline_1', label: 'Headline baris 1', type: 'text' },
      { key: 'headline_2', label: 'Headline baris 2', type: 'text' },
      { key: 'headline_highlight', label: 'Headline highlight (warna beda)', type: 'text' },
      { key: 'subheadline', label: 'Subheadline', type: 'textarea', rows: 2 },
      { key: 'cta_primary_label', label: 'Tombol utama - label', type: 'text' },
      { key: 'cta_primary_href', label: 'Tombol utama - link', type: 'text' },
      { key: 'cta_secondary_label', label: 'Tombol kedua - label', type: 'text' },
      { key: 'cta_secondary_href', label: 'Tombol kedua - link', type: 'text' },
      { key: 'background_image', label: 'Background image', type: 'image' },
    ],
  },
  about: {
    title: 'About Section',
    subtitle: 'Konten di section About.',
    section: 'about',
    fields: [
      { key: 'eyebrow', label: 'Eyebrow text', type: 'text', placeholder: 'About Nexus' },
      { key: 'title', label: 'Title', type: 'text' },
      { key: 'highlight_word', label: 'Highlight word (warna beda di title)', type: 'text' },
      { key: 'subtitle', label: 'Subtitle', type: 'textarea', rows: 3 },
      { key: 'office_image', label: 'Foto kantor', type: 'image' },
      { key: 'highlights', label: 'Highlight list (checklist)', type: 'tags' },
      { key: 'badge_text', label: 'Badge kecil di foto', type: 'text', placeholder: '12+ Years of Excellence' },
    ],
  },
  site_settings: {
    title: 'Site Settings',
    subtitle: 'Info perusahaan, kontak, dan SEO — dipakai di Header, Footer, & Contact.',
    section: 'site_settings',
    fields: [
      { key: 'company_name', label: 'Nama perusahaan', type: 'text' },
      { key: 'tagline', label: 'Tagline', type: 'text' },
      { key: 'email', label: 'Email', type: 'text' },
      { key: 'phone', label: 'Telepon', type: 'text' },
      { key: 'address', label: 'Alamat', type: 'text' },
      { key: 'meta_title', label: 'SEO Meta Title', type: 'text' },
      { key: 'meta_description', label: 'SEO Meta Description', type: 'textarea', rows: 2 },
    ],
  },
}
