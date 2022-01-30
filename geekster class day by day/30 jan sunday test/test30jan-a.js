// write a programme to print thr nth fibonacci number. take user input

var num = prompt("enetr a number")
num = parseInt(num)

var n1 = 0
var n2 = 1

if (isNaN (num))
 {
    alert("enter a valid number")
 }

else
{


   // console.log(n1)


    for(let i =1 ; i<= num ; i++)
    {
        console.log(n1)
        console.log("\n")
        var next_term = n1 + n2
        n1 = n2
        n2 = next_term
    }



}