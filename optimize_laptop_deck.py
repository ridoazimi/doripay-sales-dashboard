import json

with open('/opt/data/doripay-sales-dashboard/records.json') as f:
    records = json.load(f)

json_data = json.dumps(records)

html = """<!DOCTYPE html>
<html lang="id" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Doripay Strategic Meeting | Evaluasi & Arah Baru Perusahaan</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            premium: {
              950: '#07090e',
              900: '#0c1017',
              850: '#111722',
              800: '#172030',
              750: '#1d273a',
              700: '#233047',
              600: '#334464'
            },
            steelblue: {
              400: '#5e9edc',
              500: '#4682b4',
              600: '#316999',
              700: '#25527a'
            }
          }
        }
      }
    }
  </script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: #07090e;
      color: #e2e8f0;
      -webkit-font-smoothing: antialiased;
    }
    .font-mono {
      font-family: 'JetBrains Mono', monospace;
    }
    .custom-scroll::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    .custom-scroll::-webkit-scrollbar-track {
      background: #0c1017;
    }
    .custom-scroll::-webkit-scrollbar-thumb {
      background: #233047;
      border-radius: 3px;
    }
  </style>
</head>
<body class="bg-premium-950 text-slate-100 h-screen overflow-hidden selection:bg-steelblue-500 selection:text-white flex flex-col">

  <!-- TOP APP BAR -->
  <header class="h-14 border-b border-premium-800 bg-premium-950/95 px-6 flex items-center justify-between gap-4 select-none shrink-0">
    <div class="flex items-center gap-3">
      <div class="w-8 h-8 rounded-lg bg-steelblue-500/20 border border-steelblue-400/40 flex items-center justify-center font-bold text-steelblue-300 font-mono text-sm shadow-sm">
        DP
      </div>
      <div>
        <div class="flex items-center gap-2">
          <h1 class="text-sm font-bold tracking-tight text-white">Doripay Executive Briefing</h1>
          <span class="text-[11px] px-2 py-0.5 rounded bg-premium-850 border border-premium-800 text-steelblue-300 font-mono">Board Deck (16:9 Laptop)</span>
        </div>
        <p class="text-[11px] text-slate-500 hidden sm:block">Pertemuan Evaluasi Lapangan & Arah Strategis Bersama Dewan Komisaris</p>
      </div>
    </div>

    <!-- CONTROLS RIGHT -->
    <div class="flex items-center gap-3">
      <div class="hidden md:flex items-center gap-2 text-xs font-mono text-slate-400 bg-premium-900/80 px-3 py-1.5 rounded-lg border border-premium-800">
        <span>Navigasi:</span>
        <kbd class="px-1.5 py-0.5 rounded bg-premium-800 text-slate-300 border border-premium-700">←</kbd>
        <kbd class="px-1.5 py-0.5 rounded bg-premium-800 text-slate-300 border border-premium-700">→</kbd>
        <kbd class="px-1.5 py-0.5 rounded bg-premium-800 text-slate-300 border border-premium-700">F11</kbd>
      </div>

      <div class="flex items-center gap-1 bg-premium-900 p-1 rounded-lg border border-premium-800 text-xs font-medium">
        <button id="btn-mode-slide" onclick="switchView('slide')" class="px-3 py-1.5 rounded transition-all flex items-center gap-1.5 bg-steelblue-500 text-white font-semibold shadow-sm">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"/></svg>
          <span>Slide Deck</span>
        </button>
        <button id="btn-mode-dash" onclick="switchView('dash')" class="px-3 py-1.5 rounded transition-all flex items-center gap-1.5 text-slate-400 hover:text-white">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
          <span>Data Lapangan (47)</span>
        </button>
      </div>
    </div>
  </header>

  <!-- ======================================================== -->
  <!-- MAIN SLIDE PRESENTATION (LAPTOP 16:9 VIEWPORT)           -->
  <!-- ======================================================== -->
  <main id="view-slide" class="flex-1 w-full max-w-6xl mx-auto p-4 md:p-6 flex flex-col justify-center select-none overflow-hidden">
    
    <div id="slide-wrapper" class="w-full bg-premium-900 border border-premium-800 rounded-2xl p-6 md:p-8 flex flex-col justify-between shadow-2xl relative min-h-[500px] lg:min-h-[540px]">
      
      <!-- SUB-HEADER SLIDE -->
      <div class="flex items-center justify-between border-b border-premium-800 pb-3 mb-4 text-xs font-mono">
        <div class="flex items-center gap-2 text-steelblue-400 font-medium">
          <span class="text-slate-500 uppercase">Executive Session</span>
          <span class="text-slate-700">/</span>
          <span id="slide-topic" class="text-slate-200">Evaluasi & Arah Baru</span>
        </div>
        <div class="flex items-center gap-3">
          <span class="text-slate-500 text-[11px] hidden md:inline">Doripay Corporate Governance</span>
          <div id="slide-counter" class="text-slate-300 font-bold bg-premium-950 px-2.5 py-1 rounded-md border border-premium-800 text-xs">
            1 / 6
          </div>
        </div>
      </div>

      <!-- SLIDE PAGES CONTENT -->
      <div id="slide-content" class="flex-1 flex flex-col justify-center">

        <!-- SLIDE 1: COVER -->
        <div class="slide-page" data-page="1" data-topic="Evaluasi Penetrasi & Keputusan Strategis">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-md bg-steelblue-500/10 border border-steelblue-500/30 text-steelblue-400 text-xs font-medium mb-3">
            <span class="w-2 h-2 rounded-full bg-steelblue-400 animate-pulse"></span>
            Rapat Dewan Direksi & Komisaris
          </div>
          <h2 class="text-2xl lg:text-4xl font-extrabold text-white tracking-tight leading-tight mb-3">
            Evaluasi Lapangan Doripay: <br>
            <span class="text-steelblue-400">Pertanggungjawaban, Realitas Pasar & Solusi Pivot</span>
          </h2>
          <p class="text-sm lg:text-base text-slate-300 max-w-4xl leading-relaxed mb-6">
            Paparan transparan hasil uji lapangan 47 konter di Salatiga, kalkulasi dingin biaya sales, akuntabilitas founder, serta pengambilan keputusan strategis: <strong>bertahan dengan perang modal</strong> atau <strong>mengamankan kas perusahaan untuk pivot ke lini Layanan Digital & AI ber-margin tebal</strong>.
          </p>

          <div class="grid grid-cols-2 md:grid-cols-4 gap-3 font-mono text-xs">
            <div class="p-3.5 bg-premium-950 rounded-xl border border-premium-800">
              <div class="text-slate-500 font-medium">Konter Diaudit</div>
              <div class="text-2xl font-bold text-white mt-1">47 Konter</div>
              <div class="text-[10px] text-slate-400 mt-0.5">4 Kecamatan Lapangan</div>
            </div>
            <div class="p-3.5 bg-premium-950 rounded-xl border border-premium-800">
              <div class="text-slate-500 font-medium">Tingkat Penolakan</div>
              <div class="text-2xl font-bold text-rose-400 mt-1">70.2%</div>
              <div class="text-[10px] text-rose-300/80 mt-0.5">33 Konter Menolak</div>
            </div>
            <div class="p-3.5 bg-premium-950 rounded-xl border border-premium-800">
              <div class="text-slate-500 font-medium">Biaya Sales Tes</div>
              <div class="text-2xl font-bold text-amber-400 mt-1">Rp 80rb / hari</div>
              <div class="text-[10px] text-amber-300/80 mt-0.5">Total Tes Rp 240.000</div>
            </div>
            <div class="p-3.5 bg-premium-950 rounded-xl border border-premium-800">
              <div class="text-slate-500 font-medium">Aset Teknologi</div>
              <div class="text-2xl font-bold text-steelblue-400 mt-1">Rp 30 Juta</div>
              <div class="text-[10px] text-steelblue-300/80 mt-0.5">Sistem Siap & Aman</div>
            </div>
          </div>
        </div>

        <!-- SLIDE 2: REALITAS PASAR & SALES FUNNEL -->
        <div class="slide-page hidden" data-page="2" data-topic="Fakta Riil Pasar Konter Salatiga">
          <div class="flex items-center justify-between mb-2">
            <h3 class="text-xl lg:text-2xl font-bold text-white">Hasil Audit Lapangan: Pasar Komoditas Ekstrem</h3>
            <span class="text-xs font-mono text-steelblue-400 bg-premium-950 px-2.5 py-1 rounded border border-premium-800">47 Respon Konter</span>
          </div>
          <p class="text-xs lg:text-sm text-slate-300 mb-4">
            Kanvasing di 4 kecamatan (Sidomukti, Argomulyo, Tingkir, Sidorejo) menghasilkan data corong konversi riil:
          </p>

          <div class="grid grid-cols-1 md:grid-cols-12 gap-4">
            <!-- FUNNEL METRICS -->
            <div class="md:col-span-5 space-y-2.5 font-mono text-xs">
              <div class="p-3 rounded-xl bg-premium-950 border border-premium-800 flex items-center justify-between">
                <div>
                  <span class="text-slate-400 block text-[11px]">Total Kunjungan Toko</span>
                  <span class="text-base font-bold text-white">47 Konter</span>
                </div>
                <span class="text-xs px-2 py-0.5 rounded bg-premium-850 text-slate-300 border border-premium-750">100% Target</span>
              </div>
              <div class="p-3 rounded-xl bg-rose-950/30 border border-rose-900/50 flex items-center justify-between">
                <div>
                  <span class="text-rose-300 block text-[11px]">Ditolak di Tempat</span>
                  <span class="text-base font-bold text-rose-400">33 Konter</span>
                </div>
                <span class="text-xs font-bold px-2 py-0.5 rounded bg-rose-900/40 text-rose-300 border border-rose-800">70.2% Resistensi</span>
              </div>
              <div class="p-3 rounded-xl bg-amber-950/30 border border-amber-900/50 flex items-center justify-between">
                <div>
                  <span class="text-amber-300 block text-[11px]">Prospek Follow-Up</span>
                  <span class="text-base font-bold text-amber-400">11 Konter</span>
                </div>
                <span class="text-xs font-bold px-2 py-0.5 rounded bg-amber-900/40 text-amber-300 border border-amber-800">23.4% Menggantung</span>
              </div>
              <div class="p-3 rounded-xl bg-steelblue-950/40 border border-steelblue-700/60 flex items-center justify-between">
                <div>
                  <span class="text-steelblue-300 block text-[11px]">Closing Aktif (Daftar/Trx)</span>
                  <span class="text-base font-bold text-steelblue-300">3 Konter</span>
                </div>
                <span class="text-xs font-bold px-2 py-0.5 rounded bg-steelblue-900/50 text-steelblue-300 border border-steelblue-700">6.4% Konversi</span>
              </div>
            </div>

            <!-- ROOT CAUSE FINDINGS -->
            <div class="md:col-span-7 p-4 bg-premium-950 rounded-xl border border-premium-800 flex flex-col justify-between">
              <div>
                <div class="text-xs font-bold text-white uppercase tracking-wider mb-3 flex items-center gap-2">
                  <span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>
                  Tiga Karakteristik Inti Pasar Konter
                </div>
                <div class="space-y-3 text-xs text-slate-300 leading-relaxed">
                  <div class="p-2.5 rounded-lg bg-premium-900/80 border border-premium-850">
                    <strong class="text-white block mb-0.5">1. Zero Loyalty (Hanya Peduli Harga Modal Perak)</strong>
                    Konter tidak peduli tampilan UI, fitur tambahan, atau branding. Pilihan aplikasi semata-mata ditentukan oleh selisih modal Rp 50 - Rp 100 pada pulsa & paket data.
                  </div>
                  <div class="p-2.5 rounded-lg bg-premium-900/80 border border-premium-850">
                    <strong class="text-white block mb-0.5">2. App Fatigue & Modal Kas Terbagi</strong>
                    Setiap konter sudah mengoperasikan 3 sampai 5 aplikasi (Digipos, Bos Pulsa, ShopeePay, Mitra Bukalapak). Menambah aplikasi baru berarti memecah uang modal kas mereka.
                  </div>
                </div>
              </div>
              <div class="text-xs font-mono text-slate-400 pt-3 border-t border-premium-850 mt-3 flex items-center justify-between">
                <span>Insight Eksekutif:</span>
                <span class="text-amber-400 font-semibold">Menjual nilai fitur ke pasar komoditas pulsa adalah strategi yang keliru.</span>
              </div>
            </div>
          </div>
        </div>

        <!-- SLIDE 3: UNIT ECONOMICS DINGIN -->
        <div class="slide-page hidden" data-page="3" data-topic="Analisis Biaya & Unit Economics">
          <div class="flex items-center justify-between mb-2">
            <h3 class="text-xl lg:text-2xl font-bold text-white">The Brutal Unit Economics: Mengapa Sales Fisik Boncos</h3>
            <span class="text-xs font-mono text-rose-400 bg-rose-950/40 px-2.5 py-1 rounded border border-rose-900/40">Audit Biaya Riil Lapangan</span>
          </div>
          <p class="text-xs lg:text-sm text-slate-300 mb-4">
            Berdasarkan realisasi biaya tes lapangan: 3 hari kerja sales dengan modal keluar Rp 240.000 menghasilkan 3 konter aktif.
          </p>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 font-mono text-xs mb-4">
            <div class="p-4 bg-premium-950 rounded-xl border border-premium-800 flex flex-col justify-between">
              <div>
                <span class="text-slate-500 block text-[11px]">Biaya Sales / Konter (CAC)</span>
                <span class="text-2xl font-bold text-rose-400 mt-1">Rp 80.000</span>
              </div>
              <p class="text-[11px] text-slate-400 mt-2 font-sans leading-snug">
                1 sales keliling = biaya Rp 80.000/hari = hanya mampu mengonversi rata-rata 1 konter per hari.
              </p>
            </div>
            <div class="p-4 bg-premium-950 rounded-xl border border-premium-800 flex flex-col justify-between">
              <div>
                <span class="text-slate-500 block text-[11px]">Laba Bersih / Trx Pulsa</span>
                <span class="text-2xl font-bold text-amber-400 mt-1">Rp 50 - Rp 150</span>
              </div>
              <p class="text-[11px] text-slate-400 mt-2 font-sans leading-snug">
                Margin sangat tipis karena Doripay dipaksa perang harga melawan prinsipal provider langsung.
              </p>
            </div>
            <div class="p-4 bg-premium-950 rounded-xl border border-premium-800 flex flex-col justify-between">
              <div>
                <span class="text-slate-500 block text-[11px]">Waktu Balik Modal (Payback)</span>
                <span class="text-2xl font-bold text-steelblue-400 mt-1">~2.5 - 3 Bulan</span>
              </div>
              <p class="text-[11px] text-slate-400 mt-2 font-sans leading-snug">
                Estimasi laba Rp 30.000/bulan (10 trx/hari x Rp 100 margin) butuh 3 bulan hanya untuk menutup biaya sales Rp 80rb.
              </p>
            </div>
          </div>

          <div class="p-3.5 bg-rose-950/20 border border-rose-900/50 rounded-xl text-xs flex items-center justify-between gap-4">
            <div class="space-y-0.5">
              <span class="font-bold text-rose-300 font-mono block text-xs">Peringatan Risiko Finansial:</span>
              <p class="text-slate-300 text-xs leading-relaxed">
                Konter pulsa berpindah server seketika jika kompetitor menawarkan selisih harga Rp 50 lebih murah. Jika konter berhenti transaksi di bulan ke-2, <strong>modal akuisisi sales Rp 80.000 langsung hangus (loss)</strong> sebelum mencapai titik impas.
              </p>
            </div>
            <div class="text-right font-mono text-rose-400 shrink-0 font-bold hidden md:block">
              CAC High <br> Margin Low
            </div>
          </div>
        </div>

        <!-- SLIDE 4: PENGAKUAN KESALAHAN & TITIK BALIK LAMPUNG -->
        <div class="slide-page hidden" data-page="4" data-topic="Akuntabilitas & Titik Balik Founder">
          <div class="flex items-center justify-between mb-2">
            <h3 class="text-xl lg:text-2xl font-bold text-white">Akuntabilitas Pemimpin & Titik Balik Lampung</h3>
            <span class="text-xs font-mono text-amber-400 bg-amber-950/40 px-2.5 py-1 rounded border border-amber-900/40">Founder Self-Reflection</span>
          </div>
          <p class="text-xs lg:text-sm text-slate-300 mb-4">
            Sebagai founder, saya bertanggung jawab penuh atas hasil ini dan secara terbuka mengakui dua kekeliruan awal:
          </p>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <div class="p-4 bg-premium-950 rounded-xl border border-premium-800">
              <div class="flex items-center gap-2 mb-2">
                <span class="px-2 py-0.5 rounded bg-rose-950/60 text-rose-400 border border-rose-800 text-[10px] font-mono font-bold">KEKELIRUAN 01</span>
                <span class="text-xs font-bold text-white">Riset Pasar Awal</span>
              </div>
              <p class="text-xs text-slate-300 leading-relaxed">
                Di awal pendirian, saya belum mengecek secara mendalam realitas keras industri konter pulsa fisik yang didominasi perang modal ratusan miliar dan margin receh tanpa adanya loyalitas pelanggan.
              </p>
            </div>
            <div class="p-4 bg-premium-950 rounded-xl border border-premium-800">
              <div class="flex items-center gap-2 mb-2">
                <span class="px-2 py-0.5 rounded bg-amber-950/60 text-amber-400 border border-amber-800 text-[10px] font-mono font-bold">KEKELIRUAN 02</span>
                <span class="text-xs font-bold text-white">Self-Awareness & Keahlian Inti</span>
              </div>
              <p class="text-xs text-slate-300 leading-relaxed">
                Dulu saya belum mengenali di mana kekuatan asli diri saya, dan memaksakan diri memimpin di ranah operasional sales logistik fisik jalanan yang bukan merupakan keunggulan kompetitif saya.
              </p>
            </div>
          </div>

          <div class="p-4 bg-steelblue-950/40 border border-steelblue-700/60 rounded-xl text-xs">
            <div class="font-bold text-steelblue-300 text-xs mb-1 font-mono uppercase tracking-wider flex items-center gap-2">
              <svg class="w-4 h-4 text-steelblue-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
              Titik Balik Kesadaran (Kunjungan ke Rumah Komisaris di Lampung):
            </div>
            <p class="text-slate-200 text-xs lg:text-sm leading-relaxed">
              Semenjak berkunjung dan berdiskusi di kediaman Pak Komisaris di Lampung, saya merenung secara mendalam dan akhirnya menemukan jati diri serta keahlian asli saya yang sebenarnya: <strong>rekayasa teknologi digital, sistem automasi canggih, dan kecerdasan buatan (AI)</strong>. Di sanalah energi dan daya saing saya yang sesungguhnya.
            </p>
          </div>
        </div>

        <!-- SLIDE 5: MENGAPA KOMISARIS HARUS YAKIN PIVOT KE DIGITAL & AI -->
        <div class="slide-page hidden" data-page="5" data-topic="Bukti Nyata Kapabilitas & Alasan Pivot">
          <div class="flex items-center justify-between mb-2">
            <h3 class="text-xl lg:text-2xl font-bold text-white">Mengapa Harus Yakin? Bukti Kapabilitas Riil</h3>
            <span class="text-xs font-mono text-steelblue-400 bg-steelblue-950/50 px-2.5 py-1 rounded border border-steelblue-700/50">High-Leverage Execution</span>
          </div>
          <p class="text-xs lg:text-sm text-slate-300 mb-4">
            Keputusan pivot ini bukan pelarian atau teori kosong, melainkan pemindahan fokus ke keahlian yang sudah terbukti hasilnya:
          </p>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-3 mb-4">
            <div class="p-4 bg-premium-950 rounded-xl border border-steelblue-500/50 hover:border-steelblue-400 transition-colors">
              <div class="text-[11px] font-mono text-steelblue-400 font-bold mb-1.5">01. AUTONOMOUS AI AGENTS</div>
              <h4 class="text-xs font-bold text-white mb-1">Sistem Otomasi 24 Jam Nonstop</h4>
              <p class="text-xs text-slate-300 leading-relaxed">
                Membangun agen AI otonom yang bekerja non-stop mengeksekusi operasional, riset data, dan monitoring tanpa butuh gaji/bensin sales fisik.
              </p>
            </div>
            <div class="p-4 bg-premium-950 rounded-xl border border-steelblue-500/50 hover:border-steelblue-400 transition-colors">
              <div class="text-[11px] font-mono text-steelblue-400 font-bold mb-1.5">02. DEPLOY APLIKASI 3 MENIT</div>
              <h4 class="text-xs font-bold text-white mb-1">Kecepatan Eksekusi Ekstrem</h4>
              <p class="text-xs text-slate-300 leading-relaxed">
                Mampu merancang, memprogram, dan menerbitkan dashboard analitik interaktif langsung online dari nol hanya dalam hitungan 3 menit.
              </p>
            </div>
            <div class="p-4 bg-premium-950 rounded-xl border border-steelblue-500/50 hover:border-steelblue-400 transition-colors">
              <div class="text-[11px] font-mono text-steelblue-400 font-bold mb-1.5">03. DIGITAL DISTRIBUTION</div>
              <h4 class="text-xs font-bold text-white mb-1">Jangkauan Skala Nasional</h4>
              <p class="text-xs text-slate-300 leading-relaxed">
                Automasi scraping dan konten multimedia cerdas di Threads & TikTok untuk mendatangkan traffic calon pembeli secara gratis.
              </p>
            </div>
          </div>

          <div class="p-3.5 bg-premium-950 border border-premium-800 rounded-xl text-xs flex items-center justify-between">
            <div class="flex items-center gap-3">
              <span class="px-2.5 py-1 rounded bg-steelblue-500/20 text-steelblue-300 font-mono text-[11px] font-bold">UNIT ECONOMICS DIGITAL</span>
              <span class="text-slate-300 text-xs">Margin laba <strong>70% – 90%</strong>, modal logistik nol, dan aset Doripay Rp 30 juta tetap aman menjadi modul payment internal.</span>
            </div>
          </div>
        </div>

        <!-- SLIDE 6: KEPUTUSAN AKHIR (DUA PILIHAN DEWAN DIREKSI) -->
        <div class="slide-page hidden" data-page="6" data-topic="Pilihan Keputusan Dewan Komisaris">
          <div class="flex items-center justify-between mb-2">
            <h3 class="text-xl lg:text-2xl font-bold text-white">Keputusan Akhir untuk Meja Rapat Dewan Komisaris</h3>
            <span class="text-xs font-mono text-slate-400 bg-premium-950 px-2.5 py-1 rounded border border-premium-800">Final Decision Matrix</span>
          </div>
          <p class="text-xs lg:text-sm text-slate-300 mb-4">
            Dua pilihan nyata yang saya ajukan secara terbuka ke hadapan dewan komisaris hari ini:
          </p>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <!-- PILIHAN 1 -->
            <div class="p-5 bg-premium-950 rounded-xl border border-premium-800 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2.5 py-1 rounded bg-premium-850 text-slate-300 font-mono text-[10px] font-bold mb-2 border border-premium-750">
                  PILIHAN 1: TETAP BERTAHAN DI PPOB FISIK
                </span>
                <h4 class="text-sm font-bold text-white mb-2">Perang Harga & Terus Bakar Biaya Sales</h4>
                <p class="text-xs text-slate-400 leading-relaxed mb-4">
                  Komisaris menyetujui pendanaan subsidi selisih modal pulsa dan gaji/bensin sales keliling (Rp 80rb/hari) demi mengejar volume konter di pasar berdarah.
                </p>
              </div>
              <div class="p-3 bg-rose-950/30 border border-rose-900/40 rounded-lg text-xs font-mono text-rose-300">
                Konsekuensi: Kas perusahaan terus tergerus, margin tetap tipis, dan risiko kehilangan modal kerja sangat tinggi.
              </div>
            </div>

            <!-- PILIHAN 2 -->
            <div class="p-5 bg-premium-950 rounded-xl border-2 border-steelblue-500 flex flex-col justify-between shadow-lg shadow-steelblue-950/30">
              <div>
                <div class="flex items-center justify-between mb-2">
                  <span class="inline-block px-2.5 py-1 rounded bg-steelblue-950 border border-steelblue-600 text-steelblue-300 font-mono text-[10px] font-bold">
                    PILIHAN 2: STOP SEMENTARA & PIVOT (REKOMENDASI FOUNDER)
                  </span>
                  <span class="text-[10px] font-mono text-steelblue-400 font-bold bg-steelblue-950/60 px-2 py-0.5 rounded border border-steelblue-800">High Return</span>
                </div>
                <h4 class="text-sm font-bold text-white mb-2">Fokus Total ke Layanan Digital & AI Tech</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-4">
                  Kunci keran pengeluaran sales fisik. Doripay tetap jalan pasif (autopilot) tanpa biaya tambahan. Alihkan 90% fokus founder ke pembuatan solusi AI & produk digital dengan margin tebal (70%–90%) dan risiko kas mendekati nol.
                </p>
              </div>
              <div class="p-3 bg-steelblue-950/60 border border-steelblue-700/60 rounded-lg text-xs font-mono text-steelblue-300">
                Hasil: Kas aman, mengembalikan modal investasi Rp 30 juta jauh lebih cepat, dan memaksimalkan potensi sejati founder.
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- SLIDE BOTTOM CONTROLS (OPTIMIZED FOR LAPTOP) -->
      <div class="flex items-center justify-between border-t border-premium-800 pt-4 mt-4 select-none">
        <button id="btn-prev" onclick="prevSlide()" class="px-4 py-2 rounded-lg bg-premium-950 hover:bg-premium-800 border border-premium-800 text-xs font-semibold text-slate-300 transition-colors flex items-center gap-2 disabled:opacity-30 disabled:cursor-not-allowed">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
          <span>Slide Sebelumnya</span>
        </button>
        
        <div class="flex items-center gap-2" id="slide-indicators"></div>

        <button id="btn-next" onclick="nextSlide()" class="px-5 py-2 rounded-lg bg-steelblue-500 hover:bg-steelblue-600 text-xs font-semibold text-white transition-colors flex items-center gap-2 shadow-md shadow-steelblue-950">
          <span id="btn-next-text">Lanjut Slide</span>
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
        </button>
      </div>

    </div>

    <div class="flex items-center justify-between text-xs font-mono text-slate-500 mt-3 px-2">
      <div>Gunakan tombol keyboard <span class="text-slate-400">Panah Kanan / Spasi</span> untuk maju, <span class="text-slate-400">Panah Kiri</span> untuk mundur</div>
      <div>Mode Presentasi Layar Laptop (16:9)</div>
    </div>
  </main>

  <!-- ======================================================== -->
  <!-- DASHBOARD VIEW (LAPTOP TABLE & METRICS)                  -->
  <!-- ======================================================== -->
  <div id="view-dash" class="hidden flex-1 max-w-6xl w-full mx-auto p-4 md:p-6 space-y-4 overflow-y-auto custom-scroll">
    <div class="flex items-center justify-between border-b border-premium-800 pb-3">
      <div>
        <h2 class="text-lg font-bold text-white tracking-tight">Database & Audit Lapangan 47 Konter Salatiga</h2>
        <p class="text-xs text-slate-400">Data hasil gabungan form respon dan catatan fisik sales canvasser.</p>
      </div>
      <div class="flex items-center gap-2">
        <button onclick="switchView('slide')" class="px-3 py-1.5 rounded-lg bg-premium-900 hover:bg-premium-850 border border-premium-800 text-xs font-semibold text-steelblue-400">
          ← Kembali ke Slide
        </button>
      </div>
    </div>

    <div class="grid grid-cols-4 gap-3">
      <div class="p-3.5 bg-premium-900 rounded-xl border border-premium-800">
        <div class="text-xs font-mono text-slate-500">Konter Diaudit</div>
        <div class="text-2xl font-bold text-white font-mono mt-1">47</div>
        <div class="text-[11px] text-slate-400 mt-1">4 Kecamatan Lapangan</div>
      </div>
      <div class="p-3.5 bg-premium-900 rounded-xl border border-premium-800">
        <div class="text-xs font-mono text-slate-500">Closing Aktif</div>
        <div class="text-2xl font-bold text-steelblue-400 font-mono mt-1">3</div>
        <div class="text-[11px] text-steelblue-300 mt-1">6.4% rasio sukses</div>
      </div>
      <div class="p-3.5 bg-premium-900 rounded-xl border border-premium-800">
        <div class="text-xs font-mono text-slate-500">Follow-Up</div>
        <div class="text-2xl font-bold text-amber-400 font-mono mt-1">11</div>
        <div class="text-[11px] text-amber-300 mt-1">23.4% prospek</div>
      </div>
      <div class="p-3.5 bg-premium-900 rounded-xl border border-premium-800">
        <div class="text-xs font-mono text-slate-500">Ditolak</div>
        <div class="text-2xl font-bold text-rose-400 font-mono mt-1">33</div>
        <div class="text-[11px] text-rose-400 mt-1">70.2% resistensi pasar</div>
      </div>
    </div>

    <div class="bg-premium-900 border border-premium-800 rounded-xl p-4">
      <div class="flex items-center justify-between gap-4 mb-3">
        <h3 class="text-xs font-bold text-white uppercase font-mono">Daftar Lengkap 47 Konter</h3>
        <div class="flex items-center gap-2">
          <input type="text" id="search-input" onkeyup="filterCounters()" placeholder="Cari nama konter, kontak, catatan..." class="px-3 py-1.5 rounded-lg bg-premium-950 border border-premium-800 text-xs text-slate-200 focus:outline-none focus:border-steelblue-400 w-64" />
          <select id="filter-status" onchange="filterCounters()" class="px-3 py-1.5 rounded-lg bg-premium-950 border border-premium-800 text-xs text-slate-200 focus:outline-none focus:border-steelblue-400 font-mono">
            <option value="ALL">Semua Status</option>
            <option value="CLOSING">Closing Aktif</option>
            <option value="FOLLOWUP">Perlu Follow-Up</option>
            <option value="TOLAK">Ditolak</option>
          </select>
        </div>
      </div>

      <div class="overflow-x-auto custom-scroll border border-premium-800 rounded-lg">
        <table class="w-full text-left text-xs">
          <thead class="bg-premium-950 text-slate-400 border-b border-premium-800 font-mono text-[11px]">
            <tr>
              <th class="py-2.5 px-3">Nama Konter</th>
              <th class="py-2.5 px-3">Kecamatan</th>
              <th class="py-2.5 px-3">Status</th>
              <th class="py-2.5 px-3">Kontak WA</th>
              <th class="py-2.5 px-3">Catatan Lapangan</th>
            </tr>
          </thead>
          <tbody id="counter-table-body" class="divide-y divide-premium-800/60 font-sans">
          </tbody>
        </table>
      </div>
      <div class="mt-3 text-xs text-slate-500 font-mono" id="counter-count">
        Menampilkan 47 dari 47 konter
      </div>
    </div>
  </div>

  <!-- JAVASCRIPT CONTROLLER -->
  <script>
    const RAW_RECORDS = """ + json_data + """;
    let currentSlide = 1;
    const totalSlides = 6;

    function switchView(mode) {
      const slideView = document.getElementById('view-slide');
      const dashView = document.getElementById('view-dash');
      const btnSlide = document.getElementById('btn-mode-slide');
      const btnDash = document.getElementById('btn-mode-dash');

      if (mode === 'slide') {
        slideView.classList.remove('hidden');
        dashView.classList.add('hidden');
        btnSlide.className = 'px-3 py-1.5 rounded transition-all flex items-center gap-1.5 bg-steelblue-500 text-white font-semibold shadow-sm';
        btnDash.className = 'px-3 py-1.5 rounded transition-all flex items-center gap-1.5 text-slate-400 hover:text-white';
      } else {
        slideView.classList.add('hidden');
        dashView.classList.remove('hidden');
        btnDash.className = 'px-3 py-1.5 rounded transition-all flex items-center gap-1.5 bg-steelblue-500 text-white font-semibold shadow-sm';
        btnSlide.className = 'px-3 py-1.5 rounded transition-all flex items-center gap-1.5 text-slate-400 hover:text-white';
      }
    }

    function renderSlideIndicators() {
      const container = document.getElementById('slide-indicators');
      container.innerHTML = '';
      for (let i = 1; i <= totalSlides; i++) {
        const dot = document.createElement('button');
        dot.onclick = () => goToSlide(i);
        dot.className = `h-2 rounded-full transition-all ${i === currentSlide ? 'bg-steelblue-400 w-6' : 'bg-premium-800 w-2 hover:bg-slate-600'}`;
        container.appendChild(dot);
      }
    }

    function updateSlide() {
      const pages = document.querySelectorAll('.slide-page');
      pages.forEach(p => {
        const pageNum = parseInt(p.getAttribute('data-page'));
        if (pageNum === currentSlide) {
          p.classList.remove('hidden');
          document.getElementById('slide-topic').textContent = p.getAttribute('data-topic') || 'Doripay Strategy';
        } else {
          p.classList.add('hidden');
        }
      });

      document.getElementById('slide-counter').textContent = `${currentSlide} / ${totalSlides}`;
      document.getElementById('btn-prev').disabled = currentSlide === 1;
      
      const nextText = document.getElementById('btn-next-text');
      if (currentSlide === totalSlides) {
        nextText.textContent = 'Buka Data Lapangan';
      } else {
        nextText.textContent = 'Lanjut Slide';
      }

      renderSlideIndicators();
    }

    function nextSlide() {
      if (currentSlide < totalSlides) {
        currentSlide++;
        updateSlide();
      } else {
        switchView('dash');
      }
    }

    function prevSlide() {
      if (currentSlide > 1) {
        currentSlide--;
        updateSlide();
      }
    }

    function goToSlide(num) {
      currentSlide = num;
      updateSlide();
    }

    // KEYBOARD NAVIGATION (LAPTOP OPTIMIZED)
    window.addEventListener('keydown', (e) => {
      const slideView = document.getElementById('view-slide');
      if (!slideView.classList.contains('hidden')) {
        if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
          e.preventDefault();
          nextSlide();
        } else if (e.key === 'ArrowLeft' || e.key === 'Backspace') {
          e.preventDefault();
          prevSlide();
        }
      }
    });

    // TABLE DIRECTORY
    function filterCounters() {
      const search = document.getElementById('search-input').value.toLowerCase();
      const statusFilter = document.getElementById('filter-status').value;

      const filtered = RAW_RECORDS.filter(c => {
        const matchesSearch = c.name.toLowerCase().includes(search) || 
                              c.phone.toLowerCase().includes(search) ||
                              c.notes.toLowerCase().includes(search);
        
        let matchesStatus = true;
        if (statusFilter === 'CLOSING') {
          matchesStatus = c.status.toLowerCase().includes('doripay') || c.status.toLowerCase().includes('daftar') || c.status.toLowerCase().includes('transaksi');
        } else if (statusFilter === 'FOLLOWUP') {
          matchesStatus = c.status.toLowerCase().includes('follow-up') || c.status.toLowerCase().includes('follow up');
        } else if (statusFilter === 'TOLAK') {
          matchesStatus = c.status.toLowerCase().includes('tidak tertarik');
        }

        return matchesSearch && matchesStatus;
      });

      renderTable(filtered);
    }

    function renderTable(data) {
      const tbody = document.getElementById('counter-table-body');
      tbody.innerHTML = '';

      if (data.length === 0) {
        tbody.innerHTML = `<tr><td colspan="5" class="py-6 text-center text-slate-500 font-mono">Tidak ada data yang cocok dengan pencarian.</td></tr>`;
        document.getElementById('counter-count').textContent = `Menampilkan 0 dari ${RAW_RECORDS.length} konter`;
        return;
      }

      data.forEach(item => {
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-premium-850/50 transition-colors';

        let badgeClass = 'bg-rose-950/40 border-rose-900/40 text-rose-300';
        if (item.status.includes('Doripay') || item.status.includes('transaksi')) {
          badgeClass = 'bg-steelblue-950 border-steelblue-600 text-steelblue-300';
        } else if (item.status.includes('follow-up') || item.status.includes('Follow-up')) {
          badgeClass = 'bg-amber-950/60 border-amber-800/60 text-amber-300';
        }

        const cleanPhone = item.phone.replace(/[^0-9]/g, '');
        const phoneDisplay = item.phone && item.phone !== '-' ? 
          `<a href="https://wa.me/62${cleanPhone.startsWith('0') ? cleanPhone.slice(1) : cleanPhone}" target="_blank" class="text-steelblue-400 hover:underline font-mono">${item.phone}</a>` :
          `<span class="text-slate-600 font-mono">-</span>`;

        tr.innerHTML = `
          <td class="py-2.5 px-3 font-semibold text-white">${item.name}</td>
          <td class="py-2.5 px-3 text-slate-400">${item.district}</td>
          <td class="py-2.5 px-3">
            <span class="inline-block px-2 py-0.5 rounded border text-[10px] font-mono ${badgeClass}">
              ${item.status}
            </span>
          </td>
          <td class="py-2.5 px-3">${phoneDisplay}</td>
          <td class="py-2.5 px-3 text-slate-400 max-w-md truncate">${item.notes || '-'}</td>
        `;
        tbody.appendChild(tr);
      });

      document.getElementById('counter-count').textContent = `Menampilkan ${data.length} dari ${RAW_RECORDS.length} konter`;
    }

    updateSlide();
    renderTable(RAW_RECORDS);
  </script>
</body>
</html>
"""

with open('/opt/data/doripay-sales-dashboard/index.html', 'w') as f:
    f.write(html)

print("Optimized deck for Laptop 16:9 successfully!")
