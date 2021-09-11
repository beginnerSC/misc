#include "libswig.hpp"

std::vector<int> my_range(int n){
    
    std::vector<int> vec = {};
    for (int i=0 ; i<n ; i++)
    {
        vec.push_back(i);
    }
    return vec;    
}
double square(double x){
    return x*x;
}
double cube(double x){
    return x*x*x;
}