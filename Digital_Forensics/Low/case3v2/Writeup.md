# Writeup CTF - Digital Forensics: Case 3v2

**Author**: Abdul Latif

## Daftar File
### Barang Bukti (Asli)
- `hint.txt`
- `image.png`

### Tools / Output Analis
- Skrip Python ekstraksi steganografi (dibuat/digunakan oleh analis secara temporer)

## Analisis Kasus
Barang bukti yang diberikan adalah sebuah gambar bernama `image.png` beserta file `hint.txt`. Petunjuk menyebutkan bahwa ada informasi yang "tidak terlihat secara visual dan tersembunyi di dalam gambar ini". Petunjuk ini mengarah pada penerapan teknik Steganography, spesifiknya menggunakan metode **LSB (Least Significant Bit)**, di mana data rahasia disisipkan pada bit terkecil dari representasi warna piksel gambar.

## Langkah-langkah Penyelesaian

**Langkah 1: Identifikasi Steganografi LSB**
Berdasarkan petunjuk, analis memutuskan untuk mengekstrak data yang berada pada bit paling tidak signifikan (LSB) dari gambar `image.png`.

**Langkah 2: Pemrosesan Gambar**
Analis menggunakan sebuah skrip Python (memanfaatkan library Pillow/PIL) untuk memproses nilai piksel dari gambar. Skrip ini bertugas mengambil nilai dari channel pertama pada setiap piksel, mengekstrak bit terendah dengan operasi *bitwise AND 1*, dan menampungnya ke dalam sebuah buffer array.

**Langkah 3: Menyusun Byte Menjadi Karakter**
Bit-bit yang berhasil diekstrak kemudian dirangkai menjadi kumpulan byte (per 8 bit). Setiap byte selanjutnya dikonversi ke dalam format karakter ASCII. Setelah ratusan piksel pertama didecode, teks plain-text berupa flag yang tersembunyi di layer LSB akhirnya muncul secara utuh.

## Flag
FLAG: `flag{p1ks3l_t3rs3mbunyi_lsb!}`
