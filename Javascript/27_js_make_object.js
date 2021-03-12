// 객체 만들기

/* 
첫번째 입력에서는 학생의 이름이 공백으로 구분되어 입력되고, 두번째에는 그 학생의 수학 점수가 공백으로 구분되어 주어집니다.
두 개를 합쳐 **학생의 이름이 key**이고 **value가 수학 점수**인 객체를 출력해주세요. 
Yujin Hyewon
70 100
출력
{'Yujin': 70, 'Hyewon': 100}
*/

// const data = ["Yujin", "Hyewon"];

// const scores = [70, 100];

const keys = prompt("이름을 입력하세요").split(" ");

const values = prompt("점수를 입력하세요").split(" ");

const result = {};

for (let i = 0; i < keys.length; i++){
    result[keys[i]] = parseInt(values[i], 10);
}

console.log(result)

// parseInt(string [, radix])
// parseInt() 메소드는 string을 특정 진수로 변환해주는 메소드입니다. string을 radix로 변환한 정수(or NaN)를 리턴합니다.
// parseInt(값, 10) ==> radix 디폴트는 10진수가 아니므로 표기를 해주는 습관을 갖자.
// JavaScript는 string이 16진수나 8진수 표기법이 아니라면, radix를 10으로 설정하기 때문입니다.

```
const keys = prompt('이름을 입력하세요').split(' ');
const values = prompt('점수를 입력하세요').split(' ');
const obj = {};

for (let i=0; i<keys.length; i++) {
  obj[keys[i]] = parseInt(values[i], 10);
}

console.log(obj);
```