var s = 10 + 10 + "10"
console.log(s)

var s = 10 + ( 10 + "10" )
console.log(s)

var s = 10 + 10 / 5 * 3
console.log(s)


// in js BEDMAS follows
// bracket  -->  exponential  -->  divison  -->  multiplication  -->  addition  -->  subtraction


// NaN =  not a number

// vaise string jo number nhi hai .... aur use jab number me convert krte hai tb hme NaN milta hai


var s = 10 + "10" - "5"
console.log(s)

var s = 2 ** 4  // exponent operator = **           it is called    2 to the power of 4
console.log(s)