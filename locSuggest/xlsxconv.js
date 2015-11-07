xlsxj = require("xlsx-to-json");
xlsxj({
    input: "jetblue.xlsx", 
    output: "getawayPkg.json"
}, function(err, result) {
    if(err) {
	console.error(err);
    }else {
	console.log(result);
    }
});
