function rank(card) {
  if ((parseInt(card[0]) >= 2) || (parseInt(card[0] <= 9))){
    return parseInt(card[0])
  }
  else if (card[0] == 'T'){
    return 10;
  }
  else if (card[0] == 'J'){
    return 11;
  }
  else if (card[0] == 'Q'){
    return 12;
  }
  else if (card[0] == 'K'){
    return 13;
  }
  else if (card[0] == 'A'){
    return 14;
  }
  else{
    return false;
  }
}

