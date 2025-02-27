def count_words(s: str) -> int:
    return len(s.split())
    
def count_characters(s: str) -> dict[str, int]:
    cache: dict[str, int] = {}
    for c in s:
        if c.lower() in cache:
            cache[c.lower()] += 1
        else:
            cache[c.lower()] = 1
    return cache

def sort_list_of_dict(chars_dict: dict[str, int]) -> list[dict[str, int]]:
    chars_dict_list: list[dict] = []
    for k in chars_dict:
        chars_dict_list.append({"char": k, "num": chars_dict[k]})
    
    def sort_on(dict: dict) -> int:
        return dict["num"]
    
    chars_dict_list.sort(reverse=True,key=sort_on)
    
    return chars_dict_list