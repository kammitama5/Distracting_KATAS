function sortItOut(array){
        var odd = []
        var even = []
        for (var i = 0; i < array.length; i++){
          if (Math.floor(array[i]) % 2 === 0){
            even.push(array[i])
          }
          else{
            odd.push(array[i])
          }
        }
        even=even.sort((a,b)=>a-b);
        odd =odd.sort((a,b)=>a-b);
        return(odd.concat(even.reverse()) )
}
