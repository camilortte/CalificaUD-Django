//$("#registrar").css("display","none"); botonRegistrarse


//Aparicion -desaparciion
$("#registrar").click(function() {	
	 $("#log").hide("slow");
	$("#register").show("slow");
});

$("#volverToIniciarSesion").click(function() {	
	$("#register").hide("slow");
	$("#log").show("slow");
});

//Antes de enviar el registro comprobamos que el correo y  los passwords coincidan.
/*$('#form-register').submit(function(){
	var pass1=$('#password1').val();
	var pass2=$('#password2').val();
	var correo=$('#correo').val();
	var correo2=$('#correo2').val();
	var seguir=false;
	var mensaje="";
	if (pass1!=pass2){
		mensaje="Las contraseñas no coinciden";
		$('#error_registro').text(mensaje);
		$('#error_registro').show("slow");
		return false;
	}else {
		seguir=true;
	}

	if(correo!=correo2){
		mensaje="El correo no coincide";
		$('#error_registro').text(mensaje);
		$('#error_registro').show("slow");
		return false
	}else{
		seguir=true;
	}

	return seguir;
});  

//En el login se encripta la contrasena antes de enviarla
$('#form_login').submit(function(){
	var pass=$('#password_login').val();
	var md5=$.md5(pass);
	//alert(pass+" "+md5);
	return true;	
})*/