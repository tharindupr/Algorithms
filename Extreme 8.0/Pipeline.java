import java.util.Scanner;
class Matrix{
  int row , matrix[][]; 
  int min;
  
  Matrix(){
    row=0;
    matrix= null;
  }
 Matrix(int r, int c){
   row=r;
   if(row>0)
     matrix=new int [row][row];
   else
     matrix= null;
 }
 void read(){
   Scanner i= new Scanner (System.in);
   if(matrix==null){
     row=i.nextInt();
     matrix= new int [ row][row];
   
   for (int c=0; c<row; c++){
     for (int d=0; d< row ; d++){
       matrix[c][d]=i.nextInt();
     
     } 
     }
       
   }
 }
 
 void  traverse(){
     int mi=0;
     int total=0;
     int p = 0;
     for (int i=0; i<row; i++){
         mi= matrix[0][i];
         p=i;
        if(mi>matrix[0][i] ){
            mi = matrix[0][i];
            p= i;
        }
      
     }// return p;
    /* for (int i = p; i <= row; i++)
        matrix[i][0] = matrix[i-1][0] + matrix[i][0];
     for (int j= 1; j <= row; j++)
        matrix[0][j] = matrix[0][j-1] + matrix[0][j];*/
    
     for (int r=p;r<row;r++ ){
         for (int c=1 ;c<=row ; c++){
          
             int z=min(matrix[r][c+1],matrix[r+1][c],matrix[r-1][c]);
             
            total+=z;
             
     
         }
         }
     
     System.out.println(total);
     
 }
 int min(int x, int y, int z)
{
   if (x < y)
      return (x < z)? x : z;
   else
      return (y < z)? y : z;
}   
public static void main (String args[]){
   Matrix san = new  Matrix();
   san.read();
   //san.min();
   san.traverse();
 }
 

}
