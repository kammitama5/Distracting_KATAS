function makeString(s){
    w = []
    q = s.split(" ")
    for (var i = 0; i < q.length; i++){
        w.push((q)[i].charAt(0));
    
    }
    string = w.join("");
    return(string)
}



makeString("sees eyes xray yoat") // "sexy", "Wrong result for 'sees eyes xray yoat'")
makeString("brown eyes are nice") // "bean", "Wrong result for 'brown eyes are nice'")
makeString("cars are very nice") // "cavn", "Wrong result for 'cars are very nice'")
makeString("kaks de gan has a big head") // "kdghabh", "Wrong result for 'kaks de gan has a big head'")


