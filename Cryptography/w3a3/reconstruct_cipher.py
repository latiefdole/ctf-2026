def untranspose(ciphertext, W=4):
    N = len(ciphertext)
    R = N // W
    S = [None] * N
    idx = 0
    for c in range(W):
        for r in range(R):
            S[r * W + c] = ciphertext[idx]
            idx += 1
    return "".join(S)

def solve():
    samples = [
        ("hello_world", "igkt_ssvrsg_"),
        ("kode_sandi_lima", "a_roglodrq_qtfs_"),
        ("berjuta_xyz_vwq", "wxbctznvkqmjp___"),
        ("fungsi_program", "ylkqxogdf_u_uhk_"),
        ("teknik_cipher_bu", "zooktah_a_iwfetx")
    ]
    
    mapping = {}
    rev_mapping = {}
    
    for p, c in samples:
        s = untranspose(c, 4)
        print(f"Plaintext:  {p}")
        print(f"Substituted:{s}")
        for pi, si in zip(p, s):
            if pi.isalpha():
                if pi in mapping and mapping[pi] != si:
                    print(f"[!] Conflict for {pi}: {mapping[pi]} vs {si}")
                mapping[pi] = si
                rev_mapping[si] = pi
        print()
        
    print("Alphabet mapping (Plain -> Cipher):")
    sorted_map = sorted(mapping.items())
    for pi, si in sorted_map:
        print(f"{pi} -> {si}")
        
    print("\nMissing plain letters:")
    all_letters = set("abcdefghijklmnopqrstuvwxyz")
    missing_plain = all_letters - set(mapping.keys())
    print(sorted(list(missing_plain)))
    
    print("\nMissing cipher letters:")
    missing_cipher = all_letters - set(mapping.values())
    print(sorted(list(missing_cipher)))
    
    # Let's see if we can deduce the mapping pattern.
    # Often it's a shift or key-based alphabet.
    # Let's print the plain alphabet and corresponding cipher.
    plain_alpha = "abcdefghijklmnopqrstuvwxyz"
    cipher_alpha = []
    for c in plain_alpha:
        cipher_alpha.append(mapping.get(c, "?"))
    print("\nPlain:  " + plain_alpha)
    print("Cipher: " + "".join(cipher_alpha))
    
    # Let's check the target ciphertext
    target = "y_iwqsettlqokkouh_is"
    untrans_target = untranspose(target, 4)
    print(f"\nTarget ciphertext: {target}")
    print(f"Untransposed target: {untrans_target}")

if __name__ == '__main__':
    solve()
