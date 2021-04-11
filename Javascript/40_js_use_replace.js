// # 놀이동산에 가자
// # 모든 놀이기구는 한번에 타는 인원수 제한은 없다.
// # 하지만 제한 무게를 넘으면 무조건 다음 기구를 타야 한다.
// # 친구들이 총 몇 명 탈 수 있는지 알 수 있는 프로그램 만들기
// '''
// ex)
// 50 첫번째 줄은 제한 무게
// 5 함께한 친구들의 수
// 20 탑승할 몸무게1 (몸무게는 무작위)
// 20 탑승할 몸무게2
// 20 탑승할 몸무게3
// 20 탑승할 몸무게4
// 20 탑승할 몸무게5
// '''

let total = 0;
let count = 0;
// const limit = 50;
const limit = prompt('제한 무게를 입력하세요.');
// const n = 5;
const n = prompt('인원수를 입력하세요.');

for (let i=1; i<=n; i++){
  total += parseInt(prompt('무게를 입력해주세요.'), 10);
  if (total <= limit){
		count = i;
  }
}

console.log(count);