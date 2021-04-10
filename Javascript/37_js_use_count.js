//  뽑은 후보를 입력하면 당선자와 득표수를 출력하는 프로그램 만들기
//  ex) 원영 원영 은비 은비 은비 은비 채연 체연

const candidates = ['원영', '원영', '은비', '은비', '은비', '은비', '채연'];
// const candidates = prompt('이름을 입력해주세요.').split(' ');
let result = {};
let winner = "";

for(let index in candidates){
  let val = candidates[index];
  result[val] = result[val] === undefined ? 1 : result[val] = result[val] + 1;
}

winner = Object.keys(result).reduce(function(a, b){
  return result[a] > result[b] ? a : b
});

console.log(`${winner}(이)가 총 ${result[winner]}표로 반장이 되었습니다.`);