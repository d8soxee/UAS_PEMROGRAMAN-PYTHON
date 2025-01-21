import requests

BASE_URL = "http://127.0.0.1:5000"

def display_menu():
    print("\n=== Sistem Penitipan Barang ===")
    print("1. Titip Barang")
    print("2. Lihat Barang Dititipkan")
    print("3. Lihat Barang Diambil")
    print("4. Ambil Barang")
    print("5. Ubah Barang")
    print("6. Hapus Barang")
    print("7. Keluar")

def titip_barang():
    nama = input("Masukkan nama barang: ")
    pemilik = input("Masukkan nama pemilik: ")
    item = {"id": len(requests.get(f"{BASE_URL}/items").json()['stored_items']) + 1, 
            "nama": nama, 
            "pemilik": pemilik}
    response = requests.post(f"{BASE_URL}/items", json=item)
    print(response.json())

def lihat_barang():
    response = requests.get(f"{BASE_URL}/items")
    print(response.json())

def lihat_barang_diambil():
    response = requests.get(f"{BASE_URL}/taken-items")
    print(response.json())

def ambil_barang():
    item_id = int(input("Masukkan ID barang yang ingin diambil: "))
    response = requests.post(f"{BASE_URL}/items/take/{item_id}")
    print(response.json())

def ubah_barang():
    item_id = int(input("Masukkan ID barang yang ingin diubah: "))
    nama_baru = input("Masukkan nama baru: ")
    pemilik_baru = input("Masukkan pemilik baru: ")
    updated_item = {"nama": nama_baru, "pemilik": pemilik_baru}
    response = requests.put(f"{BASE_URL}/items/{item_id}", json=updated_item)
    print(response.json())

def hapus_barang():
    item_id = int(input("Masukkan ID barang yang ingin dihapus: "))
    response = requests.delete(f"{BASE_URL}/items/{item_id}")
    print(response.json())

if __name__ == '__main__':
    while True:
        display_menu()
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            titip_barang()
        elif pilihan == '2':
            lihat_barang()
        elif pilihan == '3':
            lihat_barang_diambil()
        elif pilihan == '4':
            ambil_barang()
        elif pilihan == '5':
            ubah_barang()
        elif pilihan == '6':
            hapus_barang()
        elif pilihan == '7':
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
