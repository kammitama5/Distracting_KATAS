function nerdify(txt){
  txt = txt.replace(/a/gi, '4')
  txt = txt.replace(/A/gi, '4')
  txt = txt.replace(/e/gi, '3')
  txt = txt.replace(/E/gi, '3')
  txt = txt.replace(/l/g, '1')
  console.log(txt)
  return txt
}
