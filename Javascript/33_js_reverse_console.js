// 거꾸로 출력하기
// 한줄에 여러개의 숫자가 입력되면 역순으로 그 숫자들을 하나씩 출력하는 프로그램 만들기
// ex) 1 2 3 4 5
// 5 4 3 2 1

const data = prompt("숫자를 입력해주세요!").split(" ").reverse();
let result = ""
// const data = ["1", "2", "3", "4", "5"]

for (let i = 0; i < data.length; i++){
	result += data[i];	
}

console.log(result)