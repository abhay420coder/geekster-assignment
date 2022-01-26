//HELLO EVERYONE

console.log("hi there")




// SINGLE LINE COMMENT



/* MULTI 
   LINE 
  COMMNET 
*/


// MULTI
// LINE
// COMMENT



console.log(1234) //number
console.log('1234') //string
console.log("1234") //string

console.log(true) //boolean
console.log("true") //string
console.log(false) //boolean

var b1
console.log(b1)            // we got "undefined" in output




// how to check the data type
// console.log(typeof var_name)


b2=34
console.log(typeof b2)   //output:- number


b3=34.57
console.log(typeof b3)  //output:- number


b4="good"
console.log(typeof b4)   //output:- string


b5='hello'
console.log(typeof b5)   //output:- string


b6=true
console.log(typeof b6)  //output:- boolean


b7=false
console.log(typeof b7)  //output:- boolean

b8= null
console.log(typeof b8)  //output:- boolean


b9="raj"
console.log(b9)  


b9=true
console.log(b9)


b9 = undefined
console.log(b9)


b9=54328
console.log(b9)



/*

you can use  var  before declaring a variable or you can not

var is totally optional

but my recommendation is ..... you have to use  var   befor declaring a variable

*/


//   %    modulus operator ( for remainder in divison )
//   /    divison operator (for quotient  in divison )
//   *    multiplication operator 
//   +    addition operator
//   -    subtraction operator 

//   ==    equal
//   !=    not equal


var b10 = 9
if(b10%2==0)
        {
	  console.log("b10 is even")
	}
 else
 	{
	  console.log("b10 is odd")
	}

console.log(10 == "10")  //true
// in JS we compare string with a number
// in JS we compare string with a string
// in JS we compare number with a number

console.log(10 > "10")  //false


console.log(12 == 12)  //true


console.log(10 >= 10)  //true



console.log(10 == 10)  //true


//  console.log()  --> this will be display in console
// ex:-   console.log("enter first number:-")

//  alert()  	   -->  this creates popup and shows in the browser
// ex:-   alert("enter first number:-")

//  prompt()	   -->   this is used to take the input from a user

//           in prompt , we can give some hint text
// ex:-     prompt("enter first number:-")

var b11 = prompt("enter b11 number")
console.log(b11)

var b12 = prompt("enter b12 number")
alert(b12)


var b13 = prompt("enter b13 number")
console.log(typeof b13)    // we always get string as output

// input always will be considerted as a string in JS
// whatever we input ...... JS considered that as a variable




console.log(10 + 15)
// if we have two numbers     +    working as sum



console.log(10 + "12")
// if we have one numbers and one string       +    working as concatination (combine both)
// in JS both numbers(10) and string(12) are considered as string . 
// so JS combine both


// if we want to convert string into  integer
// we have to -->  PARSE the string into an integer   -->       var_name = parseInt(var_name)
//  ex: parseInt(a) , parseInt(b1) , parseInt(b5)  , parseInt(b7) 


var b14 = prompt("enter b14 ")
var b15 = prompt("enter b15 ")
b14 = parseInt(b14)
b15 = parseInt(b15)

var sum = b14 + b15

console.log(sum)
alert(sum)


