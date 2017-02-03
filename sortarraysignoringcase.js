sortme = function( names ){
    return names.sort(Intl.Collator().compare);
}
