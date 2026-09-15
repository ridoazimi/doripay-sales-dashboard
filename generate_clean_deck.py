import json

with open('/opt/data/doripay-sales-dashboard/records.json') as f:
    records = json.load(f)

json_data = json.dumps(records)

html = """<!DOCTYPE html>
<html lang="id" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>Doripay Executive Strategy | Audit Penetrasi Salatiga</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
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
              500: '#4682b4', // Classic Steel Blue
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

  <!-- TOP APP BAR (COMPACT & CLEAN ON MOBILE) -->
  <header class="sticky top-0 z-50 border-b border-premium-800 bg-premium-950/95 backdrop-blur-md px-3.5 sm:px-6 py-2.5 flex items-center justify-between gap-2">
    <div class="flex items-center gap-2">
      <div class="w-7 h-7 rounded-md bg-steelblue-500/20 border border-steelblue-400/40 flex items-center justify-center font-bold text-steelblue-300 font-mono text-xs">
        DP
      </div>
      <div class="flex items-center gap-1.5">
        <h1 class="text-xs sm:text-sm font-bold tracking-tight text-white">Doripay Strategy</h1>
        <span class="text-[10px] px-1.5 py-0.5 rounded bg-premium-850 border border-premium-800 text-steelblue-300 font-mono">Salatiga</span>
      </div>
    </div>

    <!-- VIEW TOGGLE (SHORT LABELS FOR MOBILE) -->
    <div class="flex items-center gap-1 bg-premium-900 p-1 rounded-lg border border-premium-800 text-[11px] font-medium">
      <button id="btn-mode-slide" onclick="switchView('slide')" class="px-2.5 py-1 rounded transition-all flex items-center gap-1 bg-steelblue-500 text-white font-semibold">
        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"/></svg>
        <span>Slide Deck</span>
      </button>
      <button id="btn-mode-dash" onclick="switchView('dash')" class="px-2.5 py-1 rounded transition-all flex items-center gap-1 text-slate-400 hover:text-white">
        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"/></svg>
        <span>Data</span>
      </button>
    </div>
  </header>

  <!-- ======================================================== -->
  <!-- VIEW 1: MOBILE-FIRST PRESENTATION SLIDE DECK             -->
  <!-- ======================================================== -->
  <main id="view-slide" class="flex-1 max-w-5xl w-full mx-auto p-3 sm:p-6 flex flex-col justify-between touch-pan-y">
    
    <!-- SLIDE CARD WRAPPER -->
    <div id="slide-wrapper" class="w-full bg-premium-900 border border-premium-800 rounded-2xl p-4 sm:p-8 flex flex-col justify-between shadow-2xl relative">
      
      <!-- SLIDE SUB-HEADER -->
      <div class="flex items-center justify-between border-b border-premium-800 pb-3 mb-3 text-[11px] font-mono">
        <div class="flex items-center gap-1.5 text-steelblue-400 font-medium">
          <span class="text-slate-500">DECK</span>
          <span>/</span>
          <span id="slide-topic" class="text-slate-200">Kondisi Pasar & Opsi Bertahan</span>
        </div>
        <div id="slide-counter" class="text-slate-400 bg-premium-950 px-2 py-0.5 rounded border border-premium-800">
          1 / 6
        </div>
      </div>

      <!-- SLIDE CONTENT CONTAINER -->
      <div id="slide-content" class="py-2 flex-1">

        <!-- SLIDE 1: COVER & DILEMA STRATEGIS -->
        <div class="slide-page" data-page="1" data-topic="Latar Belakang & Pertimbangan">
          <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-steelblue-500/10 border border-steelblue-500/30 text-steelblue-400 text-[11px] font-medium mb-3">
            Bahan Rapat Komisaris
          </div>
          <h2 class="text-xl sm:text-3xl font-extrabold text-white tracking-tight leading-snug mb-2.5">
            Penetrasi Konter Salatiga: <br>
            <span class="text-steelblue-400">Pilihan Menyerah atau Konsekuensi Bertahan</span>
          </h2>
          <p class="text-xs sm:text-sm text-slate-400 leading-relaxed mb-4">
            Audit terhadap 47 konter membuktikan pasar PPOB didorong oleh sensitivitas harga ekstrem dengan loyalitas nol. Jika perusahaan memilih bertahan, komisaris harus siap menyetujui konsekuensi: <strong>wajib terus perang harga</strong> dan <strong>biaya akuisisi (CAC) tinggi dengan margin tipis</strong>.
          </p>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 font-mono text-[11px]">
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <div class="text-slate-500">Konter Diaudit</div>
              <div class="text-lg font-bold text-white mt-0.5">47</div>
            </div>
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <div class="text-slate-500">Ditolak</div>
              <div class="text-lg font-bold text-rose-400 mt-0.5">70.2%</div>
            </div>
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <div class="text-slate-500">Prospek FU</div>
              <div class="text-lg font-bold text-amber-400 mt-0.5">23.4%</div>
            </div>
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <div class="text-slate-500">Closing</div>
              <div class="text-lg font-bold text-steelblue-400 mt-0.5">6.4%</div>
            </div>
          </div>
        </div>

        <!-- SLIDE 2: FUNNEL REALITAS LAPANGAN -->
        <div class="slide-page hidden" data-page="2" data-topic="Data Corong Sales Lapangan">
          <h3 class="text-lg sm:text-2xl font-bold text-white mb-1.5">Corong Penjualan Lapangan (Sales Funnel)</h3>
          <p class="text-xs text-slate-400 mb-3.5">
            Hasil kunjungan kanvasing di 4 kecamatan (Sidomukti, Argomulyo, Tingkir, Sidorejo):
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 items-center">
            <div class="space-y-2 font-mono text-[11px]">
              <div class="p-2.5 rounded-lg bg-premium-950 border border-premium-800 flex items-center justify-between">
                <span class="font-sans text-slate-300">Total Kunjungan</span>
                <span class="font-bold text-white">47 Konter (100%)</span>
              </div>
              <div class="p-2.5 rounded-lg bg-rose-950/20 border border-rose-900/40 flex items-center justify-between">
                <span class="font-sans text-rose-300">Penolakan Langsung</span>
                <span class="font-bold text-rose-300">33 Konter (70.2%)</span>
              </div>
              <div class="p-2.5 rounded-lg bg-amber-950/20 border border-amber-900/40 flex items-center justify-between">
                <span class="font-sans text-amber-300">Prospek Follow-Up</span>
                <span class="font-bold text-amber-300">11 Konter (23.4%)</span>
              </div>
              <div class="p-2.5 rounded-lg bg-steelblue-950/40 border border-steelblue-700/50 flex items-center justify-between">
                <span class="font-sans text-steelblue-200">Closing (Daftar / Trx)</span>
                <span class="font-bold text-steelblue-300">3 Konter (6.4%)</span>
              </div>
            </div>
            <div class="bg-premium-950 p-3 rounded-lg border border-premium-800 flex flex-col items-center">
              <div class="w-full max-w-[200px] h-36">
                <canvas id="chart-funnel-slide"></canvas>
              </div>
            </div>
          </div>
        </div>

        <!-- SLIDE 3: AKAR MASALAH (COMPACT LIST UNTUK HP) -->
        <div class="slide-page hidden" data-page="3" data-topic="Perilaku Pasar & Alasan Tolak">
          <h3 class="text-lg sm:text-2xl font-bold text-white mb-1">Kenapa Konter Menolak?</h3>
          <p class="text-xs text-slate-400 mb-3">
            Tiga temuan kritis dari 33 konter yang menolak di lapangan:
          </p>
          <div class="space-y-2.5">
            <div class="p-3 bg-premium-950 rounded-lg border border-premium-800">
              <div class="flex items-center justify-between mb-1">
                <span class="text-[11px] font-mono font-bold text-steelblue-400">01. ZERO LOYALTY (HARGA MODAL MATI)</span>
                <span class="text-[10px] font-mono text-slate-500">Sensitif Rp100</span>
              </div>
              <p class="text-xs text-slate-300 leading-relaxed">
                Pemilik konter tidak peduli tampilan UI atau fitur canggih. Satu-satunya pertanyaan adalah: <em>"Berapa harga modal pulsa Telkomsel & kuota dibanding Bos Pulsa / Digipos?"</em>
              </p>
            </div>
            <div class="p-3 bg-premium-950 rounded-lg border border-premium-800">
              <div class="flex items-center justify-between mb-1">
                <span class="text-[11px] font-mono font-bold text-steelblue-400">02. APP FATIGUE (KELELAHAN APLIKASI)</span>
                <span class="text-[10px] font-mono text-slate-500">Pegang 3 - 5 Apk</span>
              </div>
              <p class="text-xs text-slate-300 leading-relaxed">
                Konter rata-rata sudah pasang Digipos, Bos Pulsa, dan ShopeePay. Menambah 1 aplikasi baru dianggap merepotkan dan memecah modal kasbon mereka.
              </p>
            </div>
            <div class="p-3 bg-premium-950 rounded-lg border border-premium-800">
              <div class="flex items-center justify-between mb-1">
                <span class="text-[11px] font-mono font-bold text-steelblue-400">03. DEFISIT KEPERCAYAAN & TAKUT SALDO NYANGKUT</span>
                <span class="text-[10px] font-mono text-slate-500">Faktor Trust</span>
              </div>
              <p class="text-xs text-slate-300 leading-relaxed">
                Konter belum familiar dengan brand Doripay. Mereka enggan setor deposit baru karena takut transaksi lambat, CS sulit dihubungi saat gangguan, atau saldo tertahan.
              </p>
            </div>
          </div>
        </div>

        <!-- SLIDE 4: THE BRUTAL UNIT ECONOMICS (CAC VS MARGIN) -->
        <div class="slide-page hidden" data-page="4" data-topic="Analisis Unit Economics">
          <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-rose-950/40 border border-rose-800/40 text-rose-300 text-[11px] font-mono mb-2">
            Hitungan Finansial Dingin
          </div>
          <h3 class="text-lg sm:text-2xl font-bold text-white mb-1.5">Biaya Akuisisi Tinggi vs Margin Tipis</h3>
          <p class="text-xs text-slate-400 mb-3 leading-relaxed">
            Sales keliling untuk pulsa menghadapi kebuntuan: biaya merekrut 1 konter aktif jauh lebih mahal daripada akumulasi margin transaksinya.
          </p>
          <div class="grid grid-cols-2 gap-2.5 font-mono text-[11px] mb-3">
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <span class="text-slate-500 block">CAC Sales Lapangan</span>
              <span class="text-base font-bold text-rose-400">Rp 800.000+</span>
              <span class="text-[10px] text-slate-400 block mt-0.5 font-sans">Gaji/operasional dibagi konter aktif</span>
            </div>
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <span class="text-slate-500 block">Margin Kotor / Trx Pulsa</span>
              <span class="text-base font-bold text-amber-400">Rp 50 - Rp 150</span>
              <span class="text-[10px] text-slate-400 block mt-0.5 font-sans">Tipis akibat perang harga</span>
            </div>
          </div>
          <div class="p-3 bg-steelblue-950/30 border border-steelblue-800/40 rounded-lg text-xs">
            <div class="font-bold text-steelblue-300 mb-0.5 font-mono text-[11px]">Payback Period: ~17 - 18 Bulan</div>
            <div class="text-slate-300 leading-relaxed font-sans text-[11px]">
              Dibutuhkan 1.5 tahun transaksi rutin hanya untuk menutup biaya sales 1 konter. Sementara risiko konter berpindah demi selisih Rp50 sangat tinggi setiap saat.
            </div>
          </div>
        </div>

        <!-- SLIDE 5: KONSEKUENSI JIKA BERTAHAN -->
        <div class="slide-page hidden" data-page="5" data-topic="Konsekuensi Jika Bertahan">
          <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-steelblue-500/20 border border-steelblue-400/40 text-steelblue-300 text-[11px] font-mono mb-2">
            Rekomendasi Utama ke Komisaris
          </div>
          <h3 class="text-lg sm:text-2xl font-bold text-white mb-2">
            Kenyataan Mutlak Jika Ingin Bertahan di Sini
          </h3>
          <p class="text-xs text-slate-300 mb-3.5 leading-relaxed">
            Jika dewan komisaris memutuskan Doripay <strong>tetap bertahan</strong> di pasar konter, perusahaan wajib menerima dua konsekuensi finansial:
          </p>
          
          <div class="space-y-2.5 mb-3">
            <div class="p-3 bg-premium-950 rounded-lg border-2 border-steelblue-500/60">
              <div class="text-[11px] font-mono text-steelblue-400 font-bold mb-0.5">KONSEKUENSI 1</div>
              <h4 class="text-xs sm:text-sm font-bold text-white mb-1">Wajib Selalu Siap Berperang Harga</h4>
              <p class="text-[11px] text-slate-400 leading-relaxed">
                Karena pasar konter tidak peduli branding maupun fitur, harga modal Doripay harus setara atau lebih murah dari server lokal. Margin kotor akan selalu tipis dan butuh cadangan subsidi harga.
              </p>
            </div>

            <div class="p-3 bg-premium-950 rounded-lg border-2 border-steelblue-500/60">
              <div class="text-[11px] font-mono text-steelblue-400 font-bold mb-0.5">KONSEKUENSI 2</div>
              <h4 class="text-xs sm:text-sm font-bold text-white mb-1">Wajib Terus Mengeluarkan Biaya Akuisisi (CAC) Tinggi</h4>
              <p class="text-[11px] text-slate-400 leading-relaxed">
                Untuk mengubah kebiasaan konter lama, perusahaan harus terus mendanai insentif sales dan promo saldo awal. Tanpa bakar biaya akuisisi, konversi lapangan akan tetap stagnan di ~6%.
              </p>
            </div>
          </div>
        </div>

        <!-- SLIDE 6: MATRIKS KEPUTUSAN DEWAN DIREKSI -->
        <div class="slide-page hidden" data-page="6" data-topic="Matriks Keputusan Direksi">
          <h3 class="text-lg sm:text-2xl font-bold text-white mb-1.5">Matriks Keputusan Dewan Direksi</h3>
          <p class="text-xs text-slate-400 mb-3.5">
            Dua opsi arah yang diajukan ke meja rapat komisaris hari ini:
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            <!-- JALUR A -->
            <div class="p-3.5 bg-premium-950 rounded-lg border border-premium-800 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2 py-0.5 rounded bg-premium-850 text-slate-300 font-mono text-[10px] font-bold mb-2">
                  OPSI A: CUT COST / PIVOT
                </span>
                <h4 class="text-xs sm:text-sm font-bold text-white mb-1.5">Hentikan Sales Canvassing</h4>
                <p class="text-[11px] text-slate-400 leading-relaxed mb-2.5">
                  Hentikan pengeluaran gaji/bensin sales lapangan. Hindari perang harga pulsa berdarah, lalu alihkan amunisi ke produk bermargin tebal (Top-Up Game, E-Wallet, Transfer Bank).
                </p>
              </div>
              <div class="text-[10px] font-mono text-slate-500 pt-2 border-t border-premium-800">
                Penyelamatan cash runway perusahaan
              </div>
            </div>

            <!-- JALUR B -->
            <div class="p-3.5 bg-premium-950 rounded-lg border border-steelblue-500/60 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2 py-0.5 rounded bg-steelblue-950 border border-steelblue-700 text-steelblue-300 font-mono text-[10px] font-bold mb-2">
                  OPSI B: BERTAHAN DENGAN SYARAT
                </span>
                <h4 class="text-xs sm:text-sm font-bold text-white mb-1.5">Komitmen Perang Harga & CAC</h4>
                <p class="text-[11px] text-slate-400 leading-relaxed mb-2.5">
                  Komisaris menyetujui anggaran subsidi harga dan operasional akuisisi agresif, dengan fokus eksklusif di Sidomukti (konversi 16.7%) dan eksekusi 11 konter follow-up.
                </p>
              </div>
              <div class="text-[10px] font-mono text-steelblue-400 pt-2 border-t border-premium-800">
                Mempertahankan pasar dengan komitmen modal
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- SLIDE CONTROLS (THUMB FRIENDLY ON MOBILE) -->
      <div class="flex items-center justify-between border-t border-premium-800 pt-3 mt-2">
        <button id="btn-prev" onclick="prevSlide()" class="px-3 py-1.5 rounded-lg bg-premium-950 hover:bg-premium-800 border border-premium-800 text-xs font-semibold text-slate-300 transition-colors flex items-center gap-1 disabled:opacity-30 disabled:cursor-not-allowed">
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
          <span class="hidden sm:inline">Sebelumnya</span>
        </button>
        
        <div class="flex items-center gap-1.5" id="slide-indicators">
          <!-- Rendered via JS -->
        </div>

        <button id="btn-next" onclick="nextSlide()" class="px-3.5 py-1.5 rounded-lg bg-steelblue-500 hover:bg-steelblue-600 text-xs font-semibold text-white transition-colors flex items-center gap-1">
          <span id="btn-next-text">Lanjut</span>
          <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
        </button>
      </div>

    </div>

    <!-- SWIPE HINT ON MOBILE -->
    <div class="text-center text-[10px] font-mono text-slate-600 mt-2 sm:hidden">
      Geser layar ke kiri / kanan untuk ganti slide
    </div>
  </main>

  <!-- ======================================================== -->
  <!-- VIEW 2: FULL ANALYTICS DATA & DIRECTORY                  -->
  <!-- ======================================================== -->
  <div id="view-dash" class="hidden flex-1 max-w-7xl w-full mx-auto px-3 sm:px-6 py-4 space-y-5">
    
    <!-- DASHBOARD HEADER -->
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-premium-800 pb-3">
      <div>
        <h2 class="text-lg sm:text-xl font-bold text-white tracking-tight">Database & Analisis Lapangan Salatiga</h2>
        <p class="text-xs text-slate-400">Data terpadu respon form dan catatan kunjungan kanvasing.</p>
      </div>
    </div>

    <!-- METRICS -->
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

    <!-- DIRECTORY TABLE -->
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
            <!-- Rendered via JS -->
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

      if (currentSlide === 2) {
        setTimeout(renderFunnelSlideChart, 80);
      }
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

    // TOUCH SWIPE SUPPORT FOR MOBILE
    let touchStartX = 0;
    let touchEndX = 0;
    const slideWrapper = document.getElementById('slide-wrapper');

    slideWrapper.addEventListener('touchstart', e => {
      touchStartX = e.changedTouches[0].screenX;
    }, { passive: true });

    slideWrapper.addEventListener('touchend', e => {
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
    }, { passive: true });

    function handleSwipe() {
      const diff = touchStartX - touchEndX;
      if (Math.abs(diff) > 45) {
        if (diff > 0) {
          nextSlide(); // Swipe left -> next
        } else {
          prevSlide(); // Swipe right -> prev
        }
      }
    }

    // KEYBOARD NAVIGATION
    window.addEventListener('keydown', (e) => {
      const slideView = document.getElementById('view-slide');
      if (!slideView.classList.contains('hidden')) {
        if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'Enter') {
          nextSlide();
        } else if (e.key === 'ArrowLeft') {
          prevSlide();
        }
      }
    });

    // CHART
    let funnelSlideChart = null;
    function renderFunnelSlideChart() {
      if (funnelSlideChart) return;
      const ctx = document.getElementById('chart-funnel-slide');
      if (!ctx) return;
      funnelSlideChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ['Ditolak', 'Follow-Up', 'Closing'],
          datasets: [{
            data: [33, 11, 3],
            backgroundColor: ['#991b1b', '#d97706', '#4682b4'],
            borderColor: '#0c1017',
            borderWidth: 2
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              position: 'bottom',
              labels: { color: '#94a3b8', font: { size: 10 } }
            }
          },
          cutout: '70%'
        }
      });
    }

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

print("Regenerated clean mobile-optimized index.html successfully!")
