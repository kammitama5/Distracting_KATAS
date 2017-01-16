function hello(name){
    if (name == ""){
      return "Hello, World!"
    }
    else if (name == null){
      return "Hello, World!"
    }
    else{
      a = name.toLowerCase()
      return "Hello, " + a[0].toUpperCase() + a.substr(1) + "!"
    }
  
}



