(function() {

    var getSumOfIds = function(attrs) {
        var sumOfIds = 0;
        var items = attrs.menu.items;
        for (var i = 0; i < items.length; i++) {
            if (items[i] && 'label' in items[i]) {
                sumOfIds += parseInt(items[i].id, 10);
            }
        }
        return sumOfIds;
    };

    var fs = require('fs');
    fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
        if (line !== '') {
            line = JSON.parse(line);
            console.log(getSumOfIds(line));
        }
    });

})();
