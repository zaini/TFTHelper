var fs = require('fs');
var readMe = fs.readFileSync('readme.txt', 'utf8');

console.log(readMe);

fs.writeFileSync('writtento.txt', "");