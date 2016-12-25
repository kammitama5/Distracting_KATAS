function area(d,l){
    if (d <= l){
      console.log("Not a rectangle")
    }
    else{
    m = (Math.sqrt((d * d) - (l * l)))
    a = m * l
    return(Math.round(a * 100) / 100)
    }
}

area(12, 5)
area(51, 22)