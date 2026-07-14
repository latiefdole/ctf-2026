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

def decrypt():
    plain_alpha = "abcdefghijklmnopqrstuvwxyz"
    cipher_alpha = "qwertyuiopasdfghjklzxcvbnm"
    
    # Build decryption mapping (Cipher -> Plain)
    dec_map = {c: p for p, c in zip(plain_alpha, cipher_alpha)}
    
    target = "y_iwqsettlqokkouh_is"
    untrans_target = untranspose(target, 4)
    print(f"Untransposed target: {untrans_target}")
    
    decrypted_chars = []
    for c in untrans_target:
        if c.isalpha():
            decrypted_chars.append(dec_map[c])
        else:
            decrypted_chars.append(c)
            
    decrypted_str = "".join(decrypted_chars)
    print(f"Decrypted: {decrypted_str}")

if __name__ == '__main__':
    decrypt()
