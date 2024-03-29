function calcular(){
    var nome = document.getElementById ("nome").value;
    var ano = document.getElementById ("ano").value;
    var idade = (2023 - parseInt(ano));
    if (idade < 14){
        resp.innerHTML = "Mirim"
    }
    else if ((idade == 14) || (idade == 15)){
        resp.innerHTML = "Infantil"
    }
    else if ((idade == 16) || (idade == 17)){
        resp.innerHTML = "Juvenil"
    }
    else if ((idade >= 18) && (idade <= 20)){
        resp.innerHTML = "Juniores"
    }
    else if (idade > 20){
        resp.innerHTML = "Profissional"
    }
}
function limpar(){
    var nome = document.getElementById ("nome");
    var ano = document.getElementById ("ano");
    var resp = document.getElementById ("resp");
    nome.value = "";
    ano.value = "";
    resp.innerHTML = "";
    nome.focus();
}

