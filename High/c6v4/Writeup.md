# Writeup c6v4
**Author:** Abdul Latif

## Inventarisasi File
**Barang Bukti (Asli):**
- `feistel_enc` (Executable binary dari soal)
- `disasm.txt` (File berisi hasil disassembly instruksi program)
- `keys.txt` (File berisi daftar kunci ronde)
- `ciphertext.txt` (File teks terenkripsi)
- `test_vector.txt` (File vektor uji untuk memvalidasi algoritma)

**Tools/Skrip/Output Analis:**
- `solve_c6v4.py` (Skrip dekripsi Python yang dirancang oleh analis)

## Langkah-langkah Analisis
1. Analis memulai investigasi terhadap barang bukti dan menginspeksi file `disasm.txt`. Berdasarkan alur instruksi assembly di dalamnya, analis mengidentifikasi penerapan algoritma kriptografi simetris berbasis *Feistel Network* dengan 4 ronde enkripsi.
2. Analis menelusuri secara spesifik operasi pada tiap ronde. Analis mendapati adanya operasi rotasi ke kiri sebanyak 5 bit (ROL 5), operasi XOR antar blok, serta operasi XOR dengan kunci ronde. Nilai-nilai kunci (K1 hingga K4) ditarik dari file barang bukti `keys.txt` (K1=0xDEADBEEF, K2=0xCAFEBABE, K3=0x13371337, K4=0xABCDABCD).
3. Untuk memvalidasi logika dekripsi algoritma tersebut, analis mengembangkan skrip `solve_c6v4.py`. Skrip ini terlebih dulu diuji keakuratannya menggunakan parameter masukan dan keluaran yang terdapat pada file `test_vector.txt`.
4. Setelah skrip diverifikasi bebas dari *bug*, analis menjalankan skrip `solve_c6v4.py` dengan input data dari `ciphertext.txt`. Skrip beroperasi secara berlawanan arah dengan membalik *Feistel Network* dari belakang (ronde K4 menuju K1) agar teks bisa didekripsi seutuhnya.
5. Hasil keluaran dari skrip menampilkan *plaintext* asli yang memuat *flag*.

**FLAG:** `flag{kunci_cermin_symmetry}`
