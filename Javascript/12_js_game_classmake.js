// 게임 클래스 만들기
// 파이어볼 출력하기

class Wizard{
    constructor(health, mana, armor){
        this.health = health;
        this.mana = mana;
        this.armor = armor;
    }

    attack(){
        console.log("파이어볼");
    }
}

const x = new Wizard(542, 220, 10);
console.log(x.health, x.mana, x.armor);
x.attack()


// 542, 220, 10
// 파이어볼
