import math

def solve():
    # Read pubkey.txt
    with open("C:/Users/ICT-12/Documents/CTF/w4a1/pubkey.txt", "r") as f:
        lines = f.readlines()
        n = int(lines[0].split("=")[1].strip())
        e = int(lines[1].split("=")[1].strip())

    # Read ciphertext.txt
    with open("C:/Users/ICT-12/Documents/CTF/w4a1/ciphertext.txt", "r") as f:
        lines = f.readlines()
        c = int(lines[0].split("=")[1].strip())

    def is_square(x):
        if x < 0: return False
        sq = int(math.isqrt(x))
        return sq * sq == x

    # Continued fractions expansion of e/n
    cf = []
    temp_e, temp_n = e, n
    while temp_n:
        cf.append(temp_e // temp_n)
        temp_e, temp_n = temp_n, temp_e % temp_n

    # Convergents of the continued fraction
    p0, p1 = 1, cf[0]
    q0, q1 = 0, 1
    convergents = [(p1, q1)]
    for a in cf[1:]:
        p2 = a * p1 + p0
        q2 = a * q1 + q0
        convergents.append((p2, q2))
        p0, p1 = p1, p2
        q0, q1 = q1, q2

    # Attempt to factor n using each convergent
    for k, d in convergents:
        if k == 0: continue
        if (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            b = n - phi + 1
            discr = b*b - 4*n
            if discr >= 0 and is_square(discr):
                root = math.isqrt(discr)
                p = (b - root) // 2
                q = (b + root) // 2
                if p * q == n:
                    print(f"[+] Found private exponent d: {d}")
                    m = pow(c, d, n)
                    m_hex = hex(m)[2:]
                    if len(m_hex) % 2 != 0: 
                        m_hex = '0' + m_hex
                    flag = bytes.fromhex(m_hex).decode('utf-8', errors='ignore')
                    print(f"[+] Decrypted Flag: {flag}")
                    return flag
    print("[-] Wiener's attack failed.")
    return None

if __name__ == "__main__":
    solve()
