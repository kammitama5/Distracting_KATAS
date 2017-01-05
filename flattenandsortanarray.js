"use strict";

function flattenAndSort(array) {
  var a = [].concat.apply([], array);
  a.sort(function(a,b) { return a - b; });
  return a
}

