#include<stdio.h>
int main()
{  
    int n;
    printf("enter n");
    scanf("%d",&n);
    char manish_hero='*';

        for (int i=0;i<=n;i++){
            for (int j=n-1;j>=i;--j){
                printf(" ");}
                for (int x=1;x<=i;x++){
                    printf("%c",manish_hero);

                }
            
            printf("\n");
        }

   
    
    return 0;
}
