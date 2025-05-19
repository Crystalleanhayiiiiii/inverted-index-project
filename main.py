import os
import string
# PHẦN (a) – CreateIndex
def load_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return set(word.strip().lower() for word in f.readlines())

def tokenize(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator).lower().split()

def CreateIndex(Dir, StopList):
    stopwords = load_stopwords(os.path.join(Dir, StopList))
    inverted_index = {}
    doc_table = []
    
    for filename in os.listdir(Dir):
        # Bỏ qua StopList và WordFile
        if filename in [StopList, "WordFile.txt"] or not filename.endswith(".txt"):
            continue
    
        doc_table.append(filename)
        with open(os.path.join(Dir, filename), 'r', encoding='utf-8') as f:
            words = tokenize(f.read())
            for word in words:
                if word.lower().startswith("c") and word.lower() not in stopwords:
                    if word not in inverted_index:
                        inverted_index[word] = {}
                    if filename not in inverted_index[word]:
                        inverted_index[word][filename] = 0
                    inverted_index[word][filename] += 1

    return doc_table, inverted_index
 #PHẦN (b) – Find(Word, Weight, N)
def Find(inverted_index, word, weight, N):
    word = word.lower()
    if word not in inverted_index:
        return []  # Không có từ đó trong index

    scores = {}
    for doc, freq in inverted_index[word].items():
        scores[doc] = freq * weight

    # Sắp xếp theo điểm giảm dần
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_scores[:N]

#PHẦN (c) – Find(WordFile, N)
def FindFromFile(inverted_index, wordfile_path, N):
    scores = {}

    with open(wordfile_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 2:
                continue
            word, weight = parts[0].lower(), int(parts[1])
            if word not in inverted_index:
                continue
            for doc, freq in inverted_index[word].items():
                if doc not in scores:
                    scores[doc] = 0
                scores[doc] += freq * weight

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_scores[:N]


if __name__ == "__main__":
    dir_path = "data"
    stoplist = "StopList.txt"
    wordfile = "data/WordFile.txt"

    doc_table, inverted_index = CreateIndex(dir_path, stoplist)
    

    print(">>> DocTable:")
    for doc in doc_table:
        print(f" - {doc}")

    print("\n>>> Inverted Index:")
    for term, postings in inverted_index.items():
        print(f"{term}:")
        for doc, freq in postings.items():
            print(f"    {doc} -> {freq}")

    print(">>> Top 2 tài liệu chứa từ 'creative' với trọng số 5:")
    print(Find(inverted_index, "creative", 5, 2))

    print("\n>>> Top 3 tài liệu từ danh sách trong WordFile.txt:")
    print(FindFromFile(inverted_index, wordfile, 3))
