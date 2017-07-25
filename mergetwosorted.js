function mergeArrays(arr1, arr2){
  var a = arr1.concat(arr2)
  a = a.sort((a, b) => a - b);
  return a
}

mergeArrays([3,4,9],[1,5,10])// should return [1,3,4,5,9,10]
mergeArrays([4,8,9,10,40],[43,44,85,325,326])// should return [4,8,9,10,40,43,44,85,325,326]
mergeArrays([3,4,9],[1,5,10])// should return [1,3,4,5,9,10]
