
//                                   UPDATE AN ARRAY 


array_prime = [2 , 3 , 5 , 7 , 11 ,13, 17 , 19 , 23 , 29 , 31 , 37 , 41 , 43, 47 , 53 , 59 , 61 , 67 , 71 , 73 , 79 , 83, 89 , 97]

console.log ( array_prime )
console.log ( array_prime[2] )



// if you want to update an array for particuar index in array
// SYNTAX :-
//    array_name[updated_index] = updated_value


array_prime[2] = 101
console.log ( array_prime )
console.log ( array_prime[2] )







//                              INSERT OR PUSH ANY VALUE IN ARRAY AT LAST INDEX

// if you want to push or insert any value in an array.... then you can use push method
// syntax:-
//              Array_Name.push ( pushing_element )

var array_prime_2 = [ 2 , 3 , 5, 7 ]
console.log ( array_prime_2 )               // output:- [ 2 , 3 , 5, , 7 ]

array_prime_2.push ( 11 )
console.log ( array_prime_2 )       // output:- [ 2 , 3 , 5, , 7 , 11 ]

array_prime_2.push ( 17 )
console.log ( array_prime_2 )       // output:- [ 2 , 3 , 5, , 7 , 11  , 17 ]


// if you are pushing any element using PUSH function then ...... pushing element always comes at last position or index













//                            DELETE OR REMOVE OR POP ANY VALUE IN ARRAY FROM LAST INDEX

// if you want to push or insert any value in an array.... then you can use push method
// syntax:-
//              Array_Name.pop ()


array_prime_2.pop ()
console.log ( array_prime_2 )       // output:- [ 2 , 3 , 5, , 7 , 11 ]

array_prime_2.pop ()
console.log ( array_prime_2 )       // output:- [ 2 , 3 , 5, , 7 ]

array_prime_2.pop ()
console.log ( array_prime_2 )       // output:- [ 2 , 3 , 5 ]

array_prime_2.pop ()
console.log ( array_prime_2 )       // output:- [ 2 , 3 ]