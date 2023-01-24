import java.util.Scanner;
class Fibonacci
{	
	public static void main(String args[])
	{
		int a, b, n, c, s;

        System.out.print("enter n : ");
        
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        
        a = -1;
        b = 1;
        s = 0;
        
        while (s!=n)
        {
            c = a+b;
            System.out.println(c);
            a = b;
            b = c;
            s++;
        }
	}
}