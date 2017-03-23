function invertGrades(scale, value) {
   return scale - ((value / scale) * scale) + 1
}

