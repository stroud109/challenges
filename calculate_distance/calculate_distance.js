(function() {
    'use strict';

    var regexp = /\((-?\d+), (-?\d+)\) \((-?\d+), (-?\d+)\)/;

    var calcDistance = function(line) {
        var numbers = line.match(regexp);
        var length = Math.abs(parseInt(numbers[1], 10) - parseInt(numbers[3], 10));
        var height = Math.abs(parseInt(numbers[2], 10) - parseInt(numbers[4], 10));
        return Math.sqrt(Math.pow(length, 2) + Math.pow(height, 2));
    };

    var fs = require('fs');
    fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
        if (line !== '') {
            console.log(calcDistance(line));
        }
    });

})();
