import re

with open('notes_raw.html', 'rb') as f:
    raw = f.read()

# Get the exact morse signals from HTML
signals = re.findall(rb'class="signal">(.*?)</div>', raw, re.DOTALL)
for i, sig in enumerate(signals):
    print(f'Signal {i+1} text: {sig.decode("utf-8")}')
    print(f'Signal {i+1} hex: {sig.hex()}')
    print()

# Check for hidden chars within the signal
for i, sig in enumerate(signals):
    hidden = [b for b in sig if b > 127 or (b < 32 and b not in (10, 13, 9))]
    if hidden:
        print(f'Signal {i+1} has hidden bytes: {[hex(b) for b in hidden]}')

# Non-ASCII bytes anywhere
non_vis = [(i, raw[i]) for i in range(len(raw)) if raw[i] > 127]
print(f'\nNon-ASCII bytes in file: {len(non_vis)}')

# Print full hexdump of the signal divs
for i, sig in enumerate(signals):
    print(f'\nSignal {i+1} char-by-char:')
    for j, b in enumerate(sig):
        if b > 127 or (b < 32 and b not in (10, 13, 9)):
            print(f'  HIDDEN at pos {j}: 0x{b:02X}')
