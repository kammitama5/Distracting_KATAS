function twoSort(s) {
        arr = []
        a = s.sort()
        b = a[0]
        d = (b.slice(-1))
        for (var i = 0; i < b.length - 1; i++){
          c = b[i] + '***'
          arr.push(c)
        }
        arr.push(d)
        w = arr.join("")
        return w
}

