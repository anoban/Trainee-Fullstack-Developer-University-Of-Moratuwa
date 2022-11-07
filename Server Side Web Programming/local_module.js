// a dummy user defined local module

const factorial = function factorial(num) {
    let x = 1;
        for (let i = 1; i < num+1; i++){
             x *= i;
        }
        return x;
    }

// export the function as a module!
module.exports = factorial;