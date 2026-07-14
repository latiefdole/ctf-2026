# W2-B3: Infrastruktur Ancaman — Data Konsolidasi

## ✅ SOLVED
- **FLAG: `flag{h3ndr4_w1c4ks0n0_r3dm1st_y0gy4!}`**
- **XOR KEY: `Yogyakarta2024K9mZ`** (18 char, repeating)
  - `Yogyakarta` (kota WHOIS) + `2024` (tahun domain) + `K9mZ` (token bocor, dari `Zm9K0027604071`)


Target: https://3c4819c9-ctf.dsg.id/

## File terkumpul (folder ini)
- index.html, attacker_cv.html
- whois_dump.txt, linkedin_export.txt, leaked_config.txt, email_thread.txt
- company_doc.html
- robots.txt  → membocorkan: /whois_dump.txt, /leaked_config.txt, /company_doc.html, /email_thread.txt

## Identitas pelaku
- Nama: **Hendra Wicaksono**
- Alias: **RedMist_ID**
- Domain: **redmist-id.net** (created 2024-01-01, IP 103.28.91.47, SSH port 2222)
- Email: redmist@protonmail.com / hendra.wicaksono@mandiri-digital.id
- Org: Mandiri Digital Infrastruktur
- Alamat: Jl. Parangtritis No. 47, **Yogyakarta**, DIY, 55188, ID
- Telp: +62.2746139821
- LinkedIn: linkedin.com/in/hendra-wicaksono-infra
- Pendidikan: Universitas Gadjah Mada (Teknik Informatika, 2011-2015)
- Mantan: PT Korban Finansial Indonesia (Senior Network Security Engineer, 2020-2023)

## TARGET UTAMA: DEPLOY_KEY (leaked_config.txt)
```
DEPLOY_KEY=PwMGHhoDUhwQEwZvRQUoDQYpaQFXJhNYBR9FEkZvSwQsQFl7JA==
KEY_ALGORITHM=custom-xor-b64
```
- base64-decoded = 37 byte
- hex: `3f03061e1a03521c1013066f4505280d0629690157261358051f4512466f4b042c40597b24`
- Catatan: "perlu konteks operasional lengkap untuk dekripsi"

### Status dekripsi (XOR berulang)
- Key = **"Yogyakarta"** → 11 char pertama BENAR: `flag{h3ndr_` lalu rusak.
  - keystream[0..10] = "YogyakartaY" → konsisten key diawali "Yogyakarta"
- Belum ketemu key penuh. Kemungkinan key = frasa lebih panjang gabungan beberapa sumber.
- Flag dipastikan format: `flag{h3ndr_...}`

### Kandidat key yang BELUM dicoba tuntas (buat kamu lanjut)
Petunjuk-petunjuk lain yang mungkin jadi bagian key:
- **Hash file IoC: `3f4a8d9e2b1c7056ab34ef90`** (24 hex = "skrip pemindai", company_doc.html) ← kuat
- X-Mailer-Token (email_thread, msg1): hex `5a6d394b30303237363034303731` → ascii **`Zm9K0027604071`**
  - "Zm9K..." mirip base64; `Zm9K` base64 = `foJ`? cek lagi.
- svc_network_mon (akun lama yg dibobol, company_doc)
- svc_redmist_deploy (service account, leaked_config)
- Registry Domain ID: 2387461923

## Decode helper (node)
```js
const data=Buffer.from("PwMGHhoDUhwQEwZvRQUoDQYpaQFXJhNYBR9FEkZvSwQsQFl7JA==","base64");
function dec(k){const o=Buffer.alloc(data.length);for(let i=0;i<data.length;i++)o[i]=data[i]^k.charCodeAt(i%k.length);return o.toString("latin1");}
console.log(dec("Yogyakarta")); // flag{h3ndr_...rusak
```

## IoC dari company_doc.html
- Insiden 15 Jan 2024 @ PT Korban Finansial Indonesia
- Akun dibobol: **svc_network_mon** (disabled tapi tak dihapus dari AD)
- IP sumber: 103.28.91.47 | Domain C2: redmist-id.net
- **Hash file skrip: 3f4a8d9e2b1c7056ab34ef90**

## cf-email terenkripsi (attacker_cv) → redmist@protonmail.com
token: 027067666f6b71764272706d766d6c6f636b6e2c616d6f
