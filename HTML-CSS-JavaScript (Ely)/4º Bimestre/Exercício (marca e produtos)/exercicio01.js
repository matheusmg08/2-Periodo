function carregarProduto(){
    var m = document.getElementById ("marca");
    var marca = m.options[m.selectedIndex].text;
    var prod = document.getElementById ("prod");        
    if (marca == "Apple"){
        prod.innerHTML = "<option>Escolha uma opção</option>"
        prod.innerHTML += "<option>IPhone</option>";
        prod.innerHTML += "<option>IPad</option>";
        prod.innerHTML += "<option>Macbook</option>";
    }
    else if (marca =="Samsung"){
        prod.innerHTML = "<option>Escolha uma opção</option>"
    prod.innerHTML += "<option>Galaxy S20</option>";
    prod.innerHTML += "<option>Galaxy S21</option>";
    prod.innerHTML += "<option>Galaxy Tab</option>";
    }
    else if (marca =="Xiaomi"){
        prod.innerHTML = "<option>Escolha uma opção</option>"
        prod.innerHTML += "<option>Redmi Note 10</option>"
        prod.innerHTML += "<option>Redmi Note 11</option>"
        prod.innerHTML += "<option>Redmi Note 12</option>"
    }
}
function carregarPreco() {
    var p = document.getElementById ("prod");
    var prod = p.options[p.selectedIndex].text;
    var preco = document.getElementById ("precounit");
    if (prod == "IPhone"){
        preco.innerHTML = "R$ 4.500,00"
    }
    else if (prod == "IPad"){
        preco.innerHTML = "R$ 5.000,00"
    }
    else if (prod == "Macbook"){
        preco.innerHTML = "R$ 9.000,00"
    }
    else if (prod == "Galaxy S20"){
        preco.innerHTML = "R$ 3.500,00"
    }
    else if (prod == "Galaxy S21"){
        preco.innerHTML = "R$ 4.000,00"
    }
    else if (prod == "Galaxy Tab"){
        preco.innerHTML = "R$ 4.500,00"
    }
    else if (prod == "Redmi Note 10"){
        preco.innerHTML = "R$ 1.800,00"
    }
    else if (prod == "Redmi Note 11"){
        preco.innerHTML = "R$ 2.200,00"
    }
    else if (prod = "Redmi Note 12"){
        preco.innerHTML = "R$ 3.000,00"
    }
}
function calcular(){
    var p = document.getElementById ("precounit").value;
    var qtd = document.getElementById ("quant").value;
    var resp = document.getElementById ("resp");
    var total = parseFloat(p) * parseFloat(qtd);
    resp.innerHTML = total;
}