import collections

def solution(phone_book):
    answer = True
    my_dict = collections.Counter(phone_book)

    for phone in phone_book:
        for key in my_dict.keys():
            print(phone)
            print(key)
            hash_phone = hash(phone)
            hash_key = hash(key)
            print(hash_phone, hash_key)
            if phone in key and hash_phone != hash_key:
                answer = False
            

    return print(answer)

solution(["119", "97674223", "1195524421"])