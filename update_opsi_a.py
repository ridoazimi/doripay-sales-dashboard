with open('/opt/data/doripay-sales-dashboard/index.html') as f:
    html = f.read()

old_opsi_a = """            <!-- OPSI A -->
            <div class="p-5 bg-brand-950 rounded-xl border border-brand-800 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2.5 py-1 rounded bg-brand-900 text-slate-300 font-mono text-[10px] font-bold mb-2 border border-brand-750">
                  OPSI A: MELANJUTKAN PENETRASI PPOB FISIK
                </span>
                <h4 class="text-sm font-bold text-white mb-2">Memperkuat Jalur Sales Konter Lapangan</h4>
                <p class="text-xs text-slate-400 leading-relaxed mb-4">
                  Menyiapkan pendanaan tambahan untuk membiayai operasional sales harian dan menyubsidi harga modal pulsa agar mampu bersaing dengan server lokal mapan.
                </p>
                <div class="space-y-1.5 text-xs text-slate-400 mb-2">
                  <div class="flex items-center gap-2">• <span>Kebutuhan modal kerja dan bensin sales tetap berjalan</span></div>
                  <div class="flex items-center gap-2">• <span>Waktu impas akuisisi berkisar 2.5 hingga 3 bulan per konter</span></div>
                  <div class="flex items-center gap-2">• <span>Margin laba kotor transaksi berada pada kisaran Rp 50 - Rp 150</span></div>
                </div>
              </div>
              <div class="p-3 bg-brand-900/60 border border-brand-800 rounded-lg text-xs font-mono text-slate-300">
                Fokus Opsi: Mengejar pertumbuhan volume transaksi konter dengan komitmen modal berkelanjutan.
              </div>
            </div>"""

new_opsi_a = """            <!-- OPSI A -->
            <div class="p-5 bg-brand-950 rounded-xl border border-brand-800 flex flex-col justify-between">
              <div>
                <span class="inline-block px-2.5 py-1 rounded bg-brand-900 text-slate-300 font-mono text-[10px] font-bold mb-2 border border-brand-750">
                  OPSI A: TETAP BERTAHAN & MELANJUTKAN PPOB FISIK
                </span>
                <h4 class="text-sm font-bold text-white mb-2">Konsekuensi Mutlak Bertahan di Lapangan</h4>
                <p class="text-xs text-slate-300 leading-relaxed mb-4">
                  Jika dewan komisaris memutuskan untuk tetap bertahan dan berlanjut di pasar konter fisik, maka perusahaan harus siap menghadapi 3 konsekuensi mutlak:
                </p>
                <div class="space-y-2 text-xs text-slate-300 mb-3">
                  <div class="p-2 rounded-lg bg-brand-900/70 border border-brand-800">
                    <strong class="text-white block mb-0.5">• Harus Selalu Siap Berperang Harga</strong>
                    <span class="text-slate-400 text-[11px]">Pasar tidak peduli fitur; wajib terus menyubsidi harga modal agar selalu lebih murah dari server lain.</span>
                  </div>
                  <div class="p-2 rounded-lg bg-brand-900/70 border border-brand-800">
                    <strong class="text-white block mb-0.5">• Siap Mengeluarkan Biaya Akuisisi (CAC) Lebih Tinggi</strong>
                    <span class="text-slate-400 text-[11px]">Terus mendanai gaji dan bensin sales keliling lapangan (Rp 80.000/hari/konter) untuk mencari mitra baru.</span>
                  </div>
                  <div class="p-2 rounded-lg bg-brand-900/70 border border-brand-800">
                    <strong class="text-white block mb-0.5">• Menerima Realitas Margin Sangat Tipis</strong>
                    <span class="text-slate-400 text-[11px]">Margin transaksi receh (Rp 50 - Rp 150/transaksi), sehingga perputaran modal lambat dan risiko modal mengendap tinggi.</span>
                  </div>
                </div>
              </div>
              <div class="p-2.5 bg-rose-950/30 border border-rose-900/40 rounded-lg text-xs font-mono text-rose-300">
                Konsekuensi Riil: Membutuhkan komitmen suntikan dana besar dan napas kas yang sangat panjang.
              </div>
            </div>"""

if old_opsi_a in html:
    html = html.replace(old_opsi_a, new_opsi_a)
    print("Replaced Opsi A successfully!")
else:
    print("old_opsi_a not found, attempting loose match...")

with open('/opt/data/doripay-sales-dashboard/index.html', 'w') as f:
    f.write(html)
