function mrsMiggins(str) {
    var rep = /dog |DOG|rain|RAIN|children|CHILDREN|broccoli|BROCCOLI|pension|PENSION/g;
    str = str.replace(rep, "cat"); 
    return str;
}
