package test;

import Enumeraciones.Continentes;
import Enumeraciones.Dias;
import static Enumeraciones.Dias.MIERCOLES;

public class testEnumeracion {
    public static void main(String[] args) {
        System.out.println("Dia 1: " + Dias.LUNES);
        indicarDiaSemana(Dias.LUNES);
        
        System.out.println("Continente No. 4: " + Continentes.AMERICA);
        System.out.println("No. de paises en el 4to. continenete: " 
        + Continentes.AMERICA.getPaises());
        
        System.out.println("No. habitabtes en el 4to. continenete: " + 
                Continentes.AMERICA.getHabitantes());
    }
    
    
    
    private static void indicarDiaSemana(Dias dias) {
        // El switch se abre y se cierra una sola vez
        switch(dias) {
            case LUNES:
                System.out.println("Primer día de la semana");
                break; 
            case MARTES:
                System.out.println("Segundo día de la semana");
                break;
            case MIERCOLES:
                System.out.println("Tercer día de la semana");
                break;
            case JUEVES:
                System.out.println("Tercer día de la semana");
                break;
            case VIERNES:
                System.out.println("Tercer día de la semana");
                break;
            case SABADO:
                System.out.println("Tercer día de la semana");
                break;
            case DOMINGO:
                System.out.println("Tercer día de la semana");
                break;
            // Puedes agregar el resto de los días aquí...
            default:
                System.out.println("Otro día de la semana");
                break;
        }
    }
}
