var w = "1th Mar 2068";
var output = w.split(/(\s+)/).filter( function(e) { return e.trim().length > 0; } );
output[0] = output[0].substring(0, output[0].length - 2)
console.log(output)