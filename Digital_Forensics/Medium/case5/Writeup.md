# Writeup Case 5

**Author:** Abdul Latif

## Daftar Barang Bukti (Asli)
- `key_hint.txt`
- `partial_source.c`
- `config.bin`

## Langkah-Langkah Penyelesaian:
1. **Analisis Awal**: Barang bukti yang diberikan adalah file `key_hint.txt`, `partial_source.c`, dan `config.bin`. 
2. **Pemahaman Algoritma**: Dari file `partial_source.c`, analis mengetahui bahwa file `config.bin` dienkripsi dengan algoritma XOR berulang. Kunci XOR disimpan di 4 byte pertama pada file tersebut.
3. **Ekstraksi Kunci**: Berdasarkan `key_hint.txt` dan inspeksi pada file `config.bin`, 4 byte pertamanya adalah `4B 33 61 5F` (dalam ASCII: `K3a_`).
4. **Dekripsi Payload**: Untuk menyelesaikannya, analis membuat sebuah skrip Python (tool buatan) untuk membaca file `config.bin`, mengambil 4 byte pertama sebagai kunci, lalu melakukan dekripsi XOR (dengan operasi `data[i] ^ key[(i-4)%4]`) terhadap sisa data mulai dari byte ke-5 hingga akhir.
5. **Mendapatkan Flag**: Hasil dari eksekusi skrip dekripsi tersebut mengekstrak payload tersembunyi yang berisi flag.

**FLAG:** `flag{xor_k3y_K33l_3xtr4ct3d}`
