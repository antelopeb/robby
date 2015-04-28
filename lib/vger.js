/*
*	Vger bot
*	a simple node bot who can learn commands
*	meant to run as a RESTful web service
*	with a simple web based front end to communicate
*	
*	Veejer is meant to be a useful learning tool
*	as well as a potential aid in automation...
*	so far he is none of these :)
*	
*	The interface is inspired by the interface provided
*	for Zakim on the W3C IRC bridge
*/

var fs = require("fs")

/*
*   function ask
*   @parameter q - string
*   @parameter callback - function
*/
exports.ask = function(q, callback){
    // fire off the process of answering the question
    vger.getAnswer(q, function(ans){
        callback(ans)
    })
}

/*
*   function init
*/
exports.init = function(){
    vger.initialize()
}

// define the main functions for vger here
var vger = {
    initialize : function(){
        // initialize vger by retreiving the stored commands
        console.log("initializing Vger")
        
    },
    getAnswer : function(q, callback) {
        // process the answer out to get actor/verb/object
        callback("Why did you say "+q+"?")
    }
}