console.log(" this is array ")
//                                             DECLARATION ARRAY AND DISPLAY ARRAY


// create an Array

// var array_name = [elemnet1 , element2 .......]

var arr1 = []
console.log(arr1)

var arr2 = new Array()
console.log(arr2)

var arr3 =[1234 , "something" , false , null]
console.log(arr3)
console.log(typeof arr3)  // outout:- object
// here 1234 is a number_data_type and something is string_data_type and false is boolean_data_type and null is null_data_type

// in JS , araay is considere as object , it means array is an object_data_type

// in  JS , array is collection of Data

// in JS , in array , data can be similar data type or different data type


// if you want to print specific element in Array
// console.log(array_name[index])
// alert(array_name[index])


// how we can wriote index
// index       0          1          2       3
// var arr3 =[1234 , "something" , false , null]

// index is always starting from 0,1,2,3,...............so on

console.log(arr3[3])
alert(arr3[3])

// if we try to know data type of specific element in array
// console.log (typeof array_name[index])
// alert (typeof array_name[index])

console.log(typeof arr3[2])
alert(typeof arr3[2])















//                                POINTING IN ARRAY   

// how can i pointiong in Array
var num = 8 
var arr4 = [ 1234 , num , false , null] 
console.log(arr4) // inthis array num is pointing to 8















//                                                HOW TO KEEP  ONE ARRAY INSIDE ANOTHER ARRAY :-

//                                  METHOD-1 

// IN THIS METHOD
//  REMEMBER :- parents_array always come after  child array....... when you create individually parents_array and child_array



// var child_array_1 = [child_element_1_of_child_araay_1 , child_element_2_of_child_araay_1 , child_element_3_of_child_araay_1 , child_element_4_of_child_araay_1 ]
// var child_array_2 = [child_element_1_of_child_araay_2 , child_element_2_of_child_araay_2 , child_element_3_of_child_araay_2 , child_element_4_of_child_araay_2 ]
// var child_array_3 = [child_element_1_of_child_araay_3 , child_element_2_of_child_araay_3 , child_element_3_of_child_araay_3 , child_element_4_of_child_araay_3 ]
// var child_array_4 = [child_element_1_of_child_araay_4 , child_element_2_of_child_araay_4 , child_element_3_of_child_araay_4 , child_element_4_of_child_araay_4 ]
// var child_array_5 = [child_element_1_of_child_araay_5 , child_element_2_of_child_araay_5 , child_element_3_of_child_araay_5 , child_element_4_of_child_araay_5 ]

// var parent_array = [child_element 1 , child_element 2 , child_array_1 , child_array_2 , child_element 3 , child_array_3 , child_array_4 ,  child_element 5 , child_element 6 , child_element 7 , child_array_5 , child_element 8  ]

// you can insert one or more than one array inside a array at any position


//                                  METHOD-2 

//  var another_arrray_name = [  element 1 , 
//                               element 2 , 
//                               [child_element_1_of_child_araay_1 , child_element_2_of_child_araay_1 , child_element_3_of_child_araay_1 , child_element_4_of_child_araay_1 ] , 
//                               [child_element_1_of_child_araay_2 , child_element_2_of_child_araay_2 , child_element_3_of_child_araay_2 , child_element_4_of_child_araay_2 ] , 
//                               element 3 , 
//                               [child_element_1_of_child_araay_3 , child_element_2_of_child_araay_3 , child_element_3_of_child_araay_3 , child_element_4_of_child_araay_3 ] , 
//                               [child_element_1_of_child_araay_4 , child_element_2_of_child_araay_4 , child_element_3_of_child_araay_4 , child_element_4_of_child_araay_4 ] ,  
//                               element 5 , 
//                               element 6 , 
//                               element 7 , 
//                               [child_element_1_of_child_araay_5 , child_element_2_of_child_araay_5 , child_element_3_of_child_araay_5 , child_element_4_of_child_araay_5 ] , 
//                               element 8  ]












//                            NOW I WILL DISCUSS ABOUT INDEX ONE ARRAY INSIDE A ANOTHER ARRAY :-
// step 1 = first index at main array or parrent array
// step 2 = then index at child array with the help of index of childe array in parent array

//                                  METHOD-1 

// step 1 :-
// index                    0                   1                   2              3            4                   5               6                  7                8               9                   10              11          
// var parent_array = [child_element 1 , child_element 2 , child_array_1 , child_array_2 , child_element 3 , child_array_3 , child_array_4 ,  child_element 5 , child_element 6 , child_element 7 , child_array_5 , child_element 8  ] 

