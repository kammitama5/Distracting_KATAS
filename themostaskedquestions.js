function detect(comment)
{
  var word = comment.split(" ");
  if ((word[0] == "Can") && (word[1] == "someone") && (word[2] == "explain"))
  {
    return(true);
  }
  else
  {
    return(false);
  }
  
}


detect('Can someone explain to me what this kata is about?');//true
detect('Can someone solve this kata for me?')//false
