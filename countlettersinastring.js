function countLetters (string) {
        var a = string.toLowerCase()
        var n = a.replace(/[^A-Z]+/ig, "");
        
        var x = {};
        n.split('').forEach(function(s){
          x[s] ? x [s]++ : x[s] = 1;
        })
        return x;
}