// now we know that index of child_array_1 = 2 
//                  index of child_array_2 = 3
//                  index of child_array_3 = 5
//                  index of child_array_4 = 6
//                  index of child_array_5 = 10


// step 2 :-

// now we know that index of child_array_1 = 2  so , 
// index                                [2][0]                          [2][1]                              [2][2]                          [2][3]
// var child_array_1 = [child_element_1_of_child_araay_1 , child_element_2_of_child_araay_1 , child_element_3_of_child_araay_1 , child_element_4_of_child_araay_1 ]

// now we know that index of child_array_2 = 3  so , 
// index                                [3][0]                          [3][1]                              [3][2]                          [3][3]
// var child_array_2 = [child_element_1_of_child_araay_2 , child_element_2_of_child_araay_2 , child_element_3_of_child_araay_2 , child_element_4_of_child_araay_2 ]

// now we know that index of child_array_3 = 5  so , 
// index                                [5][0]                          [5][1]                              [5][2]                          [5][3]
// var child_array_3 = [child_element_1_of_child_araay_3 , child_element_2_of_child_araay_3 , child_element_3_of_child_araay_3 , child_element_4_of_child_araay_3 ]

// now we know that index of child_array_4 = 6  so , 
// index                                [6][0]                          [6][1]                              [6][2]                          [6][3]
// var child_array_4 = [child_element_1_of_child_araay_4 , child_element_2_of_child_araay_4 , child_element_3_of_child_araay_4 , child_element_4_of_child_araay_4 ]

// now we know that index of child_array_1 = 10  so , 
// index                                [10][0]                          [10][1]                              [10][2]                          [10][3]
// var child_array_5 = [child_element_1_of_child_araay_5 , child_element_2_of_child_araay_5 , child_element_3_of_child_araay_5 , child_element_4_of_child_araay_5 ]





// you can insert one or more than one array inside a array at any position


//                                  METHOD-2 

// index                            0           1                   [2][0]                              [2][1]                              [2][2]                              [2][3]                                      [3][0]                          [3][1]                              [3][2]                              [3][3]                    [4]                       [5][0]                          [5][1]                                  [5][2]                          [5][3]                              [6][0]                              [6][1]                              [6][2]                              [6][3]                     [7]        [8]           [9]            [10][0]                                  [10][1]                             [10][2]                             [10][3]                       [11]
//  var another_arrray_name = [  element 1 , element 2 , [child_element_1_of_child_araay_1 , child_element_2_of_child_araay_1 , child_element_3_of_child_araay_1 , child_element_4_of_child_araay_1 ] ,  [child_element_1_of_child_araay_2 , child_element_2_of_child_araay_2 , child_element_3_of_child_araay_2 , child_element_4_of_child_araay_2 ] ,  element 3 ,  [child_element_1_of_child_araay_3 , child_element_2_of_child_araay_3 , child_element_3_of_child_araay_3 , child_element_4_of_child_araay_3 ] , [child_element_1_of_child_araay_4 , child_element_2_of_child_araay_4 , child_element_3_of_child_araay_4 , child_element_4_of_child_araay_4 ] ,   element 5 , element 6 ,  element 7 ,  [child_element_1_of_child_araay_5 , child_element_2_of_child_araay_5 , child_element_3_of_child_araay_5 , child_element_4_of_child_araay_5 ] ,  element 8  ]



// example:-  

var parent_array_1_child_array_1 = ["parent_array_1_child_array_1_element_1" , "parent_array_1_child_array_1_element_2" , "parent_array_1_child_array_1_element_3"]
var parent_array_1_child_array_2 = ["parent_array_1_child_array_2_element_1" , "parent_array_1_child_array_2_element_2" , "parent_array_1_child_array_2_element_3" , "parent_array_1_child_array_2_element_4" , "parent_array_1_child_array_2_element_5"]
var parent_array_1 = ["parent_array_1_child_element_1" , "parent_array_1_child_element_2" , parent_array_1_child_array_1 , "parent_array_1_element_3" , "parent_array_1_element_4" , parent_array_1_child_array_2]
console.log(parent_array_1)

// example :-

var papa = ["abahy" , "abhisheksh" , "anisha" ]
var mammi = ["vani" , "yashu" , "sumit" , "akshay"]
var dadaji = [papa , mammi , "cacha" , false ,  44.7, "chachi" , 125 , null , true]














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





//                                         FIND LENGTH OF ARRAY
// syntax :-
//             console.log ( array_name.length)
//             alert( array_name.length)






// study yourself


// Split in array

// join in array

// concate in array

// splice and slice in array

// for each

// math.max

