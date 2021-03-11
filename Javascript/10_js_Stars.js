// 별찍기


// let number = prompt('입력');
let number = 5;

let tree = "";
const stars = "*";
const blank = " ";

for (let i = 0; i < number; i++){
    // console.log(i)
    for (let j = 0; j < number-1-(1*i); j++){
        tree += blank;
    }
    // console.log(j)
    for (let k = 0; k < (2*i+1); k++){
        tree += stars;
    }
    tree += "\n";
}
console.log(tree)
/*
    *
   ***
  *****
 *******
*********
*/

for (let i = 0; i < number; i++){
    for (let j = 0; j < number-1-(1*i); j++){
        tree += stars;
    }
    tree += "\n"
}

// console.log(tree)
/* ****
***
**
*
*/

for (let i = 0; i < number; i++){
    for (let k = 0; k < (2*i+1); k++){
        tree += stars;
    }
    tree += "\n";
}

// console.log(tree)
/*
*
***
*****
*******
*********
 */