# Nexus Technology — Company Profile + CMS

Tiga project yang saling terhubung:

```
company-profile/   Public website (Vue 3 + Vite + Tailwind v4) — full dynamic, narik semua konten dari API
cms-backend/        FastAPI + MySQL — REST API + auth + upload gambar
cms-admin/           Admin panel (Vue 3 + Vite + Tailwind v4) — buat kelola konten
```

Alurnya: **Admin edit konten di `cms-admin` → tersimpan di MySQL lewat `cms-backend` → otomatis muncul di `company-profile`** (public site fetch API sekali saat load, tanpa perlu rebuild/redeploy).

---

## 1. Setup Database (MySQL/MariaDB)

```sql
CREATE DATABASE nexus_cms CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'nexus_user'@'localhost' IDENTIFIED BY 'ganti_password_ini';
GRANT ALL PRIVILEGES ON nexus_cms.* TO 'nexus_user'@'localhost';
FLUSH PRIVILEGES;
```

## 2. Jalankan Backend (`cms-backend`)

```bash
cd cms-backend
python3 -m venv venv
./venv/bin/pip install -r requirements.txt

cp .env.example .env   # sesuaikan DATABASE_URL, SECRET_KEY, ADMIN_USERNAME/PASSWORD

./venv/bin/python seed.py          # isi database dengan konten awal (sekali saja)
./venv/bin/uvicorn main:app --reload --port 8000
```

Backend jalan di `http://localhost:8000`. Dokumentasi API otomatis di `http://localhost:8000/docs`.

Admin default (bisa diganti di `.env` sebelum start pertama kali):
- Username: `admin`
- Password: `admin123`

**⚠️ Ganti password default ini sebelum deploy ke production.**

## 3. Jalankan Admin Panel (`cms-admin`)

```bash
cd cms-admin
npm install
cp .env.example .env   # VITE_API_BASE_URL -> alamat backend
npm run dev             # http://localhost:5174
```

## 4. Jalankan Public Site (`company-profile`)

```bash
cd company-profile
npm install
cp .env.example .env   # VITE_API_BASE_URL -> alamat backend
npm run dev             # http://localhost:3000
```

---

## Yang bisa diatur dari CMS

| Halaman admin | Isi |
|---|---|
| Hero | Badge, headline, subheadline, CTA, background image |
| About | Eyebrow, title, subtitle, foto kantor, highlight list |
| Site Settings | Nama perusahaan, tagline, email, telepon, alamat, SEO |
| Stats | Angka pencapaian (Projects, Clients, dst) |
| Vision & Mission | 3 kartu Vision/Mission/Values |
| Services | 8 kartu layanan |
| Milestones | Timeline "Why Choose Us" |
| Portfolio | Project showcase (dengan upload gambar) |
| Process Steps | 7 langkah kerja |
| Team | Anggota tim (foto, bio, social links) |
| Testimonials | Testimoni klien |
| Blog | Artikel blog |
| FAQ | Pertanyaan umum |
| Trusted By | Logo/nama klien di marquee |
| Pesan Masuk | Submission dari form contact di public site |

Semua gambar diupload lewat Admin Panel (media library bawaan), disimpan di `cms-backend/app/uploads/` dan disajikan via `/uploads/...`.

## Known limitations (v1)

- Response format API masih raw JSON per-resource (belum pakai envelope `{success, message, data}`)
- State management admin panel masih composable manual (belum Pinia)
- Auth hanya access token (belum ada refresh token)
- Migration DB pakai `create_all()` (belum Alembic)
- Reorder resource pakai tombol naik/turun (belum drag-and-drop)
- Social links di Site Settings belum ada UI-nya (datanya ada di DB, tinggal ditambah field di admin)

> Poin-poin di atas adalah scope retrofit fase berikutnya sesuai standar arsitektur yang sudah disepakati (repository pattern, service layer, Pinia, dst).
