function twoOldestAges(ages){
        
        ages.sort(function(a,b) { return a - b; });
        b = ages.slice(1).slice(-2)
        return b 
        
       
}
