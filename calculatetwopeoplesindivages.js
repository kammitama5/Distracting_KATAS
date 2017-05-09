function getAges(sum,difference){
    var arr = [];
    var val1 = ((difference + sum) / 2);
    var val2 = val1 - difference;
    
    if ((sum < 0) || (difference < 0) || (val1 < 0) || (val2 < 0))
    {
      return null;
    }
    else{
      arr.push(val1)
      arr.push(val2)
    }
    return arr;
};
