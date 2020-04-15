#include<stdio.h>
int main(){
    int x,i;
    int result = 0;
    printf("x=");
    scanf("%d",&x);
    while(x % 2 == 0){
        printf("2\n");
        x /= 2;
    }
    for(i = 3; i*i <= x;i++){
        while(x%i == 0){
            printf("%d\n",i);
            x /= i;
        }
    }
    if(x != 1)  printf("%d",x);
}