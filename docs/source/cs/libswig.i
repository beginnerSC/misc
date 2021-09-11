%module libswig
%{
#include "libswig.h"
%}
#define __version__ "0.0.1";
double square(double x);
double cube(double x);