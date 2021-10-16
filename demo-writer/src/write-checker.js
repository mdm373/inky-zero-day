

let str = "";
let vals = ['W','B','C']
let index = 0;
for (let y = 0; y < 300; y++) {
    for (let x = 0; x < 400; x++ ) {
        index++;
        if(index >= vals.length){
            index = 0;
        }
        str = str +vals[index]
    }
}
console.log(str);