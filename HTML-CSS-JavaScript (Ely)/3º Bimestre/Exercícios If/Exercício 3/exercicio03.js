
var dataAtual = new Date();
var numeroDiaSemana = dataAtual.getDay();
var resp = document.getElementById ("resp");
if (numeroDiaSemana == 0){
    resp.innerHTML = "Hoje é Domingo"
}
else if (numeroDiaSemana == 1){
    resp.innerHTML = "Hoje é Segunda-feira"
}
else if (numeroDiaSemana == 2){
    resp.innerHTML = "Hoje é Terça-feira"
}
else if (numeroDiaSemana == 3){
    resp.innerHTML = "Hoje é Quarta-feira"
}
else if (numeroDiaSemana == 4){
    resp.innerHTML = "Hoje é Quinta-feira"
}
else if (numeroDiaSemana == 5){
    resp.innerHTML = "Hoje é Sexta-feira"
}
else if (numeroDiaSemana == 6){
    resp.innerHTML = "Hoje é Sábado"
}


