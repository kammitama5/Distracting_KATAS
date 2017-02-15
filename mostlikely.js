function mostLikely(prob1,prob2){
        var a = prob1.replace(":", "/")
        var a1 = prob2.replace(":", "/")
        var b = eval(a) * 1.0 
        var b1 = eval(a1) * 1.0
        if (b > b1){
          return true
        }
        else{
          return false
        }
}

