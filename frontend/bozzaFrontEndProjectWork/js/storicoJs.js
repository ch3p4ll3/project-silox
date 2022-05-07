
let btnIndietro = document.getElementById('indietro')
let dimTable = document.getElementById('tableScorrimentoCheck');
let table = document.getElementById('table');



btnIndietro.onclick = function () {
    location.href = '/index.html';
  };

  
let scegliDim = function(){
    if (dimTable.checked){
        table.classList.add('tabellaAScorrimento')
    } else {
        table.classList.remove('tabellaAScorrimento')
    }
  }
  
dimTable.addEventListener('click', scegliDim)