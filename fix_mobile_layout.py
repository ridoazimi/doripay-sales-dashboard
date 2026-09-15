import re

with open('/opt/data/doripay-sales-dashboard/generate_clean_deck.py') as f:
    code = f.read()

# Make Slide 5 super clean, compact, and 100% fit on iPhone
old_slide5 = '''        <!-- SLIDE 5: KONSEKUENSI JIKA BERTAHAN -->
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
        </div>'''

new_slide5 = '''        <!-- SLIDE 5: KONSEKUENSI JIKA BERTAHAN -->
        <div class="slide-page hidden" data-page="5" data-topic="Konsekuensi Finansial Jika Bertahan">
          <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded bg-steelblue-500/20 text-steelblue-300 text-[10px] font-mono mb-1.5">
            Dilema Strategis untuk Komisaris
          </div>
          <h3 class="text-base sm:text-2xl font-bold text-white mb-1">
            2 Konsekuensi Mutlak Jika Memilih Bertahan
          </h3>
          <p class="text-[11px] text-slate-400 mb-2.5 leading-tight">
            Jika komisaris memutuskan Doripay bertahan di konter, dua konsekuensi finansial ini wajib disetujui:
          </p>
          
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 mb-2.5">
            <div class="p-2.5 bg-premium-950 rounded-lg border border-steelblue-500/50">
              <div class="flex items-center justify-between mb-1">
                <span class="text-[10px] font-mono text-steelblue-400 font-bold">KONSEKUENSI 1</span>
                <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-steelblue-950 text-steelblue-300">Margin Tipis</span>
              </div>
              <div class="text-xs font-bold text-white mb-0.5">Siap Terus Berperang Harga</div>
              <p class="text-[10px] text-slate-400 leading-snug">
                Pasar konter tidak peduli fitur apa pun. Harga modal Doripay wajib sama atau lebih murah dari server lokal, sehingga laba kotor akan terus ditekan di angka tipis (Rp 50 - Rp 150/trx).
              </p>
            </div>

            <div class="p-2.5 bg-premium-950 rounded-lg border border-steelblue-500/50">
              <div class="flex items-center justify-between mb-1">
                <span class="text-[10px] font-mono text-steelblue-400 font-bold">KONSEKUENSI 2</span>
                <span class="text-[9px] font-mono px-1.5 py-0.5 rounded bg-rose-950 text-rose-300">Bakar Modal</span>
              </div>
              <div class="text-xs font-bold text-white mb-0.5">Siap Keluar CAC Tinggi</div>
              <p class="text-[10px] text-slate-400 leading-snug">
                Mengakuisisi 1 konter membutuhkan Rp 80.000 (1 sales/hari). Tanpa mendanai biaya sales dan insentif secara berkelanjutan, konversi lapangan akan tetap stagnan di 6%.
              </p>
            </div>
          </div>

          <div class="p-2 bg-steelblue-950/40 border border-steelblue-800/50 rounded-lg text-[10px]">
            <span class="font-bold text-steelblue-300">Pertanyaan Rapat:</span> 
            <span class="text-slate-300">Apakah posisi kas dan runway perusahaan saat ini siap mendanai perang harga dan CAC tinggi tersebut?</span>
          </div>
        </div>'''

code = code.replace(old_slide5, new_slide5)

with open('/opt/data/doripay-sales-dashboard/generate_clean_deck.py', 'w') as f:
    f.write(code)

print("Slide 5 optimized for mobile screen!")
