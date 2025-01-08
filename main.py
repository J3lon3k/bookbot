def count_words(s):
    words = s.split()
    word_count = len(words)
    return word_count

def count_characters(s):
    count = {}
    s_lower = s.lower()
    for c in s_lower:
        if c.isalpha():
            if c not in count:
                count[c] = 0
            count[c] += 1

    sorted_count = []
    for key in count:
        val = count[key]
        sorted_count.append({"char" : key, "times" : val})
    
    sorted_count.sort(reverse = True, key = lambda dict : dict['times'])
    
    return sorted_count
    

def main():
    book_source = "books/frankenstain.txt"
    book_contents = None

    with open(book_source) as file:
        book_contents = file.read()
    
    word_count = count_words(book_contents)
    char_count = count_characters(book_contents)

    # generate report
    print(f"--- Begin report of {book_source} ---")
    print(f"{word_count} words found in the document")
    print()
    for c_dict in char_count:
        char = c_dict["char"]
        times = c_dict["times"]
        print(f"The '{char}' character was found {times} times")

main()