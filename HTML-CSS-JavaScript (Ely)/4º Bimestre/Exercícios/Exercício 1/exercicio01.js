function calcular() {
    var primeiro = document.getElementById ("primeiro").value;
    var segundo = document.getElementById ("segundo").value;
    var resp = document.getElementById ("resp");
    var operacao = op.options[op.selectedIndex].text;

    if (operacao == "Adição"){
        var soma = parseFloat(primeiro) + parseFloat(segundo);
        resp.innerHTML = "A opção selecionada foi adição, o resultado da adição dos dois números é: " + soma;
    }
    else if (operacao == "Subtração"){
        var sub = parseFloat(primeiro) - parseFloat(segundo);
        resp.innerHTML = "A opção selecionada foi subtração, o resultado da subtração dos dois números é: " + sub;
    }
    else if (operacao == "Multiplicação"){
        var multi = parseFloat(primeiro) * parseFloat(segundo);
        resp.innerHTML = "A opção selecionada foi multiplicação, o resultado da multiplicação dos dois números é: " + multi;
    }
    else if (operacao == "Divisão"){
        var divi = parseFloat(primeiro) / parseFloat(segundo);
        resp.innerHTML = "A opção selecionada foi divisão, o resultado da divisão dos dois números é: " + divi;
    }
    else if (operacao == "Resto"){
        var resto = parseFloat(primeiro) % parseFloat(segundo);
        resp.innerHTML = "A opção selecionada foi resto, o resultado do resto da divisão dos dois números é: " + resto;
    }
 
}
function limpar(){
    var primeiro = document.getElementById ("primeiro");
    var segundo = document.getElementById ("segundo");
    var resp = document.getElementById ("resp");
    primeiro.value = "";
    segundo.value = "";
    resp.innerHTML = "";
    primeiro.focus()
}