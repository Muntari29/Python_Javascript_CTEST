/*
2-gram 문자열에서 2개의 연속된 요소를 출력하는 방법
python -> 2-gram -> py, yt, th...
2-gram 출력 프로그램 만들기
*/

// const strs = prompt('문자를 입력하세요');
const strs = "Javascript";

for (let i = 0; i < strs.length - 1; i++){
    // console.log(`${strs[i]} ${strs[i+1]}`);
    console.log(strs[i], strs[i+1]);

}

