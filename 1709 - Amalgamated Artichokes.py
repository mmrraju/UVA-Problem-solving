'''This problem basically for C, C++, Java I tried to do with python  but got TL errors. For functionally python is slow then c, c++'''
from math import sin, cos

while True:
    try:
        p, a, b, c, d, n = map(int, input().split())
        
        max_decline = 0
        
        temp_max = p*( sin(a + b) + cos(c + d ) + 2)
        
        for i in range(2, n +1):
            current_decline = p*( sin( a*i +b) + cos(c*i + d) + 2)
            if temp_max> current_decline:
                if max_decline < (temp_max - current_decline):
                    max_decline = temp_max - current_decline
            else:
                temp_max = current_decline
                
        print(max_decline)
            
        
    except EOFError:
        break
        
        
 '''#include <bits/stdc++.h>
using namespace std;

int main() {
	int p, a, b, c, d, n;
	while (scanf("%d %d %d %d %d", &p, &a, &b, &c, &d) == 5) {
		scanf("%d", &n);
		double max_decline = 0;
		double max = p * (sin((a + b)) + cos((c + d)) + 2);
		for (int k = 2; k <= n; k++) {
			double curr = p * (sin((a * k + b)) + cos((c * k + d)) + 2);
				if (max > curr) {
					if(max_decline< max - curr){
						max_decline=max-curr;
					}
				} else {
					max = curr;
				}
		}
		printf("%.8lf\n", max_decline);
	}
	return 0;
}'''
