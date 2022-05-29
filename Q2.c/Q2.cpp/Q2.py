# 210498-Kartikeya
//Assignment 1
//Question 2 sesction 2

#include <stdio.h>

int main(void) {
	
	int n,a,b; // variables n,a,b are as per question
	scanf("(%d,",&n);
	scanf("%d,",&a);
	scanf("%d)",&b);
	int S=1;// gives value to be multiplied with s at each stage to check whether , (n-(s*S)) is divisible by b 
	int s=n;// stores a copy of n for computation
	int cnt=0;// keeps track of number of division operations performed
	while(s!=0){
	    cnt++;
	    if((n-(s*S))%b==0&& s%a==0&&S!=1){//s gives first part while n-(s*S) gives the second part in each iteration
	        printf("n1: %d n2: %d",s,n-(s*S)); //n1,n2 divide first and second parts of n respectively.
	        break;
	        
	    }
	    s/=10;// s is divided by 10 at each stage
	    S*=10;// multiplication by 10 at each stage
	  
	}
	
	return 0;
}
