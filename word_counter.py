"""Count words."""
from operator import itemgetter
def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    word_dict = {}
    # TODO: Count the number of occurences of each word in s
    for w in s.split():
        try:
            word_dict[w] += 1
        except KeyError:
            word_dict[w] = 1

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    sorted_words = sorted(word_dict.items(), key = itemgetter(0))
    s = sorted(sorted_words, key=itemgetter(1), reverse=True)

    # print s

    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    top_n = s[:n]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()