
import java.math.*;


/**
 *
 * @author Tharindu Prabhath
 */
public class DH {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        BigInteger G,p,pubkey,session;
        int pvkey;
        
        G=BigInteger.valueOf(15487469);
        p=BigInteger.valueOf(1021);
        
        
        if(args.length==1)
        {
        pvkey=Integer.parseInt(args[0]);
        pubkey=(G.pow(pvkey)).mod(p);
        System.out.println("Public key is "+pubkey.toString());
        }
        else if(args.length==2)
        {
        pvkey=Integer.parseInt(args[0]);
        pubkey=new BigInteger(args[1]);
        session=(pubkey.pow(pvkey)).mod(p);
        System.out.println("Session key is "+session.toString());     
        
        }
        
        else
        {
        System.out.println("Invalid arugments"); 
        }
    }
    
}
