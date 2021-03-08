// js 문법 중 False로 취급되는 것
// 아래 딱 하나만 True이다.

/*
1) NaN
2) 1 => True
3) ""
4) 0
5) undefined
*/

console.log(Boolean(NaN))
// false

console.log(Boolean(1))
// true

console.log(Boolean(""))
// false

console.log(Boolean(0))
// false

console.log(Boolean(undefined))
// false

/*
NaN
전역 NaN 속성은 Not-A-Number(숫자가 아님)를 나타냅니다.
이 속성은 값이 유효한 숫자가 아님을 나타낸다.
값이 NaN인지 확인하기 위해선 isNaN() 내장 함수를 사용해야한다!!

isNaN(123) //false
isNaN(-1.23) //false
isNaN(5-2) //false
isNaN(0) //false
isNaN('123') //false
isNaN('Hello') //true
isNaN('2005/12/12') //true
isNaN('') //false
isNaN(true) //false
isNaN(undefined) //true
isNaN('NaN') //true
isNaN(NaN) //true
isNaN(0 / 0) //true
isNaN(null) //false


*/