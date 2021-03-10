// 몫 나머지

const data = prompt('두 수를 입력하세요!').split(" ");
// const data = [10, 2];

const share = parseInt(data[0]) / parseInt(data[1]);
const remain = parseInt(data[0]) % parseInt(data[1]);



console.log(Math.floor(share), remain);