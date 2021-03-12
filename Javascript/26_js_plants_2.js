// 한글 이름으로 영어 이름을 반환하는 프로그램 만들기

const plants = {
    '수성' : 'Mercury',
    '금성' : 'Venus',
    '지구' : 'Earth',
    '화성' : 'Mars',
    '목성' : 'Jupiter',
    '토성' : 'Saturn',
    '천왕성' : 'Uarnus',
    '해왕성' : 'Neptune'   
};

// const data = prompt('행성 이름을 입력하세요!');
const data = '수성';

console.log(plants[data]);