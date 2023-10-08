#include <iostream>

int main(){
    int n;
    std::cout << "enter a no.  :";
    std::cin>>n;
    for(int i=1;i<n+1;i++){
        int f=0;
        for(int j=2;j<i;j++){
            if(i%j==0){
                f=1;
                break;
            }
        }
        if(f==0){
            std::cout <<i<<" : Prime"<<std::endl;
        }
    }
    return 0;
}
