/* *********************************    Arrays inside objects      ********************************* */


// 32. Add a new property to your penguin called favoriteFoods and set it equal to an array containing a list of three strings.
var penguin = 
{
  character : "Whiteblack",
  origin    : "Whiteblack the Penguin Sees the World",
  author    : "H.A.Rey and Margaret Rey",
  favouriteFoods : ["first", "second", "third"]
};




// 33. Access your penguin's second favorite food and print it to the console using console.log()
console.log(penguin.favouriteFoods[1])



// 34. Create a new variable called firstFavFood and set it equal to the first item in your penguin's array of favorite foods.

var firstFavFood = "potato";
penguin.favouriteFoods[0] = firstFavFood;
console.log(penguin.favouriteFoods);



// 35. Add another food to the end of the list.
console.log(penguin.favouriteFoods.length)
penguin.favouriteFoods[3] = "wantons"
console.log(penguin.favouriteFoods)



// 36. Print the length of your penguin's favoriteFoods array to the console with console.log()
console.log(penguin.favouriteFoods.length)
var len = penguin.favouriteFoods.length


// 37. Without modifying any of your previous code, write a new line of code that changes the value of the last item in the list to "pineapples" (overwriting the previous value).
penguin.favouriteFoods[len -1] = "pineapples"
console.log(penguin.favouriteFoods)



// 38. Create a new variable named lastFavFood that will always point to the last element of your penguin's favoriteFoods array, no matter how many items are in the list. (Hint: this is essentially the same problem as step 18 from above.)
var lastFavFood = penguin.favouriteFoods[penguin.favouriteFoods.length - 1]
console.log(lastFavFood)


// 39. Write a for loop to iterate through every food in your penguin's favoriteFood property and print each one to the console. (Hint: This loop will look exactly the same as the one you wrote for step 16 above, except now you're accessing the array as a property of an object.)
for (var i = 0; i < penguin.favouriteFoods.length; i++){
  console.log(penguin.favouriteFoods[i])
}

 


