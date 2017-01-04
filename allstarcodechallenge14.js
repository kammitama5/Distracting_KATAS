
function median(array)
{
    
    c = array.sort((a, b) => a - b);
    length1 = c.length
    len  = array.length / 2
    len1 = (array.length / 2) - 1
    oddlen = Math.trunc(len)

    if (length1 % 2 == 0){
     return(((c[len] + c[len1])) / 2)
    }
    else{
      return(c[oddlen])
    }
    
}
