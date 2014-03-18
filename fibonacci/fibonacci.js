(function() {
    'use strict';

    var fibonacci = function(n) {
        if (n === 0) {
            return 0;
        }
        else if (n <= 2) {
            return 1;
        }
        else {
            return fibonacci(n-1) + fibonacci(n-2);
        }
    };

    var fs  = require('fs');
    fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
        if (line !== '') {
            console.log(fibonacci(parseInt(line, 10)));
        }
    });
})();
