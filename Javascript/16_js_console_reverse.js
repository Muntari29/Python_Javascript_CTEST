// 거꾸로 출력하기

const strs = "거꾸로"

const result = strs.split("");
const result2 = strs.split("").reverse();
const result3 = strs.split("").reverse().join();
const result4 = strs.split("").reverse().join("");

/*
* split() 메서드는 문자열을 배열로 만들어 반환하고,
* reverse() 메서드는 배열의 순서를 반전하며,
* join() 메서드는 원소를 모두 붙여 문자열로 반환합니다.
*/

console.log(result)

console.log(result2)

console.log(result3)

console.log(result4)

/*
[ '거', '꾸', '로' ]
[ '로', '꾸', '거' ]
로,꾸,거
로꾸거 
*/

// 문자열은 리버스 함수가 없으므로 배열로 만들 후 리버스를 적용해줘야 한다.

// 문자열 구분자가 있는 경우 (,)
// 김태희, 전지현, 아이유

// strs = str.split(",").join(",")

// 문자열 구분자가 없는 경우 ()
// 김태희전지현아이유

// strs = str.split().join()


// # ABC -> CBA