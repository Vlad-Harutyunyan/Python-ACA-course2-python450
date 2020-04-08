def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

if __name__ == "__main__":
    temp1 = 'even even even this is is sentence..'
    print(word_count(temp1))
    temp2 = 'What is this book about? This book is about python coding'
    print(word_count(temp2))