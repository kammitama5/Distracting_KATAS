function squareAreaToCircle(size){
    var diam = Math.sqrt(size)
    var radius = diam / 2.0 
    var areacirc = Math.PI * (radius * radius)
    return areacirc
}
