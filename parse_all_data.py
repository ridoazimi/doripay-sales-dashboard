import json, urllib.request, urllib.parse, re

# 1. Fetch Google Sheet Form Responses 1
with open('/opt/data/google_token.json') as f:
    tk = json.load(f)

data = urllib.parse.urlencode({
    'client_id': tk['client_id'],
    'client_secret': tk['client_secret'],
    'refresh_token': tk['refresh_token'],
    'grant_type': 'refresh_token'
}).encode()

req = urllib.request.Request('https://oauth2.googleapis.com/token', data=data)
res = json.loads(urllib.request.urlopen(req).read().decode())
access_token = res['access_token']

sheet_id = '123_zXPMLC6Hbb-ey4A-StTIIRjZG0XBBHe3dZC2wRXI'
url_r1 = f'https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/Form%20Responses%201!A1:Z100'
req_r1 = urllib.request.Request(url_r1, headers={'Authorization': f'Bearer {access_token}'})
rows_r1 = json.loads(urllib.request.urlopen(req_r1).read().decode()).get('values', [])

header = rows_r1[0]
sheet_entries = []
for r in rows_r1[1:]:
    # Pad to 11 cols
    r = r + [''] * (11 - len(r))
    ts, name, district, current_app, status, phone, notes, fu_date, fu_goal, tx_per_day, top_prod = r[:11]
    name = name.strip()
    if not name and not district:
        continue
    sheet_entries.append({
        'timestamp': ts.strip(),
        'name': name if name else '(Konter Tanpa Nama)',
        'district': district.strip(),
        'current_app': current_app.strip(),
        'status': status.strip(),
        'phone': phone.strip(),
        'notes': notes.strip(),
        'fu_date': fu_date.strip(),
        'fu_goal': fu_goal.strip(),
        'tx_per_day': tx_per_day.strip(),
        'top_prod': top_prod.strip(),
        'source': 'Google Sheet (Form Respon)'
    })

print(f"Loaded {len(sheet_entries)} from Google Sheets.")

# 2. Add physical notes data (from image transcripts)
# Image 1 (Saturday & Sunday Report):
# Closing: febry cell
# FU: 88 cell (085741318888 ibu yuyun), T cell (0895703177201)
# Uninterested: pp, bsm, infinity, bonk, lunar, bless, mahkota, boss, putra jaya, sal, chimp chomp, agen 46, alva, elje, izzi, abdi, dian, tegalrejo, marui, cvas, astro, mahkota (2), arjuna, lindhae, tri, Rpm, ip
# Image 4 (Tally & Leads detail):
# Falin cell: daftar + isi saldo
# Berry cell: daftar (085122770354)
# Sumber artha cell: 081391264017 ibu helena (bertemu pemilik)
# Master cell: 085799802345 (bertemu pemilik)
# Star cell: 089688789876 (memahami apk)
# Moncer cell: 085743766663 (bertemu pemilik)

# Let's see which ones from image notes are not yet in sheet_entries
norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
sheet_names = {norm(x['name']): x for x in sheet_entries}

manual_additions = [
    {'name': 'Bless cell', 'district': 'Salatiga', 'current_app': 'Kompetitor Lokal', 'status': 'Tidak tertarik', 'phone': '-', 'notes': 'Laporan canvassing weekend sales', 'fu_date': '-', 'fu_goal': '-', 'tx_per_day': '-', 'top_prod': '-', 'source': 'Catatan Fisik Sales (Weekend)'},
    {'name': 'Chimp chomp cell', 'district': 'Salatiga', 'current_app': 'Kompetitor Lokal', 'status': 'Tidak tertarik', 'phone': '-', 'notes': 'Laporan canvassing weekend sales', 'fu_date': '-', 'fu_goal': '-', 'tx_per_day': '-', 'top_prod': '-', 'source': 'Catatan Fisik Sales (Weekend)'},
    {'name': 'Agen 46', 'district': 'Salatiga', 'current_app': 'Kompetitor / Bank', 'status': 'Tidak tertarik', 'phone': '-', 'notes': 'Laporan canvassing weekend sales', 'fu_date': '-', 'fu_goal': '-', 'tx_per_day': '-', 'top_prod': '-', 'source': 'Catatan Fisik Sales (Weekend)'},
    {'name': 'CVAS cell', 'district': 'Salatiga', 'current_app': 'Kompetitor Lokal', 'status': 'Tidak tertarik', 'phone': '-', 'notes': 'Laporan canvassing weekend sales', 'fu_date': '-', 'fu_goal': '-', 'tx_per_day': '-', 'top_prod': '-', 'source': 'Catatan Fisik Sales (Weekend)'},
    {'name': 'Mahkota cell (2)', 'district': 'Salatiga', 'current_app': 'Kompetitor Lokal', 'status': 'Tidak tertarik', 'phone': '-', 'notes': 'Cabang kedua / lokasi berbeda', 'fu_date': '-', 'fu_goal': '-', 'tx_per_day': '-', 'top_prod': '-', 'source': 'Catatan Fisik Sales (Weekend)'}
]

# Enrich existing entries with phone numbers from handwritten notes
enrichment = {
    'sumberarthacell': {'phone': '081391264017', 'notes': 'Ibu Helena - Bertemu pemilik'},
    'berrycell': {'phone': '085122770354', 'status': 'Daftar Doripay', 'notes': 'Sudah daftar, minta fitur transfer bank'},
    'mastercell': {'phone': '085799802345', 'notes': 'Bertemu pemilik'},
    'starcell': {'phone': '089688789876', 'notes': 'Memahami apk'},
    'moncercell': {'phone': '085743766663', 'notes': 'Bertemu pemilik'},
    '88cell': {'phone': '085741318888', 'notes': 'Ibu Yuyun - Sedang mempelajari'},
    'tcell': {'phone': '0895703177201', 'notes': 'Perlu follow-up pemilik'},
    'falincell': {'status': 'Sudah transaksi Doripay', 'notes': 'Daftar + isi saldo'},
    'febrycell': {'status': 'Sudah transaksi Doripay', 'notes': 'Sudah melakukan transaksi'}
}

for item in sheet_entries:
    k = norm(item['name'])
    if k in enrichment:
        if enrichment[k].get('phone') and not item['phone']:
            item['phone'] = enrichment[k]['phone']
        if enrichment[k].get('status'):
            item['status'] = enrichment[k]['status']
        if enrichment[k].get('notes'):
            item['notes'] = item['notes'] + ' | ' + enrichment[k]['notes'] if item['notes'] else enrichment[k]['notes']

all_records = sheet_entries + manual_additions
print(f"Total consolidated records: {len(all_records)}")

with open('/opt/data/doripay-sales-dashboard/records.json', 'w') as f:
    json.dump(all_records, f, indent=2)
print("Saved to /opt/data/doripay-sales-dashboard/records.json")
