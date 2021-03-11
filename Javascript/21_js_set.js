// how to make set

/*
1) var x = {1, 2, 3, 4, 5, 6, 7};
2) var x = {};
3) var x = new Set('Javascript');
4) var x = new Set(range(5));
5) var x = new Set;
*/

// var a = {1, 2, 3, 4, 5, 6, 7};
var b = {};
var c = new Set('Javascript');
// var d = new Set(range(5));
var e = new Set;


console.log(b)
// {}
console.log(c)
// Set { 'J', 'a', 'v', 's', 'c', 'r', 'i', 'p', 't' }
console.log(e)
// Set {}

console.log(typeof(b))
// object

console.log(typeof(c))
// object

console.log(typeof(e))
// object

// Set 객체는 JS의 표준 내장 객체 중 하나이다.
// Set 객체는 자료형에 관계 없이 원시 값과 객체 참조 모두 유일한 값을 저장할 수 있다.
