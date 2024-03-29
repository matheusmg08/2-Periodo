function voltar() {
    var valor_camisa = 59.70;
    var valor_bermuda = 79.70;
    var camisa_desconto = parseFloat(valor_camisa) - parseFloat (valor_camisa) * 10/100;
    var bermuda_desconto = parseFloat(valor_bermuda) - parseFloat(valor_bermuda) * 0.1;
    var c1 = document.getElementById("camiseta");
    var resp = document.getElementById ("resp");
    if (c1.src.includes("camiseta1.frente.jpg")) {
        c1.src = "camiseta1.costa.jpg"
        resp.innerHTML = "Camiseta Azul "+ "R$<b>"+valor_camisa.toFixed(2)+"</b>"
    } else if (c1.src.includes("camisabranca.frente.jpg")) {
        c1.src =  "camisabranca.costa.jpg"
        resp.innerHTML = "Camiseta Branca (está na promoção com 10% de desconto) "+ "R$<b>"+camisa_desconto.toFixed(2)+"</b>"
    }
    else if (c1.src.includes("bermudafrente.jpg")){
        c1.src = "bermudacosta.jpg"
        resp.innerHTML = "Bermuda Azul "+ "R$<b>"+valor_bermuda.toFixed(2)+"</b>"

        
    }
    else if (c1.src.includes("bermudabrancafrente.jpg")){
        c1.src = "bermudabrancacosta.jpg"
        resp.innerHTML = "Bermuda branca (está na promoção com 10% de desconto) "+ "R$<b>"+bermuda_desconto.toFixed(2)+"</b>"

    }

}
function avancar() {
    var valor_camisa = 59.70;
    var valor_bermuda = 79.70;
    var camisa_desconto = parseFloat(valor_camisa) - parseFloat (valor_camisa) * 10/100;
    var bermuda_desconto = parseFloat(valor_bermuda) - parseFloat(valor_bermuda) * 0.1;
    var c1 = document.getElementById("camiseta");
    var resp = document.getElementById ("resp");
    if (c1.src.includes("camiseta1.costa.jpg")) {
        c1.src = "camiseta1.frente.jpg"
        resp.innerHTML = "Camiseta Azul "+ "R$<b>"+valor_camisa.toFixed(2)+"</b>"

    } else if (c1.src.includes("camisabranca.costa.jpg")) {
        c1.src = "camisabranca.frente.jpg"
        resp.innerHTML = "Camiseta Branca (está na promoção com 10% de desconto) "+ "R$<b>"+camisa_desconto.toFixed(2)+"</b>"

    }
    else if (c1.src.includes("bermudacosta.jpg")){
        c1.src = "bermudafrente.jpg"
        resp.innerHTML = "Bermuda Azul "+ "R$<b>"+valor_bermuda.toFixed(2)+"</b>"

    }
    else if (c1.src.includes("bermudabrancacosta.jpg")){
        c1.src = "bermudabrancafrente.jpg"
        resp.innerHTML = "Bermuda branca (está na promoção com 10% de desconto) "+ "R$<b>"+bermuda_desconto.toFixed(2)+"</b>"

    }
   
}
function azul() {
    var valor_camisa = 59.70;
    var valor_bermuda = 79.70;
    var camisa_desconto = parseFloat(valor_camisa) - parseFloat (valor_camisa) * 10/100;
    var bermuda_desconto = parseFloat(valor_bermuda) - parseFloat(valor_bermuda) * 0.1;
    var c1 = document.getElementById("camiseta");
    var resp = document.getElementById ("resp");

    if (c1.src.includes("camisabranca.frente.jpg")){
        c1.src = "camiseta1.frente.jpg"
        resp.innerHTML = "Camiseta Azul "+ "R$<b>"+valor_camisa.toFixed(2)+"</b>"

    }
    else if (c1.src.includes("bermudabrancafrente.jpg")){
        c1.src = "bermudafrente.jpg"
        resp.innerHTML = "Bermuda Azul "+ "R$<b>"+valor_bermuda.toFixed(2)+"</b>"

    }
    else if (c1.src.includes("bermudabrancacosta.jpg")){
        c1.src = "bermudafrente.jpg"
        resp.innerHTML = "Bermuda Azul "+ "R$<b>"+valor_bermuda.toFixed(2)+"</b>"

    }
    else if (c1.src.includes("camisabranca.costa.jpg")){
        c1.src = "camiseta1.frente.jpg"
        resp.innerHTML = "Camiseta Azul "+ "R$<b>"+valor_camisa.toFixed(2)+"</b>"

    }
    

}
function branca() {
    var valor_camisa = 59.70;
    var valor_bermuda = 79.70;
    var camisa_desconto = parseFloat(valor_camisa) - parseFloat (valor_camisa) * 10/100;
    var bermuda_desconto = parseFloat(valor_bermuda) - parseFloat(valor_bermuda) * 0.1;
    var c1 = document.getElementById("camiseta");
    var resp = document.getElementById ("resp");
    if (c1.src.includes("camiseta1.frente.jpg")){
        c1.src = "camisabranca.frente.jpg"
        resp.innerHTML = "Camiseta Branca (está na promoção com 10% de desconto) "+ "R$<b>"+camisa_desconto.toFixed(2)+"</b>"

    }
    else if (c1.src.includes("bermudafrente.jpg")){
        c1.src = "bermudabrancafrente.jpg"
        resp.innerHTML = "Bermuda branca (está na promoção com 10% de desconto) "+ "R$<b>"+bermuda_desconto.toFixed(2)+"</b>"

    }
    else if (c1.src.includes("bermudacosta.jpg")){
        c1.src = "bermudabrancafrente.jpg"
        resp.innerHTML = "Bermuda branca (está na promoção com 10% de desconto) "+ "R$<b>"+bermuda_desconto.toFixed(2)+"</b>"

    }
    else if (c1.src.includes("bermudabrancacosta.jpg")){
        c1.src = "bermudafrente.jpg"
    }
    else if (c1.src.includes("camiseta1.costa.jpg")){
        c1.src = "camisabranca.frente.jpg"
        resp.innerHTML = "Camiseta Branca (está na promoção com 10% de desconto) "+ "R$<b>"+camisa_desconto.toFixed(2)+"</b>"

    }
    
}
function bermuda(){
    var valor_camisa = 59.70;
    var valor_bermuda = 79.70;
    var camisa_desconto =  parseFloat(valor_camisa) - parseFloat (valor_camisa) * 10/100;
    var bermuda_desconto = parseFloat(valor_bermuda) - parseFloat(valor_bermuda) * 0.1;
    var c1 = document.getElementById("camiseta");
    var resp = document.getElementById ("resp");
    var resp = document.getElementById ("resp");
    var b1 = document.getElementById ("camiseta");
    b1.src = "bermudafrente.jpg"
    resp.innerHTML = "Bermuda Azul "+ "R$<b>"+valor_bermuda.toFixed(2)+"</b>"

}
function camisa(){
    var valor_camisa = 59.70;
    var valor_bermuda = 79.70;
    var camisa_desconto = parseFloat (valor_camisa) * 10/100;
    var bermuda_desconto = parseFloat(valor_bermuda) * 0.1;
    var c1 = document.getElementById("camiseta");
    var resp = document.getElementById ("resp");
    var resp = document.getElementById ("resp");
    var c2 = document.getElementById("camiseta");
    c2.src = "camiseta1.frente.jpg" 
    resp.innerHTML = "Camiseta Azul "+ "R$<b>"+valor_camisa.toFixed(2)+"</b>"

}