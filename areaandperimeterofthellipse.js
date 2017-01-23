function elipse(a,b){

    var Area = (Math.PI * a * b).toFixed(1)
    var Perimeter = (Math.PI * ((3.0/2.0) * (a+b) - Math.sqrt(a * b))).toFixed(1)
    var sarea = (Area).toString()
    var sperimeter = (Perimeter).toString()
    return "Area: " + sarea + "," + " perimeter: " + sperimeter
}
