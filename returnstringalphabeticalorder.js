function alphabetOrder(str){
    var arr = []
    var result =""
    for (var i = 0; i < str.length; i++)
    {
      arr.push(str[i])
      
    }
    var b = arr.sort()
    var c = b.join("")
    //console.log(c)
    return c
}
