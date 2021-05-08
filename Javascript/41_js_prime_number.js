// 소수 판별 프로그램 
// 1과 자기자신으로만 나누어 떨어지는 수

var number = 7;

function check_prime(number){
    // 2부터 number-1까지 나누었을때 1과 자기자신으로만 나누어 떨어져야함
    for (var i = 2; i < number; i++){
        let result = number % i;
        if (result === 0){
            return console.log('소수가 아님')
        }
    }

    if (number === 1){
        return console.log('소수가 아님, 1임')
    }
    
    return console.log('소수!!')
}

check_prime(1)