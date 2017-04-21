function trickyDoubles(n){
      var a = n.toString()
      var len = (a.length / 2);
      var len1 = a.length;
      
      var x = a.slice(0, len)
      //console.log(x)
      var y = a.slice(len, len1)
      //console.log(y)
      
      
      if (x == y){
        return (n)
      }
      else{
       return (n * 2)
      }
     
      return
}
