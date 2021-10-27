/*$(document).ready(function() {
    $('#multiple-checkboxes').multiselect({
      includeSelectAllOption: true,
    });
}); */ 

$('input[name="dates"]').daterangepicker();

function validar(){
  var nome = document.getElementById("nome").value;
  var senha = document.getElementById("senha").value;
  var email = document.getElementById("email").value;
  var regex_nome = /^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]+$/;
  var regex_email = /^(.+@fatec.sp.gov.br)$/;
  if(nome == ""){
    alert('Preencha o campo "Nome".')
    return false;
  }
  if(regex_nome.test(nome) == false){
    alert('Somente letras são permitidas no Nome.');
    return false;
  }
  if (email == ""){
    alert('Preencha o campo "Email".')
    return false
  }
  if (regex_email.test(email) == false ){
    alert('Somente o email institucional é permitido.');
    return false
  }
  if (senha == ""){
    alert('Preencha o campo "Senha".')
    return false
  }
  else{
    return true
  }
}
function validarLog(){
  var senha = document.getElementById("senha").value;
  var email = document.getElementById("email").value;
  var regex_email = /^(.+@fatec.sp.gov.br)$/;
  if (email == ""){
    alert('Preencha o campo "Email".')
    return false
  }
  if (regex_email.test(email) == false ){
    alert('Somente o email institucional é permitido.');
    return false
  }
  if (senha == ""){
    alert('Preencha o campo "Senha".')
    return false
  }
  else{
    return true
  }
}

function mostrar(){
  responder = document.getElementById("responder")
  if(responder.className == "escondido"){
    document.getElementById("responder").className = "mostrar"
  }
  else{
    document.getElementById("responder").className = "escondido"
  }
}

