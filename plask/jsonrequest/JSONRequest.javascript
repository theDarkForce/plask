/*
Script: JSONRequest.js

JSONRequest implementation:	
	This object is based on JSONRequest "official" draft and allows developers to perform get or post Ajax requestes in a simple way.
	
	With 3 public methods it's possible to manage more than a single request, using a queue to order requestes and to preserve server interactions.
	
	To know more about JSONRequest, please visit this page:  <http://www.json.org/JSONRequest.html>

Version:
	0.9 - probably requires more debug

Compatibility:
	FireFox - Version 1, 1.5, 2 and 3 (FireFox uses secure code evaluation)
	Internet Explorer - Version 5, 5.5, 6 and 7
	Opera - 8 and 9 (probably 7 too)
	Safari - Version 2 (probably 1 too)
	Konqueror - Version 3 or greater

Dependencies:
	<JSONRequestError.js>

Credits:
	- JSON site for draft, <http://www.json.org/JSONRequest.html>
	- Douglas Crockford to wrote above draft, <http://www.crockford.com/>

Author:
	Andrea Giammarchi, <http://www.3site.eu>

License:
	>Copyright (C) 2007 Andrea Giammarchi - www.3site.eu
	>	
	>Permission is hereby granted, free of charge,
	>to any person obtaining a copy of this software and associated
	>documentation files (the "Software"),
	>to deal in the Software without restriction,
	>including without limitation the rights to use, copy, modify, merge,
	>publish, distribute, sublicense, and/or sell copies of the Software,
	>and to permit persons to whom the Software is furnished to do so,
	>subject to the following conditions:
	>
	>The above copyright notice and this permission notice shall be included
	>in all copies or substantial portions of the Software.
	>
	>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
	>INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	>FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
	>IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
	>DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
	>ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
	>OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

/*
 Original version: http://devpro.it/JSON/files/JSONRequest-js.html
 code address:http://devpro.it/code/153.html
 Rewrite by qianqians
 2015-7-10
 */

/*
Object: JSONRequest
	Personal JSONRequest implementation with queue and multiple exception filters.

Example:
	>try {
	>	JSONRequest.get("mypage.php", function(sn, response, exception){
	>		alert(exception || response);
	>	});
	>}
	>catch(e) {
	>	alert(e);
	>}
*/
JSONRequest = new function(){

	/* Section: Methods - Public */
	
	/*
	Method: cancel
		blocks a request and call user callback if request has been successful blocked adding 10 milliseconds as delay time for next interaction.
	
	Arguments:
		Number - A valid JSONRequest serial number.
	
	Example:
		>mybtn.serialNumber = JSONRequest.get("page?something", function(sn, result, error){alert(result)});
		>mybtn.onclick = function(){
		>	JSONRequest.cancel(this.serialNumber);
		>};
	*/
	this.cancel = function(i){
		cancel(i);
	};
	
	/*
	Method: get
		prepares a request and push them inside queue. Throws a JSONRequest Exception if some parameter is wrong.
	
	Arguments:
		String - A valid url to call using Ajax respecting Same Origin Policy.
		Function - A callback with 3 arguments: serialNumber, responceObject, exceptionObject
		Number - The number of milliseconds to wait for the response. This parameter is optional. The default is 10000 (10 seconds). 

	Returns:
		Number - A new valid serial number.
	
	Example:
		>JSONRequest.get("page.psp?var=value", function(sn, result, error){alert([sn, result, error])});
	
	Note:
		If callback has not 3 arguments this method will throw an exception.
		If request has not problems callback is called using only 2 arguments, serialNumber and responseObject.
		This method uses default JSONRequest timeout, 10 seconds.
	*/
	this.get = function(url, done, timeout){
		var d=new Date();
		
		l = cb_list.length;
		cb_list.push([done, timeout + d.getTime()]);

		var xhr_ = xhr();
		xhr_.onreadystatechange=function(){
			if (xhr_.readyState==4 && xhr_.status==200){
				if (cb_list[l] === null){
					return;
				}

				if (cb_list[l][1] < d.getTime()){
					cb_list[l][0](l, null, new JSONRequestError("timeout"));
				}else{
					cb_list[l][0](l, JSON.decode(xhr_.responseText), null);
				}
				cb_list[l] = null;
			}
		}
		xhr_.open("GET",url,true);
		xhr_.send();
		
		return l;
	};
	
	/*
	Method: post
		prepares a request and push them inside queue. Throws a JSONRequest Error if some parameter is wrong.
	
	Arguments:
		String - A valid url to call using Ajax respecting Same Origin Policy.
		Array / Object - Data to send
		Function - A callback with 3 arguments: serialNumber, responceObject, exceptionObject
		[Number] - optional milliseconds timeout. Default: 10000
	
	Returns:
		Number - A new valid serial number.
	
	Example:
		>JSONRequest.post("page.psp?var=value", {name:"Andrea"}, function(sn, result, error){alert([sn, result, error])});
	
	Note:
		Server side will recieve a JSONRequest key with escaped JSON data (using encodeURIComponent).
		If data is not an Array, an Object or a valid JSON compatible variable, this method throws a JSONRequest Exception.
	*/
	this.post = function(url, send, done, timeout){
		var d=new Date();
		
		l = cb_list.length;
		cb_list.push([done, timeout + d.getTime()]);

		var xhr_ = xhr();
		xhr_.onreadystatechange=function(){
			if (xhr_.readyState==4 && xhr_.status==200){
				if (cb_list[l] === null){
					return;
				}

				if (cb_list[l][1] < d.getTime()){
					cb_list[l][0](l, null, new JSONRequestError("timeout"));
				}else{
					cb_list[l][0](l, JSON.decode(xhr_.responseText), null);
				}

				cb_list[l] = null;
			}
		}
		xhr_.open("POST",url,true);
		xhr_.setRequestHeader("Content-Type", "application/json");
		xhr_.send(JSON.encode(send));
		
		return l;
	};
	
	/* Section: Methods - Private */
	
	/*
	Method: cancel
		removes timeout and block XHR interaction. Changes queue index properties to save memory.
	
	Arguments:
		Number - A valid JSONRequest serial number.
		[JSONRequestError] - optional dedicated error
	*/
	function cancel(l){
		cb_list[l] = null;
	};
	
	/*
	Method: xhr
		creates a new XMLHttpRequest or ActiveX object.
	
	Returns:
		new XMLHttpRequest or new Microsoft.XMLHTTP ActiveX object
	*/
	function xhr(){
		return window.XMLHttpRequest ? new XMLHttpRequest : new ActiveXObject("Microsoft.XMLHTTP");
	};
	
	/*
	Property: Private
	
	List: register callback in cb_list
	*/
	var	cb_list = new Array();
};