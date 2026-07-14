# W3-B3: Operator Bayangan — Analisis & Solusi

## Ringkasan Challenge
- **Kategori**: Recon / OSINT (Hard, 400 pts)
- **Target**: https://5b016909-ctf.dsg.id/
- **Misi**: Identifikasi kode operasional di balik alias "n0ct4lys1s"

---

## Artefak yang Ditemukan

### Halaman Publik (6 file)
| # | File | Isi Penting |
|---|------|-------------|
| 1 | `index.html` | Daftar artefak (6 file publik) |
| 2 | `forum_post.html` | Post forum + **HTML comment: epoch 1704067200** + **UID-9182** |
| 3 | `pgp_pubkey.asc` | PGP public key (RSA 2048, fingerprint ABCD 1234 EFGH 5678) |
| 4 | `profile_analysis.txt` | Profil operator, menyebut epoch 1704067200 relevan |
| 5 | `persona_cross.json` | 3 alias: n0ct4lys1s, azure_ghost_77, azknight |
| 6 | `operator_note.txt` | **Formula kode operasional** |
| 7 | `decoy_token.txt` | **JEBAKAN**: N0CT-4LYS-1S99 |

### Halaman Tersembunyi (dari robots.txt)
| Path | Status | Isi |
|------|--------|-----|
| `/archive/` | ✅ Accessible | `archived_post.html` — **kunci sesi: 756b615f696e757a61** |
| `/private/` | ❌ 403 Forbidden | Diblokir |

### Halaman Navigasi
- `profil.html` — menyebut "Total 8 file artefak"
- `analisis.html` — status investigasi aktif

---

## Dekode Kode Operasional

### Formula (dari `operator_note.txt`):
```
Kode operasional = Part1 - Part2 - Part3

Part1 = kunci sesi (dari arsip forum)
Part2 = konversi epoch join ke format YYYYMMDD  
Part3 = XOR(Part1_pertama_5_char_as_bytes, key_byte=0x1F) lalu hex-encode
```

### Part1: Kunci Sesi
- Dari `/archive/archived_post.html`: **`756b615f696e757a61`**
- Decoded: `uka_inuza`

### Part2: Epoch → YYYYMMDD
- Epoch `1704067200` → **2024-01-01 00:00:00 UTC** → **`20240101`**

### Part3: XOR Computation
- "Part1_pertama_5_char_as_bytes" = first 5 chars of Part1 as bytes
- Part1 = `756b615f696e757a61`, first 5 chars = `756b6` (as ASCII bytes) **ATAU** decoded first 5 = `uka_i`

**Option A** (first 5 chars of hex string as ASCII):
```
'7' ^ 0x1F = 0x28, '5' ^ 0x1F = 0x2a, '6' ^ 0x1F = 0x29, 'b' ^ 0x1F = 0x7d, '6' ^ 0x1F = 0x29
Part3 = 282a297d29
```

**Option B/C** (first 5 decoded bytes = "uka_i"):
```
'u'(0x75) ^ 0x1F = 0x6a, 'k'(0x6b) ^ 0x1F = 0x74, 'a'(0x61) ^ 0x1F = 0x7e, '_'(0x5f) ^ 0x1F = 0x40, 'i'(0x69) ^ 0x1F = 0x76
Part3 = 6a747e4076
```

---

## 🏁 Flag Candidates

| # | Flag |
|---|------|
| 1 | `CTF{756b615f696e757a61-20240101-6a747e4076}` |
| 2 | `CTF{756b615f696e757a61-20240101-282a297d29}` |
| 3 | `CTFIND{756b615f696e757a61-20240101-6a747e4076}` |
| 4 | `CTFIND{756b615f696e757a61-20240101-282a297d29}` |

> Coba submit dari atas ke bawah!
