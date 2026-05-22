function miFuncioin1(){
    console.log("Funcion 1");
}

function miFuncioin2(){
    console.log("Funcion 2");
}

miFuncioin1();
miFuncioin2();

//funcion callback
function imprimir(mensaje){
    console.log(mensaje);
}

function sumar(op1, op2, funcionCallback){
    let res = op1 + op2;
    funcionCallback(`El resutado es: ${res}`)
}

sumar(5,3, imprimir)

//Llamadas asincronicas
function miFuncionCallback(){
    console.log("saludo asincronico desde de 3 segundos");
}

setTimeout(miFuncionCallback, 3000);
setTimeout(function(){console.log("saludos asincrono 2");},5000)
setTimeout(()=>console.log("saludo asincrono"), 8000)


let relog = ()=>{
    let fecha = new Date();
    console.log(`${fecha.getHours()}: ${fecha.getMinutes()}: ${fecha.getSeconds()}`);
}
setInterval(relog, 1000)//se ejecuta cada 1 segundo