function liftoff(instructions){
    instructions = instructions.sort((a, b) => a - b);
    var a = instructions.reverse()
    var b  = a.join(' ') + ' liftoff!'
    return(b)
}

