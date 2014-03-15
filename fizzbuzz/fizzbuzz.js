(function() {
    'use strict';

    var fizzbuzz = function (sequence) {
        var fizz = sequence[0];
        var buzz = sequence[1];
        var max_num = sequence[2];
        var solution = [];

        for(var i = 1; i <= max_num; i++) {
            if (i % fizz === 0 && i % buzz === 0) {
                solution.push('FB');
            }
            else if (i % fizz === 0) {
                solution.push('F');
            }
            else if (i % buzz === 0) {
                solution.push('B');
            }
            else {
                solution.push(i);
            }
        }

        return solution.join(' ');
    };

    var splitLine = function (line) {
        return line.split(' ').map(Number);
    };

    var fs  = require('fs');
    fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
        if (line !== '') {
            console.log(fizzbuzz(splitLine(line)));
        }
    });
})();

