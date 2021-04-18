def solution(phone_book):
    answer = True
    my_dict = set(phone_book)

    for phone in phone_book:
        for key in my_dict:
            hash_phone = hash(phone)
            hash_key = hash(key)
            if phone.startswith(key) and hash_phone != hash_key: 
                answer = False

    return answer

solution(["123","456","789"])