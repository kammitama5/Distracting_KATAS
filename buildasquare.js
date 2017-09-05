function generateShape(int){
  g = []
  for (var i = 0; i < int; i++)
  {
    for (var j = 0; j < 1; j++){
      g.push(("+").repeat(int))
    }
  }
  g = g.join("\n")
  return g
}

