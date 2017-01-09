function getMissingElement(superImportantArray){
  
        count = 0
        total = 0
        for (var i = 0; i < (superImportantArray.length + 1); i++){
            count = count + i
        }
        a =  count
        for (var j = 0; j < superImportantArray.length; j++){
            total = total + superImportantArray[j]
        }
        b =  total
        missing = a - b
        return missing

}
