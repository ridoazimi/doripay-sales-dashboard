with open('/opt/data/doripay-sales-dashboard/generate_clean_deck.py') as f:
    text = f.read()

# Replace slide 4 content with real cost figures
old_slide4 = '''        <!-- SLIDE 4: THE BRUTAL UNIT ECONOMICS (CAC VS MARGIN) -->
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
        </div>'''

new_slide4 = '''        <!-- SLIDE 4: THE BRUTAL UNIT ECONOMICS (CAC VS MARGIN) -->
        <div class="slide-page hidden" data-page="4" data-topic="Analisis Biaya & Unit Economics Riil">
          <div class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded bg-steelblue-500/20 border border-steelblue-400/30 text-steelblue-300 text-[11px] font-mono mb-2">
            Audit Biaya Riil (3 Hari Kanvasing)
          </div>
          <h3 class="text-lg sm:text-2xl font-bold text-white mb-1.5">Kalkulasi Biaya Riil: Sales Rp 80.000 / Hari</h3>
          <p class="text-xs text-slate-400 mb-3 leading-relaxed">
            Data riil pengeluaran kanvasing kemarin: <strong>Rp 80.000 / hari x 3 hari = Rp 240.000</strong> untuk mengunjungi 47 konter dan menghasilkan <strong>3 konter aktif</strong>.
          </p>
          <div class="grid grid-cols-2 gap-2.5 font-mono text-[11px] mb-3">
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <span class="text-slate-500 block">CAC Riil Tes 3 Hari</span>
              <span class="text-base font-bold text-steelblue-300">Rp 80.000 / konter</span>
              <span class="text-[10px] text-slate-400 block mt-0.5 font-sans">Total Rp 240.000 / 3 closing</span>
            </div>
            <div class="p-2.5 bg-premium-950 rounded-lg border border-premium-800">
              <span class="text-slate-500 block">Laba Kotor per Trx Pulsa</span>
              <span class="text-base font-bold text-amber-400">Rp 50 - Rp 150</span>
              <span class="text-[10px] text-slate-400 block mt-0.5 font-sans">Margin tipis perang harga</span>
            </div>
          </div>
          <div class="p-3 bg-premium-950 border border-premium-800 rounded-lg text-xs space-y-1.5">
            <div class="flex items-center justify-between font-mono text-[11px]">
              <span class="text-slate-400">Balik Modal (Payback Period) Aktual:</span>
              <span class="text-steelblue-300 font-bold">~2 - 3 Bulan</span>
            </div>
            <p class="text-slate-400 leading-relaxed font-sans text-[11px]">
              Dengan estimasi laba ~Rp 30.000/bln per konter (10 trx/hari x Rp 100 margin), modal sales Rp 80.000 baru impas setelah 2-3 bulan.
            </p>
            <div class="pt-2 border-t border-premium-850 text-[10px] font-mono text-rose-300">
              Peringatan Risiko: Jika konter pindah ke server lain dalam 2 bulan pertama demi selisih Rp 50, biaya Rp 80.000 hangus sebelum sempat balik modal.
            </div>
          </div>
        </div>'''

text = text.replace(old_slide4, new_slide4)

with open('/opt/data/doripay-sales-dashboard/generate_clean_deck.py', 'w') as f:
    f.write(text)

print('Updated Slide 4 with real costs successfully!')
