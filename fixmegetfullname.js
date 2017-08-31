class Dinglemouse{

  constructor( firstName, lastName ){
    this.firstName = firstName
    this.lastName = lastName
    return this.firstName + " " + this.lastName;
  }
  
  getFullName(){
    if ((this.lastName == null) && (this.firstName == null)){
      return " "
    }
    else if ((this.lastName == '')){
      return this.firstName
    }
    else if (this.firstName == ''){
      return this.lastName
    }
    else if (this.lastName == null){
      return this.firstName
    }
    else if (this.firstName == null){
      return this.lastName
    }
    else{
    return this.firstName + " " + this.lastName;
    }
  }
  
}