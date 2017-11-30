function whatsMyFirstName(str) {
  name = getMyNameByPosition(str, 0);
  var name = getMyNameByPosition(str, 0);
  return name;  
}

function getMyNameByPosition(str, position) {
  return str.split(" ")[position];
}

