
package leccion_02;

public class Leccion_02 {


    public static void main(String[] args) {
        imprimirNumeros(1,2,3);
        imprimirNumeros(1,2);
        variosParametros("Juan", "Perez", 7, 8 ,9);
    }
    
    private static void variosParametros(String nombre, String apellido,int ...numeros){
        System.out.println("Nombre: " + nombre + " Apellido: " + apellido);
        imprimirNumeros(numeros);
    }
    private static void imprimirNumeros(int ...numeros){
        for(int i=0; i<numeros.length; i++){
            System.out.println("Elementos: " + numeros[i]);
        }
    }
    
}
