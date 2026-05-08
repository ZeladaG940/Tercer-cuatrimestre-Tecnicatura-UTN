'use strict'

//como avitar un error parecido
try{
    x = 10;
    mifuncion();
}
catch(error){
    console.log(error);
}
finally{
    console.log('Termina la revision de errores');//opcional para el manejo de errores
}

//la ejecucion ahora continua
console.log('Continuamos...');//esto noi se llega a ver por que esta bloqueado
