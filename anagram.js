function isAnagram(stringOne, stringTwo) {
    if ((stringOne == "") && (stringTwo == "")){
      //console.log(true)
      return true
    }
    else{
    var a = stringOne.toLowerCase().replace(/ /g,'')
    var b = stringTwo.toLowerCase().replace(/ /g,'')
    var c = a.split('').sort().join('')
    var d = b.split('').sort().join('')
    if (c == d){
      //console.log(true)
      return true
    }
    else{
      //console.log(false)
      return false
    }
    }
    return
}
