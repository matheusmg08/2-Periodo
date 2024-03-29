function calcular(){
    var resp = document.getElementById ("resp");
    var nome = document.getElementById ("nome").value;
    var opcao = idade.options[idade.selectedIndex].text;

    if (opcao == "Abaixo de 14 anos"){
        resp.innerHTML = "Seu nome é <b><i>" + nome + "</i></b> e a categoria que se enquadra é <b><i>'mirim'</i></b>"
    }
    else if (opcao == "Entre 14 e 15 anos"){
        resp.innerHTML = "Seu nome é <b><i>" + nome + "</i></b> e a categoria que se enquadra é <b><i>'infantil'</i></b>"
    }
    else if (opcao == "Entre 16 e 17 anos"){
        resp.innerHTML = "Seu nome é <b><i>" + nome + "</i></b> e a categoria que se enquadra é <b><i>'juvenil'</i></b>"
    }
    else if (opcao == "De 18 a 20 anos"){
        resp.innerHTML = "Seu nome é <b><i>" + nome + "</i></b> e a categoria que se enquadra é <b><i>'juniores'</i></b>"
    }
    else if (opcao == "Acima de 20 anos"){
        resp.innerHTML = "Seu nome é <b><i>" + nome + "</i></b> e a categoria que se enquadra é <b><i>'profissional'</i></b>"

    }
}
function limpar(){
    var nome = document.getElementById ("nome");
    var resp = document.getElementById ("resp");
    nome.value = "";
    resp.innerHTML = "";
    nome.focus();
}
