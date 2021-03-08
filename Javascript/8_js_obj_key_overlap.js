// 객체 키 값 이름 중복

var a = {
    'height' : 180,
    'weight' : 80,
    'weight' : 50,
    'weight' : 30,
    'weight' : 100,
    'temp' : 36
}

console.log(a['weight'])
// 100


// 키 내부에서 중복되는 이름이 있을 경우 자바스크립트는 맨 뒤에 적은 것을 값으로 연결해준다.
// 즉 순서상 정답은 100이다.