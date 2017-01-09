function solution(value){
        a = (5 - value.toString().length)
        b = ("0".repeat(a))
        
        ans = "Value is " + b + value.toString()
        return ans

}
