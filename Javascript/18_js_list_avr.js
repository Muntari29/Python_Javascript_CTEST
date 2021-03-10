// avg 
// 20 , 30 , 40 => 30

// const data = [20, 30, 40];
const data = prompt('과목 점수입력하시오.').split(' ');
console.log(data);
let sum_number = 0;

for (let number = 0; number < data.length; number++){
    sum_number += parseInt(data[number]);
}
console.log(sum_number)
const result = sum_number/data.length;
console.log(result)
// 76.3333333333333

console.log(Math.floor(result))
// 76

/* 
parseInt() - 문자열을 정수로 바꾸는 함수입니다.
Math.floor 메서드는 소수점 자리를 모두 버림합니다.
*/

/*
string을 n진법일 때의 값으로 바꿉니다. n은 옵션으로 2부터 36까지 입력할 수 있습니다. 입력하지 않으면 10으로 처리합니다.
string의 처리는 parseFloat()와 거의 같습니다.
소수 부분은 버립니다.
0x로 시작하면 16진법으로 처리합니다. 
*/