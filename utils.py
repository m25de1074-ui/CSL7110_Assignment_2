import itertools

def load_document(path):
    with open(path, 'r') as f:
        return f.read().strip()

def char_kgrams(text, k):
    return set(text[i:i+k] for i in range(len(text)-k+1))

def word_kgrams(text, k):
    words = text.split()
    return set(" ".join(words[i:i+k]) for i in range(len(words)-k+1))

def jaccard(set1, set2):
    if len(set1 | set2) == 0:
        return 0
    return len(set1 & set2) / len(set1 | set2)

def all_pairs(items):
    return list(itertools.combinations(items, 2))

def evaluate(predicted, actual):
    predicted = set(predicted)
    actual = set(actual)
    fp = len(predicted - actual)
    fn = len(actual - predicted)
    return fp, fn