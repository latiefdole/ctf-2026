#!/usr/bin/env python3
"""
w4b1 — Git-leaked API key dipakai ulang sebagai kunci AES.

Attack chain:
 1. `git log -p` pada repo bocoran (repo_dika.tar.gz / folder .git) mengungkap
    commit "feat: tambah konfigurasi deployment" yang menaruh api_key ASLI:
        "api_key": "TnNzU2VjdXJlS2V5MjAyNF9MZWFrQnlEaWth"
    Commit berikutnya me-redact-nya jadi "REDACTED_USE_ENV_VAR", TETAPI nilai
    lama tetap tertinggal di histori git (blob 40040c5...).
 2. api_key adalah Base64 -> "NssSecureKey2024_LeakByDika".
 3. rahasia.enc (48 byte = 3 blok) dienkripsi AES-256-CBC.
    Kunci = password ASCII di-pad NUL ke 32 byte.

Struktur ciphertext: 3 blok CBC dengan IV eksternal (acak, satu kali pakai).
 - Blok plaintext ke-2 = D(ct[1]) XOR ct[0]  -> TIDAK bergantung IV
   => "oper_api_leaked}"  (terpulihkan pasti)
 - Blok ke-3 = padding PKCS#7 penuh (0x10 * 16)
 - Blok ke-1 = "flag{" + ... + "devel"  -> bergantung IV.
   IV acak ini TIDAK ikut bocor di repo, sehingga 6 karakter tengah flag
   tidak dapat dipulihkan secara deterministik. Bentuk flag:
       flag{______developer_api_leaked}
"""
import base64
from Crypto.Cipher import AES

API_KEY_B64 = "TnNzU2VjdXJlS2V5MjAyNF9MZWFrQnlEaWth"


def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def main():
    password = base64.b64decode(API_KEY_B64)          # b"NssSecureKey2024_LeakByDika"
    print(f"[+] api_key (git-leaked, decoded): {password.decode()}")

    key = password.ljust(32, b"\x00")                 # AES-256 key, NUL-padded
    data = open("rahasia.enc", "rb").read()
    ecb = AES.new(key, AES.MODE_ECB)

    ct = [data[i:i + 16] for i in range(0, len(data), 16)]

    # Blok ke-2 & ke-3 tidak bergantung IV eksternal.
    blk1 = xor(ecb.decrypt(ct[1]), ct[0])
    blk2 = xor(ecb.decrypt(ct[2]), ct[1])
    print(f"[+] blok-2 (IV-independent)     : {blk1!r}")
    print(f"[+] blok-3 (padding)            : {blk2!r}")
    print(f"[=] tail plaintext terpulihkan  : ...{blk1.decode()}")
    print(f"[=] bentuk flag                 : flag{{______developer_api_leaked}}")


if __name__ == "__main__":
    main()
