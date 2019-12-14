function Validate() 
{
	var email = document.getElementsByName('email').value
	var pass = document.getElementsByName('password').value
	window.alert(email+pass)

 if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email))
  {

  }
    alert("You have entered an invalid email address!")
    return (false)
  }

  if (pass.length < 8)
  {
	alert("You have entered an invalid email address!")
	return (false)
  }
  
  return (true);
