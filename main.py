import requests
import sys
from termcolor import colored
import socket
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed # <--- IMPORT BARU

def check_subdomain(domain, subdomain):
    """
    Fungsi ini TIDAK BERUBAH. Setiap thread akan menjalankan fungsi ini.
    """
    full_url = f"http://{subdomain}.{domain}"
    try:
        ip_address = socket.gethostbyname(f"{subdomain}.{domain}")
        response = requests.get(full_url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
        
        if response.status_code == 200:
            status_color = 'green'
        elif 300 <= response.status_code < 400:
            status_color = 'yellow'
        else:
            status_color = 'red'
            
        status_text = colored(f"[{response.status_code}]", status_color)
        ip_text = colored(f"[{ip_address}]", 'cyan')
        
        result_line = f"{full_url.ljust(35)} {ip_text.ljust(25)} {status_text}"
        return result_line
        
    except (socket.gaierror, requests.exceptions.RequestException):
        return None

def main():
    """
    Fungsi utama untuk menjalankan alat.
    """
    if len(sys.argv) != 2:
        print("Penggunaan: python main.py <domain.com>")
        sys.exit(1)

    target_domain = sys.argv[1]
    
    wordlist_file = "wordlist.txt"
    try:
        with open(wordlist_file, 'r') as file:
            subdomain_list = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(colored(f"❌ Error: File '{wordlist_file}' tidak ditemukan!", "red"))
        sys.exit(1)
    
    found_results = []

    print("-" * 60)
    print(f"🚀 Memindai {len(subdomain_list)} subdomain untuk: {colored(target_domain, 'blue')} dengan multithreading")
    print("-" * 60)

    # --- BAGIAN UTAMA MULTITHREADING ---
    if not subdomain_list:
        print(colored("Wordlist kosong!", "yellow"))
    else:
        # Menentukan jumlah thread/pekerja. Bisa diubah sesuai kebutuhan.
        MAX_WORKERS = 100 

        # Membuat 'pool' atau kumpulan thread
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            # Memberikan setiap pekerjaan (cek subdomain) ke thread
            # 'future' adalah representasi pekerjaan yang sedang/akan berjalan
            futures = [executor.submit(check_subdomain, target_domain, sub) for sub in subdomain_list]

            # Membuat progress bar yang memproses hasil saat pekerjaan SELESAI
            pbar = tqdm(as_completed(futures), total=len(subdomain_list), desc=colored("Scanning", "cyan"), unit="sub")
            
            for future in pbar:
                result = future.result() # Ambil hasil dari pekerjaan yang sudah selesai
                if result:
                    # Langsung cetak hasilnya di bawah progress bar
                    # Kita tidak perlu lagi pbar.write() karena output sudah dipisahkan
                    print(result) 
                    found_results.append(result)
    
    print("-" * 60)
    if not found_results and subdomain_list:
        print(colored("Tidak ada subdomain yang ditemukan dari daftar.", "yellow"))
    elif found_results:
        # Cetak ulang semua hasil yang ditemukan di akhir agar rapi
        print(colored(f"\n✅ Ditemukan {len(found_results)} Subdomain:", "green"))
        for res in sorted(found_results):
            print(res)
        print("\nPemindaian selesai!")
    print("-" * 60)

if __name__ == "__main__":
    main()