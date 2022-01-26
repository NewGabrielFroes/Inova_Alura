public class TestaValores { 
    public static void main(String[] args) { 
        Conta conta = new Conta(1337, 24226);
        Conta conta2 = new Conta(1737, 26826);
        Conta conta3 = new Conta(1537, 24536);
        
        System.out.println(conta.getAgencia());
        System.out.println(conta2.getAgencia());
        System.out.println(conta3.getAgencia());
        
        conta.setAgencia(1232123);
        
        System.out.println(Conta.getTotal());
    }
}