#include <stdio.h>
int main(){
    int n;
    printf("enter the no.  :");
    scanf("%d",&n);
    for(int i=1;i<n+1;i++){
        int f=0;
        for(int j=2;j<i;j++){
            if(i%j==0){
                f=1;
                break;
            }
        }
        if(f==0){
            printf("%d : Prime \n",i);
        }
    }
    return 0;
}