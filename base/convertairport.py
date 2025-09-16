import csv, json

csv_file = 'airports.csv'   # arquivo do OurAirports
out_file = 'airports.js'    # saída em formato JS

data = {}
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ident = row.get('ident')  # ICAO/IATA identifier
        if not ident:
            continue

        # filtrar apenas grandes e médios
        airport_type = row.get('type', '').strip().lower()
        if airport_type not in ('large_airport', 'medium_airport'):
            continue

        # latitude / longitude
        try:
            lat = float(row.get('latitude_deg') or 0)
            lon = float(row.get('longitude_deg') or 0)
        except:
            continue

        data[ident.upper()] = {
            'name': row.get('name'),
            'lat': lat,
            'lon': lon,
            'municipality': row.get('municipality'),
            'country': row.get('iso_country'),
            'iata': row.get('iata_code'),
            'type': airport_type
        }

# salvar em .js (para importar no HTML)
with open(out_file, 'w', encoding='utf-8') as f:
    f.write("const airports = ")
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write(";")

print(f"✅ Arquivo '{out_file}' gerado com {len(data)} aeroportos.")
