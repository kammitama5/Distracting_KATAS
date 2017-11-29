function sortByArea(array)
{
  
  var arr1 = [] // rectangle
  var arr2 = [] // circle
  var arr3 = [] // pushed area from circle, rect
  for (var i = 0; i < array.length; i++)
  {
    if (typeof(array[i]) !== 'object'){
      arr2.push(array[i])
    }
    else{
      arr1.push(array[i])
    }
  }
  // find area of rect
  for (var x = 0; x < arr1.length; x++)
  {
    first =  arr1[x][0]
    second = arr1[x][1]
    area = first * second
    arr3.push(area.toFixed(2) / 1)
  }
  
  //find area of circle
  for (var j = 0; j < arr2.length; j++)
  {
    area = Math.PI * ((arr2[j] * arr2[j]))
    arr3.push(area.toFixed(2) / 1)
  }
  arr3 = arr3.sort((a, b) => a - b);
  
  return arr3;
}

