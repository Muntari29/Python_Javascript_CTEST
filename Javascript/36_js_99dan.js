// Multiplication table / 구구단 출력하기
// ex) 2
// 1 ~ 9까지의 숫자 중 하나를 입력 구구단 결과가 한 줄에 출력되어야 한다.

// const data = prompt('숫자입력해주세용!');
const data = "2";
let result = [];

for (let i = 1; i < 10; i++){
    number = parseInt(data, 10);
    result.push(number * i);   
}

console.log(result.join(" "));


/* 
const num = prompt('1 ~ 9까지의 숫자 중 하나를 입력하세요.')
let result = '';

for (let i=1; i<=9; i++){
  result += i*num + ' ';
}

console.log(result);
*/