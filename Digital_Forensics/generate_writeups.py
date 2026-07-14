import os
import glob

base_dir = r"C:\Users\ICT-12\Documents\CTF\Digital_Forensics"
author = "Abdul Latif"

def generate_writeup(folder_path, folder_name):
    files = os.listdir(folder_path)
    # Filter out directories
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]
    
    # Read clues
    description = ""
    for f in files:
        if "readme" in f.lower() or "note" in f.lower() or "hint" in f.lower() or "narasi" in f.lower():
            try:
                with open(os.path.join(folder_path, f), 'r', encoding='utf-8', errors='ignore') as text_file:
                    description += f"### Isi dari `{f}`:\n"
                    description += "> " + text_file.read().replace('\n', '\n> ') + "\n\n"
            except:
                pass
                
    if not description:
        description = "Deskripsi spesifik tidak ditemukan. Analisis didasarkan pada file bukti yang tersedia."

    tools_used = []
    steps = ""
    
    if any(f.endswith('.py') for f in files):
        py_files = [f for f in files if f.endswith('.py')]
        tools_used.extend(py_files)
        steps += "1. Ditemukan script analisis khusus: " + ", ".join(f"`{x}`" for x in py_files) + ".\n"
        steps += "2. Menjalankan script tersebut untuk mengekstrak atau mendekode informasi dari barang bukti.\n"
        steps += "3. Menganalisis output yang dihasilkan script untuk menemukan flag atau informasi rahasia.\n"
    
    if any("steghide" in f.lower() for f in files):
        steps += "- Menggunakan **Steghide** untuk mengekstrak file tersembunyi dari gambar/media.\n"
    if any("pcap" in f.lower() for f in files):
        steps += "- Melakukan analisis jaringan menggunakan **Wireshark** untuk menelusuri traffic yang mencurigakan.\n"
    if any(f.endswith('.bin') for f in files):
        steps += "- Menganalisis file binary (`.bin`) dengan hex editor atau tools reverse engineering untuk mencari pola/key.\n"
    if any("jpeg" in f.lower() or "jpg" in f.lower() or "png" in f.lower() for f in files):
        steps += "- Melakukan analisis metadata gambar (EXIF/GPS) dan forensik steganografi (zsteg, aperisolve, exiftool).\n"

    if not steps:
        steps = "1. Melakukan pemeriksaan tipe file menggunakan `file` atau `binwalk`.\n2. Menganalisis isi string dan metadata dari file yang diberikan.\n3. Mencari pola encoding atau kriptografi standar."

    writeup_content = f"""# Write-up CTF Digital Forensics: {folder_name}

**Author:** {author}
**Kategori:** Digital Forensics / Steganography / OSINT

---

## 1. Deskripsi Kasus

{description}

## 2. File Barang Bukti & Tools

Berikut adalah daftar file yang ditemukan pada kasus ini:
"""
    for f in files:
        writeup_content += f"- `{f}`\n"

    writeup_content += f"""
## 3. Metodologi / Langkah Penyelesaian

{steps}

## 4. Hasil Analisis / Flag

*Catatan: Eksekusi tools di atas akan menampilkan flag atau data yang dicari. Jika menggunakan custom script (Python), hasilnya dapat dilihat pada output terminal.*

---
*Dokumen ini disusun oleh {author} sebagai bagian dari dokumentasi CTF.*
"""
    
    writeup_path = os.path.join(folder_path, "Writeup.md")
    with open(writeup_path, "w", encoding="utf-8") as wf:
        wf.write(writeup_content)

for item in os.listdir(base_dir):
    item_path = os.path.join(base_dir, item)
    if os.path.isdir(item_path):
        generate_writeup(item_path, item)

print("Writeups generated successfully for all folders.")
