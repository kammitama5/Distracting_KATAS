
function betweenExtremes(numbers) {
        a = numbers.sort((a,b)=>a-b);
        b = Math.max.apply(Math, a)
        c = Math.min.apply(Math, a)
        diff = b - c 
        return(diff)
}
