package Enumeraciones;

public enum Continentes {
    // 1. Definición de las constantes (deben ir PRIMERO)
    AFRICA(53, "1.2 billones"),
    EUROPA(46, "1.1 billones"),
    ASIA(44, "1.9 billones"),
    AMERICA(34, "150.2 billones"),
    OCEANIA(14, "1.2 billones"); // Importante: termina con punto y coma (;)

    // 2. Atributos (deben ser privados)
    private final int paises;
    private final String habitantes; // Es buena práctica que también sea final

    // 3. Constructor (en los enums es privado por defecto)
    Continentes(int paises, String habitantes) {
        this.paises = paises;
        this.habitantes = habitantes;
    }

    // 4. Métodos Getters para poder acceder a los datos desde fuera
    public int getPaises() {
        return paises;
    }

    public String getHabitantes() {
        return habitantes;
    }
}
