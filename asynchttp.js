var http = require('http');

// Empty string to use to log data returned from http requests
var temp = "";


http.get(process.argv[2], function(response) {
    response.on('data', function(data) {
        temp += data;
    });
    // Waits for all data in stream to be returned and logs, it then empties the temp string to be filled again
    response.on('end', function() {
        console.log(temp.toString());
        temp = '';
        http.get(process.argv[3], function(response) {
            response.on('data', function(data) {
                temp += data;
            });
            response.on('end', function() {
                console.log(temp.toString());
                temp = '';
                http.get(process.argv[4], function(response) {
                    response.on('data', function(data) {
                        temp += data;    
                    });
                    response.on('end', function() {
                       console.log(temp.toString()); 
                    });
                });
            });
        });
    });
});

// // Learnyounode answer
// var http = require('http')  
//      var bl = require('bl')  
//      var results = []  
//      var count = 0  
       
//      function printResults () {  
//        for (var i = 0; i < 3; i++)  
//          console.log(results[i])  
//      }  
       
//      function httpGet (index) {  
//        http.get(process.argv[2 + index], function (response) {  
//          response.pipe(bl(function (err, data) {  
//            if (err)  
//              return console.error(err)  
       
//            results[index] = data.toString()  
//            count++  
       
//            if (count == 3)  
//              printResults()  
//          }))  
//        })  
//      }  
       
//      for (var i = 0; i < 3; i++)  
//        httpGet(i)