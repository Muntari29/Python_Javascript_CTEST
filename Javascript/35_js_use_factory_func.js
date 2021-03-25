// Factory 함수 만들기
// 2 제곱, 3 제곱, 4 제곱을 할 수 있는 함수를 만들자

function one2(n){
    function two2(m){
        value = m ** n;
        return value;
    }
    return two;
}

function one(n){
    function two(m){
        value = Math.pow(m, n);
        return value;
    }
    return two;
}

const a = one(2);
const b = one(3);
const c = one(4);

console.log(a)
console.log(b)
console.log(c)
console.log(a(10));
console.log(b(10));
console.log(c(10));