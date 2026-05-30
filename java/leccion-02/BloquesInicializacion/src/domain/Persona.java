package domain;

/**
 *
 * @author WinterOS
 */
public class Persona {
    private final int idPersona; // 1. QUITAMOS el "= 0" aquí
    private static int contadorPersonas;
    
    static { // Bloque de inicialización estático
        System.out.println("Ejecución del bloque estático");
        ++Persona.contadorPersonas;
    }
    
    { // Bloque de inicialización NO estático (contexto dinámico)
        System.out.println("Ejecución del bloque no estático");
        this.idPersona = Persona.contadorPersonas++; // 2. Ahora sí se puede asignar
    }
    
    public Persona() {
        System.out.println("Ejecución del constructor");
    }
    
    public int getIdPersona() { // Cambiado el nombre a uno más descriptivo
        return this.idPersona;
    }
}