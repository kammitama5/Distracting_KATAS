function arrayPlusArray(arr1, arr2) {
  const array1 = arr1.concat(arr2)
  const reducer = (accumulator, currentValue) => accumulator + currentValue;
  return array1.reduce(reducer)
}

