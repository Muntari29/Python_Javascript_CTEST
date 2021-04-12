//  호준이의 아르바이트
//  학생 점수는 공백으로 구분하여 입력한다.
//  1 ~ 3위 학생에게는 사탕을 주며 1~ 3위는 중복될 수 있으며 중복된 사람도 포함하여 사탕을 줘야한다.
//  사탕을 몇개 사면 되는지 프로그램으로 만들기
//  ex) 97 86 75 66 55 97 85 97 97 95
//  6 출력

// const scores = prompt('점수입력').split(' ').map(function(n){
//     return parseInt(n, 10);
//   });
const scores = [97, 86, 75, 66, 55, 97, 85, 97, 97, 95];
// 인풋값을 수치형데이터의 배열로 받음
console.log(scores);
// [97, 86, 75, 66, 55, 97, 85, 97, 97, 95]

// 정렬
scores.sort((a, b) => {
    return a-b;
  });

console.log(scores);
// [55, 66, 75, 85, 86, 95, 97, 97, 97, 97]

let count = 0;
let box = [];

while (box.length < 3){
    // 정렬된 배열의 맨 마지막 값을 삭제하며 삭제하는 값을 data로 선언
    let data = scores.pop()
    // 가장 높은 점수(맨마지막값)이 box내에 존재한다면 카운트를 1증가시킴
    // 1 ~ 3위까지만 사탕을 주므로 box의 길이가 3이 되는 순간부터 반복문 종료
    if (!box.includes(data)){
        box.push(data)
        console.log(box);
    } count += 1;
}

console.log(count);