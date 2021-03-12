// 입력된 하나의 문자가 대문자이면 YES / NO 출력하는 프로그램 만들기
// 알파벳 하나만 입력했을때 YES / NO

const data = prompt('문자를 입력하세요!');

if (data === data.toUpperCase()){
    console.log("YES");
} else {
    console.log("NO");
}

