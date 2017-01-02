function convertCF(num, scale){
    if (scale == "f") {
        return((num * (9 / 5)) + (32))
    }
    else if (scale == "c"){
        return((num - 32) / (9/5))
    }
    else if ((scale != "c") || (scale != "f")){
      //covert to celsius
        return((num - 32) / (9/5))
        
    }
    else{
      
        return Error
    }
}

convertCF(60, "f") //, 140);
convertCF(32, "c") //, 0);
convertCF(50) //, 10);