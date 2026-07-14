# w4a1: Kunci Kecil Terekspos — SOLVED ✅

Target: `w4a1/pubkey.txt` dan `w4a1/ciphertext.txt`

## 🚩 FLAG
```
flag{wiener_kunci_kecil_terekspos}
```

## Analisis & Solusi

### 1. Identifikasi Kelemahan
- Diberikan modulus RSA $n$ sepanjang ~1024-bit dan eksponen publik $e$ yang sangat besar (hampir menyamai ukuran $n$).
- Ketika $e$ berukuran mendekati $n$, eksponen privat $d$ biasanya bernilai kecil.
- Teorema Wiener menyatakan bahwa jika:
  $$d < \frac{1}{3} n^{1/4}$$
  maka $d$ dapat ditemukan secara efisien dalam waktu polinomial menggunakan fraksi berkelanjutan (continued fractions) dari $\frac{e}{n}$.

### 2. Implementasi Serangan
Skrip [solve_w4a1.py](file:///C:/Users/ICT-12/Documents/CTF/w4a1/solve_w4a1.py):
- Menghitung koefisien fraksi berkelanjutan dari $\frac{e}{n}$.
- Menghasilkan convergents $\frac{k}{d}$ berturut-turut.
- Untuk setiap convergent, menebak nilai $\phi(n) = \frac{ed - 1}{k}$ dan menyelesaikan persamaan kuadrat untuk memperoleh faktor $p$ dan $q$.
- Setelah $d$ ditemukan ($d = 1124952985623315647$), dekripsi ciphertext $c$ menghasilkan flag: `flag{wiener_kunci_kecil_terekspos}`.
