/*
sort 구현하기
키가 주어지면 순서대로 제대로 섰는지 확인하는 프로그램 만들기 
ex) 176 156 155 165 166 169
YES or NO
*/

// const data = prompt("문자를 입력해주세요!");
const data = "176 156 155 165 166 169";

let sortData = data.split(" ").sort(function(a, b){
    return a - b;;
}).join(" ");

console.log(data)
console.log(sortData)

if (data === sortData){
    console.log("YES")
} else {
    console.log("NO")
}