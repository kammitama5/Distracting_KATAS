function insurance(age, size, numofdays){
    base = 50 
    young = 10
    
    medium = 10
    fullsize = 15 
    custom = 15
    
    if ((numofdays <= 0) || (age <= 0)){
      //console.log(0)
      return total
    }
    else if ((age < 25) && (size == "economy")){
      total = (numofdays * base) + (young * numofdays)
      //console.log(total)
      return total
    }
    else if ((age < 25) && (size == "full-size")){
      total = (numofdays * base) + (young * numofdays) + (fullsize * numofdays)
      //console.log(total)
      return total
    }
    else if ((age < 25) && (size == "medium")){
      total = (numofdays * base) + (young * numofdays) + (medium * numofdays)
      //console.log(total)
      return total
    }
    else if ((age < 25) && (size == "my custom car")){
      total = (numofdays * base) + (young * numofdays) + (custom * numofdays)
      //console.log(total)
      return total
    }
    
    else if ((age >=25) && (size == "economy")){
      total = (numofdays * base) 
      //console.log(total)
      return total
    }
    else if ((age >=25) && (size == "full-size")){
      total = (numofdays * base) + (fullsize * numofdays)
      //console.log(total)
      return total
    }
    else if ((age >=25) && (size == "medium")){
      total = (numofdays * base) + (medium * numofdays)
      //console.log(total)
      return total
    }
    else if ((age >=25) && (size == "my custom car")){
      total = (numofdays * base) + (custom * numofdays)
      //console.log(total)
      return total
    }
    else {
      //console.log("I have no idea")
      return 
    }
  
  
  
  
}


insurance(18, "medium", 7) //, 490);
insurance(30,"full-size",30) //,1950);
insurance(21,"economy",-10) //, 0);
insurance(42,"my custom car",7) //, 455);

// if age < 25 => 10 dollars per day 
// if economy => 0 
// if medium => 10 dollars per day 
// if full size => 15 dollars per day 

//base charge => 50 dollars a day 

// negative rental days return 0 cost 