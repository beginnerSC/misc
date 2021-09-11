%module libswig
%{
#include "libswig.hpp"
%}
#define __version__ "0.0.1";
std::vector<int> my_range(int n);
double square(double x);
double cube(double x);