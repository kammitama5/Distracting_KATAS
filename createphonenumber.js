function createPhoneNumber(numbers){
        arr = []
        arr1 = []
        arr2 = []
        a = numbers.slice(0, 3)
        b = numbers.slice(3, 6)
        c = numbers.splice(6)
        
        x = a.join("")
        
        
        y = b.join("")
        
        z = c.join("")
        
        return ("(" + x +")" + " " + y + "-" + z)
 
}
