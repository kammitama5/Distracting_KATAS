function correctPolishLetters (string) {
    string = string.replace(/ą/g,'a').replace('ć','c').
	replace('ę','e').replace('ń','n').replace('ó','o').
	replace('ś','s').replace('ź','z').replace('ż','z').
	replace(/ł/g,'l');

    return(string)

}
