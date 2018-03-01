function calculateTax(dollars, taxRate) {
    var tax = (taxRate / 100.0) * dollars;
    return tax.toFixed(2);
}

