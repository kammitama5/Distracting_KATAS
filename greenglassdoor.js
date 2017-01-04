
function stepThroughWith(s) {
    if ((/([a-z])\1/i).test(s) == true){
        return true
    }
    else{
        return false
    }
}

