# 프로그래머스 해쉬 2번 문제
# 전화 번호 목록 

def solution2(phone_book):
    answer = True
    hash_map = set(phone_book)
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

# 해시를 사용하지 않은 풀이

def solution(phone_book):
    phone_book.sort()
    answer = True
    
    for number in range(0, len(phone_book)-1):
        if phone_book[number+1].startswith(phone_book[number]):
            return False

    return answer