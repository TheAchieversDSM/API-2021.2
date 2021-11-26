$('input[name="daterange"]').daterangepicker(
  {
    locale: {
      format: 'YYYY-MM-DD'
    },
    startDate: '2013-01-01',
    endDate: '2013-12-31'
  },
  function (start, end, label) {
    alert("A new date range was chosen: " + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD'));
  });

function validar() {
  var nome = document.getElementById("nome").value;
  var senha = document.getElementById("senha").value;
  var email = document.getElementById("email").value;
  var regex_nome = /^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]+$/;
  var regex_email = /^(.+@fatec.sp.gov.br)$/;
  if (nome == "") {
    alert('Preencha o campo "Nome".')
    return false;
  }
  if (regex_nome.test(nome) == false) {
    alert('Somente letras são permitidas no Nome.');
    return false;
  }
  if (email == "") {
    alert('Preencha o campo "Email".')
    return false
  }
  if (regex_email.test(email) == false) {
    alert('Somente o email institucional é permitido.');
    return false
  }
  if (senha == "") {
    alert('Preencha o campo "Senha".')
    return false
  }
  else {
    return true
  }
}
function validarLog() {
  var senha = document.getElementById("senha").value;
  var email = document.getElementById("email").value;
  var regex_email = /^(.+@fatec.sp.gov.br)$/;
  if (email == "") {
    alert('Preencha o campo "Email".')
    return false
  }
  if (regex_email.test(email) == false) {
    alert('Somente o email institucional é permitido.');
    return false
  }
  if (senha == "") {
    alert('Preencha o campo "Senha".')
    return false
  }
  else {
    return true
  }
}

function mostrar() {
  ver = document.getElementById("ver")
  if (ver.className == "escondido") {
    document.getElementById("ver").className = "mostrar"
    document.getElementById("ver1").className = "mostrar"
    document.getElementById("olho").className = 'fas fa-eye';
  }
  else {
    document.getElementById("ver").className = "escondido"
    document.getElementById("ver1").className = "escondido"
    document.getElementById("olho").className = 'fas fa-eye-slash';
  }
}
function coordenador(){

  if(document.getElementById('curso').value == "2") {
    document.getElementById("curcoord").className ="curcoord"
    document.getElementById("curso2").className = "turma";
    
  }
  else {
    document.getElementById("curcoord").className = "cursohidden"
    document.getElementById("curso2").className = "cursohidden";
  }
}
