const scores = prompt('점수입력').split(' ').map(function(n){
    return parseInt(n, 10);
  });

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
    if (!box.includes(data)){
        box.push(data)
    } count += 1;
}

console.log(count);