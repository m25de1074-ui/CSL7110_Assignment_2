import random

m = 20011  # prime > 10000

def generate_hash_functions(t):
    hash_funcs = []
    for _ in range(t):
        a = random.randint(1, m-1)
        b = random.randint(0, m-1)
        hash_funcs.append((a, b))
    return hash_funcs

def build_universe(doc_sets):
    universe = set()
    for s in doc_sets.values():
        universe |= s
    return {gram: idx for idx, gram in enumerate(universe)}

def minhash_signature(kgram_set, universe_dict, hash_funcs):
    signature = []

    for a, b in hash_funcs:
        min_hash = float('inf')
        for gram in kgram_set:
            x = universe_dict[gram]
            hash_val = (a*x + b) % m
            if hash_val < min_hash:
                min_hash = hash_val
        signature.append(min_hash)

    return signature

def approx_jaccard(sig1, sig2):
    matches = sum(1 for i in range(len(sig1)) if sig1[i] == sig2[i])
    return matches / len(sig1)