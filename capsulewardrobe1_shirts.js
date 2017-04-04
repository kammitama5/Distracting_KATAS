var capsuleWardrobe = function (shirts) {
  var total = 0;
  for (var i = 0; i < shirts.length; i++)
    if (shirts[i] >= 8){
      total = total + 1;
    }
    return total;
}
