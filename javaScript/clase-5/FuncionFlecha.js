function miFuncion(){
    console.log('saludos desde mi funcion');
}

miFuncion();
 
let myFuncion = function(){
    console.log('saludos desde la funcion anonima');
}

//funcion flecha
let miFuncionFlecha = ()=>{
    console.log('saludos desde mi funcion flecha');
}
//hay mas variantes para funciones flecha y las vamos ir viendo
miFuncionFlecha();


//lo hacemos en una linea
const saludar = () => console.log('Saludos a todos desde esta funcion');
saludar()

//otro ejemplo
const saludar2 = ()=>{
    return 'Saludos desde la funcion flecha 2'
}
console.log(saludar2());

//Simplificamos la funcion anterior
const saludae3 = ()=> 'Saludos desde la funcion flecha 3';
console.log(saludae3);

//Continuiamos con otro ejemeplo
const regresaObjeto = ()=>({nombre: 'Juan', apellido: 'Lara'});
console.log(regresaObjeto());

//Funciones flecja que reciben parametros
const funcionParametros = (mensaje)=> console.log(mensaje);

funcionParametros('saludos desde esta funcion con parametros');

//una funcion clasica
const funcionParametrosClasicas = function(mensaje){
    console.log(mensaje);
}
funcionParametrosClasicas('saludos desde la funcion clasica');

//se puede omitir los parentesis en la funcion flecha de la siguiente manera
const funcionConParametros = mensaje => console.log(mensaje);
funcionConParametros('Otra forma de trabajar con la funcion flecha');

//Ahora vemos funciones flecha con vario parametros
//Podemos abrir la funcion y tener mas cosas dentro de ella
const funcionConParametros2 = (op1, op2) => {
    let resultado = op1 + op2;
    return resultado;
}
console.log(funcionConParametros2(3,5));

