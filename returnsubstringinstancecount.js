function solution(fullText, searchText){
      a = fullText 
      b = searchText
      count = 0
      
      var index = a.indexOf(b);
      while(index!=-1){
        count = count + 1 
        index = a.indexOf(b, index + 1)
      }
      console.log(count)
}

