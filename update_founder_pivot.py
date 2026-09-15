with open('/opt/data/doripay-sales-dashboard/generate_clean_deck.py') as f:
    code = f.read()

# Replace slide 5 bottom callout
old_s5_box = '''          <div class="p-2 bg-steelblue-950/40 border border-steelblue-800/50 rounded-lg text-[10px]">
            <span class="font-bold text-steelblue-300">Pertanyaan Rapat:</span> 
            <span class="text-slate-300">Apakah posisi kas dan runway perusahaan saat ini siap mendanai perang harga dan CAC tinggi tersebut?</span>
          </div>'''

new_s5_box = '''          <div class="p-2.5 bg-steelblue-950/60 border border-steelblue-500/50 rounded-lg text-[10px] flex items-center justify-between">
            <span class="font-bold text-steelblue-300 font-mono">Dua Pilihan Akhir:</span> 
            <span class="text-slate-200">1. Bertahan dengan konsekuensi modal di atas, ATAU 2. Break total dan pivot ke Layanan Digital & AI.</span>
          </div>'''

code = code.replace(old_s5_box, new_s5_box)

# Replace slide 6 with the true 2 choices (Bertahan vs Break & Pivot AI/Digital)
old_s6 = '''        <!-- SLIDE 6: MATRIKS KEPUTUSAN DEWAN DIREKSI -->
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
        </div>'''

new_s6 = '''        <!-- SLIDE 6: MATRIKS KEPUTUSAN DEWAN DIREKSI -->
        <div class="slide-page hidden" data-page="6" data-topic="Pilihan Arah: Bertahan vs Break & Pivot">
          <h3 class="text-lg sm:text-2xl font-bold text-white mb-1">Keputusan Akhir untuk Meja Komisaris</h3>
          <p class="text-xs text-slate-400 mb-2.5 leading-tight">
            Hanya ada dua pilihan nyata di hadapan manajemen hari ini:
          </p>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
            <!-- PILIHAN 1 -->
            <div class="p-3 bg-premium-950 rounded-lg border border-premium-800 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2 py-0.5 rounded bg-premium-850 text-slate-300 font-mono text-[10px] font-bold mb-1.5">
                  PILIHAN 1: TETAP BERTAHAN
                </span>
                <h4 class="text-xs sm:text-sm font-bold text-white mb-1">Terima Perang Harga & Bakar CAC</h4>
                <p class="text-[11px] text-slate-400 leading-snug mb-2">
                  Komisaris siap menyetujui pendanaan subsidi margin pulsa dan operasional sales keliling untuk merebut volume konter di pasar berdarah.
                </p>
              </div>
              <div class="text-[10px] font-mono text-rose-300 pt-1.5 border-t border-premium-800">
                Resiko: Margin tetap tipis (Rp 100) & payback 3 bln
              </div>
            </div>

            <!-- PILIHAN 2 -->
            <div class="p-3 bg-premium-950 rounded-lg border-2 border-steelblue-500 flex flex-col justify-between">
              <div>
                <div class="flex items-center justify-between mb-1.5">
                  <span class="inline-block px-2 py-0.5 rounded bg-steelblue-950 border border-steelblue-600 text-steelblue-300 font-mono text-[10px] font-bold">
                    PILIHAN 2: BREAK & PIVOT (REKOMENDASI)
                  </span>
                  <span class="text-[9px] font-mono text-steelblue-400 font-bold">High Leverage</span>
                </div>
                <h4 class="text-xs sm:text-sm font-bold text-white mb-1">Fokus Total ke Layanan Digital & AI</h4>
                <p class="text-[11px] text-slate-300 leading-snug mb-2">
                  Break total dari perang harga fisik konter. Alihkan sumber daya ke keunggulan kompetitif utama founder: pengembangan sistem AI Agent, otomatisasi digital 24 jam, dan pembuatan web instan dengan margin laba tinggi tanpa beban logistik fisik.
                </p>
              </div>
              <div class="text-[10px] font-mono text-steelblue-300 pt-1.5 border-t border-steelblue-800/60">
                Hasil: Margin tebal, scalable nasional, zero bensin sales
              </div>
            </div>
          </div>
        </div>'''

code = code.replace(old_s6, new_s6)

with open('/opt/data/doripay-sales-dashboard/generate_clean_deck.py', 'w') as f:
    f.write(code)

print("Updated with true 2-choice dilemma successfully!")
