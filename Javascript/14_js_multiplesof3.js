// 3의 배수라면 짝 , 3의 배수가 아니라면 n 그대로 출력

const n = prompt("알고싶은 값을 입력하세요!");

if (n % 3 ==0) {
    console.log('3의 배수이므로 짝!');
} else {
    console.log(`${n}`);
}