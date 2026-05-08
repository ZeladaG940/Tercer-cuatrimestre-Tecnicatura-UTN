class Empleado{
    constructor(nombre, sueldo){
        this._nombre = nombre;
        this._sueldo = sueldo;
    }
    obtenerDetalles(){
        return `Empleado: ${this._nombre},
        Sueldo: ${this._sueldo}`
    }
}

class Gerente extends Empleado{
    constructor(nombre, sueldo, departamento){
        super(nombre, sueldo);
        this._departamento = departamento;
    }

    //Agregamos la sobre escritura
    obtenerDetalles(){
        return `Gerente: ${super.obtenerDetalles()}, dept: ${this._departamento}`;
    }
}

const gerente1 = new Gerente("zelada", 5000, "systemas")
console.log(gerente1);

const empleado1 = new Empleado("maicol", 3000)
console.log(empleado1);