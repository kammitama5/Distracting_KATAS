/* *********************************    Review of objects      ********************************* */

// 19. Pick a penguin from Wikipedia's List of Fictional Penguins and create an object named myPenguin with properties that represent the information listed in each column on that Wikipedia page (for example: the character's name, origin, and author).
var myPenguin = 
{
  character : "Whiteblack",
  origin    : "Whiteblack the Penguin Sees the World",
  author    : "H.A.Rey and Margaret Rey"
};



// 20. Use console.log() to print the penguin's name to the console as part of a welcome message, like "Hello, I'm a penguin and my name is [NAME HERE]!"
console.log("Hello, I'm a penguin and my name is " + myPenguin.character + ".");



// 21. Write another line of code that adds a new property to your penguin called canFly and set it to false. (Note: Don't modify your penguin-creation code that you wrote above! Do this step in a separate line of code.)
myPenguin["canFly"] = false;
console.log(myPenguin);



// 22. Add a method to your penguin called chirp that prints to the console: "CHIRP CHIRP! Is this what penguins sound like?" (Note: Again, don't modify your previous code! Do this step by writing a new line of code.)
myPenguin.chirp = function(){console.log("CHIRP CHIRP!");}
console.log(myPenguin.chirp());



// 23. Add another method to your penguin called sayHello that prints to the console the same message from step 20 above. But this time, be sure to use the mystical, magical, all-powerful this keyword to access your penguin's name, so that way if you c hange its name later, your method will still work!
myPenguin.sayHello = function(){console.log(this.character);}
console.log(myPenguin.sayHello());


// 24. Next, call your penguin's sayHello() method and make sure that it works! (Hint: if you need an example of what it looks like when you call a method of an object, look at console.log() -- that's how you call the log() method of the console object!)
console.log(myPenguin.sayHello());



// 25. Without modifying any of your previous code, change the penguin's name to "Penguin McPenguinFace" and then call your penguin's sayHello() function one more time to make sure it still works.
myPenguin.character = "Penguin McPenguinFace";
console.log(myPenguin.sayHello());


// 26. Write another method called fly, and inside that method, use an if / else statement to print "I can fly!" to the console if your penguin's canFly property is true, or "No flying for me!" if its canFly property is false.
myPenguin.fly = function(canFly){
  if(canFly === true){
    console.log("I can fly");
  }
  else{
    console.log("No flying for me!");
  }
}



// 27. Call your penguin's fly() method and make sure it works!
console.log(myPenguin.fly(true));
console.log(myPenguin.fly(false));



// 28. Change the canFly property to true -- again, without modifying any of your previous code!
canFly=true;
myPenguin.fly(canFly=true);
//console.log(penguin.fly());



// 29. Now call your penguin's fly() method again and make sure it works as expected!
myPenguin.fly();



// 30. Write a for ... in loop to print each key to the console. (Hint: See this page for an example of this special type of loop.)
var keys = [];
for (var i in myPenguin) keys.push(i);
console.log(keys)

// 31. Write another for ... in loop to print the value of each key to the console. (Hint: You'll need to use bracket notation to access the values this way, instead of dot notation!)
var values = [];
for (var i in myPenguin) values.push(myPenguin[i]);
console.log(values);
//dammit the last part didn't print LOL. 


