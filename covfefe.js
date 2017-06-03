function covfefe(str)
{
  // 

  if (str.includes("coverage"))
  {
    var textTitle = "coverage"
    var str = str.replace(/coverage/g, 'covfefe');
  }
  else {
    str = str + " covfefe";
  }
   //console.log(str)
    return str;
}

