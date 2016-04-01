function check(e){

	if (e.e1.value == e.e2.value){
		if (e.pw1.value == e.pw2.value){
			return true
		}
	}
	else{
		alert("Emails or passwords DON'T match");
		return false;
	}
}

function changecolor(){
			var url = document.URL;
			
			if (url.search("aboutme") > 0){
				document.getElementById("aboutme").style.background = 'green';
				document.getElementById("aboutme").style.textTransform = 'uppercase';
			}
			else if (url.search("work") > 0){
				document.getElementById("work").style.background = 'green';
				document.getElementById("work").style.textTransform = 'uppercase';
			}
			else if (url.search("form") > 0 || url.search("login") > 0 || url.search("loggedin") > 0){
				document.getElementById("form").style.background = 'green';
				document.getElementById("form").style.textTransform = 'uppercase';
			}
			else {
				document.getElementById("index").style.background = 'green';
				document.getElementById("index").style.textTransform = 'uppercase';
			}
		}