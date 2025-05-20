import requests
import os

# Telifsiz görsellerin URL'leri
images = {
    'logo.png': 'https://raw.githubusercontent.com/your-username/your-repo/main/logo.png',  # Logo için özel bir logo tasarlamanız gerekecek
    'hero-bg.jpg': 'https://images.unsplash.com/photo-1497366216548-37526070297c?w=1920&h=1080&fit=crop',  # Modern ofis görseli
    'about-us.jpg': 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&h=600&fit=crop',  # Ekip çalışması
    'blog-1.jpg': 'https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&h=600&fit=crop',  # Teknoloji
    'blog-2.jpg': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=600&fit=crop',  # Siber güvenlik
    'blog-3.jpg': 'https://images.unsplash.com/photo-1551434678-e076c223a692?w=800&h=600&fit=crop',  # İş toplantısı
    'client-1.png': 'https://cdn.worldvectorlogo.com/logos/google-2015.svg',  # Google
    'client-2.png': 'https://cdn.worldvectorlogo.com/logos/microsoft-5.svg',  # Microsoft
    'client-3.png': 'https://cdn.worldvectorlogo.com/logos/aws-2.svg',  # AWS
    'client-4.png': 'https://cdn.worldvectorlogo.com/logos/ibm-1.svg',  # IBM
    'client-5.png': 'https://cdn.worldvectorlogo.com/logos/intel-6.svg',  # Intel
    'client-6.png': 'https://cdn.worldvectorlogo.com/logos/sap-3.svg',  # SAP
    'pattern.png': 'https://www.transparenttextures.com/patterns/cubes.png'  # Arka plan deseni
}

# images klasörünü oluştur
if not os.path.exists('images'):
    os.makedirs('images')

# Her görseli indir
for filename, url in images.items():
    print(f'İndiriliyor: {filename}')
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(os.path.join('images', filename), 'wb') as f:
                f.write(response.content)
            print(f'Başarıyla kaydedildi: {filename}')
        else:
            print(f'Hata: {filename} indirilemedi - HTTP {response.status_code}')
    except Exception as e:
        print(f'Hata: {filename} indirilemedi - {str(e)}') 