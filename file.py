#!/usr/bin/env python3
"""One-Time Pad (OTP) CLI - enkripsi & dekripsi.

Mode 1: Alfabet A-Z      -> C = (P + K) mod 26
Mode 2: ASCII printable  -> C = (P + K) mod 95  (karakter 32..126)

Key dibuat acak (secrets / CSPRNG) dengan panjang sama dengan plaintext.
"""
import secrets
import string

MATKUL_NAME = "KRIPTOGRAFI"
GROUP_MEMBERS = [
    "Delvina Salma Hidayah - 237006103",
    "Sherly Nandia Mathovani - 237006167"
]

ALPHA = string.ascii_uppercase                       # A-Z (26)
ASCII = "".join(chr(i) for i in range(32, 127))      # printable ASCII (95)

ALPHABETS = {"1": ALPHA, "2": ASCII}

def print_group_information():

    print(f"Nama Matakuliah : {MATKUL_NAME}")
    print("Anggota:")

    for member in GROUP_MEMBERS:
        print(f"- {member}")

    print()


def generate_key(length: int, alphabet: str) -> str:
    """Key random sepanjang plaintext."""
    return "".join(secrets.choice(alphabet) for _ in range(length))


def encrypt(plaintext: str, key: str, alphabet: str) -> str:
    n = len(alphabet)
    return "".join(
        alphabet[(alphabet.index(p) + alphabet.index(k)) % n]
        for p, k in zip(plaintext, key)
    )


def decrypt(ciphertext: str, key: str, alphabet: str) -> str:
    n = len(alphabet)
    return "".join(
        alphabet[(alphabet.index(c) - alphabet.index(k)) % n]
        for c, k in zip(ciphertext, key)
    )


def valid(text: str, alphabet: str) -> bool:
    return len(text) > 0 and all(ch in alphabet for ch in text)




def choose_mode() -> str | None:
    print("\nPilih jenis karakter:")
    print("  1. Alfabet A-Z")
    print("  2. String ASCII (karakter 32-126)")
    choice = input("Pilihan [1/2]: ").strip()
    if choice not in ALPHABETS:
        print("[!] Pilihan tidak valid.")
        return None
    return ALPHABETS[choice]


def do_encrypt() -> None:
    alphabet = choose_mode()
    if alphabet is None:
        return

    plaintext = input("Masukkan plaintext : ")
    if alphabet is ALPHA:
        plaintext = plaintext.upper().replace(" ", "")
    if not valid(plaintext, alphabet):
        print("[!] Plaintext kosong atau mengandung karakter di luar mode yang dipilih.")
        return

    key = generate_key(len(plaintext), alphabet)
    ciphertext = encrypt(plaintext, key, alphabet)

    print("\n=== HASIL ENKRIPSI ===")
    print(f"Plaintext  : {plaintext}")
    print(f"Key        : {key}")
    print(f"Ciphertext : {ciphertext}")
    print("(Simpan key dengan aman, key dibutuhkan untuk dekripsi & hanya boleh dipakai sekali.)")


def do_decrypt() -> None:
    alphabet = choose_mode()
    if alphabet is None:
        return

    ciphertext = input("Masukkan ciphertext: ")
    key = input("Masukkan key       : ")
    if alphabet is ALPHA:
        ciphertext = ciphertext.upper().replace(" ", "")
        key = key.upper().replace(" ", "")

    if not valid(ciphertext, alphabet) or not valid(key, alphabet):
        print("[!] Ciphertext/key kosong atau mengandung karakter di luar mode yang dipilih.")
        return
    if len(ciphertext) != len(key):
        print(f"[!] Panjang key ({len(key)}) harus sama dengan ciphertext ({len(ciphertext)}).")
        return

    print("\n=== HASIL DEKRIPSI ===")
    print(f"Plaintext  : {decrypt(ciphertext, key, alphabet)}")


def main() -> None:
    while True:
        print_group_information()
        print("\n===== ONE-TIME PAD (OTP) =====")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Keluar")
        choice = input("Pilih menu [1-3]: ").strip()

        if choice == "1":
            do_encrypt()
        elif choice == "2":
            do_decrypt()
        elif choice == "3":
            print("Sampai jumpa!")
            break
        else:
            print("[!] Menu tidak valid.")


if __name__ == "__main__":
    main()
