// Circle area
// 원이 넓이를 구하는 함수 만들어보자
// 반지름 * 반지름 * 3.14

function CircleArea(radius){
    return radius * radius * 3.14;
}

console.log(CircleArea(5))




function circle(n) {
    const result = n * n * 3.14;
  
    return result;
  }
  
  const r = prompt("원의 반지름을 입력하세요.");
  
  console.log(circle(r));