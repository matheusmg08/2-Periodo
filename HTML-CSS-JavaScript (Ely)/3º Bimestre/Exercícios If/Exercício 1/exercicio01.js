function calcular(){
    var gasolina = document.getElementById ("gasolina").value;
    var etanol = document.getElementById ("etanol").value;
    var preco = parseFloat(gasolina) * 0.7
    if (etanol > preco ){
        resp.innerHTML = "Está compensando abastecer na gasolina"
    }
    else{
        resp.innerHTML = "Está compensando abastecer no ácool"
    }
} 
function limpar(){
    var gasolina = document.getElementById ("gasolina");
    var etanol = document.getElementById ("etanol");
    var resp = document.getElementById ("resp");
    gasolina.value = "";
    etanol.value = "";
    resp.innerHTML = "";
    gasolina.focus();

}