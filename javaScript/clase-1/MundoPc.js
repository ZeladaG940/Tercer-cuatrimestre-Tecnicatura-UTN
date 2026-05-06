class DispositivoEntra{
    constructor(tipoEntrada, marca){
        this._tipoEntrada = tipoEntrada;
        this._marca       = marca;
    }
    get tipoEntrada(){
        return this._tipoEntrada;
    }
    get marca(){
        return this._marca;
    }

    set tipoEntrada(tipoEntrada){
        this._tipoEntrada = tipoEntrada;
    }
    set marca(marca){
        this._marca = marca
    }
}

class Raton extends DispositivoEntra{
    static contadorRatones = 0;
    constructor (tipoEntrada, marca){
        super(tipoEntrada, marca);
        this._idRaton = ++Raton.contadorRatones;
    }
    get idRaton(){
        return this._idRaton;
    }
    set idRaton(idRaton){
        this._idRaton = idRaton;
    }
    toString(){
        return `Raton: [idRaton: ${this._idRaton}, tipoEntrada: ${this._tipoEntrada}, marca: ${this._marca}]`;
    }
}

let raton1 = new Raton("usb", "logitech");
console.log(raton1.toString());
let raton2 = new Raton("bluetoonth", "PH");
console.log(raton2.toString());

class Teclado extends DispositivoEntra{
    static contadorTeclado = 0;
    constructor(tipoEntrada, marca){
        super(tipoEntrada, marca)
        this._idTeclado = ++Teclado.contadorTeclado;
    }
    get idTeclado(){
        return this._idTeclado;
    }
    set idTeclado(idTeclado){
        this._idTeclado = idTeclado;
    }
    toString(){
        return `Teclado [idTeclado: ${this._idTeclado}, tipoEntrada: ${this._tipoEntrada}, marca: ${this._marca}]`
    }
}
let teclado1 = new Teclado("usb", "HP");
console.log(teclado1.toString());
let teclado2 = new Teclado("bluetoonth", "Razer");
console.log(teclado2.toString());

class Monitor{
    static contadorMonitor = 0;
    constructor(marca, tamanio){
        this._idMonitor = ++Monitor.contadorMonitor;
        this._tamanio = tamanio;
        this._marca = marca;
    }
    get idMonitor(){
        return this._idMonitor
    }
    toString(){
        return `Monitor [idMonitor: ${this.idMonitor}, tamanio: ${this._tamanio}, marca: ${this._marca}]`;
    }
}

let monitor1 = new Monitor("HP", 24);
let monitor2 = new Monitor("SAMSUNG", 32);
console.log(monitor1.toString());
console.log(monitor2.toString());

class Computadora{
    static contadorComputadora = 0;
    constructor(nombre, monitor, teclado, raton){
        this._idComputadora = ++Computadora.contadorComputadora;
        this._nombre = nombre;
        this._monitor = monitor;
        this._raton = raton;
        this._teclado = teclado;
    }
    toString(){
        return `Computadora ${this._idComputadora}: ${this._nombre} \n ${this._monitor} \n ${this._raton} \n ${this._teclado}`;
    }
    //nombre
    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre
    }
    //monitor
    get monitor(){
        return this._monitor;
    }
    set monitor(monitor){
        this._monitor = monitor
    }
    //raton
    get raton(){
        return this._raton;
    }
    set raton(raton){
        this._raton = raton
    }
    //teclado
    get teclado(){
        return this._teclado;
    }
    set teclado(teclado){
        this._teclado = teclado
    }
}

let computadora1 = new Computadora("FPS", "monitor1", "teclado1", "raton1");
let computadora2 = new Computadora("Zelda", "monitor2", "teclado2", "raton2");
console.log(computadora1.toString());
console.log(computadora2.toString());
console.log(`${computadora1}`);

class Orden{
    static contadorOrden = 0;
    constructor(){
        this._idOrden = ++Orden.contadorOrden;
        this._computadoras = [];
    }
    get idOrden(){
        return this._idOrden;
    }
    //metodo
    agregarComputadoras(computadora){
        this._computadoras.push(computadora);//se agrega lols objetos a al arreglo this._computadoras
    }
    mostrarOrden(){               //equivalente al toString
        let computadoraOrden = "";
        for(let computadora of this._computadoras){
            computadoraOrden += `${computadora}`;
        };
        console.log(`Orden: ${this.idOrden}, computadora: ${computadoraOrden}`);
    }
}
let orden1 = new Orden();
orden1.agregarComputadoras(computadora1);
orden1.agregarComputadoras(computadora2);
orden1.mostrarOrden()

let orden2 = new Orden();
orden2.agregarComputadoras(computadora1);
orden2.agregarComputadoras(computadora2);
orden2.mostrarOrden();

