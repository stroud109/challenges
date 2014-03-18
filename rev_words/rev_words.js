(function() {
    'use strict';

    var revWords = function(line) {
        return line.split(' ').reverse().join(' ');
    };

    var fs = require('fs');
    fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
        if (line !== '') {
            console.log(revWords(line));
        }
    });

})();
