// # 오타 수정하기
// # 입력되는 모든 q 를 e로 바꾸는 프로그램 만들기
// 입력 : querty
// 출력 : euerty

// 입력 : hqllo my namq is hyqwon
// 출력 : hello my name is hyewon

const data = "hqllo my namq is hyqwon";

let a = data.replaceAll("q", "e");

console.log(a)

//1. 함수 사용
const word = prompt('입력하세요.');

function replaceAll(str, searchStr, replaceStr) {
   return str.split(searchStr).join(replaceStr);
}

console.log(replaceAll(word,"q","e"));

//2. 정규식 사용
const word = prompt('입력하세요.');

console.log(word.replace(/q/gi, 'e'));