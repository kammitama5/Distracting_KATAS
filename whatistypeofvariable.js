function type(value) {
    var a = Object.prototype.toString.apply(value)
    b = a.slice(8,-1)
    c = b.toLowerCase()
    return c
}
