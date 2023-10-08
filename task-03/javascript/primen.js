const readline = require('readline');
const rl=readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter a number: ", (input) => {
    const n = parseInt(input);
    for (let i = 1; i <= n; i++) {
        let f = 0;
        for (let j = 2; j<i; j++) {
            if (i % j == 0) {
                f = 1;
                break;
            }
        }
        if (f==0) {
            console.log(`${i} : Prime`);
        }
    }
    rl.close();


});