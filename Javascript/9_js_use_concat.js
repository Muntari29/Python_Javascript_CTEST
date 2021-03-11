// concat 함수 사용하기


var year = '2019';
var month = '04';
var day = '26';
var hour = '11';
var minute = '34';
var second = '27';

var result = year.concat(
    "/", month,
    "/", day,
    " ", hour,
    ":", minute,
    ":", second
    )

console.log(result);
// 2019/04/26 11:34:27

var result2 = `${year}/${month}/${day} ${hour}:${minute}:${second}`
console.log(result2)
// 2019/04/26 11:34:27

// .concat()은 문자열을 이어 붙이는 메서드입니다.

// 문법
// string1.concat( [string2 [, string3 [, ... [, stringN]]]] )
// string1은 필수 요소, string2 등은 선택 요소입니다.
// 인수가 문자열이 아닌 경우 먼저 문자열로 변환한 다음 string1에 연결합니다.
// 예를 들어

// 'ab'.concat( 'cd', 'ef' )
// 는 abcdef입니다.