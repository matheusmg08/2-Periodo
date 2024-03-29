function calcular(){

    valor1 = document.getElementById ("valor1").value;
    valor2 = document.getElementById ("valor2").value;
    valor3 = document.getElementById ("valor3").value;
    resp = document.getElementById ("resp");
    if (parseFloat(valor1) < (parseFloat(valor2) + parseFloat(valor3)) && parseFloat(valor2) < (parseFloat(valor1) + parseFloat(valor3)) && parseFloat(valor3) < (parseFloat(valor1) + parseFloat(valor2))){
         
       resp.innerHTML = "É possível montar um triângulo com esse valor.\t"   

        if ((valor1 == valor2) && (valor1 == valor3) && (valor2 == valor3)){
            resp.innerHTML += "Triângulo Equilátero"
        }
        else if ((valor1 == valor2) || (valor1 == valor3) || (valor2 == valor3)){
            resp.innerHTML += "Triângulo Isóceles"
        }
        else if ((valor1 != valor2) && (valor1 != valor3) && (valor2 != valor3)){
            resp.innerHTML += "Triângulo Escaleno"
        }
    } 
    else{
        resp.innerHTML = "Não é possível montar um triângulo com esses valores!"
    }  

}
function limpar(){
    valor1 = document.getElementById ("valor1").value;
    valor2 = document.getElementById ("valor2").value;
    valor3 = document.getElementById ("valor3").value;
    resp = document.getElementById ("resp");
    valor1 = "";
    valor2 = "";
    valor3 = "";
    resp.innerHTML = "";
    valor1.focus()

}