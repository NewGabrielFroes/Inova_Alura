public class TestaFatorial {
	
	public static void main(String[] args) {
	    int fatorial = 1;
	    
	    for(int n = 0; n <= 10; n++) {
	    	if(n > 0) {
	            fatorial = fatorial * n;
	        }
	    	
	    	System.out.println("O Fatorial de " + n + " é: " + fatorial);
	    }
	}

}
