const data = prompt('숫자입력해주세용!');
// const data = "2";
let result = [];

for (let i = 1; i < 10; i++){
    number = parseInt(data, 10);
    result.push(number * i);   
}

console.log(result.join(" "));