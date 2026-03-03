from collections import defaultdict
import itertools

def lsh_candidates(signatures, r, b):
    buckets = defaultdict(list)

    for doc_id, sig in signatures.items():
        for band in range(b):
            start = band * r
            end = start + r
            band_tuple = tuple(sig[start:end])
            buckets[(band, band_tuple)].append(doc_id)

    candidates = set()
    for bucket in buckets.values():
        if len(bucket) > 1:
            for pair in itertools.combinations(bucket, 2):
                candidates.add(tuple(sorted(pair)))

    return candidates

def lsh_probability(s, r, b):
    return 1 - (1 - s**r)**b