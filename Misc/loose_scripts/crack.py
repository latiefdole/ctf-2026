import bcrypt, sys, time

h = b"$2b$12$4eHOHLQ6NUjNYsKZ6qm9WeMZ9iTM5Utg5N.EtzPP2Y.acNq5Azv8y"
words = [w.strip() for w in open(sys.argv[1], encoding="utf-8") if w.strip()]
print(f"Trying {len(words)} candidates (bcrypt cost 12)...", flush=True)
start = time.time()
found = None
for i, w in enumerate(words, 1):
    cand = w.lower()
    if bcrypt.checkpw(cand.encode(), h):
        found = cand
        break
    if i % 10 == 0:
        print(f"  {i}/{len(words)} tested ({time.time()-start:.1f}s)", flush=True)
if found:
    print(f"\n[+] FOUND PASSWORD: {found}")
else:
    print(f"\n[-] Not found in this list ({time.time()-start:.1f}s)")
