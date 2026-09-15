import json

with open('/opt/data/doripay-sales-dashboard/records.json') as f:
    records = json.load(f)

json_data = json.dumps(records)

html = """<!DOCTYPE html>
<html lang="id" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
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
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: #07090e;
      color: #e2e8f0;
      -webkit-font-smoothing: antialiased;
    }
    .font-mono {
      font-family: 'JetBrains Mono', monospace;
    }
    .touch-pan-y {
      touch-action: pan-y;
    }
    .custom-scroll::-webkit-scrollbar {
      width: 4px;
      height: 4px;
    }
    .custom-scroll::-webkit-scrollbar-track {
      background: #0c1017;
    }
    .custom-scroll::-webkit-scrollbar-thumb {
      background: #233047;
      border-radius: 2px;
    }
  </style>
</head>
<body class="bg-premium-950 text-slate-100 min-h-screen selection:bg-steelblue-500 selection:text-white flex flex-col">

  <!-- TOP APP BAR -->
  <header class="sticky top-0 z-50 border-b border-premium-800 bg-premium-950/95 backdrop-blur-md px-3.5 sm:px-6 py-2.5 flex items-center justify-between gap-2">
    <div class="flex items-center gap-2">
      <div class="w-7 h-7 rounded-md bg-steelblue-500/20 border border-steelblue-400/40 flex items-center justify-center font-bold text-steelblue-300 font-mono text-xs">
        DP
      </div>
      <div class="flex items-center gap-1.5">
        <h1 class="text-xs sm:text-sm font-bold tracking-tight text-white">Doripay Strategy</h1>
        <span class="text-[10px] px-1.5 py-0.5 rounded bg-premium-850 border border-premium-800 text-steelblue-300 font-mono">Board Deck</span>
      </div>
    </div>

    <!-- VIEW TOGGLE -->
    <div class="flex items-center gap-1 bg-premium-900 p-1 rounded-lg border border-premium-800 text-[11px] font-medium">
      <button id="btn-mode-slide" onclick="switchView('slide')" class="px-2.5 py-1 rounded transition-all flex items-center gap-1 bg-steelblue-500 text-white font-semibold">
        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"/></svg>
        <span>Slide Deck</span>
      </button>
      <button id="btn-mode-dash" onclick="switchView('dash')" class="px-2.5 py-1 rounded transition-all flex items-center gap-1 text-slate-400 hover:text-white">
        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
        <span>Data Lapangan</span>
      </button>
    </div>
  </header>

  <!-- ======================================================== -->
  <!-- MAIN SLIDE CONTAINER                                     -->
  <!-- ======================================================== -->
  <main id="view-slide" class="flex-1 max-w-5xl w-full mx-auto p-3 sm:p-6 flex flex-col justify-between touch-pan-y">
    
    <div id="slide-wrapper" class="w-full bg-premium-900 border border-premium-800 rounded-2xl p-4 sm:p-8 flex flex-col justify-between shadow-2xl relative">
      
      <!-- SUB-HEADER -->
      <div class="flex items-center justify-between border-b border-premium-800 pb-3 mb-3 text-[11px] font-mono">
        <div class="flex items-center gap-1.5 text-steelblue-400 font-medium">
          <span class="text-slate-500">MEETING DEWAN KOMISARIS</span>
          <span>/</span>
          <span id="slide-topic" class="text-slate-200">Evaluasi & Arah Baru</span>
        </div>
        <div id="slide-counter" class="text-slate-400 bg-premium-950 px-2 py-0.5 rounded border border-premium-800">
          1 / 6
        </div>
      </div>

      <!-- SLIDE PAGES -->
      <div id="slide-content" class="py-2 flex-1">

        <!-- SLIDE 1: COVER -->
        <div class="slide-page" data-page="1" data-topic="Evaluasi Penetrasi & Keputusan Strategis">
          <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-steelblue-500/10 border border-steelblue-500/30 text-steelblue-400 text-[11px] font-medium mb-3">
            Pertemuan Strategis Direksi & Komisaris
          </div>
          <h2 class="text-xl sm:text-3xl font-extrabold text-white tracking-tight leading-snug mb-2.5">
            Evaluasi Lapangan Doripay: <br>
            <span class="text-steelblue-400">Pertanggungjawaban, Realitas Pasar & Solusi Pivot</span>
          </h2>
          <p class="text-xs sm:text-sm text-slate-400 leading-relaxed mb-4">
            Paparan hasil uji lapangan 47 konter, kalkulasi dingin biaya operasional, pengakuan evaluasi internal founder, serta pertimbangan memilih antara <strong>bertahan dengan perang modal</strong> atau <strong>stop sementara kanvasing fisik untuk pivot ke layanan digital & AI ber-margin tebal</strong>.
          </p>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 font-mono text-[11px]">
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <div class="text-slate-500">Konter Diaudit</div>
              <div class="text-lg font-bold text-white mt-0.5">47 Konter</div>
            </div>
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <div class="text-slate-500">Tingkat Penolakan</div>
              <div class="text-lg font-bold text-rose-400 mt-0.5">70.2%</div>
            </div>
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <div class="text-slate-500">Biaya Sales Tes</div>
              <div class="text-lg font-bold text-amber-400 mt-0.5">Rp 80rb / hari</div>
            </div>
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <div class="text-slate-500">Aset Teknologi</div>
              <div class="text-lg font-bold text-steelblue-400 mt-0.5">Terbangun & Aman</div>
            </div>
          </div>
        </div>

        <!-- SLIDE 2: REALITAS LAPANGAN & FUNNEL -->
        <div class="slide-page hidden" data-page="2" data-topic="Fakta Riil Pasar Konter Salatiga">
          <h3 class="text-lg sm:text-2xl font-bold text-white mb-1">Hasil Audit 47 Konter: Pasar Sensitif Harga</h3>
          <p class="text-xs text-slate-400 mb-3">
            Kanvasing di 4 kecamatan (Sidomukti, Argomulyo, Tingkir, Sidorejo) membuka fakta perilaku pasar:
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 mb-3">
            <div class="space-y-2 font-mono text-[11px]">
              <div class="p-2 rounded-lg bg-premium-950 border border-premium-800 flex justify-between">
                <span class="text-slate-400">Total Kunjungan</span>
                <span class="text-white font-bold">47 Konter</span>
              </div>
              <div class="p-2 rounded-lg bg-rose-950/20 border border-rose-900/40 flex justify-between">
                <span class="text-rose-300">Ditolak di Tempat</span>
                <span class="text-rose-300 font-bold">33 (70.2%)</span>
              </div>
              <div class="p-2 rounded-lg bg-amber-950/20 border border-amber-900/40 flex justify-between">
                <span class="text-amber-300">Prospek Follow-Up</span>
                <span class="text-amber-300 font-bold">11 (23.4%)</span>
              </div>
              <div class="p-2 rounded-lg bg-steelblue-950/40 border border-steelblue-700/50 flex justify-between">
                <span class="text-steelblue-300">Closing Aktif</span>
                <span class="text-steelblue-300 font-bold">3 Konter (6.4%)</span>
              </div>
            </div>

            <div class="p-3 bg-premium-950 rounded-lg border border-premium-800 text-xs flex flex-col justify-between">
              <div>
                <div class="font-bold text-white mb-1">Fakta Perilaku Konter:</div>
                <ul class="text-[11px] text-slate-300 space-y-1.5 leading-snug">
                  <li>• <strong>Loyalitas Nol:</strong> Tidak peduli fitur atau branding. Satu-satunya penentu adalah selisih modal Rp 50 - Rp 100.</li>
                  <li>• <strong>App Fatigue:</strong> Rata-rata sudah memakai 3-5 aplikasi (Digipos, Bos Pulsa, ShopeePay).</li>
                  <li>• <strong>Modal Terpecah:</strong> Enggan setor deposit baru karena takut saldo mengendap di brand baru.</li>
                </ul>
              </div>
              <div class="text-[10px] font-mono text-slate-500 pt-2 border-t border-premium-850 mt-2">
                Menjual fitur ke pasar komoditas pulsa tidak efektif
              </div>
            </div>
          </div>
        </div>

        <!-- SLIDE 3: UNIT ECONOMICS DINGIN -->
        <div class="slide-page hidden" data-page="3" data-topic="Analisis Biaya & Unit Economics">
          <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-steelblue-500/20 text-steelblue-300 text-[10px] font-mono mb-1.5">
            Audit Biaya Riil Lapangan
          </div>
          <h3 class="text-lg sm:text-2xl font-bold text-white mb-1">Unit Economics: 1 Sales = Rp 80rb / Hari = 1 Konter</h3>
          <p class="text-xs text-slate-400 mb-2.5 leading-tight">
            Data aktual 3 hari tes lapangan: modal sales Rp 240.000 menghasilkan 3 konter aktif (CAC = Rp 80.000/konter).
          </p>

          <div class="grid grid-cols-2 gap-2 font-mono text-[11px] mb-2.5">
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <span class="text-slate-500 block">Biaya Sales / Konter (CAC)</span>
              <span class="text-base font-bold text-rose-400">Rp 80.000</span>
              <span class="text-[9px] text-slate-400 block mt-0.5 font-sans">1 hari keliling hanya closing 1 konter</span>
            </div>
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <span class="text-slate-500 block">Laba Kotor / Trx Pulsa</span>
              <span class="text-base font-bold text-amber-400">Rp 50 - Rp 150</span>
              <span class="text-[9px] text-slate-400 block mt-0.5 font-sans">Margin sangat tipis karena perang harga</span>
            </div>
          </div>

          <div class="p-2.5 bg-premium-950 border border-premium-800 rounded-lg text-xs space-y-1">
            <div class="flex items-center justify-between font-mono text-[11px]">
              <span class="text-slate-300">Waktu Balik Modal (Payback Period):</span>
              <span class="text-steelblue-300 font-bold font-mono">~2.5 - 3 Bulan per Konter</span>
            </div>
            <p class="text-[10px] text-slate-400 leading-snug">
              Dengan estimasi laba Rp 30.000/bulan (10 trx/hari x Rp 100 margin), biaya sales Rp 80.000 baru impas setelah 3 bulan.
            </p>
            <div class="text-[10px] font-mono text-rose-300 pt-1 border-t border-premium-850">
              Risiko Utama: Jika konter pindah ke server lain dalam 2 bulan pertama demi selisih Rp 50, biaya Rp 80.000 langsung hangus (boncos).
            </div>
          </div>
        </div>

        <!-- SLIDE 4: PENGAKUAN KESALAHAN & TITIK BALIK LAMPUNG -->
        <div class="slide-page hidden" data-page="4" data-topic="Akuntabilitas & Titik Balik Founder">
          <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 text-[10px] font-mono mb-1.5">
            Akuntabilitas & Evaluasi Diri
          </div>
          <h3 class="text-lg sm:text-2xl font-bold text-white mb-1">
            Pengakuan Kesalahan Pemimpin & Titik Balik
          </h3>
          <p class="text-xs text-slate-300 mb-2.5 leading-snug">
            Sebagai founder, saya bertanggung jawab penuh atas hasil ini dan secara terbuka mengakui dua kekeliruan awal:
          </p>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-2.5">
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <div class="text-[10px] font-mono text-amber-400 font-bold mb-1">KEKELIRUAN 1: RISET PASAR</div>
              <p class="text-[11px] text-slate-300 leading-snug">
                Di awal, saya belum mengecek secara mendalam realitas kerasnya pasar konter fisik yang hanya digerakkan oleh margin perak tanpa loyalitas.
              </p>
            </div>
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <div class="text-[10px] font-mono text-amber-400 font-bold mb-1">KEKELIRUAN 2: SELF-AWARENESS SKILL</div>
              <p class="text-[11px] text-slate-300 leading-snug">
                Dulu saya belum sepenuhnya menyadari di mana kekuatan asli diri saya, dan memaksakan bermain di ranah operasional logistik sales lapangan.
              </p>
            </div>
          </div>

          <div class="p-2.5 bg-steelblue-950/40 border border-steelblue-800/60 rounded-lg text-xs">
            <div class="font-bold text-steelblue-300 text-[11px] mb-0.5 font-mono">Titik Balik Kesadaran (Perjalanan ke Lampung):</div>
            <p class="text-[10px] text-slate-300 leading-snug">
              Semenjak berkunjung dan berdiskusi di rumah Pak Komisaris di Lampung, saya merenung mendalam dan akhirnya menemukan jati diri serta kompetensi inti saya yang sebenarnya: <strong>arsitektur teknologi, sistem automasi, dan kecerdasan buatan (AI)</strong>.
            </p>
          </div>
        </div>

        <!-- SLIDE 5: MENGAPA KOMISARIS HARUS YAKIN PIVOT KE DIGITAL & AI -->
        <div class="slide-page hidden" data-page="5" data-topic="Bukti Nyata Kapabilitas & Alasan Pivot">
          <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-steelblue-500/20 text-steelblue-300 text-[10px] font-mono mb-1.5">
            Validasi Kapabilitas Nyata
          </div>
          <h3 class="text-lg sm:text-2xl font-bold text-white mb-1">
            Kenapa Pivot ke Layanan Digital & AI? Bukti Track Record
          </h3>
          <p class="text-xs text-slate-400 mb-2.5 leading-tight">
            Keputusan pivot ini bukan pelarian, melainkan perpindahan amunisi ke ring kekuatan asli yang sudah terbukti hasilnya:
          </p>

          <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 mb-2.5">
            <div class="p-2.5 bg-premium-950 rounded-lg border border-steelblue-500/50">
              <div class="text-[10px] font-mono text-steelblue-400 font-bold mb-1">01. AUTONOMOUS AI AGENT</div>
              <p class="text-[10px] text-slate-300 leading-snug">
                Terbukti berhasil membangun sistem AI Agent otonom yang bekerja 24 jam nonstop mengeksekusi operasional tanpa butuh gaji/bensin.
              </p>
            </div>
            <div class="p-2.5 bg-premium-950 rounded-lg border border-steelblue-500/50">
              <div class="text-[10px] font-mono text-steelblue-400 font-bold mb-1">02. DEPLOY SISTEM 3 MENIT</div>
              <p class="text-[10px] text-slate-300 leading-snug">
                Mampu merancang dan menerbitkan web app, dashboard analitik, dan tools interaktif secara kilat dalam hitungan menit.
              </p>
            </div>
            <div class="p-2.5 bg-premium-950 rounded-lg border border-steelblue-500/50">
              <div class="text-[10px] font-mono text-steelblue-400 font-bold mb-1">03. AUTOMATION SCRAPING</div>
              <p class="text-[10px] text-slate-300 leading-snug">
                Mengembangkan automasi continuous stream di platform digital (Threads & TikTok) untuk mendatangkan traffic tanpa biaya iklan mahal.
              </p>
            </div>
          </div>

          <div class="p-2.5 bg-premium-950 border border-premium-800 rounded-lg text-[10px] flex items-center justify-between">
            <div>
              <span class="font-bold text-white">Keunggulan Bisnis:</span> 
              <span class="text-slate-300">Margin laba 70% - 90%, zero beban logistik fisik, dan jangkauan pasar instan nasional. Aset Doripay tetap aman menjadi modul payment internal.</span>
            </div>
          </div>
        </div>

        <!-- SLIDE 6: KEPUTUSAN AKHIR (DUA PILIHAN JELAS) -->
        <div class="slide-page hidden" data-page="6" data-topic="Pilihan Keputusan Dewan Komisaris">
          <h3 class="text-lg sm:text-2xl font-bold text-white mb-1">Keputusan Akhir untuk Meja Rapat Komisaris</h3>
          <p class="text-xs text-slate-400 mb-2.5 leading-tight">
            Dua pilihan nyata di hadapan dewan direksi hari ini:
          </p>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
            <!-- PILIHAN 1 -->
            <div class="p-3 bg-premium-950 rounded-lg border border-premium-800 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2 py-0.5 rounded bg-premium-850 text-slate-300 font-mono text-[10px] font-bold mb-1">
                  PILIHAN 1: TETAP BERTAHAN DI PPOB FISIK
                </span>
                <h4 class="text-xs sm:text-sm font-bold text-white mb-1">Perang Harga & Terus Bakar CAC</h4>
                <p class="text-[10px] text-slate-400 leading-snug mb-2">
                  Komisaris menyetujui pendanaan subsidi selisih harga pulsa dan biaya sales keliling (Rp 80rb/hari) demi mengejar volume konter di pasar berdarah.
                </p>
              </div>
              <div class="text-[9px] font-mono text-rose-300 pt-1.5 border-t border-premium-800">
                Risiko: Kas terus tergerus, margin tetap receh, balik modal 3 bulan per konter.
              </div>
            </div>

            <!-- PILIHAN 2 -->
            <div class="p-3 bg-premium-950 rounded-lg border-2 border-steelblue-500 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between mb-1">
                  <span class="inline-block px-2 py-0.5 rounded bg-steelblue-950 border border-steelblue-600 text-steelblue-300 font-mono text-[10px] font-bold">
                    PILIHAN 2: STOP SEMENTARA & PIVOT (REKOMENDASI)
                  </span>
                  <span class="text-[9px] font-mono text-steelblue-400 font-bold">High Leverage</span>
                </div>
                <h4 class="text-xs sm:text-sm font-bold text-white mb-1">Fokus Total ke Layanan Digital & AI Tech</h4>
                <p class="text-[10px] text-slate-300 leading-snug mb-2">
                  Kunci keran pengeluaran sales fisik. Doripay tetap jalan pasif (autopilot) tanpa biaya tambahan. Alihkan 90% fokus founder ke pembuatan solusi AI & digital dengan margin tebal dan risiko kas nol.
                </p>
              </div>
              <div class="text-[9px] font-mono text-steelblue-300 pt-1.5 border-t border-steelblue-800/60">
                Hasil: Kas aman, mengembalikan modal investasi lebih cepat, memaksimalkan potensi asli founder.
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- SLIDE BOTTOM NAV -->
      <div class="flex items-center justify-between border-t border-premium-800 pt-3 mt-2">
        <button id="btn-prev" onclick="prevSlide()" class="px-3 py-1.5 rounded-lg bg-premium-950 hover:bg-premium-800 border border-premium-800 text-xs font-semibold text-slate-300 transition-colors flex items-center gap-1 disabled:opacity-30 disabled:cursor-not-allowed">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
          <span class="hidden sm:inline">Sebelumnya</span>
        </button>
        
        <div class="flex items-center gap-1.5" id="slide-indicators"></div>

        <button id="btn-next" onclick="nextSlide()" class="px-3.5 py-1.5 rounded-lg bg-steelblue-500 hover:bg-steelblue-600 text-xs font-semibold text-white transition-colors flex items-center gap-1">
          <span id="btn-next-text">Lanjut</span>
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
        </button>
      </div>

    </div>

    <div class="text-center text-[10px] font-mono text-slate-600 mt-2 sm:hidden">
      Geser layar ke kiri / kanan untuk ganti slide
    </div>
  </main>

  <!-- ======================================================== -->
  <!-- DASHBOARD VIEW                                           -->
  <!-- ======================================================== -->
  <div id="view-dash" class="hidden flex-1 max-w-7xl w-full mx-auto px-3 sm:px-6 py-4 space-y-5">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-premium-800 pb-3">
      <div>
        <h2 class="text-lg sm:text-xl font-bold text-white tracking-tight">Database & Audit Lapangan 47 Konter</h2>
        <p class="text-xs text-slate-400">Data terpadu respon form dan catatan kanvasing sales.</p>
      </div>
    </div>

    <div class="grid grid-cols-2 lg:grid-cols-4 gap-2.5">
      <div class="p-3 bg-premium-900 rounded-lg border border-premium-800">
        <div class="text-[11px] font-mono text-slate-500">Konter Diaudit</div>
        <div class="text-xl sm:text-2xl font-bold text-white font-mono mt-0.5">47</div>
        <div class="text-[10px] text-slate-400 mt-1">4 Kecamatan</div>
      </div>
      <div class="p-3 bg-premium-900 rounded-lg border border-premium-800">
        <div class="text-[11px] font-mono text-slate-500">Closing</div>
        <div class="text-xl sm:text-2xl font-bold text-steelblue-400 font-mono mt-0.5">3</div>
        <div class="text-[10px] text-steelblue-300 mt-1">6.4% rasio sukses</div>
      </div>
      <div class="p-3 bg-premium-900 rounded-lg border border-premium-800">
        <div class="text-[11px] font-mono text-slate-500">Follow-Up</div>
        <div class="text-xl sm:text-2xl font-bold text-amber-400 font-mono mt-0.5">11</div>
        <div class="text-[10px] text-amber-300 mt-1">23.4% prospek</div>
      </div>
      <div class="p-3 bg-premium-900 rounded-lg border border-premium-800">
        <div class="text-[11px] font-mono text-slate-500">Ditolak</div>
        <div class="text-xl sm:text-2xl font-bold text-rose-400 font-mono mt-0.5">33</div>
        <div class="text-[10px] text-rose-400 mt-1">70.2% resistensi</div>
      </div>
    </div>

    <div class="bg-premium-900 border border-premium-800 rounded-xl p-3.5">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 mb-3">
        <h3 class="text-sm font-bold text-white">Direktori 47 Konter</h3>
        <div class="flex flex-wrap items-center gap-2">
          <input type="text" id="search-input" onkeyup="filterCounters()" placeholder="Cari konter..." class="px-2.5 py-1 rounded bg-premium-950 border border-premium-800 text-xs text-slate-200 focus:outline-none focus:border-steelblue-400 w-36 sm:w-48" />
          <select id="filter-status" onchange="filterCounters()" class="px-2 py-1 rounded bg-premium-950 border border-premium-800 text-xs text-slate-200 focus:outline-none focus:border-steelblue-400">
            <option value="ALL">Semua</option>
            <option value="CLOSING">Closing</option>
            <option value="FOLLOWUP">Follow-Up</option>
            <option value="TOLAK">Ditolak</option>
          </select>
        </div>
      </div>

      <div class="overflow-x-auto custom-scroll border border-premium-800 rounded-lg">
        <table class="w-full text-left text-[11px]">
          <thead class="bg-premium-950 text-slate-400 border-b border-premium-800 font-mono">
            <tr>
              <th class="py-2 px-3">Konter</th>
              <th class="py-2 px-3">Kecamatan</th>
              <th class="py-2 px-3">Status</th>
              <th class="py-2 px-3">Kontak</th>
              <th class="py-2 px-3">Catatan</th>
            </tr>
          </thead>
          <tbody id="counter-table-body" class="divide-y divide-premium-800/60 font-sans">
          </tbody>
        </table>
      </div>
      <div class="mt-2 text-[10px] text-slate-500 font-mono" id="counter-count">
        Menampilkan 47 dari 47 konter
      </div>
    </div>
  </div>

  <!-- SCRIPT -->
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
        btnSlide.className = 'px-2.5 py-1 rounded transition-all flex items-center gap-1 bg-steelblue-500 text-white font-semibold';
        btnDash.className = 'px-2.5 py-1 rounded transition-all flex items-center gap-1 text-slate-400 hover:text-white';
      } else {
        slideView.classList.add('hidden');
        dashView.classList.remove('hidden');
        btnDash.className = 'px-2.5 py-1 rounded transition-all flex items-center gap-1 bg-steelblue-500 text-white font-semibold';
        btnSlide.className = 'px-2.5 py-1 rounded transition-all flex items-center gap-1 text-slate-400 hover:text-white';
      }
    }

    function renderSlideIndicators() {
      const container = document.getElementById('slide-indicators');
      container.innerHTML = '';
      for (let i = 1; i <= totalSlides; i++) {
        const dot = document.createElement('button');
        dot.onclick = () => goToSlide(i);
        dot.className = `h-1.5 rounded-full transition-all ${i === currentSlide ? 'bg-steelblue-400 w-4' : 'bg-premium-800 w-1.5'}`;
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
        nextText.textContent = 'Data';
      } else {
        nextText.textContent = 'Lanjut';
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

    // TOUCH SWIPE
    let touchStartX = 0;
    let touchEndX = 0;
    const slideWrapper = document.getElementById('slide-wrapper');

    slideWrapper.addEventListener('touchstart', e => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    slideWrapper.addEventListener('touchend', e => {
      touchEndX = e.changedTouches[0].screenX;
      const diff = touchStartX - touchEndX;
      if (Math.abs(diff) > 45) {
        if (diff > 0) nextSlide();
        else prevSlide();
      }
    }, { passive: true });

    // KEYBOARD NAV
    window.addEventListener('keydown', (e) => {
      const slideView = document.getElementById('view-slide');
      if (!slideView.classList.contains('hidden')) {
        if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') nextSlide();
        else if (e.key === 'ArrowLeft') prevSlide();
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
        tbody.innerHTML = `<tr><td colspan="5" class="py-4 text-center text-slate-500 font-mono">Tidak ada data.</td></tr>`;
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
          <td class="py-2.5 px-3 font-medium text-white">${item.name}</td>
          <td class="py-2.5 px-3 text-slate-400">${item.district}</td>
          <td class="py-2.5 px-3">
            <span class="inline-block px-1.5 py-0.5 rounded border text-[9px] font-mono ${badgeClass}">
              ${item.status}
            </span>
          </td>
          <td class="py-2.5 px-3">${phoneDisplay}</td>
          <td class="py-2.5 px-3 text-slate-400 max-w-xs truncate">${item.notes || '-'}</td>
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

print("Generated final deck successfully!")
