import stats
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        content = f.read()
        return content
    
def main() -> None:
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path: str = sys.argv[1]
    book: str = get_book_text(book_path)

    count_characters: dict[str, int] = stats.count_characters(book)
    list_counts: list[dict] = stats.sort_list_of_dict(count_characters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f'Found {stats.count_words(book)} total words')
    print("--------- Character Count -------")
    
    for count in list_counts:
        if count["char"].isalpha():
            print(f"{count['char']}: {count['num']}")
                
    print("============= END ===============")
main()