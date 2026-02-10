# --- CONFIG BOT (Replace with your own) ---
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

# --- CORE LOGIC ---
def get_location_info(ip):
    try:
        # Hit IP-API buat ambil geo data
        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response['status'] == 'success':
            return {
                "city": response.get("city", "Unknown"),
                "country": response.get("country", "Unknown"),
                "isp": response.get("isp", "Unknown"),
                "lat": response.get("lat", 0),
                "lon": response.get("lon", 0)
            }
    except:
        pass
    return None

def send_telegram_notif(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        # Kirim data ke Telegram
        requests.post(url, data=payload, timeout=5)
    except:
        pass # Biar web gak crash kalau bot error

# --- ROUTES ---
@app.route('/')
def index():
    # Ambil IP pengunjung
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    geo = get_location_info(ip_addr)

    # notifikasi
    if geo:
        msg = (
            f" *Notifikasi Kunjungan Baru*\n\n"
            f" *Lokasi:* {geo['city']}, {geo['country']}\n"
            f" *ISP:* {geo['isp']}\n"
            f" *IP Address:* `{ip_addr}`\n\n"
            f" [Buka Google Maps](https://www.google.com/maps?q={geo['lat']},{geo['lon']})\n"
            f"---"
        )
    else:
        msg = f" *Notifikasi Kunjungan Baru*\nIP: `{ip_addr}` (Lokasi tidak terdeteksi)"

    send_telegram_notif(msg)

    # Render halaman portfolio
    return render_template('index.html', d=data)

if __name__ == '__main__':
    app.run(debug=True)
