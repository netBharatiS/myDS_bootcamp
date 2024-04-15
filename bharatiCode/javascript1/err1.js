'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}


/*
 * Complete the 'preprocessDate' function below.
 *
 * The function is expected to return a STRING_ARRAY.
 * The function accepts STRING_ARRAY dates as parameter.
 */

function preprocessDate(dates) {
    // Write your code here
  //string w = dates.split; 
  
 var output = dates.split(/(\s+)/).filter( function(e) { return e.trim().length > 0; } );
 output[0] = output[0].substring(0, output[0].length - 2);
 console.log(output);
 
//  if output[1] = 'Jan'; output[1] = '01';
//  elseif output[1] = 'Feb'; output[1] = '02';
//  elseif output[1] = 'Mar'; output[1] = '03';
//  elseif output[1] = 'Apr'; output[1] = '04';
//  elseif output[1] = 'May'; output[1] = '05';
//  elseif output[1] = 'Jun'; output[1] = '06';
//  elseif output[1] = 'Jul'; output[1] = '07';
//  elseif output[1] = 'Aug'; output[1] = '08';
//  elseif output[1] = 'Sep'; output[1] = '09';
//  elseif output[1] = 'Oct'; output[1] = '10';
//  elseif output[1] = 'Nov'; output[1] = '11';
//  elseif output[1] = 'Dec'; output[1] = '12';
 
 console.log(output[2], '-',output[1], '-', output[0]);
 
 //
}
function main() {
 
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const datesCount = parseInt(readLine().trim(), 10);

    let dates = [];

    for (let i = 0; i < datesCount; i++) {
        const datesItem = readLine();
        dates.push(datesItem);
    }

    const result = preprocessDate(dates);

    ws.write(result.join('\n') + '\n');

    ws.end();
}
