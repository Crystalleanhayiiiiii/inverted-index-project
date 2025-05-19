# Inverted Index Project – Python Implementation
Sinh viên thực hiện:  Lê Anh Tình N21DCCN189
Project cuối EX6 Đề :As a project, write a program that implements inverted indexes. Your program must contain the following routines: 
(a) CreateIndex(Dir, StopList) takes a directory name and a file called StopList (in that directory) as input. It returns an inverted index as output. The DocTable includes all files in the directory Dir, except for the StopList file. The TermTable includes only all words occurring in the directory that start with the letter C (lower- or uppercase).

(b) Find(Word, Weight, N) finds the top N documents in the index associated with the word specified in the input.

(c) Find(WordFile, N) is similar to the above, but there is one difference. Instead of taking a single word as part of the input, it takes a file called WordFile as input. This file has, on each line, a word (string) and a weight (integer). It then attempts to find, using the inverted index, the top N matches for this query.

Mục tiêu:  
Xây dựng một hệ thống tìm kiếm văn bản đơn giản sử dụng chỉ mục đảo (inverted index), bao gồm ba chức năng chính:

(a) CreateIndex(Dir, StopList)  
Tạo chỉ mục đảo từ các văn bản trong thư mục.

(b) Find(Word, Weight, N)  
Tìm top N tài liệu chứa một từ khóa cụ thể với trọng số.

(c) Find(WordFile, N)  
Tìm top N tài liệu phù hợp nhất với danh sách các từ khóa có trọng số, được đọc từ file.

Hướng dẫn cài đặt:
Cài Python từ python.org
Mở terminal tại thư mục chứa main.py


Cấu trúc thư mục project:

    PROJECT_FOLDER/
    ├── data/
    │   ├── file1.txt
    │   ├── file2.txt
    │   ├── StopList.txt
    │   └── WordFile.txt
    ├── main.py
    └── README.md


----------------------------------------------------------------

Các hàm chính:

    CreateIndex(dir, stoplist)
        → Trả về DocTable và TermTable

    Find(inverted_index, word, weight, N)
        → Tìm top N tài liệu chứa 1 từ

    FindFromFile(inverted_index, wordfile_path, N)
        → Tìm top N tài liệu từ nhiều từ có trọng số

----------------------------------------------------------------

(a) CreateIndex(Dir, StopList)

Chức năng:
- Đọc tất cả các file văn bản trong thư mục Dir (ngoại trừ file StopList và các file bị loại khác như WordFile).
- Tách từ, chuyển về chữ thường, loại bỏ dấu câu.
- Chỉ giữ lại các từ bắt đầu bằng chữ "C" hoặc "c".
- Loại bỏ các từ nằm trong danh sách StopList.
- Trả về chỉ mục đảo 
```markdown
Input:
    Dir       : thư mục chứa các file .txt
    StopList  : tên file chứa danh sách từ dừng

Output:
    DocTable: ánh xạ chỉ số → tên tài liệu
    TermTable: từ → {tên tài liệu → số lần xuất hiện}

Ví dụ 
Input:

Thư mục data/ chứa:
    data/
    ├── file1.txt
    ├── file2.txt
    └── StopList.txt

Nội dung StopList.txt:
    the
    and
    of
    in
    on
    code
    computer

Nội dung file1.txt:
    The computer is powerful. Creativity comes from chaos, not just code.
    Creative minds change the world.

Nội dung file2.txt:
    Coding is challenging. Many concepts in computer science are complex.
    Creative solutions require courage and collaboration.

Output tương ứng:

    DocTable = {
        0: "file1.txt",
        1: "file2.txt"
    }

    TermTable = {
        "creativity": {"file1.txt": 1},
        "comes": {"file1.txt": 1},
        "chaos": {"file1.txt": 1},
        "creative": {"file1.txt": 1, "file2.txt": 1},
        "change": {"file1.txt": 1},
        "coding": {"file2.txt": 1},
        "challenging": {"file2.txt": 1},
        "concepts": {"file2.txt": 1},
        "complex": {"file2.txt": 1},
        "courage": {"file2.txt": 1},
        "collaboration": {"file2.txt": 1}
    }
```
----------------------------------------------------------------

(b) Find(Word, Weight, N)

Tác vụ:
- Truy vấn một từ khóa và tìm top N tài liệu chứa từ đó.
- Điểm số tính bằng:
    score = frequency_in_doc × weight
````markdown
Input:
    Find(inverted_index, "creative", 5, 2)

Output:
    [("file1.txt", 5), ("file2.txt", 5)]

Giải thích:
- "creative" xuất hiện 1 lần trong mỗi file → 1 × 5 = 5 điểm

----------------------------------------------------------------
```
(c) Find(WordFile, N)

Tác vụ:
- Đọc danh sách từ và trọng số từ một file (WordFile.txt), mỗi dòng là:
    word weight
- Sau đó tính điểm cộng dồn cho mỗi tài liệu:
    score[doc] += freq(word, doc) × weight
````markdown
Input file WordFile.txt:
    creative 5
    complex 2
    concept 4

Tính điểm:
- "creative": file1 = 5, file2 = 5
- "complex": file1 = 2, file2 = 0
- "concept": không có từ "concept", chỉ có "concepts" → 0 điểm

Output:
    [("file1.txt", 7), ("file2.txt", 5)]
```

