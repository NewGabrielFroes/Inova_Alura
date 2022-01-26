public class TestaGetESet { 
    
	public static void main(String[] args) { 
        Conta conta = new Conta();
        //conta.numero = 1777;
        conta.setNumero(1337);
        System.out.println(conta.getNumero()); 
        
        Cliente paulo = new Cliente();
        // conta.titular = paulo;
        paulo.setNome("Paulo Silveira");
        paulo.setCpf("123.456.789-22");
        paulo.setProfissao("Programador");
        
        conta.setTitular(paulo);
        
        System.out.println(conta.getTitular().getNome());
        
        conta.getTitular().setProfissao("Comerciante");
        // agora em duas linhas:
        Cliente titularDaConta = conta.getTitular();
        titularDaConta.setProfissao("Cozinheiro");
        
        System.out.println(conta.getTitular().getProfissao());
	}
}
