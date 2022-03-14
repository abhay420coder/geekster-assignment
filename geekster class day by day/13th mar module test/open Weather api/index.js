var button = document.querySelector('.button');
var inputValue = document.querySelector('.inputValue');
var name2 = document.querySelector('.name');
var desc = document.querySelector('.desc');
var temp = document.querySelector('.temp');




// const weatherReport  = function (){
//     fetch('https://api.openweathermap.org/data/2.5/weather?'+inputValue.value+'&appid=090a46aceaba5a812193672cda6ca56b');
//    .then(response => response.json())
//    .then(data => console.log(data))

// .catch(err => alert("wrong City names"))
// }



button.addEventListener('click', function (){
    fetch('https://api.openweathermap.org/data/2.5/weather?'+inputValue.value+'&appid=090a46aceaba5a812193672cda6ca56b');
   .then((response) => response.json())
   .then((data) => {
       var name2Value = data['name2'];
       var tempValue = data['main']['temp'];
       var descValue = data['weather'][0]['description'];

       name2.innerHTML = name2Value;
       temp.innerHTML  = tempValue ;
       desc.innerHTML  = descValue ;
   });

   

   

.catch((err) => alert("wrong City names"));
})



