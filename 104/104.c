#include<stdio.h>
int main(){
    int a,b,c;
    printf("enter the number");
    scanf("%d",&a);
    printf("enter the second number");
    scanf("%d",&b);
    printf("enter the third number");
    scanf("%d",&c);
    if(a>b && a>c){
        printf("a is largest");

    }
    else if(b>c && b>a){
        printf("b is largest");
    }
    else{
        printf("c is largest");
    }
    return 0;
}