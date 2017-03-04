function reverseLetter(str) {

    var a = str.replace(/[^a-z]/gi,'') 
    var b = a.split("").reverse().join("");
    return (b)
 
}


