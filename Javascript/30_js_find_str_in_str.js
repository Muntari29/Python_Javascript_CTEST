//문자열 속 문자 찾기
// 해당 문자로 시작하는 index를 반환하는 프로그램 만들기
/* 
sentence = 'pineapple is very apple'
str_data_exists = 'apple'
str_data_does_not_exists = '123'
*/

const sentence = "pineapple is very apple";

// const sentence = prompt("문장을 입력해보세요!");
// const findStr = prompt("찾고 싶은 문자열을 입력하세요!");

const findStr = "apple";

console.log(sentence.indexOf(findStr));
// 4

console.log(sentence.match(findStr));
/*
[
    'apple',
    index: 4,
    input: 'pineapple is very apple',
    groups: undefined
]
*/

// indexOf() 내장 함수 사용문제
// 문자열 또는 배열에서 사용할 수 있으며 원하는 문자열 배열의 특정값을 찾으면 인덱스르 반환한다.
// 이떄 찾는 값이 없을 경우 -1을 반환하다.
// 이를 이용해 문자열 또는 배열에 특정값이 포함되어있는지 확인 할 수 있다.
// "문자열".indexOf("찾을 문자")

// math() 내장 함수
// 해당 문자열.match('찾을 단어')
// 문자열이 정규식과 일치하면, 일치하는 전체 문자열을 첫 번째 요소로 포함하는 Array를 반환한 다음 괄호 안에 캡처된 결과가 옵니다. 
// 일치하는 것이 없으면 null이 반환됩니다.
// 문자열 검색으로 자주사용 되는 함수이다. 
// 이를 활용해 해당 텍스트 포함여부를 알 수 있고, 정규표현식 사용이 가능하여 더 다양한 검색 조건을 제공한다.
