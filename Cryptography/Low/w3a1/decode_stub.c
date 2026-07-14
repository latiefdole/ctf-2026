/* Potongan decoder dari laporan analisis malware PT Proteksi Digital */
/* File ini hanya mengilustrasikan format - bukan kode lengkap        */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

/* Kunci XOR 4-byte - nilai asli telah diredaksi dalam laporan ini */
static uint8_t key[4] = {0x00, 0x00, 0x00, 0x00};

void decode_config(FILE *fp) {
    uint16_t len;
    while (fread(&len, 2, 1, fp) == 1) {
        uint8_t *buf = malloc(len);
        if (!buf) break;
        if (fread(buf, 1, len, fp) != len) { free(buf); break; }
        for (int i = 0; i < len; i++) {
            buf[i] ^= key[i % 4];
        }
        /* buf sekarang berisi string yang ter-decode */
        fwrite(buf, 1, len, stdout);
        fputc('\n', stdout);
        free(buf);
    }
}

int main(int argc, char *argv[]) {
    if (argc < 2) { fprintf(stderr, "Usage: %s <config.bin>\n", argv[0]); return 1; }
    FILE *fp = fopen(argv[1], "rb");
    if (!fp) { perror("fopen"); return 1; }
    decode_config(fp);
    fclose(fp);
    return 0;
}
