
def rabin_karp(text,pattern,q=101):
    d = 256
    n = len(text)
    m = len(pattern)
    h = pow(d, m-1) % q #precomputed value for hash rolling
    p_hash = 0
    t_hash = 0
    matches = [] #stores starting indices of matches


    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q #udate pattern hash
        t_hash = (d * t_hash + ord(text[i])) % q #update text hash

    for i in range(n-m+1):
        if p_hash == t_hash:
            if text[i:i + m] == pattern:
                matches.append(i)
        if i<n-m:
            t_hash = (d*(t_hash - ord(text[i]) * h ) +ord(text[i+m])) % q

            if t_hash<0:
                t_hash += q
    return matches


def phrase_search_in_document():
    print("Welcome to phrase detecction app!")

    document = input("enter the main text (document): ")
    phrase =input("enter the phrase to search for: ")

    matches = rabin_karp(document,phrase)

    if matches:
        print(f"Phrase found {len(matches)} times at positions (0-indexed): {matches}")
    else:
        print("Phrase not found in the document.")

if __name__ == "__main__":
    phrase_search_in_document()