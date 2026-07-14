# Writeup CTF - Digital Forensics: Case 3

**Author**: Abdul Latif

## Daftar File
### Barang Bukti (Asli)
- `narasi.txt`
- `traffic.pcap`

### Tools / Output Analis
- Tool analisis jaringan (misal: Wireshark / skrip Python buatan analis)

## Analisis Kasus
Barang bukti yang diberikan adalah file `narasi.txt` dan `traffic.pcap`. Berdasarkan file `narasi.txt`, terdapat indikasi komunikasi tidak sah berupa eksfiltrasi data yang tersembunyi di dalam lalu lintas jaringan. Analis ditugaskan untuk menelusuri paket-paket pada `traffic.pcap` demi menemukan data yang disembunyikan tersebut.

## Langkah-langkah Penyelesaian

**Langkah 1: Analisis Paket Jaringan**
Sebagai langkah awal, analis meninjau file `traffic.pcap` secara menyeluruh. Karena petunjuk mengarah pada data yang disembunyikan, analis memindai string dan pola data yang tidak wajar pada muatan (payload) paket jaringan.

**Langkah 2: Ekstraksi Data Suspect**
Melalui pemindaian tersebut, analis menemukan sebuah string yang aneh dan dicurigai sebagai data eksfiltrasi. String tersebut menggunakan format pengkodean Base64, yaitu:
`ZmxhZ3twY2FwX2MyX3IzZl9iNHMzNjRfM3hmMWx9`

**Langkah 3: Decoding Payload**
Untuk membaca isi pesan tersebut, analis mendecode string Base64 yang ditemukan. Hasil decoding dari string Base64 tersebut mengembalikan sebuah pesan dalam bentuk plain-text yang ternyata merupakan format dari flag.

## Flag
FLAG: `flag{pcap_c2_r3f_b4s364_3xf1l}`
