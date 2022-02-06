console.log("it is working")
    
var arr = []

arr[0] = "aayush"
arr[100] = "sinha"

console.log(arr)

var arr2 = [ "element 1" , "element 2" , "element 3" , "element 4" ,"element 5" ]
console.log(arr2)



var arr3 = []

arr3[1.4] = "raj"
arr3["abcd"] = "jam"

console.log(arr3)

var arr4 = []
arr4[6-3]= "good"

console.log(arr4)

var arr5 = []
arr5[6-3+12*3]= "man"

console.log(arr5)

var arr6 = []
var num = 82;
arr6[num] = "motu"

console.log(arr6)


// syntax of Object

/* 
object_name {
                key_name_1 : key_value_1 ,
                key_name_2 : key_value_2 ,
                key_name_3 : key_value_3 ,
                key_name_4 : key_value_4 ,
                key_name_5 : key_value_5 ,
                key_name_6 : key_value_6 ,
                key_name_7 : key_value_7 ,
                            .
                            .
                            .
                            .
                            .
                            .
                key_name_n : key_value_n , 
           }

*/


//                       DISPLAY OF OBJECT
//              console.log(object_name)

//            console.log(object_name.key_name)         or
//            console.log(object_name[index_name])



//             UPDATE THE OBJECT VALUE

//             object_name.key_name = updated_value         or
//             object_name[key_name] = updated_value






//                               POINT THE KEY IN OBJECT

//           var var_name = key_name

// console.log ( object_name.var_name)    // this is wrong... we get undefined.... if we denoting index of object from variable ..... then we will not use dot ..... we have to use bracket []

// console.log ( object_name[var_name] )    // this is right












var obj1 ={
    "first_name" : "aayush"  ,
    "last_name"  :  "sinha" ,
    "g" : 1233 
          }

          console.log(obj1)

          // for index in object

          // object_name.index_name         or
          // object_name[index_name]

          console.log(obj1.last_name)
          console.log(obj1["first_name"])

          obj1.first_name = "rajesh"

          console.log(obj1)

          var k = "first_name"

          console.log(obj1.k) // this is wrong... we get undefined.... if we denoting index of object from variable ..... then we will not use dot ..... we have to use bracket []

          console.log(obj1[k]) // this is right




var arr8 = []
console.log(arr8[1000]) // index 1000 of array 8 is not .... so we get output   undefined

 console.log(obj1.m) // key_name  m  of obj1 is not .... so we get output   undefined
          



